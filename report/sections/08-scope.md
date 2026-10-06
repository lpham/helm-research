# Proposed 30-day scope and readiness criteria

## Milestone definition

A real-funds launch within 30 days is not supported (section 1). The 30-day milestone is therefore defined as:

> **An end-to-end system running on test networks, with every money path, approval and support process working, plus vendor contracts and legal questions in progress, so that a controlled real-funds pilot can start as soon as the legal and vendor gates clear.**

Onboarding-only production (signup, sponsor attribution, referral links and wallet creation, with no Deposits) can be opened at day 30 if counsel agrees that pre-registration raises no issue in the target markets.

## Weekly plan

| Week | Outcomes | Owners | Dependencies | Acceptance criteria |
|---|---|---|---|---|
| 1 – Decide and procure | Decision log covering commission base, markets, KYC scenario and treasury approvers. Scripted demos of MLM Soft and Exigo. Parallel wallet spikes on Privy and on Turnkey with Alchemy Smart Wallets or ZeroDev Kernel. Written MLM-acceptance requests to Privy, Turnkey, Alchemy, ZeroDev (Offchain Labs), MLM Soft and the KYC vendor. Counsel engaged with the question list. Environments and repositories set up. | Client product owner; Cyclone delivery lead and architect | Client availability; vendor demo slots | Decisions signed off; demo scorecards and wallet spike results completed; vendor questionnaires sent; counsel engagement confirmed |
| 2 – Foundations | Member signup, sponsor attribution and referral links. Privy wallet creation on test networks. MLM core sandbox with a placeholder plan. Ledger schema and event model. Admin roles and audit log skeleton. Helpdesk tenant and case types. | Cyclone engineering | MLM and Privy sandbox access | A test Member can register under a sponsor, receive a wallet and appear in the Sponsor Tree; all admin actions are logged |
| 3 – Money flows on test networks | Deposit detection with independent reconciliation. Member-signed withdrawals. Commission calculation from test events. Treasury payouts with quorum approval. Sanctions screening on every address. KYC tiers in sandbox. | Cyclone engineering; client compliance owner (tier thresholds) | Placeholder thresholds agreed; KYC sandbox | Deposits credited exactly once, including under duplicate and delayed webhooks; payouts need two approvers; a sanctioned test address is blocked |
| 4 – Harden and review | Commission test pack (unilevel levels, matching, rank qualification, compression, caps, plan version change, reversal). Incident and suspension runbooks. Kill switches. Helpdesk integration and knowledge base drafts. Security self-assessment and pen test booked. Readiness review. | Cyclone QA and DevOps; client operations lead | Complete placeholder plan; knowledge base review | Test pack passes; runbooks rehearsed in a tabletop exercise; readiness report issued with open gates listed |

## Requirements before accepting real funds

All of the following must be met. None can be waived to meet a date.

1. **Defined product mechanics and Member terms**, including the commission base and complete plan rates, approved by counsel.
2. **Legal confirmation** for the launch jurisdictions covering custody classification, KYC thresholds, Travel Rule applicability and the compensation plan.
3. **Written vendor acceptance** of the MLM model from the wallet, MLM and verification vendors.
4. **Custody and signing controls** in force: separate treasury with quorum approval; any platform signer policy-restricted and held in an HSM or KMS; key rotation and recovery tested.
5. **Deposits and withdrawals** proven on test networks and in a small real-funds rehearsal using operator funds.
6. **Ledger and daily reconciliation** to on-chain balances, with breaks investigated before payouts.
7. **Verification and screening** live for the agreed scenario, with sanctions screening on every address.
8. **Commission calculations tested** against the agreed test pack, with explanations exportable per Member.
9. **Administrative permissions and auditability**: role-based access, maker-checker approvals for all funds movements, immutable audit log.
10. **Incident response**: service suspension and withdraw-only modes, failed and stuck transaction handling, Member communication templates.
11. **Independent penetration test and wallet review** completed, with high-severity findings fixed.

## Controlled pilot features

- Crypto Deposits in the assets and networks supported by the chosen components; withdrawals to the Member's own address.
- Sponsor Tree and Commission calculation on the confirmed base, with payouts in batches after a hold period.
- Tiered KYC and sanctions screening.
- Admin back office with approvals; helpdesk with funds, verification and Commission queues.
- Exposure limits: an invitation-only Member list, caps per Member and in total, and the ability to suspend.

## Later phases

- Live Yield Product through the adapter, after legal confirmation and vault due diligence.
- Fiat on-ramp, after written provider approvals.
- QUANT trading integration (Option 3), after due diligence.
- CRM layer, Telegram and WhatsApp support channels, AI support restricted to approved knowledge.
- Native mobile apps.
- PRD roadmap items with high regulatory sensitivity (binary options, B-Books, debit cards, fund products), each subject to separate legal review.

## Readiness assessment

Expected status at day 30 if week-1 decisions are made on time:

| Criterion | Expected status at day 30 | Blocking for real funds? |
|---|---|---|
| Product mechanics and Member terms | Commission base decided; terms drafted, not approved | Yes, until counsel approves |
| Legal confirmation | Questions with counsel; answers pending | **Yes** |
| Custody and signing controls | Designed and working on test networks | Yes, until reviewed |
| Deposits and withdrawals | Working on test networks | Yes, until the real-funds rehearsal |
| Ledger and reconciliation | Working on test networks | Yes, until the real-funds rehearsal |
| Verification and screening | Sandbox; thresholds provisional | Yes, until thresholds are approved |
| Commission calculations | Test pack passing against the placeholder plan | Yes, until rerun on the approved plan |
| Admin permissions and auditability | Built and tested | No |
| Incident response and suspension | Runbooks drafted and rehearsed | No, once rehearsed |
| Security testing | Scheduled | **Yes** |
| Vendor acceptance | Requested | **Yes** |

**Conclusion:** at day 30 the system should be ready to demonstrate end to end. It should not be described as production-ready for real funds until every blocking item above is closed.
