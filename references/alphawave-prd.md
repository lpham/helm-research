# Alpha Wave Product Requirements Document

Status: final-programme draft for DOCS4.

Product: Alpha Wave.

Domain: `firstwavealpha.com`.

## 1. Authority

This document is the current final-folder PRD for Alpha Wave. It is governed by
the feature taxonomy in `docs/Latest Product Updates/Helm PRD Features.md` and
the canonical baseline in `docs/Latest Product Updates/Alpha Wave Source of
Truth Brief.md`, `docs/Latest Product Updates/Alpha Wave Product Story.md`, and
`docs/Latest Product Updates/Alpha Wave PRD.md`.

The phase list is authoritative for forward product scope. Meeting notes may
clarify a listed feature, expose technical context, or mark a conflict, but a
meeting-only idea does not become product scope unless a later written ruling
adds it.

This PRD does not approve custody, card issuance, fund management, investment
advice, financial advice, compensation formulas, payout rates, KYC thresholds,
subscription prices, return claims, trading venues, book models, or vendor
selection. Those items remain `OPEN` where the sources have not settled them.

Source anchors:

- `Helm PRD Features.md :: PHASE 0` through `PHASE 4`
- `Alpha Wave Source of Truth Brief.md :: Governing Rules`
- `Alpha Wave Product Story.md :: Source Rule`
- `Alpha Wave PRD.md :: Authority`
- `AGENTS.md :: The stealth launch`
- `AGENTS.md :: Hard rules`

## 2. Product Intent

Alpha Wave is a phase-gated financial services product with a referral-driven
growth engine, member identity, wallet and account surfaces, trading-adjacent
workflows, support, education, compliance evidence, reward systems, and later
institutional financial layers.

The first product spine is simple: a member signs up, is correctly attributed to
their sponsor path, receives a system-controlled referral link, shares it, and
can see their downline form without exposing private identity data. Everything
that touches deposits, payouts, subscriptions, trading, cards, support vendors,
wallets, compensation, or fund products is added behind explicit phase gates and
security review.

The product must be useful at each phase without pretending later phases are
already live. A gated surface may be visible as a roadmap or blocked state only
when the copy is truthful and the backing system refuses unavailable data rather
than inventing values.

## 3. Product Principles

P1. Feature-list authority.

Every forward requirement must trace to the approved phase feature list. Meeting
notes explain, constrain, or qualify those features. They do not add scope by
themselves.

P2. Gate, do not erase.

Out-of-phase features remain designed behind gates. Gates are reversible policy
or configuration controls, not destructive deletion. If a feature has ledgers,
jobs, audit records, or regulatory evidence, those records continue to exist
behind the gate.

P3. Real data or refusal.

Balances, earnings, rewards, portfolios, trade activity, genealogy counts,
subscription status, support status, compliance state, and fund data must come
from real records. If a source is absent, stale, unavailable, or unapproved, the
product says unavailable or blocked. It does not present invented figures.

P4. Member privacy.

A member's chosen public identifier is the only peer-facing identity. Real
names, emails, contact details, private support notes, compliance records,
wallet secrets, and sensitive financial records are not exposed to other
members.

P5. Money integrity.

Any money path uses integer minor units, append-only ledgers, auditable state
changes, idempotency where commands can repeat, and explicit refusal when the
system cannot verify eligibility or source records.

P6. Referral integrity.

Referral codes are system generated. A member cannot choose, influence, guess,
rotate, or self-assign their own code or sponsor. Attribution is resolved
server-side and fails closed.

P7. Financial restraint.

The product records choices and evidence, but does not claim to provide
financial advice, investment advice, return assurances, principal protection,
regulatory approval, or liquidity assurances.

P8. Vendor neutrality.

Meeting notes mention possible vendors and implementation approaches. This PRD
does not select them unless a source ruling has done so. Candidate vendors and
paths remain options for later technical and commercial decisions.

## 4. Personas

Member:

- Creates an Alpha Wave account.
- Receives and shares a system-controlled referral link.
- Views their account, referral path, team growth, allowed wallet surfaces, and
  gated financial surfaces.
- Completes compliance, risk, advice-evidence, subscription, or support flows
  when a phase requires them.

Leader or builder:

- Invites members through referral and campaign tools.
- Monitors downline growth using member-safe identifiers.
- Needs team insights and support routing without direct access to private
  member contact details.

Support agent:

