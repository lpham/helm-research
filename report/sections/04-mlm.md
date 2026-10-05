# MLM platform comparison, shortlist and exclusions

## Approach

Fifteen vendors were considered. They include white-label platforms marketed for crypto MLM, established enterprise direct-selling platforms, and headless or API-first commission engines. Bespoke development agencies and self-built engines were excluded by design. Vendors were assessed only from public sources; nothing was demonstrated or tested.

Because the Sponsor Tree is the only tree in AlphaWave's plan, binary and matrix placement trees are not required. The capabilities that matter are unilevel, generation, matching and rank logic; compression and caps; plan versioning with effective dates; simulation; Commission explanations; clawbacks; and a hard separation between Commission calculation and payout execution. **No vendor publicly documents all of these.**

## Eligibility conditions

A vendor had to meet all four conditions before scoring. Low price cannot compensate for a failed condition.

1. **No display-only yield.** Any "staking", "ROI" or "investment plan" module must be capable of being fully disabled; it is never used as a Yield Product.
2. **Payout can be separated from calculation**, so that payouts execute from AlphaWave's own wallet layer under its controls, not inside the MLM software.
3. **Documented integration surface**: a published API guide or reference, or vendor documentation of the event and data model.
4. **A maintained product from an identifiable vendor**, not a clone script or a one-off custom build.

## Vendors reviewed

| Vendor | Type | Crypto | Yield | Security evidence | Pricing | Outcome |
|---|---|---|---|---|---|---|
| MLM Soft | Headless SaaS engine | Token wallets as bookkeeping; payout adapter (claim) | None (by design) | None found | $499–$1,999/month + $10k–$30k setup (verified) | **Shortlist (lead)** |
| Exigo | Enterprise direct-selling platform | None | None | SOC 2 and PCI claimed; report not public | Quote | **Shortlist (alternative)** |
| Epixel | Integrated white-label | Payouts in BTC, ETH, USDT and others; "smart contract" commissions (claims) | "Investment plan" marketing only | ISO 27001 claims inconsistent (2013 and 2022 editions) | CA$1,381 and CA$6,914 tiers published; USD quote | **Shortlist (integrated option)** |
| Cloud MLM | Source-code licence, self-hosted | CoinPayments and Bitaps gateways named (custodial) | Calculated-return module (disable) | None | From $750 one-time + 18% yearly maintenance (verified) | **Shortlist (low-cost, exit)** |
| FlawlessMLM | Comp engine, SaaS or package | Claims only in third-party articles | None | None | $6,000 package or $1,499/month (verified) | Reserve |
| Infinite MLM | One-time licence | Claims (BTC, ETH, USDT, MetaMask) | "Staking & ROI dashboard" (display only) | ISO 27001:2013 (expired edition); SOC 2 asserted | $699 Basic (verified) | Reserve |
| Tapfiliate | Affiliate platform with multi-level API | None | None | Not found | Enterprise quote for API | Fallback for a very simple plan only |
| Post Affiliate Pro | Affiliate platform, up to 99 tiers (claim) | None | None | Not found | From $139/month | Fallback for a very simple plan only |
| Hybrid MLM | One-time licence + source | Gateways in top tier only | Commissions on "investment" and "ROI" | None | $599–$4,549 one-time | Excluded |
| ARM MLM | Scripts | "Forsage clone" smart contract | Entry-fee model | None | From $799 | Excluded |
| ByDesign | Enterprise | None | None | SOC 2 and ISO badges | Quote | Excluded (overlaps Exigo with less documentation) |
| InfoTrax | Enterprise, order-centric | None | None | Not found | Not found | Excluded |
| DirectScale | Enterprise API | None | None | Not found | Not found | Excluded (domain now redirects to Exigo; relationship unconfirmed) |
| Trinity (Firestorm) | Party-plan back office | None | None | Not found | Subscription | Excluded |
| Development agencies (Osiz, Suffescom and others) | Custom builds and clones | Claims | "Guaranteed ROI" language | None | Quote | Excluded (self-built) |

