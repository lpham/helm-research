# Cost, effort and 12-month operating estimates

## Basis of estimates

- **Currency and date:** USD, prices seen on 6 October 2026. Prices exclude tax.
- **Scale:** a controlled pilot with up to 3,000 commission-active Members, under 10,000 monthly active wallet users, about 1,000 new Members per month and five helpdesk agents.
- **Scope:** Option 2 (modular). Release 1 has no fiat on-ramp, no custom smart contracts and no live Yield Product.
- **Labour:** Cyclone's day rates are contracted, so effort is shown in **person-months** only. Monetary figures cover external software and services.
- **Excluded:** legal counsel fees, licensing applications, banking costs, entity set-up, marketing, and Member-funded network fees.
- **Evidence labels:** **V** = verified public price; **Q** = vendor quotation required; **E** = Cyclone consultant estimate. Where a public price exists but the required features sit in a quote-only tier, the figure is marked E.

## External software and services

| Component | Low | Base | High | Basis |
|---|--:|--:|--:|---|
| MLM core: MLM Soft subscription (monthly) | $999 | $1,999 | $4,000 | V for Community and Network tiers; high case is E for Enterprise (Q) |
| MLM core: setup and customisation (one-time) | $10,000 | $20,000 | $30,000 | V ("usually varies between $10,000 to $30,000") |
| Member wallets: Privy (monthly) | $499 | $1,500 | $3,000 | E. Public tiers are $299–$499/month, but the policy engine, key quorums and production webhooks are Enterprise (Q) |
| Operator treasury tooling (monthly) | $0 | $299 | $999 | V: Privy key quorum (within Privy Enterprise), Cobo Starter, Fireblocks Essentials |
| KYC and AML screening, scenario B (monthly) | $250 | $1,200 | $2,000 | E from V per-check prices (Didit, Sumsub, Veriff) |
| Wallet screening and transaction monitoring (monthly) | $0 | $100 | $1,500 | V for the free Chainalysis oracle and Didit per-check prices; commercial KYT is Q |
| Helpdesk, 5 agents (monthly) | $145 | $585 | $1,350 | V list prices; high case includes Q items |
| Hosting, RPC/indexer, monitoring and logging (monthly) | $800 | $2,000 | $4,000 | E |
| Gas sponsorship for Member wallet actions (monthly) | $200 | $500 | $1,000 | E; pass-through, volume-dependent |
| Fiat on-ramp (Release 1) | $0 | $0 | $0 | Deferred to Phase 2; an aggregator such as Onramper costs $199–$599/month (V) |
| Penetration test, pre-launch (one-time) | $12,000 | $25,000 | $40,000 | E (no public rate cards; an automated test from $3,500 is V but not sufficient alone) |
| Wallet and key-management review (one-time) | $10,000 | $20,000 | $30,000 | E |
| Smart contract audit | $0 | $0 | $0 | Not needed while Release 1 deploys no custom contracts; $15,000–$100,000+ if it does (E) |

