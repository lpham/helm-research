# 01b — MLM vendors addendum: InfoTrax, Trinity, headless engines, MLM Soft API

- Project: Helm (client: AlphaWave). Author: Cyclone research.
- Research date: 2026-10-06. Currency: USD unless stated otherwise.
- Extends `01-mlm-vendors.md`, which this note does not modify. The scope, labels and terminology are the same.
- Evidence labels (same as note 01):
  - **Verified**: a primary source confirms the fact. That source can be vendor documentation, a published price, or a regulator or certification body.
  - **Vendor claim**: marketing copy only.
  - **Not verified**: no evidence was found.
- Method: official vendor websites, documentation and pricing pages, fetched directly. No vendors were contacted and no accounts were created.
- **Search budget note:** the session's WebSearch quota was already exhausted when this pass began, so no search engine queries were run. Every source was fetched from an official URL directly. Help-centre articles were retrieved via MLM Soft's public Zendesk Help Center API (for example `https://help.mlmsoft.net/api/v2/help_center/en-us/articles/39249636419475.json`), because the HTML pages return 403 to automated fetchers. Citations below link to the human-readable article URLs.
- Terminology follows `GLOSSARY.md` (Member, Sponsor Tree, Commission, Deposit, Yield Product). Vendor wording ("distributor", "affiliate", "volume", "PV") is quoted, not adopted.

---

## 1. Summary: does anything change the shortlist?

**The shortlist stays the same: MLM Soft (primary), Epixel, Cloud MLM, Exigo. MLM Soft's position is stronger. The gaps still open are security attestation, plan versioning, simulation and clawbacks.**