- Works cases through approved tooling.
- Sees only the minimum member data required for the case.
- Cannot request private keys, bypass policy gates, change sponsor placement,
  approve payouts outside controls, or make financial recommendations.

Admin operator:

- Oversees operations, audit, feature gates, campaign management,
  compensation-review workflows, support escalation, payout-readiness checks,
  and compliance evidence.
- Uses role-scoped authority, with sensitive actions logged.

Compliance and policy reviewer:

- Reviews KYC, source-of-funds, Risk Analyzer, Record of Advice, support copy,
  trading disclosures, card disclosures, compensation controls, and fund-layer
  restrictions.

Product and technical operator:

- Evaluates implementation approaches, vendor candidates, data sources, and
  integration patterns.
- Must not convert an option from the meetings into a final product decision
  without a written ruling.

## 5. Scope

This PRD covers:

- Phase 0 through Phase 4 product requirements.
- Launch-critical signup, referral attribution, genealogy, team visibility, and
  support.
- Wallet, account, portfolio, trading, transfer, earn, deposit, payout,
  subscription, reward, academy, support, compensation, risk, advice-evidence,
  card, saving, fund-data, binary-options, book, and institutional features as
  gated phase requirements.
- Data requirements, security controls, acceptance criteria, and open decisions
  needed before downstream implementation.

This PRD excludes:

- Any feature absent from the phase list unless later ruled in.
- Standalone mobile application scope.
- Prop-trading paper accounts.
- Prediction markets as a separate product from listed Binary Options.
- Token acquisition or partnership-token reward products.
- Admin CRM as a user-facing product.
- Repository migration tasks as product features.
- Specific user-count targets, latency values, prices, card colors, cashback
  values, KYC thresholds, compensation rates, payout formulas, and return
  figures.

## 6. Global Functional Requirements

### GFR-001 Source Traceability

Every product requirement, story, and phase plan must identify the feature-list
phase it belongs to. If a requirement comes from meeting context, it must also
name the listed feature it clarifies.

Acceptance:

- No forward requirement is sourced only to a meeting transcript.
- Meeting-only ideas appear only in excluded-scope or open-decision sections.
- Phase conflicts are documented as `OPEN`.

### GFR-002 Member Account Creation

Alpha Wave must support account creation through approved signup channels while
preserving referral attribution and separating general onboarding from
checkout, KYC, Risk Analyzer, and later trading decision flows.

Acceptance:

- A referral visit carries attribution through account creation.
- An absent, expired, invalid, or tampered referral context does not create a
  false sponsor assignment.
- Email changes require re-verification before they become account authority.
- Social login, email login, and identity provider choices remain vendor
  decisions until ruled.

Source anchors: `Tech Team Meet :: User onboarding and registration flow`,
`Tech Team Meet :: Data Persistence and Session Management`.

### GFR-003 Referral Link And Genealogy

The referral system must issue system-controlled referral links, assign sponsor
placement server-side, and support genealogy views that show only allowed
member identifiers.

Acceptance:

- Referral code generation is not user controlled.
- A member cannot self-assign, overwrite, or move their sponsor.
- Genealogy views do not expose emails, legal names, direct contact details, or
  private support data.
- Any feature that walks or aggregates the tree must meet the repository depth
  rule before implementation.

Source anchors: `Alpha Wave PRD.md :: G6. Referral integrity`,
`Meeting started 2026_10_02 16_46 :: Phase One Signup, Onboarding, and
Genealogy Scaling`.

### GFR-004 Team And Campaign Management

Team management and campaign management must help leaders understand network
growth, campaign attribution, and invite performance without exposing peer PII
or allowing members to manipulate attribution.

Acceptance:

- Team views use member-safe identifiers.
- Campaign links, expiry, reward overrides, and campaign analytics require
  audit records before activation.
- Direct member-to-member email or contact exposure is not required by this
  PRD.
- Campaign performance uses real event records.

Source anchors: `Meeting started 2026_10_02 19_13 :: Team Management and
Campaign Management Goals`, `Meeting started 2026_10_02 19_13 :: Team
Management Communication and Support`.

### GFR-005 Wallet Surfaces

Cold wallet, smart wallet, smart contract wallet, smart contract service,
deposit, transfer, payout, and strategy permission flows must treat private-key
or signature misuse as a critical risk.

Acceptance:

- Support and third-party scripts cannot request or capture private keys.
- Wallet permissions, if implemented, are explicit, auditable, and revocable
  where the chosen architecture allows.
- Smart execution permissions are distinct from custody claims.
- Deposit, transfer, and payout commands are refused when eligibility, source
  records, or required policy decisions are missing.

Source anchors: `Tech Team Meet :: Cold Wallet and Smart Contract
Architecture`, `Meeting started 2026_10_02 16_46 :: API Access and Security
Risks Involving Private Keys`.

### GFR-006 Portfolio, Trading, And Transparency

Portfolio, invest, active trade, user manual trading, live charts, monitoring,
transparency, fund data tracking, B-Books, and Hybrid Book features must use
real system or approved external records and must disclose data state clearly.

Acceptance:

- Portfolio values identify their source category: ledger, wallet, venue,
  strategy, fund record, or approved external feed.
- Live charts show real data and label delay, derivation, or unavailability.
- Trade markers reconcile to real orders, fills, transactions, or ledger
  records.
- Trading architecture remains `OPEN` across API-only, SDK, internal runtime,
  and hybrid approaches.
- B-Books and Hybrid Book do not ship without conflict, legal, venue, custody,
  and risk review.

Source anchors: `Meeting started 2026_10_02 16_46 :: Transparency Layers,
Quantitative Engine, and Trading Runtimes`, `Tech Team Meet :: Trade execution
infrastructure`, `Meeting started 2026_10_02 16_46 :: Portfolio Management and
Hybrid Book Architecture`.

### GFR-007 Earn, Rewards, Subscription, And Access Gates

Earn, Rewards, Subscription, Daily Active Rewards, and card-tier gamification
are separate concepts with separate data sources and controls.

Acceptance:

- Earn is backed by earning records, commissions, trading activity, manual
  trading earnings, or approved financial records.
- Rewards can represent non-cash benefits, points, access, rank, perks, or
  tier progress where approved.
- Subscription gates can block or unlock feature access without rewriting
  financial ledgers.
- Values, prices, grace periods, thresholds, and tier benefits remain `OPEN`
  unless a later ruling settles them.

Source anchors: `Meeting started 2026_10_02 16_46 :: Rewards, Non-Monetary
Subscriptions, and Feature Gating`, `Meeting started 2026_10_02 19_13 ::
Rewards and Earn Engines`.

### GFR-008 Support, Academy, And FAQ

Support, advanced support, basic academy, advanced academy, and advanced FAQ
features must help members without exposing sensitive information or presenting
education as financial advice.

Acceptance:

- Support is ticketed, role-scoped, and auditable.
- AI support, if used, is constrained to approved knowledge and escalation.
- Academy content can include readings, checklists, courses, and reference
  material, but cannot promise outcomes.
- Advanced FAQ responses cannot override compliance, support escalation, or
  product gates.

Source anchors: `Meeting started 2026_10_02 16_46 :: Support System and
AI-Powered Ticketing`, `Meeting started 2026_10_02 16_46 :: Basic academy
content implementation standard`, `Meeting started 2026_10_02 16_46 :: Phase
Two Staking, Layer Three Integration, and Advanced Academy`.

### GFR-009 Compensation Plan

The current compensation plan can be represented as current-state input in
Phase 0. Stress testing occurs in Phase 1. Full compensation-plan activation
belongs to Phase 2 after review and approval.

Acceptance:

- No new formula, payout rate, rank math, or payable rule is introduced in this
  PRD.
- Stress testing examines exploit resistance, auditability, payout integrity,
  and scale behavior.
- A payout engine is required before payable compensation is activated.
- Product docs must distinguish stress-test output from payable rules.

Source anchors: `Meeting started 2026_10_02 16_46 :: Compensation Plan Stress
Testing and Compliance Audit Trails`, `Meeting started 2026_10_02 19_13 ::
Compensation Plan Engines and Technology Evaluation`.

### GFR-010 Risk Analyzer And Record Of Advice

Risk Analyzer and Record of Advice collect classification, consent, policy, and
decision evidence. They do not provide advice.

Acceptance:

- Risk labels, if used, are classifications only.
- Record of Advice stores evidence of independent user choices, policy version,
  disclosures, consent, and renewal state.
- Question count, renewal triggers, and product-gate consequences remain
  `OPEN`.
- Risk and advice evidence is not visible to peers.