Sources: [MLM Soft pricing](https://www.mlmsoft.com/cloudplatform/subscription), [Exigo platform](https://www.exigo.com/exigo-platform/), [Epixel](https://www.epixelmlmsoftware.com/), [Epixel CAD pricing](https://www.epixelmlmsoftware.com/en-ca/pricing), [Cloud MLM pricing](https://cloudmlmsoftware.com/pricing/), [FlawlessMLM](https://flawlessmlm.com/en/mlm-marketing-software), [Infinite MLM pricing](https://infinitemlmsoftware.com/pricing), [Tapfiliate REST API](https://tapfiliate.com/docs/rest/), [Post Affiliate Pro pricing](https://www.postaffiliatepro.com/pricing/), [Hybrid MLM pricing](https://www.hybridmlm.io/pricing/).

Two findings apply across the market:

- **"Smart contract commission" claims are unsupported.** Epixel, Infinite MLM and Hybrid MLM advertise them, but no contract address, code repository or audit report was found for any of them.
- **Several ISO 27001 claims cannot be current.** All accredited ISO/IEC 27001:2013 certificates expired or were withdrawn on 31 October 2025 ([SGS transition notice](https://www.sgs.com/en/news/2024/05/iso-iec-27001-transition-what-you-should-know)). Every certification in this market should be treated as unverified until a current certificate or SOC 2 report is provided.

## Weighted scorecard

Scores run from 1 (weak or no evidence) to 5 (strong, documented). They are Cyclone's assessment of public evidence and will change after demonstrations.

| Criterion | Weight | MLM Soft | Exigo | Cloud MLM | Epixel | FlawlessMLM |
|---|--:|--:|--:|--:|--:|--:|
| Compensation features (plans, versioning, simulation, clawbacks, explanations) | 25% | 3 | 4 | 3 | 3 | 4 |
| Commission base flexibility (non-order events) | 15% | 5 | 2 | 3 | 3 | 2 |
| Integration (API, webhooks, headless, separation of payout) | 20% | 4 | 5 | 2 | 3 | 2 |
| Security and controls evidence | 15% | 1 | 4 | 1 | 2 | 1 |
| Time to deploy | 10% | 4 | 1 | 3 | 3 | 3 |
| Exit, data ownership and lock-in | 10% | 3 | 3 | 5 | 2 | 3 |
| Commercial transparency and cost | 5% | 5 | 1 | 5 | 3 | 4 |
| **Weighted score** | | **3.40** | **3.35** | **2.80** | **2.75** | **2.65** |

The top two are close for different reasons. MLM Soft wins on commission-base flexibility, speed and price; Exigo wins on controls evidence and integration maturity but is slower and quote-only. **The decisive item for MLM Soft is security due diligence**: no SOC 2 report, ISO certificate or penetration test summary was found. Both should be demonstrated side by side.

## Shortlist

**1. MLM Soft (lead candidate for the modular architecture).**

- Its REST API (API3) "covers all the functionality of the platform", with per-tenant Swagger documentation ([developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API), verified in vendor documentation).
- Custom plan properties can be flagged as volume, bonus or rank and "set by API request", so a fee-revenue amount can be sent per Member per event and used as the commission base ([plan properties](https://help.mlmsoft.net/hc/en-us/articles/39249705385235-Plan-properties-configuration), verified in vendor documentation).
- Commissions post to a bookkeeping wallet; payout runs separately through a payment adapter. The vendor describes itself as "not a financial institution", which fits a Cyclone-owned ledger and wallet layer.
- Published pricing: $499, $999 and $1,999 per month for up to 300, 1,000 and 3,000 accounts with commercial activity in the last three months; Enterprise on quote; setup "usually varies between $10,000 to $30,000" (verified). The entry tier allows one wallet and one administrator, so Community or Network is the realistic starting point, and a large network will reach Enterprise pricing.
- Gaps: no security attestation; plan versioning, simulation and automatic clawbacks not documented; the API authenticates with a username and password rather than documented API keys.

**2. Exigo (enterprise alternative).**

- More than 200 APIs with public developer documentation ([developers.exigo.com](https://developers.exigo.com/), verified). SOC 2, PCI and GDPR compliance claimed (vendor claim; request the report). Mature payout integrations (PayQuicker, Worldpay, Hyperwallet, iPayout).
- No crypto capability, which matters less in the modular design because crypto sits outside the MLM core. Non-product bases would be modelled as synthetic orders or custom volumes.
- No public pricing; enterprise lead times make a 30-day configuration unlikely.

**3. Epixel (integrated white-label option).**

- The broadest crypto-MLM feature set among established vendors, with a public integration guide covering JWT authentication, webhooks and SSO ([api.epixelsoftware.help](https://api.epixelsoftware.help/), verified that the guide exists).
- Every crypto-execution claim needs a technical demonstration. Custody and key ownership are undocumented. Its "cryptocurrency investment plan" page uses language such as "investment will double or may triple", which must not be reused.

**4. Cloud MLM (low-cost, strongest exit position).**

- Full Laravel source code from $750 one-time, self-hostable, with 21 plan types (verified). Holding the source removes vendor lock-in but transfers security responsibility to Cyclone.
- Its named gateways (CoinPayments, Bitaps) are custodial, which conflicts with the Member-owned wallet design; they would be replaced by Cyclone's wallet integration. Its investment and "staking rewards" modules must be disabled.

**Reserve and fallbacks.** FlawlessMLM documents the strongest comp-engine features (what-if simulation, rule versioning, returns handling) and is the reserve headless engine. Tapfiliate and Post Affiliate Pro could support a deliberately simple plan (fixed percentages per level on fee revenue) but lack rank qualification, compression and versioning.

## Exclusions

| Vendor | Reason |
|---|---|
| Hybrid MLM | Its investment plan pays level Commissions on recruits' "investment" and "ROI", with returns funded from "company profits" generated with invested funds. This is a Ponzi-risk design pattern ([source](https://www.hybridmlm.io/investment-mlm-plan/)). |
| ARM MLM | Markets a "Forsage clone" entry-fee smart contract. The SEC charged Forsage's founders over an alleged pyramid and Ponzi scheme ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)). |
| Infinite MLM | Display-only "Staking & ROI" dashboard; REST API documentation link returns an error; ISO claim refers to an expired edition. Held in reserve only as a like-for-like alternative to Cloud MLM. |
| ByDesign, InfoTrax | Order-centric enterprise platforms with no crypto evidence and less public documentation than Exigo. |
| DirectScale | Its domain redirected to Exigo on the research date; corporate status unconfirmed. Assess through Exigo if at all. |
| Trinity (Firestorm) | Party-plan back office without API documentation. |
| Development agencies | Custom builds and clone scripts, often marketed with "guaranteed ROI" language. They fall under the self-built exclusion. |
| CaptivateIQ, Everstage, QuotaPath and similar | Sales-compensation tools priced per payee and built around sales hierarchies, not Member genealogies. |