1. **MLM Soft: Helm's key requirement is now documented, not just claimed.**
   - **API3 covers the whole platform.** The vendor documents API3 as a REST service that "covers all the functionality of the platform". It runs on Compensation Plan Engine CPE32 ("based on document model, and Kafka highload queue"). Each tenant gets auto-generated Swagger docs at `https://{project}.mlmsoft.com/api3/api/docs` ([Developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API)).
   - **Custom plan properties can be set over the API.** They can be flagged as Volume, Bonus or Rank and marked "External editable (can be set by API request)" ([Plan properties configuration](https://help.mlmsoft.net/hc/en-us/articles/39249705385235-Plan-properties-configuration)). A property such as `FEE_REVENUE` could therefore be sent per Member per event and used as the commission base.
   - **Label: Verified (vendor documentation).** It still has to be proven in a demo against the Helm test case.
   - **The public API reference is still not public.** The Swagger UI lives inside each customer's own instance, and no security attestation was found. **Not verified.**
2. **InfoTrax: no shortlist change.**
   - Its "FastTree" commission engine, webhooks and "web-based SDK" are **vendor claims** ([FlexCloud](https://www.infotraxsys.com/flexcloud)).
   - We found no crypto, API reference, pricing or security attestation.
   - It is order- and product-centric ("every product sale and signup"). It overlaps with Exigo and has less public evidence than Exigo.
3. **Trinity Software (Firestorm): excluded.**
   - It is a party-plan, Shopify-oriented back office with subscription pricing ([trinitysoft.net](https://trinitysoft.net/), [Firestorm](https://trinitysoft.net/firestorm/)).
   - We found no API documentation, crypto support, security attestation or engine detail.
   - Do not confuse it with `trinitysoft.com`, an unrelated cosmetics-manufacturing software company (redirects to [trinitysoft.website](https://www.trinitysoft.website/)).
4. **DirectScale and Exigo: relationship still unconfirmed.**
   - `directscale.com` (and `directscale.com/blog`) returns HTTP 302 to `exigo.com`. **Verified (observed again 2026-10-06).**
   - Exigo's [home](https://www.exigo.com/), [company](https://www.exigo.com/company/) and [leadership](https://www.exigo.com/company/leadership-team/) pages do not mention DirectScale.
   - DirectScale's developer portal is still online ([developers.directscale.com](https://developers.directscale.com/)). The changelog index we retrieved showed only one entry, dated 4 November 2022 ([changelog](https://developers.directscale.com/changelog)).
   - A merger or acquisition is plausible but **Not verified**. Ask Exigo directly (question in §6).
5. **Headless or API-first alternatives: none replaces MLM Soft.** Two affiliate platforms have documented multi-level referral APIs that accept arbitrary amounts. They are a credible **fallback for a deliberately simple plan** (fixed percentages per level on fee revenue), not an MLM comp engine:
   - **Tapfiliate**: MLM parent endpoints and per-level commissions in its REST API. API access only on Enterprise ([REST docs](https://tapfiliate.com/docs/rest/), [pricing](https://tapfiliate.com/pricing/)).
   - **Post Affiliate Pro**: "up to 99 tiers" and a PHP API with `setMultiTierCreation` ([pricing](https://www.postaffiliatepro.com/pricing/), [Pap_Api_Transaction](https://support.qualityunit.com/427087-Pap_Api_Transaction)).

   Neither documents rank qualification, compression, generation or matching bonuses, plan versioning or SOC 2.

   Generic incentive-compensation platforms (CaptivateIQ, Everstage, QuotaPath and similar) are **excluded**. They are priced per payee or per seat and built around sales-team hierarchies, not member genealogies (§3.4).

**Net effect on the architecture recommendation:** none. Keep MLM Soft as the primary candidate and keep FlawlessMLM in reserve (note 01). Add Tapfiliate as a "minimum viable referral engine" fallback, and only if the client accepts a fixed-percentage, level-limited plan for Release 1.

---

## 2. MLM Soft — updated findings (supersedes the 403 gap in note 01)

| Area | Evidence | Label |
|---|---|---|
| Public API reference | API3 has "auto-generated documentation which can be accessed the same endpoint as the API itself: `/api3/api/docs/`", for example `https://yourprojectname.mlmsoft.com/api3/api/docs` ([Developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API)). The Swagger UI article contains only a video demo of Swagger, console and Postman use ([Swagger UI](https://help.mlmsoft.net/hc/en-us/articles/44976746185619-Swagger-UI)) | Verified: docs exist per tenant. No public, account-free endpoint reference: Not verified |
| API scope and architecture | "A restful services which covers all the functionality of the platform. It works with new version of Compensation Plan Engine (CPE32), based on document model, and Kafka highload queue" ([Developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API)) | Verified (vendor documentation). "All functionality": Vendor claim |
| Authentication | `POST /api3/auth/login` with login and password returns a bearer `accessToken` and `refreshToken`. The example uses admin credentials ("For the beginning you can use admin access") ([Developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API)) | Verified. No API keys, OAuth client credentials, scopes or rate limits are documented: Not verified (security question) |
| **Arbitrary-event commission base** | Inputs are "documents", for example `POST /api3/document/create` with `{"Doc-type":"Purchase","data":{"accountId":1,"props":{"PV":10000}}}`. Plan properties can be created freely, flagged "Volume, Bonus, Rank", and marked "External editable (can be set by API request)" ([Developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API), [Plan properties](https://help.mlmsoft.net/hc/en-us/articles/39249705385235-Plan-properties-configuration)). The integration flow says to send "account/volume change requests… one property per request", and that "order of such requests is very important" ([Integration flow](https://help.mlmsoft.net/hc/en-us/articles/39249664149907-Integration-flow)) | **Verified (vendor documentation)** that custom, API-settable volume properties exist. Using them for a fee-revenue base is our working assumption and needs a demo |
| Async processing and idempotency | The API is asynchronous. `user/create` returns a queued `documentId`, and the result is fetched by polling `document/get` or received by webhook ([Integration flow](https://help.mlmsoft.net/hc/en-us/articles/39249664149907-Integration-flow)) | Verified. Idempotency keys and duplicate handling: Not verified |
| Webhooks | "Type III (Webhook)": once a `user/create` request is processed, "your system will get a notification as HTTP POST request with email and MLMSoft UserId" ([Integration flow](https://help.mlmsoft.net/hc/en-us/articles/39249664149907-Integration-flow)). A Zapier integration article also exists ([Zapier](https://help.mlmsoft.net/hc/en-us/articles/40866493572499-Integration-with-external-services-by-Zapier)) | Verified for registration events. Full event catalogue, signing and retries: Not verified |
| Plans and trees | Each plan is "an isolated entity and has its own properties and rules", bound to one or more trees, with day, week or month periodicity and manual or automatic period change ([Configure plans](https://help.mlmsoft.net/hc/en-us/articles/39249721958931-Configure-plans)) | Verified (vendor documentation) |
| Calculation pipeline | Period close runs as scheduled documents in sequence: "CounterCalc, VolumeCalc, RankCalc, BonusCalc, PeriodClose – AutoPayout (executed last)" ([Period Closing and Auto Payout](https://help.mlmsoft.net/hc/en-us/articles/39249583187219-Period-Closing-and-Auto-Payout-Setup), [Calculation](https://help.mlmsoft.net/hc/en-us/articles/39249601732755-Calculation)) | Verified. AutoPayout is optional (scheduling is opt-in) |
| Calculation vs payout and custody | "MLM Soft is not a financial institution, thus MLM Soft platform don't provide any payment processing, but commission calculations and transactions management." A wallet balance "simply means that you as a company owes that amount". A payout request creates the debit when it is created, so the money "can't be requested twice". If a payout is cancelled, the amount is credited back as a separate transaction. Wallet currency "isn't necessary an actual currency… 'points', 'tokens', anything", and unlimited wallets are allowed ([Virtual wallets](https://help.mlmsoft.net/hc/en-us/articles/39249754307603-Virtual-wallets)) | **Verified (vendor documentation).** Strong fit with Privy custody plus a Cyclone ledger |
| Payout rails | Payin and payout "payment systems" can be integrated (via gateway) or custom, with operator-defined "payment credentials" fields ([Payment systems](https://help.mlmsoft.net/hc/en-us/articles/39249722329363-Payment-systems)) | Verified. A custom payout system could represent "Privy wallet address". Executing crypto transfers: Not verified (and should stay outside MLM Soft) |
| Returns and clawbacks | "Returns" are POS documents raised from orders, refunded to a selected wallet ([Returns](https://help.mlmsoft.net/hc/en-us/articles/39249761102355-Returns)). Automatic reversal of Commissions already paid upline is not described | Partial. Commission clawback: Not verified |
| Versioning and simulation | A help-centre search for "simulation" returned no articles. No plan-versioning or effective-date article was found | Not verified |
| RBAC | Four preset roles. For example, "Network Manager" cannot approve payout requests or make manual wallet transfers. "Financial Manager" cannot change sponsors or add or delete users. Custom roles use a hierarchical access tree ([Roles](https://help.mlmsoft.net/hc/en-us/articles/39249739546899-Roles)) | Verified (supports segregation of duties). MFA and audit-log export: Not verified |
| Hosting and tenancy | "Multi-instance architecture… a separate instance of the platform is automatically created for you". Hosted in "one of the data centers that we use worldwide". SaaS includes "backup and recovery" ([Intro to the platform](https://help.mlmsoft.net/hc/en-us/articles/39249770659091-Intro-to-the-platform)) | Vendor claim. Region choice, RPO/RTO: Not verified |
| Legal entity | "MLM Software Inc.", 5011 Gate Parkway, Bldg 100, Jacksonville, Florida 32256, USA ([privacy policy](https://www.mlmsoft.com/privacy-policy)) | Verified (as published) |
| Security attestations | The privacy policy mentions only "SSL encryption" and "a secure server", and says data may go to unnamed "overseas facilities" ([privacy policy](https://www.mlmsoft.com/privacy-policy)). `mlmsoft.com/security` returns 404. No SOC 2, ISO 27001 or pen-test statement was found | **Not verified.** This remains the critical gap |

**Assessment change.** MLM Soft moves from "event-driven by claim" to "event-driven by documentation". It has custom API-settable volume properties, an async document API, webhooks for registration, and a documented separation between calculation and payout in which no money moves. The remaining blockers are:

- SOC 2 / ISO 27001 evidence;
- an API auth model that relies on user credentials (no documented API keys or scopes);
- plan versioning and simulation;
- automatic Commission clawback on reversed events.

---

## 3. Per-vendor sections (new vendors)

### 3.1 InfoTrax Systems (FlexCloud / Evo)

| Dimension | Evidence | Label |
|---|---|---|
| Positioning | "Backend operations software" for direct sales companies. Its "best-in-class commission engine" is described as "fast, customizable, and can handle any compensation structure" ([home](https://www.infotraxsys.com/)) | Vendor claim |
| Engine | Runs on "proprietary FastTree technology" and "can manage the intricacies of any direct selling compensation plan". Tracks "every product sale and signup in each distributor's downline". Supports promos and contests ([FlexCloud](https://www.infotraxsys.com/flexcloud)) | Vendor claim |
| Plan types | Not listed by name | Not verified |
| Versioning, simulation, clawbacks | Only as consulting services: "modeling growth and changes in your commission structure", "compensation payout modeling" ([Commission consulting](https://www.infotraxsys.com/commission-consulting)). No product feature documented | Not verified (as a software feature) |
| Commission base flexibility | The engine is described in terms of product sales and signups. Non-order events are not mentioned | Not verified |
| Crypto | None on the home, FlexCloud, Evo or consulting pages | Not verified |
| API, webhooks, headless | "Webhooks… give you real-time insights into the actions of every distributor", with selectable events triggering email alerts or "API requests". A "web-based SDK" for branded distributor sites ([FlexCloud](https://www.infotraxsys.com/flexcloud)). BigCommerce partnership ([home](https://www.infotraxsys.com/)). No public API reference or sandbox found | Vendor claim |
| Back office | Evo: messaging, volume dashboards, rank-advancement reports, social sharing. No API, payment or security content ([Evo](https://www.infotraxsys.com/evo)) | Vendor claim |
| Security attestations | None on the pages reviewed. `infotraxsys.com/security` returns 404 | Not verified. See open question 6.3 on regulatory history |
| Pricing | Not published | Quote required |
| Lead time, exit | Not published | Not verified |

**Verdict: not shortlisted.** It is an order-centric enterprise engine with less public evidence than Exigo, and it has no crypto or attestation evidence. Revisit only if Exigo is rejected and an alternative enterprise engine is needed.

### 3.2 Trinity Software (Firestorm)

| Dimension | Evidence | Label |
|---|---|---|
| Positioning | Direct-selling platform for MLM, party plan and affiliate programmes. Firestorm® (MLM and party plan with e-commerce) and Ignite™ (marketing automation) ([trinitysoft.net](https://trinitysoft.net/)) | Vendor claim |
| Plan types | Mentions "Binary, Forced Matrix" and multilevel ([trinitysoft.net](https://trinitysoft.net/)) | Vendor claim |
| Versioning, simulation, clawbacks | Not mentioned ([Firestorm](https://trinitysoft.net/firestorm/)) | Not verified |
| Commission base flexibility | Not documented | Not verified |
| Crypto | None found | Not verified |
| API, headless | Shopify integration only ([Firestorm](https://trinitysoft.net/firestorm/)). `trinitysoft.net/api/` returns 404. No developer docs found | Not verified |
| Security attestations | None found | Not verified |
| Pricing | "Subscription pricing, 0 per distributor fees, 0 transaction fees", with "Unlimited Members & Customers" ([Firestorm](https://trinitysoft.net/firestorm/), [trinitysoft.net](https://trinitysoft.net/)). The [pricing page](https://trinitysoft.net/pricing-revised/) is an embedded image, so figures could not be extracted | Pricing model: Vendor claim. Amounts: Not verified |
| Lead time | "Launch your new system quickly!" in "four easy steps". Claims "1,000+ enterprises and start-ups" served ([Firestorm](https://trinitysoft.net/firestorm/)) | Vendor claim |
| Exit | Not documented | Not verified |

**Verdict: excluded.** It is a party-plan and Shopify back office with no API documentation, crypto support or controls evidence. It does not fit a headless integration with Privy.

### 3.3 DirectScale ↔ Exigo (status check)

| Item | Evidence | Label |
|---|---|---|
| Domain redirect | `https://www.directscale.com/` and `https://directscale.com/blog` both return HTTP 302 to `https://www.exigo.com/` (curl, 2026-10-06) | Verified (observed) |
| Exigo public statements | No mention of DirectScale on [exigo.com](https://www.exigo.com/), [company](https://www.exigo.com/company/) or [leadership](https://www.exigo.com/company/leadership-team/). Exigo's CEO is listed as Gary Fitzgerald | Verified (absence on these pages) |
| DirectScale developer portal | Still online, with v1.0 and v2.0 docs, a C# client, an Extension API and webhooks ([developers.directscale.com](https://developers.directscale.com/)). The changelog index we retrieved showed one entry, dated 4 November 2022 ([changelog](https://developers.directscale.com/changelog)) | Verified (online). Active maintenance: Not verified |
| Corporate relationship | A merger or acquisition is inferred from the redirect only | **Not verified** |

**Implication.** Treat DirectScale as part of the Exigo evaluation. Do not build against DirectScale's API until Exigo confirms the product's roadmap and support status.

### 3.4 Headless and API-first commission engines

Screening criterion: the engine must calculate multi-level (genealogy or downline) Commissions on amounts submitted by API. Candidates that only support flat, single-level affiliate or sales-rep commissions are excluded.

#### 3.4.1 Tapfiliate (affiliate platform with MLM levels): **conditional fallback**

| Dimension | Evidence | Label |
|---|---|---|
| Genealogy | REST endpoints `POST/DELETE /affiliates/{child_affiliate_id}/parent/` ("MLM: Parent affiliate") and `GET /programs/{id}/mlm-levels/` ([REST docs](https://tapfiliate.com/docs/rest/)) | Verified (API docs) |
| Multi-level calculation | Conversion responses show both a `standard` commission and `commission_type: "level-2"` / `kind: "level"` commissions to the upline affiliate ([REST docs](https://tapfiliate.com/docs/rest/)) | Verified (API docs). Maximum depth: Not verified |
| Arbitrary-event calculation | `POST /conversions/` accepts any `amount`, a free `external_id` and `meta_data`. A conversion can be identified by `customer_id`. `PATCH` supports `recalculate_commissions`. Commissions can be approved or disapproved ([REST docs](https://tapfiliate.com/docs/rest/)) | Verified. A fee-revenue event can be posted as a "conversion" (working assumption) |
| Reversal | "Disapprove a commission", "Delete a Conversion", and an amount change with `recalculate_commissions` ([REST docs](https://tapfiliate.com/docs/rest/)) | Verified |
| Comp-plan depth | No rank qualification, compression, generation or matching bonuses, or period close documented | Not verified (likely absent) |
| API details | `X-Api-Key` header, HTTPS only, rate-limit headers, API version 1.6 in the base URL ([REST docs](https://tapfiliate.com/docs/rest/)) | Verified |
| Pricing | Launch $89/mo, Scale $179/mo ("Standard multi-level marketing (MLM)"), Enterprise custom. **"API access" is listed only for Enterprise** ([pricing](https://tapfiliate.com/pricing/)) | Verified public. Helm needs Enterprise, so the effective price requires a quote |
| SOC 2 | Not found. The pricing page mentions only GDPR and a permission system ([pricing](https://tapfiliate.com/pricing/)) | Not verified |
| Crypto | Payout methods are configured per affiliate. No crypto payout rail confirmed | Not verified |

#### 3.4.2 Post Affiliate Pro (Quality Unit): **conditional fallback (weaker)**

| Dimension | Evidence | Label |
|---|---|---|
| Genealogy and multi-level | "A unique multi-level marketing feature that allows you to define commission structures for up to 99 tiers", on the Pro plan and above ([pricing](https://www.postaffiliatepro.com/pricing/)) | Vendor claim (pricing page) |
| Arbitrary-event calculation | `Pap_Api_Transaction` is a PHP class that can "manually add commissions", with `setTotalCost()`, `setCommission()`, `setStatus()` (A/P/D), `setTier()` and `setMultiTierCreation("Y")` to "automaticaly count multi-tier commissions for parent affiliates" ([Pap_Api_Transaction](https://support.qualityunit.com/427087-Pap_Api_Transaction)) | Verified (vendor docs) |
| API docs | API v1 and v3 index, with API-key articles ([API](https://support.qualityunit.com/712031-API)). The main documented client is a PHP library rather than a modern REST/OpenAPI spec | Verified (exists). REST coverage: Not verified |
| Pricing | Starter $89, Pro $139, Ultimate $269, Network $649 per month (annual: $79 / $129 / $249 / $599) ([pricing](https://www.postaffiliatepro.com/pricing/)) | Verified public |
| SOC 2 | Not on the pricing page | Not verified |
| Comp-plan depth | Fixed per-tier rates. No rank, compression or versioning documented | Not verified |

#### 3.4.3 Excluded candidates

| Candidate | Finding | Reason excluded |
|---|---|---|
| FirstPromoter | "Multi-tier commissions… across up to 3 levels" on every plan. APIs and webhooks on every plan. $49 / $99 / $149 per month by affiliate-revenue band ([pricing](https://firstpromoter.com/pricing), [docs](https://docs.firstpromoter.com/introduction)) | Hard limit of 3 levels and SaaS-referral orientation. No SOC 2 found. Could cover a very simple 3-level plan but is weaker than Tapfiliate |
| CaptivateIQ | "Completes annual audits against SOC1 and SOC2 security requirements" ([security policy](https://www.captivateiq.com/security-policy)) | Sales-incentive compensation for employee sales teams. No evidence of member-genealogy (downline) calculation. Per-payee enterprise model. Its SOC 2 statement is the strongest found in this pass, but the product category does not fit |
| Everstage | "Per-payee model". "Purpose-built for teams managing 20 - 30+ payees". No public rate ([pricing](https://www.everstage.com/pricing)) | Sales-team ICM. Per-payee pricing does not scale to thousands of Members. No genealogy evidence |
| QuotaPath | $35 or $50 per user per month plus a $525 or $800 platform fee. "Manager & Team-Based Plans" ([pricing](https://www.quotapath.com/pricing/)) | Per-seat sales-comp tool. A manager/team hierarchy is not an unlimited-depth Sponsor Tree |
| Commissionly | Commission automation for "payments, insurance". No multi-level, API or pricing on the home page ([home](https://www.commissionly.io/)) | No genealogy evidence |
| "Pillar" / "Pillar Commissions" | `pillar.io` is a creator link-in-bio commerce platform ([pillar.io](https://pillar.io/)). `pillarcommissions.com` did not resolve | No MLM commission product identified. Not verified |
| Spiff (Salesforce), Xactly, Varicent, Kobie | Not reviewed with primary sources in this pass (search budget exhausted). Spiff, Xactly and Varicent are sales-ICM products in the same category as CaptivateIQ and Everstage. Kobie is a loyalty platform | Not verified. Expected to fail the genealogy criterion for the same category reasons. Confirm only if the client asks |

**Bottom line for §3.4.** No dedicated, MLM-specific headless engine with public API docs and a SOC 2 report was identified. The real choice is between:

- **MLM Soft**, a full MLM engine with an API (no attestation); and
- **Tapfiliate Enterprise**, a referral-level engine with an excellent public API but a shallow comp model (no attestation found).

Generic ICM vendors have the attestations but not the genealogy model.

---

## 4. Comparison table (consistent with note 01 §3)

Legend: **V** = Verified, **C** = Vendor claim, **N** = Not verified, **—** = not offered or not applicable. MLM Soft cells marked † are upgraded from note 01.

| Capability | MLM Soft (updated) | InfoTrax | Trinity (Firestorm) | Tapfiliate | Post Affiliate Pro | FirstPromoter (excl.) |
|---|---|---|---|---|---|---|
| Unilevel / generation / rank (Sponsor Tree plans) | C | C ("any structure") | C | V (levels only; no rank) | C (tiers only) | V (3 levels) |
| Binary / matrix (placement tree) | C | N | C | — | — | — |
| Multiple trees | V† (plans bound to one or more trees) | N | N | — | — | — |
| Plan versioning / effective dates | N | N | N | N | N | N |
| Simulation / what-if | N | N (consulting only) | N | N | N | N |
| Commission explanations / trace | V† (wallet transaction log) | N | N | V (commission per conversion) | V (transaction records) | N |
| Refunds / clawbacks | C (order returns only) | N | N | V (disapprove / recalculate) | V (status D) | N |
| Calc separated from payout | V† | N | N | C | C | N |
| Non-order commission base (arbitrary amount via API) | V† (API-settable volume properties) | N | N | V (conversion `amount`) | V (`setTotalCost`) | N |
| Crypto deposits | — (by design) | N | N | — | — | — |
| Crypto payouts | N (custom payout system possible) | N | N | N | N | N |
| SOC 2 report available | N | N | N | N | N | N |
| ISO 27001 (current 2022 edition) | N | N | N | N | N | N |
| Public API docs | V† (per-tenant Swagger; help-centre guide) | N | N | V | V (PHP API) | V |
| Webhooks | V† (registration events) | C | N | C (triggered notifications, quota by plan) | N | C |
| Sandbox / stage env | N | N | N | N | N | N |
| Hosting model | SaaS, dedicated instance (C) | Cloud (C) | SaaS (C) | SaaS (V) | SaaS (V) | SaaS (V) |
| Published pricing | V | — | N (image only) | V (API on Enterprise only, quote) | V | V |

---

## 5. Pricing evidence (USD; research date 2026-10-06)

| Vendor | Item | Amount | Type | Status | Source |
|---|---|---|---|---|---|
| MLM Soft | Startup / Community / Network; setup | Unchanged from note 01 ($499 / $999 / $1,999 per month; setup "$10,000 to $30,000") | Recurring / one-time | Verified public | [pricing](https://www.mlmsoft.com/cloudplatform/subscription) |
| InfoTrax | All | — | — | Quote required | [home](https://www.infotraxsys.com/) |
| Trinity (Firestorm) | Subscription | Not extractable (image). "0 per distributor fees, 0 transaction fees" | Recurring | Quote required. Model: Vendor claim | [pricing](https://trinitysoft.net/pricing-revised/), [Firestorm](https://trinitysoft.net/firestorm/) |
| Exigo / DirectScale | All | — | — | Quote required | [exigo.com](https://www.exigo.com/) |
| Tapfiliate | Launch / Scale | $89 / $179 per month ($74 / $149 per month billed annually) | Recurring | Verified public | [pricing](https://tapfiliate.com/pricing/) |
| Tapfiliate | Enterprise (required for API access) | Custom | Recurring | Quote required | [pricing](https://tapfiliate.com/pricing/) |
| Post Affiliate Pro | Starter / Pro / Ultimate / Network | $89 / $139 / $269 / $649 per month ($79 / $129 / $249 / $599 annual) | Recurring | Verified public | [pricing](https://www.postaffiliatepro.com/pricing/) |
| FirstPromoter (excluded) | Starter / Business / Enterprise | $49 / $99 / $149 per month (affiliate-revenue bands to $5k, to $15k, above $15k per month) | Recurring | Verified public | [pricing](https://firstpromoter.com/pricing) |
| QuotaPath (excluded) | Growth / Premium | $35 / $50 per user per month + $525 / $800 platform fee per month | Recurring | Verified public | [pricing](https://www.quotapath.com/pricing/) |
| Everstage (excluded) | Per payee | Not published | Recurring | Quote required | [pricing](https://www.everstage.com/pricing) |
| CaptivateIQ (excluded) | All | Not reviewed | — | Quote required (not reviewed) | — |

Caveats:

- Affiliate-platform prices exclude implementation, which Cyclone would carry because the integration is API-driven.
- Per-payee ICM pricing scales with the number of paid Members and is not comparable to MLM tiers based on "income centres".

---

## 6. Open questions

**MLM Soft (additions to note 01 Q16–18)**

1. Provide read access to the API3 Swagger reference (`/api3/api/docs`) for a demo instance before contract. List the document types available besides `Purchase`.
2. Can API3 authenticate with service credentials (API keys or OAuth client credentials, with scopes) instead of admin login and password? What are the rate limits and token lifetimes?
3. Can a custom "External editable" volume property (for example `FEE_REVENUE`, in USD with 6+ decimals) drive unilevel, generation and matching bonuses? How is a submitted value reversed after a period has closed, and do upline Commissions claw back automatically?
4. Is there an idempotency key or a duplicate-detection rule for `document/create` and volume changes? What happens on Kafka redelivery?
5. List the full webhook event catalogue (beyond registration), signing method, retry policy and ordering guarantees.
6. Do you support plan versioning with effective dates, and what-if simulation on historical period data?
7. Provide SOC 2 Type II / ISO 27001:2022 evidence, or the latest penetration-test summary. Which data-centre regions are available, and who are the subprocessors ("overseas facilities")?

**InfoTrax**

8. What are the commission engine's plan types, versioning and simulation features, as product features rather than consulting? Is there a public API reference and sandbox? Can non-order events carry commissionable volume?
9. Provide current security attestations, plus pricing and lead time.
10. *Regulatory history (unconfirmed):* the analyst recalls a 2019 U.S. FTC data-security action involving InfoTrax Systems. We could not retrieve ftc.gov pages during this pass, so this is **Not verified** and must be checked on ftc.gov before it is mentioned in any client deliverable. If confirmed, request evidence of the remediation programme and independent assessments.

**Trinity Software**

11. Is there a public API? Is a headless deployment (no Firestorm back office) possible? Provide text pricing and security attestations. Low priority, since the vendor is excluded.

**Exigo / DirectScale**

12. Confirm the corporate relationship (the domain redirects to Exigo). Is the DirectScale platform and API still supported, and on what roadmap? Should new customers be placed on Exigo or DirectScale?

**Tapfiliate (if the fallback is pursued)**

13. What is the maximum number of MLM levels? Can per-level rates differ by affiliate group, and can rank-like groups be changed via API?
14. Enterprise pricing for API access. SOC 2 or other security attestation. Webhook catalogue and signing. Data export of the full parent tree and commission history.
15. Can payouts be disabled entirely, so that Tapfiliate only reports approved commissions for Cyclone's ledger and Privy-based payout?

---

## 7. Evidence limitations

- No WebSearch queries were available (quota already exhausted). Discovery relied on known official domains and direct URL probing. Vendors reachable only via search (for example, possible MLM-specific API engines not listed here) may have been missed.
- The MLM Soft help centre was read through Zendesk's public JSON API, because the HTML pages return 403 to automated fetchers. The content is the vendor's own published documentation.
- InfoTrax, Trinity and Exigo publish little technical detail. Their absence of evidence is not evidence of absence.
- Spiff, Xactly, Varicent and Kobie were not reviewed with primary sources.