Source anchors: `Tech Team Meet :: Risk analyzer and record of advice`,
`Meeting started 2026_10_02 19_13 :: Compliance Database and Record of Advice
Engine`.

### GFR-011 Institutional Layers

CeFi, Fund Management, and Fund of Funds are Phase 4 institutional-scope
features requiring separate legal, custody, entity, reporting, audit, and
operational design.

Acceptance:

- No fund structure, custodian, jurisdiction, fee model, manager authority, or
  launch date is assumed.
- Member access remains gated until legal and compliance approval exists.
- Source-of-funds, KYC, reporting, audit, and suitability controls are designed
  before implementation.

Source anchors: `Meeting started 2026_10_02 19_13 :: Product roadmap and
development phases`, `Meeting started 2026_10_02 16_46 :: Phase Three Binary
Trading, Phase Four Institutional Banking, and Mobile App Strategy`.

## 7. Non-Functional Requirements

### NFR-001 Security

Auth, session, money, wallet, support, referral, admin, trading, card, and fund
surfaces require adversarial security review before build acceptance. Client
input cannot determine identity, sponsor, rank, role, payout, wallet authority,
or trading eligibility without server-side verification.

### NFR-002 Privacy

The product must minimize PII exposure across member, leader, support, admin,
export, and analytics surfaces. Peer-facing responses contain member-safe
identifiers only.

### NFR-003 Auditability

Sensitive commands must create durable audit records with actor, authority,
target, previous state where safe to record, new state, reason, timestamp, and
idempotency key where applicable.

### NFR-004 Data Refusal

Unavailable, unapproved, stale, or untrusted data must produce an unavailable
or blocked state. The product must not silently coerce unknown values to zero,
empty lists, generic success, or invented examples.

### NFR-005 Accessibility And Clarity

Phase-gated and blocked states must clearly tell the member whether a feature
is unavailable, pending verification, blocked by policy, or not yet in their
phase. The copy must not create a promise of financial outcome.

### NFR-006 Observability

Every sensitive flow requires logs, metrics, and alerts sufficient to
investigate failures without exposing private data in logs.

## 8. Phase Requirements

### Phase 0: Baseline Foundation

Authoritative features: Sign Up and Onboarding; Referral Link and Genealogy;
Cold Wallet; Smart Contract Wallet; Team Management; Portfolio; Account; Invest
or Active Trade; Transfer; Earn; Support; current compensation-plan input;
Deposit; Payout.

Outcome:

Phase 0 establishes account identity, referral attribution, basic genealogy,
team visibility, account surfaces, wallet-adjacent surfaces, support, current
comp-plan input, and gated money-path readiness.

Detailed requirements:

- P0-001 Signup creates a member account with verified contact state according
  to the chosen identity provider.
- P0-002 Referral attribution persists from link visit through account creation.
- P0-003 Referral codes are generated by the system and audited.
- P0-004 Genealogy displays member-safe identifiers and downline structure.
- P0-005 Team management shows direct and indirect team activity using real
  records.
- P0-006 Account displays identity, security, and profile state without
  exposing peer data.
- P0-007 Cold wallet and smart contract wallet surfaces remain gated until the
  architecture and security controls are approved.
- P0-008 Portfolio, invest, active trade, transfer, earn, deposit, and payout
  surfaces show blocked or unavailable states unless backed by real records and
  approved gates.
- P0-009 Support is available through controlled channels and forbids
  private-key sharing.
- P0-010 Current comp-plan input can be documented for stress-test preparation
  but cannot create new payable rules.

Phase 0 exit criteria:

- Account creation and referral attribution work end to end.
- Genealogy and team views do not expose private identity.
- Support path is live and safe.
- Money-path surfaces are either correctly gated or backed by approved real
  data and controls.
- Open money, wallet, payout, and compensation decisions are registered.

### Phase 1: Operating Platform

Authoritative features: Phase 0 features plus Campaign Management, Rewards,
Monitoring, Transparency, Fiat Onramp/Offramp, Subscription, Academy Basic,
trusted third-party Support, Comp Plan Stress Test, Risk Analyzer, Record of
Advice, Debit Card, and Gamification for Debit Card Tiers.

Outcome:

Phase 1 turns the foundation into an operating member platform with acquisition,
support, access gates, education, compliance evidence, transparency, and
financial-account surfaces.

Detailed requirements:

- P1-001 Signup supports the approved identity paths while preserving referral
  attribution.
