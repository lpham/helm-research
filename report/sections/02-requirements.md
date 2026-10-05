# Business requirements and working assumptions

## Business context

AlphaWave has an established MLM distribution network and wants to offer a financial product through it. The intended platform covers:

- Member onboarding and sponsor attribution;
- wallets or smart accounts;
- crypto Deposits and withdrawals;
- a product currently described as "staking", whose mechanism is not yet defined;
- MLM genealogy and configurable compensation plans;
- administrative tools and customer support;
- fiat deposits, either in the first release or later.

An associated trading company, QUANT, has built an MVP covering onboarding and smart-account creation, and intends to connect a trading engine to Hyperliquid. Its capabilities have not been independently verified. Cyclone is the implementation company and technology lead. It prefers to buy core software and integrate it rather than build core systems.

No operating jurisdiction, legal entity or target market has been confirmed. This report is therefore jurisdiction-neutral. AlphaWave will engage legal counsel on regulatory obligations; nothing in this report is legal advice, and no vendor software or certification authorises the business model.

## Requirements as understood

The client's product requirements document (PRD) and compensation plan overview were treated as statements of business intention, not as validated specifications. The scope below reflects those documents and the decisions taken during this research.

| Area | First release | Later phases |
|---|---|---|
| Onboarding | Signup, sponsor attribution, referral link, privacy-safe downline view | Campaigns, academy, gamification |
| Wallets | Member-owned embedded wallets; separate operator treasury | Additional chains and assets |
| Deposits | Crypto only, assets and networks as supported by the selected components | Fiat on-ramp, subject to provider approval and legal review |
| Withdrawals | Crypto to the Member's own external address | Fiat off-ramp |
| Yield Product | Not live with real funds; provider-neutral adapter and read-only or test-network demonstration | Lending vaults or Staking through a named provider, after legal confirmation |
| MLM | Sponsor Tree, compensation plan configured in the bought engine, Commission calculation separate from payout, tested against defined cases | Full plan, simulations, campaigns |
| Operations | Admin back office with roles, approvals and audit trail; helpdesk | CRM, advanced analytics |
| Trading | None | QUANT integration via Hyperliquid, with restrictions (Option 3) |

## Working assumptions

The following assumptions underpin the recommendations. Each one that materially changes the outcome is flagged in section 11 as a decision for the client.

1. **Cyclone leads technology** and acts as integrator of purchased core software. Self-built compensation engines, including QUANT's, are excluded.
2. **Jurisdiction-neutral design.** Controls are designed to be switched on by policy once counsel has identified obligations.
3. **Privy is the base case for Member wallets**, without any of its Stripe- or Bridge-backed features.
4. **Tiered KYC (scenario B) is the base case** for tooling and cost estimates (see section 3.5).
5. **The commission base is open.** The compensation plan overview pays Commissions on subscription sales, but that model has been superseded. This report presents the bases that real software supports and their structural risks; the client must confirm the base.
6. **Web-first delivery.** The PRD itself excludes a standalone mobile app from the first release.
7. **Pilot scale** for cost purposes: up to 3,000 commission-active Members, under 10,000 monthly active wallet users and about 1,000 new Members per month.

## Contradictions in the reference documents

The research brief takes precedence where documents conflict. The following contradictions and unresolved assumptions were found:

| # | Topic | Observation | Treatment in this report |
|---|---|---|---|
| 1 | Status of the PRD | The PRD calls itself a "final-programme draft", yet leaves custody, compensation formulas, payout rates, KYC thresholds, return claims and vendor selection open. | Treated as non-binding intention. |
| 2 | "Staking" timing | The brief lists staking as a proposed component; the PRD places "Staking or Saving" in Phase 2 and says it "requires a separate definition before build". | Yield Product researched in full but not live in Release 1. |
| 3 | KYC | The client assumes crypto Deposits need no KYC. The PRD leaves KYC open and gated on legal approval; the compensation plan requires KYC for Certified Leader rank and above. | Assumption treated as unverified; tiered KYC is the base case. |
| 4 | Commission base | The compensation plan pays only on subscription sales. That model has since been superseded and the new base is undefined. | Bases compared on evidence; decision required (section 11). |
| 5 | Build status | The compensation plan says the engine is "fully built into the system" and switched off; the PRD says no formula is approved. The brief says Cyclone prefers to buy. | Self-built engines excluded; a bought engine is recommended. |
| 6 | Plan arithmetic | Level rates for levels 2–10 are missing, so total payout cannot be checked against the stated 30% cap per sale. Whether the leadership match counts toward the cap is unclear. | Listed as client questions. |
| 7 | QUANT and Hyperliquid | Central to the brief but absent from the client documents. | QUANT treated as a Phase 2 integration only. |
| 8 | Scope breadth | The PRD roadmap includes binary options, B-Books, debit cards and fund products. | Not researched; flagged as high-sensitivity later-phase items. |
| 9 | Recruitment-based qualification | Ranks depend on counts of verified referrals and active enrollees, and leadership ranks require "plan tier 7 or higher". | Flagged for legal review as an observation, not a conclusion. |
