"""Generate the report's architecture and fund-flow diagrams as SVG.

Run: python3 report/figures/gen.py   (writes *.svg next to this file)

Each diagram is a list of boxes (id, x, y, w, h, label, kind) and arrows
(from, to, label, style). Coordinates are in px on a fixed canvas; the PDF
scales the SVG to the text width.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"
INK = "#1b2a41"
MUTED = "#5b6b7f"
KINDS = {
    # fill, stroke
    "buy": ("#e6f0f5", "#1f6f8b"),      # purchased / third-party component
    "build": ("#fdf3e3", "#b7791f"),    # Cyclone-built
    "member": ("#eef0f3", "#5b6b7f"),   # Member / external party
    "chain": ("#eaf5ec", "#2f855a"),    # on-chain asset location
    "risk": ("#fbeaea", "#c53030"),     # high-risk / excluded element
    "group": ("none", "#9aa7b6"),       # boundary
}


def box(b):
    _id, x, y, w, h, label, kind = b
    fill, stroke = KINDS[kind]
    dash = ' stroke-dasharray="5 4"' if kind == "group" else ""
    rx = 4 if kind != "group" else 8
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
           f'fill="{fill}" stroke="{stroke}" stroke-width="1.4"{dash}/>']
    lines = label.split("\n")
    if kind == "group":
        out.append(f'<text x="{x + 8}" y="{y + 15}" font-size="10.5" '
                   f'fill="{MUTED}" font-weight="bold">{escape(lines[0])}</text>')
        return "\n".join(out)
    lh = 13
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2 + 4
    for i, line in enumerate(lines):
        weight = "bold" if i == 0 else "normal"
        size = 11 if i == 0 else 9.5
        color = INK if i == 0 else MUTED
        out.append(f'<text x="{x + w / 2}" y="{y0 + i * lh}" font-size="{size}" '
                   f'text-anchor="middle" fill="{color}" font-weight="{weight}">'
                   f'{escape(line)}</text>')
    return "\n".join(out)


def anchor(b, side):
    _id, x, y, w, h, *_ = b
    return {
        "l": (x, y + h / 2), "r": (x + w, y + h / 2),
        "t": (x + w / 2, y), "b": (x + w / 2, y + h),
    }[side]


def arrow(boxes, a):
    src, dst, label, style = (a + (None,))[:4] if len(a) == 3 else a
    s_id, s_side = src.split(".")
    d_id, d_side = dst.split(".")
    x1, y1 = anchor(boxes[s_id], s_side)
    x2, y2 = anchor(boxes[d_id], d_side)
    color = {"money": "#2f855a", "data": "#1f6f8b", "ctrl": "#b7791f",
             "risk": "#c53030"}.get(style or "data")
    dash = ' stroke-dasharray="4 3"' if style == "data" else ""
    marker = f"url(#m-{style or 'data'})"
    # Orthogonal path: horizontal-first when leaving left/right, else vertical-first.
    if s_side in "lr" and d_side in "lr":
        mx = (x1 + x2) / 2
        d = f"M{x1},{y1} L{mx},{y1} L{mx},{y2} L{x2},{y2}"
        lx, ly = mx, (y1 + y2) / 2
    elif s_side in "tb" and d_side in "tb":
        my = (y1 + y2) / 2
        d = f"M{x1},{y1} L{x1},{my} L{x2},{my} L{x2},{y2}"
        lx, ly = (x1 + x2) / 2, my
    elif s_side in "lr":
        d = f"M{x1},{y1} L{x2},{y1} L{x2},{y2}"
        lx, ly = (x1 + x2) / 2, y1
    else:
        d = f"M{x1},{y1} L{x1},{y2} L{x2},{y2}"
        lx, ly = x1, (y1 + y2) / 2
    out = [f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.5"{dash} '
           f'marker-end="{marker}"/>']
    if label:
        parts = label.split("\n")
        width = max(len(p) for p in parts) * 5.4 + 8
        height = 12 * len(parts) + 4
        out.append(f'<rect x="{lx - width / 2}" y="{ly - height / 2}" width="{width}" '
                   f'height="{height}" fill="white" opacity="0.92" rx="2"/>')
        for i, p in enumerate(parts):
            out.append(f'<text x="{lx}" y="{ly - height / 2 + 12 + i * 12}" '
                       f'font-size="9" text-anchor="middle" fill="{color}">{escape(p)}</text>')
    return "\n".join(out)


def legend(x, y, items):
    out = []
    for i, (kind, text) in enumerate(items):
        fill, stroke = KINDS[kind]
        xi = x + i * 150
        out.append(f'<rect x="{xi}" y="{y}" width="14" height="10" fill="{fill}" '
                   f'stroke="{stroke}" stroke-width="1.2"/>')
        out.append(f'<text x="{xi + 20}" y="{y + 9}" font-size="9.5" fill="{MUTED}">'
                   f'{escape(text)}</text>')
    return "\n".join(out)


def line_legend(x, y):
    items = [("money", "Funds movement"), ("data", "Data / events"), ("ctrl", "Control / approval")]
    out = []
    for i, (style, text) in enumerate(items):
        color = {"money": "#2f855a", "data": "#1f6f8b", "ctrl": "#b7791f"}[style]
        dash = ' stroke-dasharray="4 3"' if style == "data" else ""
        xi = x + i * 150
        out.append(f'<line x1="{xi}" y1="{y + 5}" x2="{xi + 22}" y2="{y + 5}" '
                   f'stroke="{color}" stroke-width="1.5"{dash}/>')
        out.append(f'<text x="{xi + 28}" y="{y + 9}" font-size="9.5" fill="{MUTED}">'
                   f'{escape(text)}</text>')
    return "\n".join(out)


def render(name, width, height, boxes, arrows, legend_items, lines=True):
    by_id = {b[0]: b for b in boxes}
    defs = "".join(
        f'<marker id="m-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        for k, c in {"money": "#2f855a", "data": "#1f6f8b", "ctrl": "#b7791f", "risk": "#c53030"}.items()
    )
    groups = [b for b in boxes if b[6] == "group"]
    others = [b for b in boxes if b[6] != "group"]
    body = [box(b) for b in groups]
    body += [arrow(by_id, a) for a in arrows]
    body += [box(b) for b in others]
    body.append(legend(10, height - 34, legend_items))
    if lines:
        body.append(line_legend(10, height - 16))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
           f'width="{width}" height="{height}" font-family="{FONT}">'
           f'<defs>{defs}</defs><rect width="100%" height="100%" fill="white"/>'
           + "\n".join(body) + "</svg>")
    (OUT / f"{name}.svg").write_text(svg)


STD_LEGEND = [("buy", "Purchased / third party"), ("build", "Cyclone-built"),
              ("member", "Member / external"), ("chain", "On-chain location")]

# ---------------------------------------------------------------- Option 2: architecture
render("opt2-architecture", 820, 470, [
    ("app", 20, 20, 780, 40, "Member web app (Cyclone)\nsignup · referral link · team view · wallet · Deposits · withdrawals", "build"),
    ("bo", 20, 80, 780, 40, "Admin back office (Cyclone)\nroles · maker-checker approvals · audit log · case links", "build"),
    ("api", 20, 140, 780, 36, "Integration layer and orchestration (Cyclone)\nidempotent events · webhooks · retries · feature gates (KYC tier, jurisdiction, kill switches)", "build"),
    ("led", 20, 200, 180, 70, "Platform ledger\nsingle financial source of truth\nreconciliation", "build"),
    ("mlm", 215, 200, 180, 70, "MLM core (MLM Soft)\nSponsor Tree · plan versions\nCommission calculation", "buy"),
    ("wal", 410, 200, 180, 70, "Wallet layer (Privy)\nMember embedded wallets\npolicies · Earn API", "buy"),
    ("kyc", 605, 200, 195, 70, "Verification (Sumsub / Didit)\nKYC tiers · sanctions\nwallet screening", "buy"),
    ("tre", 20, 290, 180, 56, "Operator treasury\nkey quorum or Cobo / Fireblocks", "buy"),
    ("idx", 215, 290, 180, 56, "Chain indexer / RPC\nindependent deposit check", "buy"),
    ("yld", 410, 290, 180, 56, "Yield adapter (later)\nPrivy Earn → Morpho / Aave", "buy"),
    ("hd", 605, 290, 195, 56, "Helpdesk\nZendesk / Freshdesk", "buy"),
    ("chain", 20, 366, 570, 40, "Public blockchains (assets and networks supported by the chosen components)", "chain"),
    ("mem", 605, 366, 195, 40, "Members · support agents", "member"),
], [
    ("led.b", "tre.t", None, "ctrl"),
    ("idx.b", "chain.t", None, "data"),
    ("wal.b", "yld.t", None, "ctrl"),
], STD_LEGEND, lines=False)

# ---------------------------------------------------------------- Option 2: fund flow
render("opt2-fundflow", 820, 390, [
    ("g_mem", 10, 10, 430, 320, "Member-controlled", "group"),
    ("g_op", 460, 10, 350, 320, "Operator-controlled", "group"),
    ("ext", 30, 40, 170, 50, "Member's own wallet\nor exchange account", "member"),
    ("mw", 230, 140, 190, 60, "Member embedded wallet\nPrivy, Member-owned", "chain"),
    ("out", 30, 250, 170, 50, "External address\nMember-signed withdrawal", "member"),
    ("vault", 230, 250, 190, 60, "Lending vault (later)\nMorpho / Aave, ERC-4626\nshares held by Member", "chain"),
    ("led", 480, 40, 150, 50, "Platform ledger\nobserves and reconciles", "build"),
    ("mlm", 650, 40, 150, 50, "MLM core\ncalculates Commissions", "buy"),
    ("tre", 480, 140, 150, 60, "Operator treasury\nquorum approval", "chain"),
    ("ops", 650, 140, 150, 60, "Finance approvers\nmaker-checker\naddress screening", "build"),
    ("fee", 650, 250, 150, 60, "Platform fee wallet\nshare of yield only", "chain"),
], [
    ("ext.r", "mw.t", "crypto Deposit", "money"),
    ("mw.l", "out.t", "withdrawal", "money"),
    ("mw.b", "vault.t", "deposit via scoped signer", "money"),
    ("vault.r", "fee.l", "fee on yield (not principal)", "money"),
    ("tre.l", "mw.r", "Commission\npayout", "money"),
    ("mlm.l", "led.r", None, "data"),
    ("led.b", "tre.t", "approved batch", "ctrl"),
    ("ops.l", "tre.r", None, "ctrl"),
], STD_LEGEND)

# ---------------------------------------------------------------- Option 1: architecture + fund flow
render("opt1-integrated", 820, 380, [
    ("g_v", 200, 10, 410, 250, "White-label MLM vendor (Epixel / Cloud MLM)", "group"),
    ("mem", 20, 60, 160, 50, "Member", "member"),
    ("portal", 220, 40, 180, 50, "Member portal\nvendor UI, white-labelled", "buy"),
    ("eng", 420, 40, 170, 50, "Comp engine\nSponsor Tree, Commissions", "buy"),
    ("ew", 220, 120, 370, 56, "Vendor e-wallet\ninternal balances; payouts executed inside vendor software", "buy"),
    ("roi", 220, 196, 180, 44, "\"ROI / staking\" module\nmust be disabled", "risk"),
    ("adm", 420, 196, 170, 44, "Vendor admin panel\nCyclone customisation", "buy"),
    ("gw", 630, 120, 170, 56, "Crypto gateway\nCoinPayments (custodial)\nor undocumented", "risk"),
    ("chain", 630, 220, 170, 40, "Blockchains", "chain"),
    ("cust", 20, 280, 780, 44, "Custody and signing authority not documented by any candidate · \"smart contract\" claims without addresses or audits", "risk"),
], [
    ("mem.r", "portal.l", None, "data"),
    ("mem.b", "ew.l", "Deposit", "money"),
    ("ew.r", "gw.l", None, "money"),
    ("gw.b", "chain.t", None, "money"),
], STD_LEGEND + [("risk", "Unverified / high risk")])

# ---------------------------------------------------------------- Option 3: QUANT Phase 2
render("opt3-quant", 820, 330, [
    ("g_mem", 10, 10, 420, 250, "Member-controlled", "group"),
    ("g_q", 450, 10, 360, 250, "Phase 2 only, after due diligence", "group"),
    ("mw", 30, 50, 170, 56, "Member embedded wallet\ncore balance", "chain"),
    ("sub", 240, 50, 170, 56, "Separate trading account\nopt-in, capped amount", "chain"),
    ("hl", 240, 170, 170, 56, "Hyperliquid account\nowned by Member", "chain"),
    ("agent", 470, 170, 150, 56, "Trade-only API key\ncannot withdraw", "buy"),
    ("eng", 470, 50, 150, 56, "QUANT trading engine\nstrategy signals", "risk"),
    ("mon", 660, 50, 140, 56, "Cyclone risk monitor\nlimits · kill switch", "build"),
    ("led", 30, 170, 170, 56, "Platform ledger\nseparate sub-ledger\nfor trading P&L", "build"),
    ("disc", 660, 170, 140, 56, "Legal sign-off\ndisclosures before\nenablement", "build"),
], [
    ("mw.r", "sub.l", "opt-in", "money"),
    ("sub.b", "hl.t", None, "money"),
    ("eng.b", "agent.t", None, "ctrl"),
    ("agent.l", "hl.r", "orders", "ctrl"),
    ("mon.l", "eng.r", None, "ctrl"),
    ("hl.l", "led.r", "P&L", "data"),
], STD_LEGEND + [("risk", "Unverified component")])

print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