- P1-002 Campaign management supports campaign-specific links, campaign state,
  attribution, expiry, and audit before reward overrides are activated.
- P1-003 Rewards are modeled separately from Earn and compensation.
- P1-004 Monitoring and Transparency expose real status, trade, ledger, wallet,
  or event evidence.
- P1-005 Fiat onramp/offramp remains vendor-neutral and gated pending provider,
  KYC, payments, chargeback, jurisdiction, and settlement decisions.
- P1-006 Subscription gates premium access according to approved billing and
  access policy.
- P1-007 Academy Basic provides educational material and checklists without
  financial advice.
- P1-008 Trusted third-party support can be adopted only after security review
  for data access, wallet safety, screen visibility, retention, and role scope.
- P1-009 Compensation plan stress testing evaluates the current plan without
  activating new payable rules.
- P1-010 Risk Analyzer and Record of Advice capture evidence and consent
  without making advice claims.
- P1-011 Debit Card and card-tier gamification stay listed in Phase 1, while
  activation timing and provider choices remain `OPEN`.

Phase 1 exit criteria:

- Campaign attribution cannot compromise referral integrity.
- Rewards, Earn, Subscription, and compensation are separated in data and copy.
- Transparency surfaces reconcile to real evidence.
- Risk Analyzer and Record of Advice have compliance-approved copy and storage.
- Vendor-dependent features have decision records before activation.

### Phase 2: Platform Depth

Authoritative features: Sign Up and Onboarding; Staking or Saving; Support
Advanced; Academy Advanced; Comp Plan Full; Smart Contract Service; Offline
Engine; Layer 3; Fund Data Tracking; TA Capital Trade Deck; Advanced FAQs.

Outcome:

Phase 2 deepens the platform with advanced support and education, saving or
staking exploration, full compensation-plan readiness, smart contract service
work, offline calculation capability, layer integration, and fund-data tracking.

Detailed requirements:

- P2-001 Sign-up remains compatible with Phase 1 account and attribution rules.
- P2-002 Staking or Saving requires a separate definition before build:
  recurring saving, staking contracts, savings product, or another approved
  form.
- P2-003 Advanced Support can include AI assistance only inside approved
  knowledge, escalation, and data boundaries.
- P2-004 Academy Advanced requires curriculum ownership, content taxonomy,
  review process, and non-advice guardrails.
- P2-005 Comp Plan Full requires approved formulas, audit controls, payout
  engine, ledger design, reversal path, and security review.
- P2-006 Smart Contract Service requires wallet, signature, chain, permission,
  revocation, support, and audit design.
- P2-007 Offline Engine can compute eligibility, compensation, fund tracking,
  or strategy-derived values only from approved data and must label freshness.
- P2-008 Layer 3 remains an architectural placeholder until the technical
  design defines the layer and its role.
- P2-009 Fund Data Tracking must reconcile to real fund, wallet, venue, ledger,
  or approved external records.
- P2-010 TA Capital Trade Deck remains listed but requires discovery before
  detailed requirements can be approved.
- P2-011 Advanced FAQs must use approved content and escalation paths.

Phase 2 exit criteria:

- Saving or staking scope is formally defined.
- Advanced support and FAQ data boundaries are approved.
- Full compensation plan passes product, legal, security, and ledger review.
- Fund data tracking has reconciled sources and refusal states.
- Smart contract service has a threat model and operational controls.

### Phase 3: Daily Engagement And Trading Features

Authoritative features: Gamification; Daily Active Rewards; Binary Options;
User Manual Trading; Live Charts; B-Books; Hybrid Book.

Outcome:

Phase 3 adds active daily engagement and higher-risk trading experiences. It
requires stronger conduct, disclosure, suitability, market-data, order, and
conflict controls.

Detailed requirements:

- P3-001 Gamification must not obscure financial risk or drive unsuitable
  behavior.
- P3-002 Daily Active Rewards require conduct review, reward limits, abuse
  controls, and non-misleading copy.
- P3-003 Binary Options require a standalone legal, ethical, pool-math, odds,
  loss-disclosure, jurisdiction, and responsible-use design.
- P3-004 User Manual Trading requires approved venue, order, wallet, risk,
  Record of Advice, and support paths.
- P3-005 Live Charts use real market data or clearly labeled delayed or
  unavailable states.
- P3-006 B-Books require definition before requirements can be finalized.
- P3-007 Hybrid Book requires conflict disclosure, venue policy, custody,
  ledgering, routing, member disclosure, and legal review.

