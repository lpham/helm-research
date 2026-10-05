You are a senior research consultant specializing in MLM platforms, crypto/DeFi infrastructure, fintech architecture, CRM and customer operations.

Research available solutions and recommend a practical architecture for a first release within 30 days. Produce an evidence-based, client-facing report in English, delivered as a professionally formatted PDF and an editable source document.

## 1. Research objective

Identify the fastest credible implementation path using existing software, with appropriate controls for funds, withdrawals, commissions and operations.

This is an initial business discovery and solution architecture exercise. Do not create a detailed PRD, user stories, API specifications or implementation backlog.

The research should provide enough information to:
- Select an architecture direction.
- Shortlist MLM and CRM vendors.
- Estimate costs, implementation effort and operating expenses.
- Define a realistic 30-day release scope.
- Identify the due diligence and business decisions required before implementation.

If a client PRD is supplied, treat it as reference material expressing business intentions, not as a binding or validated specification.

## 2. Business context

The client has an established MLM distribution network and wants to offer a financial product through that network.

The proposed platform includes:
- User onboarding.
- Wallets or smart accounts.
- Crypto deposits and withdrawals.
- A product currently described as “staking,” whose underlying mechanism remains undefined.
- MLM genealogy and configurable compensation plans.
- Administrative tools and customer support.
- Fiat deposit capabilities, either in the initial release or through a subsequent integration.

The client prefers a crypto/DeFi-first approach and currently assumes that crypto deposits can be offered without KYC. Treat this as an unverified business assumption requiring confirmation according to the operating model and relevant jurisdictions.

An associated QUANT trading company has built an MVP reportedly covering onboarding and smart account creation. It intends to connect its trading engine to Hyperliquid and may offer a staking/yield product.

The QUANT platform’s technical capabilities, custody model, security and operational readiness have not been independently verified. Its trading engine is an optional component, not a mandatory architectural dependency. Evaluate alternatives that avoid exposing customer funds to algorithmic trading during the initial release.

The implementation company:
- Has extensive experience integrating third-party core platforms and operating systems serving multiple user groups.
- Can build web, mobile, admin dashboards and customer operations integrations.
- Prefers to purchase existing core software and act as the integrator responsible for the application layer.

No operating jurisdiction, legal entity location or target customer market has been confirmed. Maintain jurisdiction neutrality.

The client will engage legal counsel to determine regulatory obligations and licensing requirements. Research should assess software capabilities that support compliance, without implying that a vendor’s software or certifications authorize the client’s business model.

## 3. Research principles

Clearly distinguish:
- Verified facts.
- Vendor or client claims.
- Working assumptions.
- Unresolved questions.

Do not assume:
- Crypto deposits automatically remove KYC obligations.
- Wallet connection or smart accounts establish a non-custodial model.
- A “DeFi” label establishes decentralization.
- Crypto payment support includes staking infrastructure.
- Hyperliquid integration provides native staking.
- Software compliance features guarantee eligibility for an unspecified future license.

Distinguish among:
- Native staking.
- Liquid staking.
- Lending.
- Trading vaults.
- Operator-managed yield programs.
- Modules that merely calculate or display returns.

Also distinguish fiat-to-crypto on-ramps from directly accepting, holding and managing fiat funds.

Continue research using clearly labeled scenarios where information is missing. Identify which missing inputs materially change the recommendation.

## 4. MLM platform research

Find approximately 6–10 relevant vendors, subject to credible evidence, and shortlist 3–4 for deeper assessment. Do not pad the list with unsuitable vendors.

Prioritize white-label MLM solutions offering crypto deposits, payouts and staking/yield functionality. Compare these with modular alternatives where integrated offerings lack sufficient evidence or controls.

Evaluate:

### Compensation plans and genealogy
- Unilevel, binary, matrix, generation, matching and rank-based plans.
- Configuration, customization and combined plans.
- Sponsor and placement trees.
- Qualification, compression, caps and carry-over.
- Plan versioning and effective dates.
- Simulation, recalculation and commission explanations.
- Refunds, reversals and clawbacks.
- Separation of commission calculation from payout execution.
- Auditability and data export.

### Crypto, staking and fiat
- Native functionality versus third-party integrations.
- Supported assets, networks and geographic availability.
- Deposit detection, withdrawals and commission payouts.
- Custody, signing authority and administrative control.
- Actual staking/yield provider or protocol.
- Source of yield, fees, lockups, liquidity and withdrawal restrictions.
- Whether the feature executes an underlying product or only displays calculated returns.
- Fiat on-ramp/off-ramp partners, eligibility and onboarding requirements.
- Reconciliation, duplicate prevention, webhook retries and failed transaction handling.

### Security and compliance support
- RBAC, MFA, audit logs, encryption, backups and disaster recovery.
- SOC 2/ISO 27001 evidence, scope and validity.
- Penetration tests, platform security audits and smart contract audits, including dates, scope and remediation evidence.
- KYC/KYB, AML, sanctions screening and transaction monitoring.
- Configurable verification workflows, record retention and reporting.
- Specific functionality behind claims of “MLM compliance.”
- Controls supporting future compliance requirements, subject to jurisdiction-specific assessment.

