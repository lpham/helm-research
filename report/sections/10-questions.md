# Questions for vendors, QUANT and legal counsel

## Vendors

**All shortlisted MLM vendors (MLM Soft, Exigo, Epixel, Cloud MLM)**

1. Will you contract with a platform that distributes a crypto product through an MLM network, with Commissions paid in crypto?
2. Provide your current SOC 2 Type II report or ISO/IEC 27001:2022 certificate, and the latest penetration test summary with remediation status.
3. Demonstrate a Sponsor-Tree-only plan with unilevel levels, a matching bonus, rank qualification, dynamic compression, per-Member caps, a plan version effective from a future date, simulation of that version, recalculation after a reversed event, and a per-Commission explanation export.
4. Can a commissionable event carry an arbitrary amount and type that is not a product order, such as a fee-revenue event? How is it submitted (endpoint, idempotency key) and reversed?
5. Can payouts be disabled so that the platform only emits approved payout instructions to an external wallet system?
6. Describe API authentication, rate limits, versioning and deprecation, webhook signing and retries, and sandbox availability.
7. Describe administrator MFA, maker-checker approvals, immutable audit logs and log export.
8. What data can be exported (genealogy, ledger, Commission history), in what format, and on what exit terms?
9. What are hosting regions, data residency, SLA, backup objectives and support hours?
10. What is a realistic lead time for the plan above, and can you provide two references of similar scale?

**Vendor-specific**

11. MLM Soft: provide access to the API3 reference before contract; describe the webhook catalogue; confirm whether API keys are supported instead of username and password; describe versioning, simulation and clawback support; give Enterprise pricing beyond 3,000 active accounts.
12. Exigo: confirm support for non-order commissionable volume and payout to external crypto rails; give pricing and lead time; clarify the relationship with DirectScale.
13. Epixel: provide contract addresses, repositories and audits for "multi-chain smart contract" commission processing; state who holds signing keys; clarify the ISO 27001 edition; provide USD pricing.
14. Cloud MLM: confirm the investment and "staking rewards" modules can be fully removed; state what security review the codebase has had and the patch cadence.

**Privy**

15. Will Privy onboard this business model, and do embedded wallets, policies, key quorums and Earn require any Stripe or Bridge account?
16. Which features in our design require the Enterprise plan, and at what price?
17. Has the Earn fee wrapper been audited, and by whom? What are its upgrade and admin controls?
18. How does key export work for Members if the platform leaves Privy?

**Turnkey, Alchemy and ZeroDev (Stripe-independent wallet alternative)**

19. Will you onboard this business model? Turnkey: which plan covers delegated API keys, policies and gas sponsorship, and can policies restrict a platform key to deposits into named ERC-4626 vaults with amount caps? Alchemy: confirm Turnkey as a supported signer for Smart Wallets, the pricing for wallet APIs, and SOC 2 status. ZeroDev (Offchain Labs): confirm acceptance given the reputational-harm termination right, provide the Kernel v4 audit report, and confirm paymaster coverage on HyperEVM.

**Treasury vendors (Cobo, Fireblocks)**

20. Will you onboard this business model? Which plan covers quorum approvals and batch payouts on the networks we need?

**Verification vendors (Sumsub, Didit)**

21. Will you onboard this business model? Which plan covers tiered verification, wallet screening and Travel Rule? What are data residency and retention options?

**Helpdesk vendors**

22. Zendesk: Enterprise pricing for audit log and custom roles. Freshdesk: whether custom objects are included in Pro. Intercom: which plan includes the audit log.

**On-ramp providers (Phase 2)**

23. After full disclosure of the model, will you approve the platform in writing? Who is merchant of record? Do aggregators route the platform through each provider's own business review?

## QUANT (Phase 2)

1. What exactly does the MVP include today, and which parts run in production?
2. What custody model does the MVP use, and who can sign for user funds?
3. Can the engine operate solely through trade-only keys on Member-owned Hyperliquid accounts, with no withdrawal authority?
4. What risk limits, kill switches and monitoring exist? Who can override them?
5. What security assessments, penetration tests and audits have been performed, with dates and scope?
6. How is historical performance measured and presented, and has it been independently verified?
7. What incidents have occurred, and how were they handled?
8. What is the relationship between QUANT and the "Quantitative Engine" and "TA Capital Trade Deck" referenced in the PRD?

## Legal counsel

**Scope and structure**

1. In which jurisdictions will AlphaWave be established, and in which will Members be recruited or served? Which regimes apply as a result?
2. Which legal entity provides each service (wallet, Deposits, Yield Product, Commission calculation, Commission payout)? Is Cyclone, as integrator and operator of the application layer, exposed to any of these classifications?

**Custody and licensing**

3. Under the proposed wallet model, with or without a policy-restricted platform signer, does AlphaWave have "control" over Member assets?
4. Does holding Commissions in an operator treasury before payout amount to safekeeping or transfer on behalf of Members?
5. Does a Yield Product that routes Deposits to a third-party protocol make AlphaWave a virtual asset service provider, an investment manager, or neither?

**KYC and AML**

6. Is any no-KYC tier permissible, and up to what cumulative amounts and for which actions?
7. What information must be collected for withdrawals and payouts to self-hosted wallets? Does the Travel Rule apply?
8. What sanctions screening is required for wallet addresses and Members, against which lists and how often?
9. Which record-retention, suspicious-activity reporting and compliance-officer obligations apply?
10. Is identity needed for tax reporting on Commissions, independently of AML?

**MLM, securities and consumer protection**

11. Which commission bases are lawful under pyramid-scheme laws in each target jurisdiction: platform fee revenue, Deposit volume, yield amounts?
12. Is the Yield Product, under each mechanism considered (Staking, lending, trading vault, operator-managed), a security, investment contract, collective investment scheme or deposit-taking activity? The SEC and CFTC issued a joint interpretation on crypto assets, including protocol staking, on 17 March 2026 ([SEC 2026-30](https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets)); how do it and local equivalents apply?
13. Do Members who recruit and earn Commissions need any licence or registration?
14. What earnings disclosures, risk warnings and marketing controls are required, including over Member-created content?

**Vendors and banking**

15. Can AlphaWave rely on a vendor's KYC (for example an on-ramp's) for its own obligations?
16. Are any vendor terms incompatible with the business model as structured?

Reference sources for counsel (examples, not an assessment of applicability): [FATF 2021 guidance on virtual assets](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html), [EU MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), [EU Transfer of Funds Regulation](https://eur-lex.europa.eu/eli/reg/2023/1113/oj), [FinCEN FIN-2019-G001](https://www.fincen.gov/sites/default/files/2019-05/FinCEN%20Guidance%20CVC%20FINAL%20508.pdf), [FTC guidance on multi-level marketing](https://www.ftc.gov/business-guidance/resources/business-guidance-concerning-multi-level-marketing), [FTC Business Opportunity Rule](https://www.ftc.gov/legal-library/browse/rules/business-opportunity-rule), [Investor.gov on pyramid schemes](https://www.investor.gov/introduction-investing/investing-basics/glossary/pyramid-schemes).