Phase 3 exit criteria:

- Binary Options have a separate approved design.
- Trading architecture is selected and reviewed.
- Live data sources are contracted, monitored, and labeled.
- Book models have conflict and compliance approval.
- Rewards do not bypass suitability, subscription, or compliance controls.

### Phase 4: Institutional Expansion

Authoritative features: CeFi; Fund Management; Fund of Funds.

Outcome:

Phase 4 expands Alpha Wave into institutional and fund-layer products. This is
not a member-facing promise until legal, operational, entity, custody, audit,
reporting, and compliance work is complete.

Detailed requirements:

- P4-001 CeFi requires definition of centralized-finance products, permitted
  jurisdictions, custody model, reporting, and member eligibility.
- P4-002 Fund Management requires fund structure, manager authority, custody,
  compliance, reporting, fee model, risk disclosures, valuation, and audit
  design.
- P4-003 Fund of Funds requires due diligence, allocation policy, monitoring,
  liquidity, valuation, conflict review, manager selection, and reporting
  design.
- P4-004 Member access remains gated until regulatory and operational approval
  exists.

Phase 4 exit criteria:

- Entity, custody, compliance, and audit model approved.
- Fund operations and reporting model approved.
- Member eligibility and access gating approved.
- Product copy reviewed for regulatory claims.

## 9. Data Requirements

The final implementation must define authoritative sources for:

- Member account, identity state, verification state, and profile state.
- Referral code, referral link, campaign link, sponsor placement, and
  attribution events.
- Genealogy edges and computed views.
- Team, campaign, and reward activity.
- Wallet records, addresses, smart permissions, signatures, deposits,
  transfers, payouts, and revocations.
- Portfolio positions, strategy allocations, order events, fills, transactions,
  charts, venue records, and fund data.
- Earn, reward, subscription, compensation, payout, and card-tier ledgers.
- Support tickets, support agent actions, escalation state, and approved
  support knowledge.
- Academy content, FAQ content, completion evidence, and content review state.
- Risk Analyzer answers, classification, Record of Advice, consent, policy
  version, renewal state, KYC, and source-of-funds evidence.
- Admin actions, gate changes, exports, and audit trails.

Data constraints:

- Unknown is not zero.
- Blocked is not success.
- Unavailable is not empty.
- Candidate provider is not selected provider.
- Stress-test output is not payable rule.
- Education is not advice.

## 10. Release Gates

Gate RG-001: Launch-critical referral gate.

Sign-up, referral attribution, referral link issuance, and genealogy must work
before leader launch.

Gate RG-002: Server-side feature gate.

Sensitive money, wallet, contribution, payout, support, trading, card,
subscription, and institutional routes require server-side gates before access.

Gate RG-003: Money gate.

Deposit, transfer, payout, Earn, compensation, subscription, card, and trading
flows require ledger, audit, idempotency, authorization, and refusal-state
design.

Gate RG-004: Wallet gate.

Wallet and smart permission flows require threat model, support policy, vendor
review, signature design, revocation, and recovery policy.

Gate RG-005: Trading gate.

Trading and book features require architecture selection, venue review, data
source review, risk disclosure, compliance review, and operational controls.

Gate RG-006: Compliance gate.

KYC, Risk Analyzer, Record of Advice, source-of-funds, jurisdiction, advice
copy, and renewal triggers require legal and compliance approval.

Gate RG-007: Vendor gate.

Support, CRM, payment, onramp, offramp, wallet, card, trade, market-data, and
compensation vendors require security, data, commercial, compliance, and
operational review.

Gate RG-008: Institutional gate.

CeFi, fund management, and fund of funds require entity, regulatory, custody,
audit, reporting, operations, and member eligibility approval.

## 11. Risks

RISK-001 Scope creep from meeting transcripts.

Control: enforce feature-list authority and excluded-scope review.

RISK-002 Private identity leakage through team, campaign, support, exports, or
analytics.

Control: member-safe identifiers, role-scoped data, response-shape review, and
export review.

RISK-003 Referral manipulation.

Control: server-side sponsor assignment, system-generated codes, audit logs,
and tamper refusal.

RISK-004 Wallet or signature compromise.

Control: no private-key requests, support restrictions, permission scoping,
revocation, vendor review, and logging.

RISK-005 Money-path inaccuracy.

