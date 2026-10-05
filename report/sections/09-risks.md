# Risks and due diligence requirements

## Risk register

Likelihood (L) and impact (I) are rated High, Medium or Low by Cyclone for the recommended Option 2.

| # | Risk | L | I | Mitigation |
|---|---|:-:|:-:|---|
| R1 | Counsel finds the compensation plan or commission base unlawful in a target market | M | H | Decide the base early; prefer Commissions funded from realised fee revenue with caps and hold periods; no Commissions on Deposits until counsel confirms |
| R2 | A vendor declines or later terminates the business because of the MLM model (wallet, KYC, payments) | H | H | Full disclosure during onboarding; written acceptance before build depends on it; replaceable components behind Cyclone interfaces; fallback vendors identified |
| R3 | The hybrid wallet model (platform signer) is classified as custody or money transmission | M | H | Release 1 without a platform signer on Member wallets; add a scoped signer only after counsel's view; key quorum with a Member signature as an alternative |
| R4 | Compromise of treasury or platform signer keys | L | H | Quorum approval; HSM or KMS; strict policies; separation of keys; withdrawal limits; wallet review before launch |
| R5 | MLM Soft fails security due diligence or cannot support the plan | M | M | Side-by-side demo with Exigo; scripted test pack; request SOC 2, ISO 27001:2022 or penetration test evidence before contract |
| R6 | Commission errors or disputes (rates, compression, reversals) | M | H | Complete specification; test pack; per-Member explanations; hold period before payout; maker-checker on adjustments |
| R7 | Commission clawback impossible once paid on-chain | H | M | Pay after a hold period; net future Commissions against reversals; state this in Member terms |
| R8 | Fraud through fake Members (self-sponsoring, sybil accounts) | H | M | Tiered KYC before payouts; device and behaviour signals; caps; Commission eligibility rules |
| R9 | Reconciliation breaks between ledger, wallets and chain | M | H | Two independent Deposit signals; idempotency on transaction identifiers; daily reconciliation with payouts blocked on unresolved breaks |
| R10 | Yield protocol loss (smart contract, oracle, curator, liquidity) when the Yield Product goes live | M | H | Vault allow-list with curator criteria; exposure caps; kill switch; Member disclosures by category; no projected returns shown |
| R11 | Members misunderstand returns or rely on promotional earnings claims | H | H | Compliance-reviewed content; no return promises; earnings disclosures; control of Member-created marketing |
| R12 | Gas costs for per-Member wallets exceed budget | M | L | Choose low-fee networks; batch payouts; sponsorship limits |
| R13 | Delays in legal review or vendor onboarding push the pilot beyond plan | H | M | Start both in week 1; treat as critical path; keep engineering milestones independent of them |
| R14 | Dependence on Privy, which is owned by Stripe: its terms could be aligned with Stripe's MLM prohibition | M | H | Use no Stripe or Bridge features; confirm acceptance in writing; wallet layer behind a Cyclone interface; Member key export; Turnkey with Alchemy Smart Wallets or ZeroDev Kernel tested in parallel as the independent alternative |
| R15 | QUANT integration exposes Member funds to trading losses | L (Release 1) | H | No QUANT access in Release 1; Phase 2 only through opt-in, capped, trade-only accounts after due diligence |

## Due diligence requirements

**MLM vendor (before contract):**

- Current SOC 2 Type II report or ISO/IEC 27001:2022 certificate, with scope and period; latest penetration test summary and remediation.
- Scripted demonstration of the Helm test pack, including a non-order commission base sent by API, plan versioning, simulation, reversal and per-Member explanations.
- Data export of genealogy, plan history and Commission history; exit terms.
- API authentication, rate limits, versioning, webhook signing and retries; sandbox access.

**Wallet and treasury vendors:**

- Written acceptance of the MLM model and confirmation that core wallet features need no Stripe or Bridge account (Privy).
- Enterprise pricing; SOC 2 report; policy-engine capabilities; key export and migration path.
- Audit status of the Earn fee wrapper and any contracts the platform would rely on.

**Verification vendor:** acceptance of the model; certifications; data residency; record retention; Sumsub's disclosed 2024 support-system incident ([Sumsub statement](https://sumsub.com/newsroom/security-incident-update/)).

**Yield providers (later phase):** audit history, incident history and remediation, curator risk framework, liquidity profile, and custody implications of the integration pattern.

**QUANT (Phase 2):** independent technical review of the engine, custody model, security controls, operational readiness, historical performance methodology and incident history. QUANT's MVP capabilities have not been verified in this research.