Sources: [MLM Soft](https://www.mlmsoft.com/cloudplatform/subscription), [Privy](https://www.privy.io/pricing), [Cobo](https://www.cobo.com/pricing), [Fireblocks](https://www.fireblocks.com/pricing), [Sumsub](https://sumsub.com/pricing/), [Zendesk](https://www.zendesk.com/pricing/), [Freshdesk](https://www.freshworks.com/freshdesk/omni/pricing/), [Cobalt](https://www.cobalt.io/pricing).

## One-time implementation costs (external)

| | Low | Base | High |
|---|--:|--:|--:|
| MLM setup and customisation | $10,000 | $20,000 | $30,000 |
| Penetration test | $12,000 | $25,000 | $40,000 |
| Wallet and key-management review | $10,000 | $20,000 | $30,000 |
| **Total one-time** | **$32,000** | **$65,000** | **$100,000** |

## Monthly operating costs (external)

| | Low | Base | High |
|---|--:|--:|--:|
| MLM subscription | $999 | $1,999 | $4,000 |
| Wallet infrastructure | $499 | $1,500 | $3,000 |
| Treasury tooling | $0 | $299 | $999 |
| KYC, AML and wallet screening | $250 | $1,300 | $3,500 |
| Helpdesk | $145 | $585 | $1,350 |
| Hosting, RPC, monitoring | $800 | $2,000 | $4,000 |
| Gas sponsorship | $200 | $500 | $1,000 |
| **Total monthly** | **≈ $2,900** | **≈ $8,200** | **≈ $17,800** |

## Indicative 12-month total cost of ownership (external)

| | Low | Base | High |
|---|--:|--:|--:|
| One-time | $32,000 | $65,000 | $100,000 |
| 12 × monthly | $34,700 | $98,200 | $214,200 |
| **Indicative 12-month total** | **≈ $67,000** | **≈ $163,000** | **≈ $314,000** |

What would move these figures most:

- **Network size.** MLM Soft's Network tier covers up to 3,000 commission-active accounts; a larger active base moves to Enterprise pricing (Q).
- **Wallet volume.** Privy's pay-as-you-go pricing above 10,000 monthly active users is $2,000 plus $0.05 per user (V); Enterprise pricing is negotiated.
- **Wallet vendor.** The Turnkey and Alchemy alternative is priced per signature and per compute unit (Turnkey $0.05 per signature on Pro, V), so its cost scales with transaction volume rather than monthly active users; at pilot scale it is expected to fall within the Privy range above (E).
- **KYC scenario.** Scenario A raises verification spend; scenario C lowers it but closes the fiat route and raises other risks.
- **Commercial transaction monitoring.** Chainalysis, TRM and Elliptic publish no prices; third-party sources suggest five-figure annual contracts (not verified).
- **A live Yield Product** adds audit review of the chosen vaults and any fee wrapper, and possibly a smart contract audit.

## Effort by workstream (person-months)

Engineering effort is not the same as elapsed time. Vendor procurement, provider approvals and legal review run in parallel and cannot be shortened by adding staff.

| Workstream | 30-day milestone | Cumulative to controlled pilot |
|---|--:|--:|
| Delivery management and solution architecture | 1.0 | 2.5 |
| MLM core integration and compensation plan configuration | 1.0 | 2.5 |
| Wallet and treasury integration (Privy, policies, quorum) | 0.75 | 1.5 |
| Ledger, Deposit detection and reconciliation | 1.0 | 3.0 |
| Member web app | 1.5 | 3.5 |
| Admin back office (roles, approvals, audit, case links) | 1.0 | 2.5 |
| KYC and screening integration | 0.5 | 1.0 |
| Helpdesk configuration and integration | 0.5 | 1.25 |
| QA, Commission test pack and test automation | 1.0 | 2.5 |
| DevOps, security engineering and monitoring | 0.75 | 2.0 |
| **Total** | **9.0** | **22.25** |

All figures are consultant estimates (E). The 30-day figure assumes the client's decisions in section 11 are made in week 1; otherwise configuration work on the compensation plan slips.

## Minimum delivery team

| Role | FTE | Responsibility |
|---|--:|---|
| Delivery lead | 1.0 | Plan, vendor coordination, decision log, readiness reviews |
| Solution architect and blockchain lead | 1.0 | Architecture, wallet and treasury design, custody controls |
| Backend engineers | 2.0 | Ledger, reconciliation, MLM and KYC integrations |
| Wallet and blockchain engineer | 1.0 | Privy integration, policies, indexer, gas sponsorship |
| Frontend engineers | 2.0 | Member web app and admin back office |
| QA engineer | 1.0 | Commission test pack, end-to-end and negative tests |
| DevOps and security engineer | 0.75 | Environments, secrets, monitoring, incident tooling |
| **Cyclone total** | **≈ 8.75** | |
| Client: product owner | 0.5 | Product mechanics, Member terms, compensation plan decisions |
| Client: compliance owner | 0.5 | KYC scenario, policies, counsel liaison |
| Client: operations and support lead | 0.5–1.0 | Support processes, knowledge base review, finance approvals |
| External: legal counsel | As engaged | Questions in section 10 |

## Dependencies and critical path

The critical path to accepting real funds runs through decisions and approvals rather than engineering:

1. **Client decisions** (week 1): commission base, target markets, KYC scenario, treasury approvers.
2. **Legal characterisation** of the compensation plan, custody model and KYC thresholds (estimated four to six weeks from engagement; outside Cyclone's control).
3. **Vendor acceptance and contracts**: Privy's written acceptance of the MLM model and Enterprise terms; MLM Soft contract and security evidence; KYC vendor onboarding (each runs its own business review).
4. **Compensation plan specification** with complete rates and the confirmed base, then configuration and testing against the Commission test pack.
5. **Ledger reconciliation proven** on test networks, then on a small real-funds rehearsal using operator funds.
6. **Independent penetration test and wallet review**, with high-severity findings fixed.
7. **Go/no-go review** against the readiness criteria in section 8.

Items 2 and 3 typically determine the launch date. Engineering can complete the 30-day milestone in parallel, but real funds wait for both.