### Integration, operations and commercial terms
- API documentation, SDKs, webhooks and sandbox availability.
- Authentication, rate limits and API versioning.
- Headless and white-label capabilities.
- CRM, wallet, custody, payment and ledger integrations.
- Data ownership, export and migration.
- Hosting, data residency, SLA and support.
- Setup fees, licenses, usage fees and customization charges.
- Implementation lead time and customer references.
- Vendor lock-in, third-party dependencies and exit terms.

Exclude vendors from the recommended shortlist when critical capabilities cannot be substantiated. Explain the exclusion.

## 5. CRM and customer operations research

Compare Odoo, Salesforce and 2–4 other suitable alternatives.

Evaluate:
- Unified customer profiles and links to MLM, wallet and verification records.
- Ticketing, knowledge base and support channels.
- Case management for deposits, withdrawals, verification issues and commission disputes.
- Escalation, SLA, permissions, audit trails and approvals.
- API/webhook integration and SSO.
- Licensing, implementation, customization and administration costs.
- Deployment time and ongoing staffing requirements.

Recommend a minimum viable customer operations setup for the first 30 days and a subsequent expansion path.

Explain the boundaries between CRM, helpdesk, admin back office and financial ledger. Do not propose CRM as the authoritative source for financial balances.

## 6. Architecture options

Compare at least three approaches:
1. Integrated white-label MLM, crypto and staking/yield platform.
2. Modular architecture combining MLM, wallet/custody, staking/DeFi infrastructure and CRM.
3. Integration with the QUANT MVP, subject to independent due diligence and defined restrictions on access to customer funds.

For each approach, provide:
- A high-level architecture diagram.
- A fund-flow diagram showing custody and responsibility boundaries.
- The parties controlling assets, providing the financial product and processing withdrawals.
- Sources of truth for identity, genealogy, balances, transactions and commissions.
- Components to purchase, configure, integrate or build.
- A path to fiat deposits.
- Ability to replace the QUANT engine or another vendor.
- Implementation complexity, timeline, cost and material risks.
- Conditions required before accepting real funds.

Assess whether web-first delivery is sufficient for the initial release and whether native mobile should be deferred.

Recommend one primary direction and one fallback, explaining the tradeoffs and conditions.

## 7. Cost and effort estimates

Use USD as the primary currency. Record the research date and pricing assumptions.

Separate:
- Verified public pricing.
- Vendor quotation required.
- Consultant estimates.

Provide low/base/high estimates for:
- MLM setup and licensing.
- CRM licensing and implementation.
- Wallet/custody infrastructure.
- Fiat on-ramp integration.
- Verification and monitoring services where applicable.
- Hosting and monitoring.
- Integration, web and admin development.
- Mobile development if included.
- Ledger and reconciliation.
- Security assessment and relevant testing.
- Training, operational documentation and contingency.

Show:
- One-time implementation costs.
- Monthly operating costs.
- Indicative 12-month total cost of ownership.
- Person-days by workstream and role.
- Minimum delivery team.
- Dependencies and critical path.

Distinguish engineering effort from elapsed implementation time. Do not assume vendor procurement, partner onboarding or legal review can be completed through additional development resources.

## 8. Proposed 30-day scope

Propose a high-level weekly delivery plan with outcomes, owners, dependencies and acceptance criteria.

Separate:
- Requirements before accepting real funds.
- Features necessary for a controlled pilot.
- Features suitable for later phases.

Assess readiness for:
- Defined product mechanics and customer terms.
- Relevant legal confirmation.
- Custody and signing controls.
- Working deposits and withdrawals.
- Ledger and reconciliation.
- Applicable verification and monitoring.
- Tested commission calculations.
- Administrative permissions and auditability.
- Incident response, service suspension and transaction failure handling.

If a real-funds launch within 30 days is unsupported, state this clearly and recommend the closest credible milestone, such as sandbox delivery or onboarding readiness. Do not describe an incomplete system as production-ready.

## 9. Evidence standards

Use current information and prioritize:
- Official vendor websites and documentation.
- API documentation and pricing pages.
- Trust centers and audit reports.
- Official protocol and payment provider documentation.
- Authoritative regulatory sources when identifying jurisdiction-dependent questions.
- Independent sources for corroboration where useful.

Provide direct, clickable citations for material claims.

Record “not verified” when evidence is unavailable. Do not invent pricing, audits, certifications, SDKs or integration capabilities.

Use a weighted comparison scorecard, but apply minimum eligibility conditions before scoring. Low price must not compensate for missing critical controls or an unsupported deployment path.

Do not contact vendors, share client information, create paid accounts or make purchases.

## 10. Final deliverables

Produce an English report containing:
1. Executive summary and recommended direction.
2. Business requirements and working assumptions.
3. Key findings and constraints.
4. MLM comparison, shortlist and exclusions.
5. CRM comparison and recommendation.
6. Architecture options and fund flows.
7. Cost, effort and 12-month operating estimates.
8. Proposed 30-day scope and readiness criteria.
9. Risks and due diligence requirements.
10. Questions for vendors, the QUANT company and legal counsel.
11. Business decisions required from the client.
12. Sources, research date and evidence limitations.

Use professional, neutral, client-facing language. Avoid internal commentary about the client’s age, technical understanding or personal background.

Deliver:
- A professionally formatted PDF.
- An editable source document.

Use readable tables, clear diagrams, consistent pagination and clickable references. Render and visually inspect the PDF before delivery to check for clipping, broken layouts and unreadable content.

The final recommendation must identify what can be decided now, what requires vendor demonstration or quotation, what requires technical due diligence, and what requires legal confirmation.