Control: integer minor units, append-only ledgers, refusal states, idempotency,
and reconciliation.

RISK-006 Advice or return claim.

Control: compliance-reviewed copy, Record of Advice evidence, education
guardrails, and no guaranteed outcome language.

RISK-007 Vendor overcommitment.

Control: mark vendors as candidates until approved decision records exist.

RISK-008 Trading conflict or market-conduct failure.

Control: separate design for trading, Binary Options, B-Books, Hybrid Book,
and live data.

RISK-009 Fund-layer regulatory implication.

Control: Phase 4 institutional gate before any member-facing commitment.

## 12. Open Decisions

OPEN: Identity provider and social-login implementation.

OPEN: Genealogy product scale and presentation bounds, while implementation
must still meet the repository depth rule.

OPEN: Wallet architecture, wallet provider, smart contract wallet shape,
signature flow, revocation, and recovery.

OPEN: Deposit, payout, transfer, and source-of-funds policy.

OPEN: KYC timing, thresholds, renewal, and jurisdiction rules.

OPEN: Trading architecture across API-only, SDK, internal runtime, and hybrid
paths.

OPEN: Portfolio and transparency source-of-truth hierarchy.

OPEN: Support and CRM vendor selection.

OPEN: AI support scope and approved knowledge boundaries.

OPEN: Subscription pricing, grace period, non-payment behavior, and access
blocking.

OPEN: Rewards, card tiers, cashback, points, and benefit thresholds.

OPEN: Debit card activation phase, provider, colors, fees, wallet linkage, and
processing model.

OPEN: Compensation formulas, payout rates, trusted third-party engine, and
audit approach.

OPEN: Risk Analyzer question count, scoring, renewal triggers, and Record of
Advice language.

OPEN: Staking or Saving scope and whether it involves contracts, recurring
saving, or another approved product.

OPEN: Smart Contract Service and Layer 3 definitions.

OPEN: Fund Data Tracking source model and reconciliation rules.

OPEN: TA Capital Trade Deck details.

OPEN: Binary Options legal category, odds, pool math, responsible-use controls,
and loss disclosure.

OPEN: B-Books definition and controls.

OPEN: Hybrid Book conflict, venue, custody, routing, and disclosure model.

OPEN: CeFi, Fund Management, and Fund of Funds entity, custody, jurisdiction,
audit, reporting, and operations model.

## 13. Traceability

| PRD Area | Source anchor |
|---|---|
| Phase taxonomy | `Helm PRD Features.md :: PHASE 0` through `PHASE 4` |
| Feature-list authority | `Alpha Wave Source of Truth Brief.md :: Governing Rules` |
| Product narrative | `Alpha Wave Product Story.md :: The Arc` |
| Launch-critical flow | `AGENTS.md :: The stealth launch` |
| Member privacy | `AGENTS.md :: Hard rules`; `Alpha Wave PRD.md :: G2. Identity containment` |
| Real data | `Alpha Wave PRD.md :: G3. Real data only` |
| Wallet safety | `Alpha Wave PRD.md :: G5. Wallet and private-key safety` |
| Referral integrity | `Alpha Wave PRD.md :: G6. Referral integrity` |
| Money integrity | `Alpha Wave PRD.md :: G7. Money and payout integrity` |
| Support | `Meeting started 2026_10_02 16_46 :: Support System and AI-Powered Ticketing` |
| Risk and advice | `Tech Team Meet :: Risk analyzer and record of advice` |
| Transparency and trading | `Meeting started 2026_10_02 16_46 :: Transparency Layers, Quantitative Engine, and Trading Runtimes` |
| Compensation | `Meeting started 2026_10_02 19_13 :: Compensation Plan Engines and Technology Evaluation` |
| Binary Options and live charts | `Tech Team Meet :: Gamification and predictive trading features` |
| Institutional scope | `Meeting started 2026_10_02 19_13 :: Product roadmap and development phases` |

## 14. Acceptance Summary

This PRD is acceptable when:

- It reflects Phase 0 through Phase 4 without adding meeting-only scope.
- Every sensitive area has a gate or an `OPEN` decision.
- No vendor, formula, threshold, return, provider, or legal result is invented.
- Money, wallet, trading, support, compensation, card, and fund features are
  constrained by security and compliance gates.
- The stories, technical report, and phase plans can trace back to this PRD.

*Internal planning document. Not legal, tax, investment, or financial advice.*
