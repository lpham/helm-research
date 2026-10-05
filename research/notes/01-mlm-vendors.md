# 01 — MLM software vendors with crypto capabilities

- Project: Helm (client: AlphaWave). Author: Cyclone research.
- Research date: 2026-10-06. Currency: USD unless stated otherwise.
- Scope: white-label MLM cores with crypto Deposit, payout and Yield Product features, plus API-first/headless commission engines to compare against. Self-built comp engines are out of scope.
- Method: vendor websites, pricing pages, documentation and regulator sources only. No vendors were contacted and no accounts or demos were requested.
- Evidence labels:
  - **Verified**: a primary source (vendor documentation, a published price, a regulator or certification body) confirms the fact.
  - **Vendor claim**: the claim appears only in vendor marketing copy, with no documentation, report or certificate behind it.
  - **Not verified**: no evidence was found.
- Terminology follows `GLOSSARY.md`: Member, Sponsor Tree, Commission, Deposit, Yield Product, Staking. Vendors' own words ("staking", "investment", "ROI", "distributor") are quoted as they appear and are not adopted as our terms.

---

## 1. Summary

### Top findings

1. **No vendor reviewed offers a real Yield Product.** Where a vendor uses "staking", the evidence describes one of two things:
   - an "ROI" or "staking" dashboard; or
   - an operator-configured percentage return ("daily percentage returns based on individual member investments").

   No vendor names an underlying staking, liquid-staking or lending protocol or provider. These are **modules that merely calculate and display returns**, which brief §3 tells us to flag ([Cloud MLM investment plan](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/), [Infinite MLM crypto investment page](https://infinitemlmsoftware.com/industries/crypto-investment-network), [Hybrid MLM investment plan](https://www.hybridmlm.io/investment-mlm-plan/)). **Verified** that the vendors present these features this way, and **Not verified** that any real yield is executed. Whatever Yield Product Helm offers must come from a separate staking/DeFi or custody provider, not from the MLM core.
2. **"Smart contract commissions" claims are not backed by evidence.** Epixel says "Commissions are instantly processed via multi-chain smart contracts (ETH, BNB, Polygon, Tron)" ([Epixel home](https://www.epixelmlmsoftware.com/)). Infinite MLM and Hybrid MLM make similar claims. We found no contract addresses, repositories, audit reports or custody descriptions for any of them. Label: **Vendor claim**.
3. **Crypto support in these products is mostly gateway integration and internal e-wallet bookkeeping.** Only Cloud MLM names its gateways (CoinPayments and Bitaps) ([Cloud MLM crypto page](https://cloudmlmsoftware.com/cryptocurrency-mlm-software/)). Custody, signing authority and key ownership are undocumented for every vendor. CoinPayments describes itself as a custodial service ([CoinPayments](https://www.coinpayments.net/)), so crypto routed through it would be held by a third party. That is not a non-custodial model and does not fit the Privy embedded-wallet base case without further design.
4. **The enterprise direct-selling platforms have the strongest controls evidence but no crypto evidence.**
   - Exigo: SOC 2 claim, more than 200 APIs, public developer documentation ([Exigo platform](https://www.exigo.com/exigo-platform/), [developers.exigo.com](https://developers.exigo.com/)).
   - ByDesign: SOC 2 / ISO 27001 badges ([bydesign.com](https://bydesign.com/)).
   - Neither shows any crypto payment or payout integration. Exigo's payout integrations are PayQuicker, Worldpay, Hyperwallet and iPayout ([Exigo integrations](https://www.exigo.com/company/integrations/)).
5. **Several security certifications are stale or inconsistent.**
   - Infinite MLM advertises "ISO 27001:2013 Certified" ([about](https://infinitemlmsoftware.com/about-us)).
   - The Epixel home page says "ISO/IEC 27001:2013 certified", while its crypto page footer shows ISO 27001-2022 ([home](https://www.epixelmlmsoftware.com/), [crypto page](https://www.epixelmlmsoftware.com/cryptocurrency-mlm-software)).
   - All accredited ISO/IEC 27001:2013 certificates expired or were withdrawn on 31 October 2025 ([SGS transition notice](https://www.sgs.com/en/news/2024/05/iso-iec-27001-transition-what-you-should-know)).
   - We therefore treat every ISO claim as **Not verified** until we see a current 2022-edition certificate and its scope.
6. **What crypto-MLM software commonly uses as a commission base is the deposit, which the scripts call "investment".** The typical bases are the amount a Member deposits and the "ROI" paid on it, plus entry or package fees (see §5). Event-driven engines (MLM Soft) can technically calculate on any event the platform sends, including platform fee revenue. Product-order platforms (Exigo, ByDesign) would need a synthetic order to carry a non-product base.

### Shortlist (deeper assessment)

| # | Vendor | Role in Helm | Why shortlisted | Main conditions |
|---|---|---|---|---|
| 1 | **MLM Soft** | Headless commission engine and genealogy, with the Privy wallet and a separate yield provider | API-first SaaS. Event-triggered rules engine. Virtual wallets per currency, including token wallets. Calculation is separate from payout. Full calculation traceability. Published monthly pricing and setup range ([home](https://www.mlmsoft.com/), [pricing](https://www.mlmsoft.com/cloudplatform/subscription), [payouts](https://www.mlmsoft.com/about/blog/payout-automation-simplify-your-mlm-payout-process)) | No published security attestation. Public API reference not confirmed (help centre returned 403). Plan versioning, simulation and clawbacks not documented |
| 2 | **Epixel MLM Software** | Integrated white-label option with crypto payouts (commission ledger only; no yield) | Most extensive crypto-MLM feature set among established vendors. Public API docs covering JWT auth, webhooks and SSO ([api.epixelsoftware.help](https://api.epixelsoftware.help/)). Regional pricing published. 450+ clients claimed | Smart-contract and custody claims unverified. ISO claim inconsistent. Endpoint-level docs not public. "Investment plan" marketing |
| 3 | **Cloud MLM Software** | Low-cost, source-code-licensed core (reduces exit risk) | Only vendor naming crypto gateways (CoinPayments, Bitaps). Full Laravel source code licence from USD 750, self-hostable ([pricing](https://cloudmlmsoftware.com/pricing/)) | No certifications. Investment/ROI module is a red flag (do not enable). Small vendor. Source-code ownership shifts security responsibility to Cyclone |
| 4 | **Exigo** | Enterprise-grade fallback comp engine, with crypto handled entirely outside | SOC 2 / PCI claim. 200+ APIs. Public developer docs. Mature payout integrations ([platform](https://www.exigo.com/exigo-platform/)) | No crypto. No public pricing. Order-centric model. Enterprise lead times unlikely to fit 30 days |

**Recommendation direction for the architecture workstream (working assumption):** buy the commission engine and Sponsor Tree, and keep custody, wallets and yield out of the MLM core.

- Wallet: Privy, or a custody provider.
- Yield: a named staking or DeFi provider.
- Ledger: Cyclone-owned.
- MLM core (MLM Soft as the primary candidate): receives Deposit, fee and yield events as commissionable events, calculates Commissions, and publishes payout instructions.
- Payout execution: performed by the wallet or custody layer under Cyclone controls.

Epixel and Cloud MLM remain options for an integrated white-label front end, but only with their crypto and ROI modules disabled or used purely as a ledger display.

### Exclusions

| Vendor | Reason excluded from shortlist |
|---|---|
| Infinite MLM Software | Its "Staking & ROI Management Dashboard" displays returns and names no provider ([source](https://infinitemlmsoftware.com/industries/crypto-investment-network)). Gateways are discussed but not named as integrations ([blog](https://infinitemlmsoftware.com/blog/crypto-payment-gateways-for-mlm/)). The REST API doc URL returns 404 ([link](https://infinitemlmsoftware.com/docs/integration/rest-api)). SOC 2 is asserted without a report or trust centre, and the ISO 27001:2013 certificate it advertises could not still be valid. Held in reserve as a like-for-like alternative to Cloud MLM. |
| Hybrid MLM (hybridmlm.io) | Its investment-plan material describes level commissions on recruits' investments and on their ROI, with returns funded from "company profits" generated with invested funds ([source](https://www.hybridmlm.io/investment-mlm-plan/)). That is a Ponzi-risk design pattern. Its crypto page names no gateways, chains or custody ([source](https://www.hybridmlm.io/cryptocurrency-mlm-software/)). No certifications found. Crypto gateways appear only in its $2,549 tier. |
| ARM MLM | Markets a "Forsage Clone Script" smart-contract MLM with an entry-fee commission model ("Pay 0.5 ETH to join") ([source](https://www.armmlm.com/tron-smart-contract-mlm-software/)). The SEC charged Forsage's founders and promoters as an alleged crypto pyramid and Ponzi scheme ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)). Unsuitable reference design. No audit evidence. |
| FlawlessMLM | Its comp engine features are well documented: what-if simulation, rule versioning, returns handling ([source](https://flawlessmlm.com/en/mlm-commission-software)). Pricing is published ($6,000 packaged / $1,499 per month enterprise SaaS, [source](https://flawlessmlm.com/en/mlm-marketing-software)). However, its crypto gateway claims (Tron/ETH/BSC/BTC) appear only in third-party articles, and its `/en/paysystem` page now serves generic homepage content. No certifications found. **Reserve** headless alternative to MLM Soft if crypto handling stays external. |
| ByDesign Technologies (Freedom) | Enterprise direct-selling platform with SOC 2 / ISO 27001 badges ([bydesign.com](https://bydesign.com/)). No crypto evidence. No public pricing. Overlaps with Exigo, which has better public developer documentation. |
| DirectScale | Public REST API with Live/Stage environments ([docs](https://developers.directscale.com/docs/public-api-overview)). However, `directscale.com` returned a 302 redirect to `exigo.com` on 2026-10-06. Corporate status and product roadmap could not be verified, so it should be assessed through Exigo if at all. |
| InfoTrax, Trinity | Considered as named in the brief. No crypto evidence was gathered, and the search budget was exhausted before primary sources were reviewed. **Not verified**. Not shortlisted. |
| "Ostrich MLM" | No vendor with this name could be identified from primary sources. **Not verified**. |
| Bespoke "crypto MLM development" agencies (e.g. Osiz, Developcoins, Nadcab, Suffescom, Blockchain App Factory) | These sell custom builds and clone scripts, not a maintained white-label product, so they fall under the self-built exclusion. Their marketing repeats "guaranteed ROI" and "staking pool APY" language with no named yield source ([example](https://www.suffescom.com/cryptocurrency-mlm-software-development), [example](https://www.osiztechnologies.com/cryptocurrency-mlm-software-development)). |

---

## 2. Per-vendor sections

### 2.1 MLM Soft (headless / API-first engine)

| Area | Evidence | Label |
|---|---|---|
| Positioning | "Full rest API, webhooks, and plugins" for integration with e-commerce, CRM, payments and marketing systems ([home](https://www.mlmsoft.com/)) | Vendor claim (no public API reference reviewed) |
| API docs | A help centre article "Swagger UI" describes API3 with Swagger, console and Postman examples ([help.mlmsoft.net](https://help.mlmsoft.net/hc/en-us/articles/44976746185619-Swagger-UI)). The page returned 403 to our fetcher, so contents were not reviewed | Not verified |
| Plan types | Unilevel, breakaway/stair-step (generation, differential), binary, revolving matrix, hybrid ([comp plan page](https://www.mlmsoft.com/cloudplatform/compensation-plan)) | Vendor claim |
| Trees | "Graph-based architecture" lets a member exist in multiple structures simultaneously, so a sponsor tree and a placement tree can coexist ([comp plan page](https://www.mlmsoft.com/cloudplatform/compensation-plan)) | Vendor claim |
| Engine | Event-triggered rules, where "certain metrics affect the others". Real-time and batch (weekly/monthly) calculation. "Millions of trigger-events in a single minute". A 10M-member network calculated in about 15 minutes ([comp plan page](https://www.mlmsoft.com/cloudplatform/compensation-plan)) | Vendor claim |
| Explanations / audit | "Full calculation chains and history" ([home](https://www.mlmsoft.com/)) | Vendor claim |
| Versioning, simulation, clawbacks, compression, caps | Not documented on reviewed pages | Not verified |
| Calc vs payout separation | On period close, commissions post as transactions to a "virtual wallet", which shows "what the company owes distributors without involving real money". Payout runs separately via a "payment adapter". Operators can filter payout requests ([payout article](https://www.mlmsoft.com/about/blog/payout-automation-simplify-your-mlm-payout-process)) | Vendor claim (good fit for a Cyclone-owned ledger) |
| Crypto | Wallets support fiat currencies, and "you can create separate wallets for cryptocurrency tokens" ([token sale article](https://www.mlmsoft.com/about/blog/boost-your-token-sale-with-a-referral-program)). Payout options include "cryptocurrency" ([payout article](https://www.mlmsoft.com/about/blog/payout-automation-simplify-your-mlm-payout-process)). No named crypto gateway, chain or custody | Vendor claim. Custody: Not verified (none, by design) |
| Staking / yield | None | n/a. MLM Soft does not claim to offer this |
| Commission bases | Custom plans calculate rewards for "customers, affiliates and investors" in token-sale referral programs ([token sale article](https://www.mlmsoft.com/about/blog/boost-your-token-sale-with-a-referral-program)). Event-driven metrics imply non-order events can be commissionable | Vendor claim. Must be confirmed in a demo |
| Security / compliance | No SOC 2, ISO 27001 or pen-test evidence found | Not verified |
| Hosting | Cloud SaaS. Hardware, licence, maintenance, backups and new versions included ([pricing](https://www.mlmsoft.com/cloudplatform/subscription)) | Verified (as published) |
| Pricing | Startup $499/mo (up to 300 income centres; one currency/wallet, one tree, one admin). Community $999/mo (1,000). Network $1,999/mo (3,000). Enterprise custom. Setup "usually varies between $10,000 to $30,000". SMS ≈ $0.1/message ([pricing](https://www.mlmsoft.com/cloudplatform/subscription)) | Verified (published) |

**Assessment.** This is the best structural fit for a modular architecture in which Privy (or a custodian) holds assets and Cyclone owns the ledger. The Startup tier is too restrictive for Helm because it allows a single wallet and a single admin. Community or Network is the realistic entry point. Security attestation is the critical gap.

### 2.2 Epixel MLM Software

| Area | Evidence | Label |
|---|---|---|
| Company | "450+ Successful MLM Companies", more than 88 countries ([home](https://www.epixelmlmsoftware.com/)) | Vendor claim |
| Plan types | Binary, Unilevel, Matrix, Breakaway, Generation, Monoline, Board ([crypto page](https://www.epixelmlmsoftware.com/cryptocurrency-mlm-software)) | Vendor claim |
| Crypto assets | BTC, ETH, USDT, XRP, BCH, LTC, BSV, EOS, BNB, ADA, and "basically any digital coin" ([crypto page](https://www.epixelmlmsoftware.com/cryptocurrency-mlm-software)) | Vendor claim |
| Crypto payouts | "Process, pay, and settle commissions instantly in BTC, ETH, USDT, USDC, BNB, TRX, or custom tokens". "Commissions are instantly processed via multi-chain smart contracts (ETH, BNB, Polygon, Tron)" ([home](https://www.epixelmlmsoftware.com/)) | Vendor claim. No contracts, addresses or audits found |
| Exchanges / gateways | "Seamless crypto exchange integration" with Binance, Coinbase and Kraken. "Supports all popular cryptocurrency payment APIs" ([industry page](https://www.epixelmlmsoftware.com/industries/cryptocurrency), [crypto page](https://www.epixelmlmsoftware.com/cryptocurrency-mlm-software)) | Vendor claim |
| Custody | "Cold storage options" mentioned ([industry page](https://www.epixelmlmsoftware.com/industries/cryptocurrency)). Who holds keys is not stated | Not verified |
| Staking / yield | Not offered. The "Cryptocurrency investment plan" page is generic marketing ("investment will double or may triple") with no mechanism ([page](https://www.epixelmlmsoftware.com/cryptocurrency-investment-plan-using-mlm-software)) | Not verified. Red-flag language |
| Commission bases | Crypto trading MLM: "Compensations can be set either for new trader registration or for the first trade or any other unique strategy" ([page](https://www.epixelmlmsoftware.com/cryptocurrency-trading-mlm-software)). A case study covers crypto referral bonuses paid in tokens ([case study](https://www.epixelmlmsoftware.com/case-studies/custom-referral-program-blockchain-business)) | Vendor claim |
| Security | KYC/AML integration, 2FA, encryption ([industry page](https://www.epixelmlmsoftware.com/industries/cryptocurrency)). ISO/IEC 27001:2013 and ISO 9001:2015 claimed on the home page, with ISO 27001-2022 in another page footer | Vendor claim. ISO: Not verified (inconsistent; the 2013 edition expired 31 Oct 2025) |
| API | Public integration guide covering app registration, apikey header for public access, JWT access/refresh tokens, webhook and SSO configuration, error codes. Endpoint-level reference and sandbox not shown ([api.epixelsoftware.help](https://api.epixelsoftware.help/)) | Verified (guide exists). Endpoint coverage: Not verified |
| Pricing | The global pricing page shows tiers with prices hidden behind "Contact" ([pricing](https://www.epixelmlmsoftware.com/pricing)). The Canadian page publishes Kickstart "starts from" CA$1,381 and Growth CA$6,914, with Ultimate on quote. The billing period is not clear on the page ([en-ca pricing](https://www.epixelmlmsoftware.com/en-ca/pricing)) | Verified (CAD only). USD: quote required |
| Hosting / source | Cloud platform implied. Source-code licence not stated | Not verified |

**Assessment.** This is the strongest integrated white-label candidate among the crypto-MLM vendors, but every crypto-execution claim needs a technical demonstration. Use it as a comp engine plus a Member back office, and keep custody and yield external.

### 2.3 Cloud MLM Software (Bpract Software Solutions LLP, India)

| Area | Evidence | Label |
|---|---|---|
| Company | Bpract Software Solutions LLP, Kozhikode, India. "1,000+ MLM licences issued since 2015" ([home](https://cloudmlmsoftware.com/)) | Vendor claim |
| Plan types | 21 plan types including binary, unilevel, matrix, monoline, board, generation, hybrid, stair-step ([home](https://cloudmlmsoftware.com/), [crypto page](https://cloudmlmsoftware.com/cryptocurrency-mlm-software/)) | Vendor claim |
| Crypto gateways | Names CoinPayments and Bitaps for settlement. "Exact coverage depends on your configuration" ([crypto page](https://cloudmlmsoftware.com/cryptocurrency-mlm-software/), [bitcoin page](https://cloudmlmsoftware.com/bitcoin-cryptocurrency-mlm-software)) | Vendor claim (gateway names are specific). CoinPayments itself is custodial: **Verified** ([CoinPayments](https://www.coinpayments.net/)) |
| Payout architecture | Three steps: (1) the plan engine posts earned amounts; (2) the e-wallet ledger records them with an audit trail; (3) settlement runs via crypto gateways with pricing feeds ([bitcoin page](https://cloudmlmsoftware.com/bitcoin-cryptocurrency-mlm-software)) | Vendor claim (calc/payout separated) |
| Custody | "Multi-signature wallets", "institutional custody", "hardware vault options", "policy-based access", approval workflows ([crypto page](https://cloudmlmsoftware.com/cryptocurrency-mlm-software/)). No provider named | Vendor claim. Not verified |
| Staking / yield | "Tokenised plan studio" supports "staking rewards" with vesting ([crypto page](https://cloudmlmsoftware.com/cryptocurrency-mlm-software/)). The investment plan offers "daily percentage returns based on individual member investments" and lets operators "configure ROI, lock-in, and reinvestment logic per tier" ([investment plan](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/)) | Verified that this is a **calculated-return module** (operator-set %). No protocol. **Red flag** |
| Integrations | "REST APIs and webhooks integrate with liquidity pools, exchanges, and DeFi platforms" ([crypto page](https://cloudmlmsoftware.com/cryptocurrency-mlm-software/)). No public API documentation found | Vendor claim |
| Compliance | AML/KYC, chain analytics, "regulator-ready" tax reports ([bitcoin page](https://cloudmlmsoftware.com/bitcoin-cryptocurrency-mlm-software)). No certifications listed on the home page | Vendor claim. Certifications: Not verified |
| Hosting / source | "The full Laravel source code is delivered under the licence, with a self-hosted option". Managed hosting available ([pricing](https://cloudmlmsoftware.com/pricing/)) | Verified (published terms) |
| Pricing | Source Licence "from USD 750" one-time, all 21 plan types, 6 months of support. Maintenance thereafter "from 18% of the licence fee" per year. Managed Setup and Enterprise on quote ([pricing](https://cloudmlmsoftware.com/pricing/)) | Verified (published) |

**Assessment.** This option gives the lowest cost and the strongest exit position, because Cyclone would hold the source. It suits a scenario where Cyclone hardens and hosts the core. The ROI/investment module must not be enabled. The crypto gateway path (custodial CoinPayments) conflicts with a Privy-based custody design, so it should be replaced by Cyclone's wallet integration.

### 2.4 Exigo (enterprise fallback)

| Area | Evidence | Label |
|---|---|---|
| Controls | "Exigo's systems and processes are certified as SOC2, PCI, and GDPR Compliant". Built on Microsoft Azure ([platform](https://www.exigo.com/exigo-platform/)). Report scope and date not published | Vendor claim (request the SOC 2 Type II report) |
| API | "Over 200 Application Programming Interfaces". SOAP web services, OData REST and SQL access. Developer portals ([developers.exigo.com](https://developers.exigo.com/), [api.exigo.com/3.0](https://api.exigo.com/3.0/), [web service reference](http://developer.exigo.com/api/webservice/reference)) | Verified (public docs exist) |
| Payouts | PayQuicker, Worldpay, Hyperwallet, iPayout ([integrations](https://www.exigo.com/company/integrations/)) | Vendor claim |
| Crypto | None found on the platform, home or integrations pages | Not verified |
| Comp features | "Compensation & Commission Management". Versioning and simulation not detailed on reviewed pages ([platform](https://www.exigo.com/exigo-platform/)) | Not verified |
| Pricing | Not published. Exigo Core is "sized and priced for where you are now" ([startup page](https://www.exigo.com/startup-mlm-software/)) | Quote required |
| Note | `directscale.com` redirected to `exigo.com` on 2026-10-06 (HTTP 302, observed) | Verified (observed redirect). Relationship: Not verified |

**Assessment.** Use Exigo only if the client values audited enterprise controls over speed. Crypto, wallet and yield would sit entirely outside it, with Deposit or fee events mapped to orders. A 30-day timeline is unlikely to be achievable.

### 2.5 Reserve and excluded vendors (brief notes)

- **Infinite MLM Software** (Infinite Open Source Solution LLP, Calicut, India; "3,000+" companies) ([about](https://infinitemlmsoftware.com/about-us)).
  - Crypto: BTC, ETH, USDT (BEP20), MetaMask and Trust Wallet, "fiat-to-crypto onramps", "Smart Contract Commission Engine", "Staking & ROI Management Dashboard" ([crypto investment page](https://infinitemlmsoftware.com/industries/crypto-investment-network)). Label: Vendor claim.
  - Pricing: Basic $699 one-time; other tiers hidden behind a form; "one-time license with lifetime access" ([pricing](https://infinitemlmsoftware.com/pricing)). Label: Verified for Basic only.
  - Certifications: "ISO 27001:2013 & SOC 2 Certified" ([about](https://infinitemlmsoftware.com/about-us)). Label: Vendor claim, no report. The ISO edition is expired.
- **Hybrid MLM.**
  - Pricing: one-time Essential $599, Professional $1,549, Golden $2,549 (unlocks "Investment" plan and "Crypto Gateways"), Enterprise $4,549. Base price $499. Source code provided. Payment terms 40/40/20 ([pricing](https://www.hybridmlm.io/pricing/)). Label: Verified (published).
  - Investment plan: "Commissions are earned regularly whenever a recruit's investment generates ROI" ([investment plan](https://www.hybridmlm.io/investment-mlm-plan/)). Label: Verified (as described); red flag.
- **ARM MLM.** Advertises an entry package at $799 and stage-based price ranges ([pricing guide](https://www.armmlm.com/mlm-software-pricing/)). Markets a Forsage clone smart contract ([page](https://www.armmlm.com/tron-smart-contract-mlm-software/)). Excluded, see §1.
- **FlawlessMLM.** Documents "what-if simulation", "rule versioning maintains historical rule sets so past calculations can be reproduced exactly", and handling of "returns and cancellations" ([commission software](https://flawlessmlm.com/en/mlm-commission-software)). Pricing: "$6,000 for packaged builds and scales to $1,499/month for enterprise SaaS plans", implementation 1–4 months ([page](https://flawlessmlm.com/en/mlm-marketing-software)). Crypto: Not verified on its own site.
- **ByDesign (Freedom).** "SOC 2 / ISO 27001" badges, 2.7k+ comp plans configured, 185 countries ([bydesign.com](https://bydesign.com/)). Labels: Vendor claim; crypto Not verified.
- **DirectScale.** Public REST API at `https://dsapi.directscale.com/v1`, with stage at `dsapi-stage`, invitation-only keys, and a Client Extension for custom endpoints ([docs](https://developers.directscale.com/docs/public-api-overview)). Label: Verified (docs). Crypto: Not verified.

---

## 3. Comparison table

Legend: **V** = Verified, **C** = Vendor claim, **N** = Not verified, **—** = not offered or not applicable.

| Capability | MLM Soft | Epixel | Cloud MLM | Exigo | Infinite MLM | Hybrid MLM | FlawlessMLM |
|---|---|---|---|---|---|---|---|
| Unilevel / generation / rank (Sponsor Tree plans) | C | C | C | C | C | C | C |
| Binary / matrix (placement tree) | C | C | C | C | C | C | C |
| Multiple trees (sponsor + placement) | C (graph model) | N | N | N | N | N | N |
| Plan versioning / effective dates | N | N | N | N | N | N | C |
| Simulation / what-if | N | C ("commission forecasting", Growth tier) | C (investment-plan "what-if" fees) | N | N | N | C |
| Commission explanations / trace | C | N | C (audit trail) | N | N | N | C |
| Refunds / clawbacks | N | N | N | C (refunds in money-out) | N | N | C |
| Calc separated from payout | C | N | C | C | N | N | N |
| Non-order commission base | C (events, token sales) | C (trader registration / first trade) | C (investment %) | N | C (staking/ROI) | C (investment & ROI) | N |
| Crypto deposits | N | C | C (CoinPayments, Bitaps) | — | C | C (Golden tier) | N |
| Crypto payouts | C (payout adapter) | C | C | — | C | C | N |
| Custody / key ownership documented | — | N | N | — | N | N | N |
| Real yield provider named | — | — | — (calculated %) | — | — (dashboard) | — (calculated) | — |
| Smart-contract audit evidence | — | N | — | — | N | N | — |
| SOC 2 report available | N | N | N | C | C | N | N |
| ISO 27001 (current 2022 edition) | N | N (2013 / 2022 inconsistent) | N | N | N (2013 expired) | N | N |
| KYC integration | N | C | C | N | C | C (manual KYC) | N |
| Public API docs | N (403) | V (guide) | N | V | N (404) | N | N |
| Webhooks | C | C | C | N | N | N | N |
| Sandbox / stage env | N | N | N | N | N | N | N |
| Hosting model | SaaS (V) | Cloud (C) | Source licence, self-host (V) | SaaS on Azure (C) | One-time licence (V) | One-time + source (V) | SaaS or package (C) |
| Published pricing | V | V (CAD only) | V | — | V (Basic only) | V | V |

---

## 4. Plan-design fit note

Per `GLOSSARY.md`, the Sponsor Tree is the only tree in the Helm plan. Binary and matrix plans, which need a placement tree, are therefore not required. The capabilities that matter are:

- unilevel, generation, matching and rank logic on the Sponsor Tree;
- compression and caps;
- plan versioning with effective dates;
- simulation;
- commission explanations;
- clawbacks for reversed Deposits or failed transactions;
- a hard separation between Commission calculation and payout execution.

No vendor publicly documents all of these. FlawlessMLM documents the most (simulation, versioning, returns). MLM Soft documents traceability and calculation/payout separation. **Every shortlisted vendor needs a scripted demo against Helm test cases (see §7).**

---

## 5. Commission base evidence

Question: can Commissions be calculated on something other than product orders? The evidence groups into six bases. Each is quoted as the vendor describes it.

| Base | Vendor evidence (quoted) | Label | Notes |
|---|---|---|---|
| **Product orders / PV** | Exigo money-in/out of "payments, commissions, and refunds" ([platform](https://www.exigo.com/exigo-platform/)). DirectScale API organised around "customers, orders, products" ([docs](https://developers.directscale.com/docs/public-api-overview)) | C / V | The default base for enterprise direct-selling platforms. A non-product base needs a synthetic order or custom volume (consultant assumption; confirm in demo) |
| **Deposit or "investment" amount** | Hybrid MLM: "Commissions are earned when a recruit makes an initial investment" (L1 10%, L2 5%, L3 2% example) ([source](https://www.hybridmlm.io/investment-mlm-plan/)). Cloud MLM: "daily percentage returns based on individual member investments" ([source](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/)) | V (as described) | **The most common base in crypto-MLM software.** Commissions funded from new Deposits create a structural Ponzi/pyramid risk and need legal review |
| **Yield / "ROI" amount** | Hybrid MLM: "Commissions are earned regularly whenever a recruit's investment generates ROI" ([source](https://www.hybridmlm.io/investment-mlm-plan/)). Infinite MLM: "Staking & ROI Management Dashboard" for "DeFi staking or lending pools" ([source](https://infinitemlmsoftware.com/industries/crypto-investment-network)) | V (as described) / C | Common. In these products the "ROI" is itself operator-calculated, not protocol yield |
| **Entry fee / package purchase** | ARM MLM Forsage clone: "Pay 0.5 ETH to join", "0.025 ETH commission from each person's 0.5 ETH entry fee" ([source](https://www.armmlm.com/tron-smart-contract-mlm-software/)) | V (as described) | The pattern the SEC alleged was a pyramid scheme ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)). Avoid |
| **Trading activity** | Epixel: "Compensations can be set either for new trader registration or for the first trade or any other unique strategy" ([source](https://www.epixelmlmsoftware.com/cryptocurrency-trading-mlm-software)) | C | Relevant only if QUANT trading is later integrated |
| **Arbitrary platform events (incl. token purchases, fees)** | MLM Soft: event-triggered rules ("millions of trigger-events"). For token-sale referral programs, it does "all the commission calculations and distribute[s] the rewards to your customers, affiliates and investors" ([comp plan](https://www.mlmsoft.com/cloudplatform/compensation-plan), [token sale](https://www.mlmsoft.com/about/blog/boost-your-token-sale-with-a-referral-program)) | C | The only route found to a **platform fee revenue** base. No vendor explicitly advertises "commission on platform fee revenue" (Not verified as a named feature) |

**What is common.** Crypto-MLM products overwhelmingly calculate Commissions on two bases: the Member's Deposit (called "investment") and a configured "ROI" on that Deposit. Entry or package fees are the third common base. Enterprise platforms calculate on orders. Configurable event engines can calculate on any amount the integrating platform sends.

**Implications for the Helm recommendation (working options, not decisions; legal review required):**

- **Option A: platform fee revenue.** Commissions are a share of fees Helm actually earns, for example a fee on realised yield or a Deposit fee. Commissions are funded from realised revenue. This needs an event-driven engine (MLM Soft) or synthetic orders (Exigo or others). No vendor offers it out of the box. **Lowest structural risk.**
- **Option B: Deposit volume** (for example, time-weighted balances). Widely supported in crypto-MLM software, but it ties rewards to recruitment of new money, which is the pattern behind Ponzi and pyramid scheme concerns. Needs strong caps, clawbacks and legal sign-off.
- **Option C: yield amount.** Only credible if the yield is real and comes from a named provider. In vendor products "ROI" is a calculated number, so it must never be the source of truth. The source of truth should be Cyclone's ledger, fed by the yield provider.

---

## 6. Pricing evidence (USD unless noted; research date 2026-10-06)

| Vendor | Item | Amount | Type | Status | Source |
|---|---|---|---|---|---|
| MLM Soft | Startup / Community / Network | $499 / $999 / $1,999 per month (300 / 1,000 / 3,000 income centres) | Recurring SaaS | Verified public | [pricing](https://www.mlmsoft.com/cloudplatform/subscription) |
| MLM Soft | Customisation setup | "usually varies between $10,000 to $30,000" | One-time | Verified public (range) | [pricing](https://www.mlmsoft.com/cloudplatform/subscription) |
| MLM Soft | Enterprise | Custom (per-account or flat fee) | — | Quote required | [pricing](https://www.mlmsoft.com/cloudplatform/subscription) |
| Epixel | Kickstart / Growth | CA$1,381 "starts from" / CA$6,914 (billing period unclear) | Unclear | Verified public (CAD only); USD quote required | [en-ca pricing](https://www.epixelmlmsoftware.com/en-ca/pricing) |
| Epixel | Ultimate (API engines, custom roles) | — | — | Quote required | [pricing](https://www.epixelmlmsoftware.com/pricing) |
| Cloud MLM | Source licence | From $750 | One-time | Verified public | [pricing](https://cloudmlmsoftware.com/pricing/) |
| Cloud MLM | Annual maintenance after 6 months | From 18% of licence fee | Recurring | Verified public | [pricing](https://cloudmlmsoftware.com/pricing/) |
| Cloud MLM | Managed setup / Enterprise | — | — | Quote required | [pricing](https://cloudmlmsoftware.com/pricing/) |
| Exigo | All | — | — | Quote required | [startup page](https://www.exigo.com/startup-mlm-software/) |
| Infinite MLM | Basic | $699 | One-time | Verified public | [pricing](https://infinitemlmsoftware.com/pricing) |
| Infinite MLM | Standard / Enterprise | Hidden behind form | — | Quote required | [pricing](https://infinitemlmsoftware.com/pricing) |
| Hybrid MLM | Essential / Professional / Golden / Enterprise | $599 / $1,549 / $2,549 / $4,549 | One-time | Verified public (excluded vendor) | [pricing](https://www.hybridmlm.io/pricing/) |
| FlawlessMLM | Packaged build / enterprise SaaS | $6,000 / $1,499 per month | One-time / recurring | Verified public (vendor page) | [page](https://flawlessmlm.com/en/mlm-marketing-software) |
| ARM MLM | Entry package | $799 | Not stated | Verified public (excluded vendor) | [pricing guide](https://www.armmlm.com/mlm-software-pricing/) |
| ByDesign | All | — | — | Quote required | [bydesign.com](https://bydesign.com/) |

Pricing caveats:

- Low one-time licences ($599–$750) exclude customisation, hardening, hosting and security testing.
- Listed prices are not comparable to enterprise SaaS totals.
- Third-party directory prices (for example, Cloud MLM "Investment Plan $1,600") were not used.

---

## 7. Open questions for vendors

**All shortlisted vendors**

1. Provide the current SOC 2 Type II report (period, scope, carve-outs), or an ISO/IEC 27001:2022 certificate (certifying body, scope, expiry). Provide the latest penetration test summary and remediation status.
2. Run a scripted demo of a Sponsor-Tree-only plan with:
   - unilevel levels;
   - a generation/matching bonus;
   - rank qualification;
   - dynamic compression;
   - a per-Member cap;
   - plan version B effective from a future date;
   - simulation of B against period data;
   - recalculation after a reversed Deposit (clawback);
   - a per-Commission explanation export.
3. Can a commissionable event carry an arbitrary amount and type that is not a product order, such as a fee-revenue event, a Deposit event or a yield-accrual event? How is it submitted (API endpoint, idempotency key) and how is it reversed?
4. How is Commission calculation separated from payout? Can payouts be disabled entirely, so that the platform only emits approved payout instructions to an external wallet or custody system?
5. Cover the following for the API: the public API reference, authentication, rate limits, versioning and deprecation policy, webhook signing and retries, and sandbox availability.
6. Cover the following for RBAC: MFA for admins, maker-checker approvals, immutable audit logs, and log export.
7. Cover the following for data: ownership, full export format (genealogy, ledger, commission history), exit assistance and contract termination terms.
8. Provide hosting region options, data residency, SLA, backup/RPO/RTO, and support hours.
9. Provide a realistic implementation lead time for the above plan, and two references of similar scale (ideally in crypto or fintech).

**Epixel**

10. Provide deployed contract addresses, a repository and audit reports for the "multi-chain smart contract" commission processing. Who holds the signing keys and treasury?
11. Clarify the ISO 27001 edition (the home page says 2013, a footer says 2022). Provide a USD price list and the billing period for Kickstart and Growth.
12. Is the API documentation at `api.epixelsoftware.help` complete for genealogy, commissions, wallets and payouts? Is there a sandbox?

**Cloud MLM**

13. Which CoinPayments and Bitaps flows are implemented (deposit addresses, IPN/webhooks, mass payouts)? How are duplicates and retries handled? Can the gateways be replaced by an external wallet layer?
14. Which security review, if any, has the Laravel codebase undergone? What is the patch cadence for source-licence customers?
15. Confirm the investment/ROI and "staking rewards" modules can be fully disabled.

**MLM Soft**

16. Provide public access to the API3 Swagger reference. What are the webhook event catalogue and retry semantics?
17. Do token or crypto wallets support decimal precision and asset types suitable for multiple chains and assets? Is the "payment adapter" a supported extension point for a Privy- or custody-based payout?
18. What are plan versioning, simulation and clawback support? What is the enterprise pricing basis beyond 3,000 income centres?

**Exigo**

19. Does Exigo support non-order commissionable volume? Can it pay out to external crypto rails? What is the pricing and lead time for Exigo Core? What is the relationship to DirectScale (domain redirect)?

---

## 8. Evidence limitations

- The WebSearch budget for the session was exhausted mid-research. InfoTrax, Trinity, the MLM Soft help centre (403) and the Infinite MLM REST API page (404) could not be reviewed in full.
- No vendor publishes a SOC 2 report or a current ISO certificate publicly. All certification statements above are vendor claims until documents are provided.
- Crypto "smart contract" and custody claims could not be tested without demos, which the research rules prohibit.
- Prices change frequently. Marketing pages show "discounted" prices (Hybrid MLM), and some prices are regional (Epixel CAD).
