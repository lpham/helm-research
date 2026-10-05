# 07 — Addendum: on-ramp gaps and yield evidence gaps

- **Project:** Helm (Cyclone for AlphaWave)
- **Workstream:** Addendum to `03-fiat-onramp.md` and `04-yield.md`. Those notes are not edited; this note adds to them and corrects them where stated.
- **Research date:** 2026-10-06
- **Jurisdiction:** None confirmed. All findings are jurisdiction-neutral. Nothing here is a legal conclusion.
- **Decision context:** Release 1 is crypto-only Deposits. A fiat on-ramp is Phase 2, conditional on (a) counsel's review of the compensation plan and (b) written approval from at least two providers, or from an aggregator plus approved underlying providers.

**Evidence labels** (same as notes 03 and 04)
- **Verified:** read directly on the provider's or protocol's own page, repository, governance forum or audit report on the research date. Exact wording is quoted where it matters.
- **Vendor claim:** the provider's or protocol's description of itself (marketing, docs overview), not independently tested.
- **Not verified:** no primary evidence found, the page could not be read, or only press or secondary sources were available.

**Incident status labels** (section B.2)
- **Confirmed:** a primary source supports the yield note's claim.
- **Discrepancy:** a primary source exists but differs from the yield note in a material detail.
- **Not verified:** no primary source could be read.

**Method note.** The session's web-search quota was used up before this addendum began, so no search-engine queries were run. Every source below was reached by fetching a known official URL directly, or by reading the vendor's or protocol's own GitHub repositories (documentation source, audit folders) and public APIs (Discourse forum JSON). Pages that returned HTTP 403/404 or rendered only through JavaScript are listed in section D.

Glossary terms used: **Member**, **Deposit**, **Commission**, **Sponsor Tree**, **Yield Product**, **Staking** (see `GLOSSARY.md`).

---

## Summary

1. **None of the newly checked on-ramps publishes a statement accepting MLM. Most simply do not name it in public terms.** Alchemy Pay's legal pages still cannot be read. Its merchant guide describes a sales-led KYB review with no published prohibited-business list. Meld's Terms of Service (Meld Universal Inc., 15 May 2026) contain no MLM wording, but they pass each underlying provider's terms through to the customer. Most of those providers bar MLM (note 03). Mercuryo's partner terms (v5, 09.02.2026) and global and US individual terms do not name MLM. Its EEA terms (v1.0.5) name "Ponzi or pyramid schemes". Guardarian's terms prohibit illegal activity and fraud but name no scheme types. **Verified** (quotes and links in A.1–A.5).
2. **"Silent" is not the same as "accepts".** Each of these providers reviews partners at its own discretion (Mercuryo: "written express approval"; Alchemy Pay: "KYB Review"). Each also reserves the right to bar activity that its card schemes, acquirers or third-party providers prohibit (Mercuryo EEA §3.4). Written approval after full disclosure is still the only usable evidence of acceptance.
3. **Meld does not remove underlying-provider approval.** Meld's docs list an "Active account with the service provider" as a prerequisite, and its ToS says customers who do not accept a supplier's terms "should not ... use" that supplier's products. Privy routes its extended currencies through Meld only after the app completes KYB with Meld. **Verified.** In practice an aggregator still needs at least two underlying providers to accept Helm.
4. **Ramp Network:** the 2022 article listing "multi-level marketing" among industries Ramp "cannot currently work with" is still live and unchanged (last edited 8 Sep 2022). The current partner T&Cs (7 Jan 2026) and user ToS (24 Sep 2026) do not name MLM. Ramp still reserves termination for "reputational risk". The MLM restriction is therefore **Verified as published but dated**. **MoonPay:** no public partner or business terms were found. The consumer-level "certain multi-level marketing programs" clause is still in force (Terms of Use effective 13 May 2026). **Verified.**
5. **Unlimit Crypto's domain now redirects to `stable.com`, which returned no readable content.** Its current status is **Not verified**, and it should not be shortlisted until that is clarified. Kado was not researched (no primary source could be reached without search).
6. **Audit histories now have primary sources.**
   - **Rocket Pool:** 15 audits from April 2021 to February 2026 by Trail of Bits, Consensys Diligence, Sigma Prime, ChainSafe, Cantina and Bailsec, the latest being for the Saturn 1 upgrade.
   - **JitoSOL:** runs on the Solana Program Library (SPL) stake-pool program (`SPoo1...`), which has ten audit or formal-verification reports from 2021 to 2025. Jito's own satellite programs (StakeNet, Interceptor, Restaking) were audited by OtterSec, Offside Labs and Certora. Both StakeNet reports are marked "DRAFT".
   - **Verified** (B.1).
7. **Incident checks against note 04:**
   - **Confirmed:** Kiln/SwissBorg and Aave CAPO. The CAPO net DAO cost was later reduced from about 358 to about 317 WETH.
   - **Confirmed with a material update:** Kelp rsETH. Note 04 describes the coverage package as settled. At 24 April 2026 it was still a contested proposal at ARFC stage. By May 2026, most stolen rsETH had been recovered through liquidations and the DeFi United coalition was covering the rest.
   - **Not verified from primary sources:** Stream/xUSD and the three Hyperliquid HLP events, which are press-only. There are minor discrepancies in the HLP rows of note 04 (B.2).

---

## A. On-ramp gaps

### A.1 Alchemy Pay

| Topic | Finding | Label | Source |
|---|---|---|---|
| MLM / pyramid wording | No public prohibited-business list found. The legal and terms pages are JavaScript-rendered and returned no readable text (`alchemypay.org/terms`, `ramp.alchemypay.org` terms). The merchant guide includes no prohibited list | Not verified | [Merchant guide](https://alchemypay.readme.io/docs/merchant-access-and-integration-guide) |
| Partner due diligence | Six steps: "Contact Sales" (BD@alchemypay.org) → business information → "KYB Review" (compliance review; production credentials on approval) → sandbox integration → go live → support. The intake form asks for a "Project Brief" category (e.g., Centralized Exchange, DeFi/DEX, Gambling, Wallet, Fintech/Neo Bank, Others). There is no MLM category. Page updated 7 May 2026 | Verified | [Merchant guide](https://alchemypay.readme.io/docs/merchant-access-and-integration-guide) |
| Integration model | Page (hosted) integration; Standard API ("redirected to the ACH checkout page", on-ramp only); Native API (merchant builds all pages, on- and off-ramp); App, Android and iOS SDKs; webhooks ("When users buy or sell coins, we will push order information to merchants") | Verified (docs) | [On-ramp](https://alchemypay.readme.io/docs/alchemypay-on-ramp), [API integration](https://alchemypay.readme.io/docs/api-integration), [Webhook](https://alchemypay.readme.io/docs/webhook) |
| Merchant of record | Not stated in docs read | Not verified | — |
| KYC by provider | On-ramp flow: first-time buyers "may involve KYC which needs to provide personal information and complete a verification process" within the Alchemy Pay flow. A KYC page says "Merchant-side KYC on behalf of the user is not supported", but that page appears to relate to Alchemy Pay's card product, so it is not relied on here for the on-ramp | Vendor claim | [On-ramp](https://alchemypay.readme.io/docs/alchemypay-on-ramp), [KYC registration](https://alchemypay.readme.io/docs/kyc-registration) |
| Regions (broad) | On-ramp: "more than 40 countries' Bank transfer, Mobile wallets, regional providers". Off-ramp: "over 50+ countries". The coverage page names currencies including INR, IDR, JPY, KRW and VND (no decimals allowed for these) | Vendor claim | [On-ramp](https://alchemypay.readme.io/docs/alchemypay-on-ramp), [Coverage, fees and limits](https://alchemypay.readme.io/docs/fiat-currency-country-payment-method-coverage-plus-fees-and-limits) |
| Published fees | The coverage page points to an embedded table that could not be read. No fee figures were obtained | Not verified (quote required) | [Coverage, fees and limits](https://alchemypay.readme.io/docs/fiat-currency-country-payment-method-coverage-plus-fees-and-limits) |
| Off-ramp | Yes (Native API; off-ramp parameters documented) | Verified (docs) | [Off-ramp parameters](https://alchemypay.readme.io/docs/off-ramp-custom-parameters) |
| Privy | Not a Privy-listed provider. It can deliver to any wallet address via its own widget (analyst assessment, as in note 03) | — | — |

### A.2 Meld (aggregator; Privy's extended-currency partner)

| Topic | Finding | Label | Source |
|---|---|---|---|
| MLM / pyramid wording | Meld Universal Inc. Terms of Service (last updated 15 May 2026) contain no MLM, network-marketing, pyramid or Ponzi wording. They restrict "fraudulent or illegal activities" | Verified (absence in text read) | [Meld ToS](https://www.meld.io/policy/terms-of-service) |
| Pass-through of provider terms | "Suppliers have their own terms and conditions, and if Customer does not agree to abide by the applicable terms and conditions for any Suppliers, then Customer should not install or use such Third Party Products." | Verified | [Meld ToS](https://www.meld.io/policy/terms-of-service) |
| Exclusivity | "Customer will not partner or enter into any agreement with any other payment or onramp aggregation or orchestration service during the term." This matters if Helm wants Meld *and* Onramper as redundancy | Verified | [Meld ToS](https://www.meld.io/policy/terms-of-service) |
| Partner due diligence | Privy: "complete KYB with Meld to access their global onramp network." Meld docs: prerequisite "Active account with the service provider"; "either Meld can set it up for you, or you can set it up yourself". Whether each provider runs its own KYB on the end platform is not stated | Verified (KYB with Meld; provider account prerequisite). Per-provider review Not verified | [Privy funding config](https://docs.privy.io/guide/react/wallets/usage/funding/configuration), [Meld: Adding Onramps](https://docs.meld.io/docs/stablecoins/for-all-products/service-provider-setup) |
| Integration model | Three products: "White-Label API — you build the UI, Meld powers the rails"; "Meld Checkout — Meld's hosted UI"; "Virtual Account — bank-transfer onramp / offramp with no provider UI". Webhooks documented | Verified (docs) | [Crypto overview](https://docs.meld.io/docs/stablecoins/crypto-overview_/index), [Webhook events](https://docs.meld.io/docs/stablecoins/for-all-products/webhook-events) |
| Merchant of record | Meld describes itself as facilitating "discovery of, access to, and interaction with third-party providers". The user is redirected to "the onramp's UI, where they complete the transaction". Analyst reading: the underlying provider is the seller. Meld does not state merchant-of-record status | Verified (wording); MoR Not verified | [Meld ToS](https://www.meld.io/policy/terms-of-service), [Ramps flow](https://docs.meld.io/docs/stablecoins/crypto-overview_/ramps-flow) |
| KYC by provider | "The actual transaction is completed within the onramp's UI, where the user will have to complete KYC and enter payment information." | Verified (docs) | [Ramps flow](https://docs.meld.io/docs/stablecoins/crypto-overview_/ramps-flow) |
| Regions / scale | "50+ Network Partners", "54 Local Payment Methods", "184 Countries"; "SOC 2 Compliant". Privy: "Meld adds card, bank transfer, and local payment coverage across 100+ countries." Providers named in docs include Stripe, Transak, Mercuryo, Coinbase, Robinhood and PayPal | Vendor claim | [meld.io](https://www.meld.io/), [Privy card onramps](https://docs.privy.io/wallets/funding/fiat-onramp), [Adding Onramps](https://docs.meld.io/docs/stablecoins/for-all-products/service-provider-setup) |
| Published fees | None found | Not verified (quote required) | — |
| Off-ramp | Yes (sell flow; Virtual Account payouts) | Verified (docs) | [Sell flow](https://docs.meld.io/docs/stablecoins/additional-information/flow/sell-flow), [Payouts](https://docs.meld.io/docs/stablecoins/virtual-account-integration/payouts) |
| Privy compatibility | **Yes.** "To unlock the full list of 50+ currencies below, open the Funding page, click Configure on Meld, and complete its KYB." Default without Meld: "USD, EUR, AUD, and BRL through Stripe and MoonPay." | Verified | [Privy card onramps](https://docs.privy.io/wallets/funding/fiat-onramp) |

**Implication.** If Helm uses Privy's funding UI, the extra currencies depend on Meld KYB *plus* the providers Meld routes to. Several of those (Stripe, Transak, Coinbase) bar MLM in their own terms (note 03).

### A.3 Mercuryo (update to note 03 §4.6)

| Topic | Finding | Label | Source |
|---|---|---|---|
| Partner terms, MLM | "Terms of Service for Business", **Version 5, applicable from 09.02.2026**. No MLM, network-marketing, pyramid or Ponzi wording | Verified (absence in text read) | [Business terms](https://mercuryo.io/legal/terms-business/) |
| Individual terms (global) | Version 4.7.5 (from 08.12.2025), §10.1(viii): clients may not "provide Services which are prohibited by the law or conflict with public order and good morals". Scheme types are not named | Verified | [Global terms](https://mercuryo.io/legal/terms-global/) |
| Individual terms (US) | MoneyDream LLC (Delaware), v1.1 (from 05.13.2026), §7.1(10): no use "for goods or services that are prohibited by law or contradict public order and moral principles". Scheme types are not named | Verified | [US terms](https://mercuryo.io/legal/terms-US/) |
| Individual terms (EEA) | v1.0.5 (from 01.07.2026), §3.4: "You shall not use the Platform or any Service in connection with any unlawful, prohibited or restricted activity, including unlawful gambling or betting, fraud, deception, Ponzi or pyramid schemes, ... or any activity prohibited by applicable law ...". MLM is not named | Verified | [EEA terms](https://mercuryo.io/legal/terms-eea/) |
| Partner due diligence | Partner must supply an application, website domain, proof of rights to the website and a company-register extract. "The Company may interact with the partners only after receiving a written express approval from Mercuryo." | Verified | [Business terms](https://mercuryo.io/legal/terms-business/) |
| Integration | Widget and API (note 03). The business page returned HTTP 403 | Verified (note 03) | [API migration docs](https://github.com/mercuryoio/api-migration-docs) |
| Merchant of record | Not stated in terms read | Not verified | — |
| KYC by provider | Global terms: KYC/DD at account opening (email, phone, passport/ID, proof of address). EEA: regulated KYC performed for the third-party provider Criptan Trade, S.L. from 1 Jul 2026 | Verified | [Global terms](https://mercuryo.io/legal/terms-global/), [EEA terms](https://mercuryo.io/legal/terms-eea/) |
| Entities / regions | Moneymaple Tech Ltd (Canada, FINTRAC MSB); Moneychurros S.L. (Spain, listed as MiCA CASP); Monetley Ltd (UK, FCA EMI); Moneytea Ltd (UK, EMD agent). The page also says Criptan Trade, S.L. (CNMV, MiCA) provides exchange services "on behalf of MONEYCHURROS S.L." Country coverage not published in pages read | Verified (licence page as stated) | [Licences](https://mercuryo.io/legal/licenses/) |
| Published fees (end user) | Global terms: "The Company's fee for buying BTC and other virtual currencies in exchange for fiat equals to 3.95%; the fee for transfer to the bank card equals to 3.95% (minimum - 4 EUR)." "The Fee for payments made through the Pix method is 4 percent, with a minimum amount of 4 euros." | Verified | [Global terms](https://mercuryo.io/legal/terms-global/) |
| Partner fees | "Mercuryo Commission ... percentage mutually agreed"; "Subscription Fee ... determined at the discretion of Mercuryo ... payable ... in advance"; partner may add an "Upper Commission" | Verified (structure); amounts Not verified | [Business terms](https://mercuryo.io/legal/terms-business/) |
| Off-ramp | Sell endpoints exist (note 03); global terms price "transfer to the bank card" | Verified | [Global terms](https://mercuryo.io/legal/terms-global/) |
| Privy | Not a Privy default. Meld lists Mercuryo as a routable provider | Verified (Meld docs) | [Adding Onramps](https://docs.meld.io/docs/stablecoins/for-all-products/service-provider-setup) |

### A.4 Ramp Network re-check

| Topic | Finding | Label | Source |
|---|---|---|---|
| Restricted industries article | Still live. Published 9 Aug 2022, last edited 8 Sep 2022. Unchanged wording: "Get-rich-quick schemes, multi-level marketing, drop-shipping, or other activities that may be considered unfair, deceptive, or abusive acts or practices (UDAAP)", plus "Any activities that are illegal or that Ramp Network, in its sole discretion, identifies as high-risk" | Verified (dated 2022) | [Ramp blog](https://rampnetwork.com/blog/integrating-with-ramp-network-things-you-need-to-get-started) |
| Partner T&Cs | Last updated 7 Jan 2026. No enumerated industry list. Due-diligence checks after execution; immediate suspension or termination "without advance notice" for failed due diligence or "security or reputational risks". Maintenance fee US$2,000/yr below US$1M volume (reduced 50% to US$1,000 for 2025, invoiced January 2026) | Verified | [Partner T&Cs](https://rampnetwork.com/partners-terms-conditions) |
| User ToS | UK terms 24 Sep 2026; US terms 17 Mar 2026. §15 "Use restrictions": no "illegal activity", nothing "unlawful, criminal, harmful or fraudulent". MLM is not named | Verified | [ToS](https://rampnetwork.com/terms-of-service) |
| Assessment | No newer public statement either withdraws or reaffirms the 2022 MLM restriction. Treat Ramp as **restricted** unless Ramp says otherwise in writing | Analyst assessment | — |

### A.5 MoonPay re-check

- **Partner or business terms:** none public. The `/legal` index lists Standard Terms, MoonPay Rails Terms, Stablecoin Terms, Launchpad Terms, Licences, Pricing disclosure and Privacy. There are no partner, merchant or acceptable-use terms. Guessed paths `/legal/partner_terms` and `/legal/acceptable_use_policy` returned no policy text. **Verified (absence).** ([MoonPay legal](https://www.moonpay.com/legal))
- **Consumer clause still in force:** Terms of Use effective 13 May 2026, §4.1(h) "Unacceptable Activity": transactions that "support pyramid or ponzi schemes, matrix programs, other 'get rich quick' schemes or certain multi-level marketing programs". **Verified.** ([Express Checkout ToU](https://www.moonpay.com/legal/terms_of_use_express_checkout))
- **Pricing disclosure (new):** MoonPay fee "up to 4.5%". Minimums up to US$3.99 (direct) or US$4.50 (partner-referred). Non-USD markups of 0.25–10%. Partner "Ecosystem Fees" are shown as line items. Virtual accounts about 1% (0–10% range). **Verified.** ([Pricing disclosure](https://www.moonpay.com/legal/pricing_disclosure))
- **Partner KYB:** "Once you've completed the KYB process, your API keys will be made available". MoonPay is merchant of record. **Verified.** ([On-ramp docs](https://dev.moonpay.com/docs/on-ramp-overview))

### A.6 Optional Asia-relevant providers

**Guardarian**
- **Entities:** FinSeven CZ s.r.o. (Czech Republic) and GRNTech Solution Inc. (Ontario; FINTRAC MSB C10001703). Main ToS last updated 5 May 2026. A B2B ToS section on the same page is dated 31 Dec 2025. **Verified.** ([Guardarian ToS](https://guardarian.com/terms-of-service))
- **Prohibited use:** users may not be "involved in any illegal activities, including but not limited to money laundering, terrorist financing, fraud, illegal gambling, illegal weapons sale and drug trafficking". Pyramid, Ponzi and MLM are not named. **Verified (absence of scheme names).**
- **Partner due diligence (B2B section):** the company must "identify and verify your identity" and shares data with "Sum and Substance". **Verified.**
- **Fees:** the ToS shows only refund fees (e.g., SEPA "5 EUR ... plus bank fees"). Transaction fees: **Not verified**.
- **Integration model, merchant of record, regions, off-ramp:** **Not verified** (no docs read).

**Unlimit Crypto**
- `www.crypto.unlimit.com` now returns **301 → `https://stable.com/`**. That page returned no readable content. **Verified (redirect); status Not verified.** ([redirect source](https://www.crypto.unlimit.com/))
- The Unlimit group legal page still links an "Unlimit Crypto User Privacy Notice" at the old domain. **Verified.** ([Unlimit legal](https://www.unlimit.com/legal/))
- Do not shortlist until it is clear which entity now operates the product.

**Kado / others:** not researched (no search available). **Not verified.**

### A.7 MLM-acceptance table (addendum providers; read with note 03 §5)

| Provider | Applies to integrating platform? | MLM / pyramid wording (quoted) | Discretionary review | Label | Source |
|---|---|---|---|---|---|
| Alchemy Pay | Merchant agreement not public | None readable | "KYB Review" by compliance | Not verified | [Merchant guide](https://alchemypay.readme.io/docs/merchant-access-and-integration-guide) |
| Meld | Meld ToS + each supplier's terms ("should not ... use" if not accepted) | None in Meld ToS | KYB with Meld (Privy); provider account prerequisite | Verified (absence + pass-through) | [Meld ToS](https://www.meld.io/policy/terms-of-service) |
| Mercuryo (business) | Yes | None | "written express approval" | Verified (absence) | [Business terms](https://mercuryo.io/legal/terms-business/) |
| Mercuryo (EEA users) | Transaction-level | "Ponzi or pyramid schemes"; "any activity prohibited by ... card scheme" | — | Verified | [EEA terms](https://mercuryo.io/legal/terms-eea/) |
| Ramp Network | Partner level (article) | "Get-rich-quick schemes, multi-level marketing, drop-shipping ..." | DD review; "reputational risks" | Verified (2022 article, still live) | [blog](https://rampnetwork.com/blog/integrating-with-ramp-network-things-you-need-to-get-started), [Partner T&Cs](https://rampnetwork.com/partners-terms-conditions) |
| MoonPay | Transaction-level; partner terms not public | "pyramid or ponzi schemes, matrix programs ... certain multi-level marketing programs" | KYB | Verified (consumer); partner Not verified | [ToU](https://www.moonpay.com/legal/terms_of_use_express_checkout) |
| Guardarian | ToS incl. B2B section | None (illegal activity, fraud) | Identity verification via Sumsub | Verified (absence) | [ToS](https://guardarian.com/terms-of-service) |
| Unlimit Crypto | — | — | — | Not verified (domain redirects) | — |

**Reading the table.** "No MLM wording" means only that the public text is silent. Every provider keeps discretionary approval and termination rights. None states that it accepts MLM businesses.

### A.8 Fees (addendum providers)

| Provider | Published end-user fees | Platform/partner cost | Label | Source |
|---|---|---|---|---|
| Alchemy Pay | Not obtainable (embedded table unreadable) | Not published | Quote required | [Coverage page](https://alchemypay.readme.io/docs/fiat-currency-country-payment-method-coverage-plus-fees-and-limits) |
| Meld | Not published (provider fees apply) | Not published | Quote required | — |
| Mercuryo | Buy 3.95%; bank-card payout 3.95% (min €4); Pix 4% (min €4) | Agreed commission + discretionary subscription fee | Verified (end-user); partner amounts Quote required | [Global terms](https://mercuryo.io/legal/terms-global/), [Business terms](https://mercuryo.io/legal/terms-business/) |
| MoonPay | Up to 4.5%; minimums up to $3.99 / $4.50; non-USD markup 0.25–10% | Not published | Verified | [Pricing disclosure](https://www.moonpay.com/legal/pricing_disclosure) |
| Ramp Network | Shown at checkout | $2,000/yr maintenance if < $1M volume ($1,000 for 2025) | Verified (partner fee) | [Partner T&Cs](https://rampnetwork.com/partners-terms-conditions) |
| Guardarian | Not published in ToS (refund fees only) | Not published | Quote required | [ToS](https://guardarian.com/terms-of-service) |

---

## B. Yield gaps

### B.1 Audit histories

#### Rocket Pool (rETH)

Sources: the audit list on Rocket Pool's Immunefi programme page (last updated 2 Sep 2026; max bounty US$150,000) and Rocket Pool's own docs source on GitHub. The report PDFs on `rocketpool.net/files/audits/` and the `rocketpool.net/protocol/security` page returned HTTP 403 to automated fetch, so **report contents were not reviewed**. Auditor, date and scope are as listed by the protocol. **Verified** (listing).

| # | Auditor | Date (as listed) | Scope | Report |
|---|---|---|---|---|
| 1 | Trail of Bits | 30 Apr 2021 | Initial protocol (pre-mainnet) | [PDF](https://github.com/trailofbits/publications/blob/master/reviews/RocketPool.pdf) |
| 2 | Consensys Diligence | 30 Apr 2021 | Initial protocol | [Report](https://consensys.net/diligence/audits/2021/04/rocketpool/) |
| 3 | Sigma Prime | 30 Apr 2021 | Initial protocol | [PDF](https://rocketpool.net/files/audits/sigma-prime-audit.pdf) |
| 4 | Sigma Prime | 31 Oct 2021 | Fix review | [PDF](https://rocketpool.net/files/audits/sigma-prime-fix-review.pdf) |
| 5 | Consensys Diligence | 31 May 2022 | Redstone upgrade | [PDF](https://rocketpool.net/files/audits/consensys-audit-redstone.pdf) |
| 6 | Sigma Prime | 31 May 2022 | Redstone | [PDF](https://rocketpool.net/files/audits/sigma-prime-audit-redstone.pdf) |
| 7 | Sigma Prime | 30 Nov 2022 | Atlas upgrade (deployed 18 Apr 2023) | [PDF](https://rocketpool.net/files/audits/sigma-prime-audit-atlas.pdf) |
| 8 | Consensys Diligence | 31 Dec 2022 | Atlas | [PDF](https://rocketpool.net/files/audits/consensys-audit-atlas.pdf) |
| 9 | Consensys Diligence | 30 Nov 2023 ("Late November to Mid December 2023") | Houston upgrade | [Report](https://consensys.io/diligence/audits/2023/12/rocket-pool-houston/) |
| 10 | Sigma Prime | 29 Feb 2024 ("x2 ... Late November 2023, then a second round March 2024") | Houston | [PDF](https://rocketpool.net/files/audits/sigma-prime-audit-houston.pdf) |
| 11 | ChainSafe | 31 Mar 2024 ("Mid January to April 2024") | Houston | [PDF](https://rocketpool.net/files/audits/chainsafe-audit-houston.pdf) |
| 12 | Sigma Prime | 31 Aug 2024 | Houston hotfix review | [PDF](https://rocketpool.net/files/audits/sigma-prime-houston-hotfix-review.pdf) |
| 13 | Cantina | 22 Dec 2025 | Saturn 1 (megapools, rETH buffer) | [PDF](https://rocketpool.net/files/audits/cantina-audit-saturn-1.pdf) |
| 14 | Bailsec | 29 Jan 2026 | Saturn 1 | [PDF](https://rocketpool.net/files/audits/bailsec-audit-saturn-1.pdf) |
| 15 | Sigma Prime | 5 Feb 2026 | Saturn 1 | [PDF](https://rocketpool.net/files/audits/sigma-prime-audit-saturn-1.pdf) |

Sources: [Immunefi: Rocket Pool](https://immunefi.com/bug-bounty/rocketpool/information/); [Houston audits (docs source)](https://github.com/rocket-pool/docs.rocketpool.net/blob/main/docs/en/upgrades/houston/whats-new.md); [Saturn 1 audits (docs source)](https://github.com/rocket-pool/docs.rocketpool.net/blob/main/docs/en/upgrades/saturn-1/whats-new.mdx). Saturn 0 was deployed 28 Oct 2024 (parameter change only; docs). Whether Saturn 1 is deployed on mainnet as of the research date is **Not verified**.

Note for note 04: Rocket Pool's Saturn 1 docs describe an rETH withdrawal buffer of 1% of TVL (RPIP-65). This adds to note 04's RPIP-71 queue point. **Verified** (docs source above).

#### Jito (JitoSOL and related programs)

**Architecture.** "JitoSOL is built on the stake pool program developed by Solana Labs". It uses "the Solana Program Library deployed stake pool program at address `SPoo1Ku8WFXoNDMHPsrGSTSG1Y47rzgn41SLUNakuHy`". Upgrade keys are "owned by a committee of Solana Staking Ecosystem participants". "Jito DAO has the manager role for the JitoSOL pool", and validator selection runs through StakeNet. **Verified** ([Jito security overview, docs source](https://github.com/jito-foundation/jito-omnidocs/blob/master/jitosol/jitosol-liquid-staking/security/overview/index.md), [Deployed programs](https://github.com/jito-foundation/jito-omnidocs/blob/master/jitosol/jitosol-liquid-staking/security/deployed-programs/index.md)). jito.network returned HTTP 403, so the docs were read from Jito's GitHub source.

| Component | Auditor | Date | Scope / notes | Label | Report |
|---|---|---|---|---|---|
| SPL stake pool (JitoSOL core) | Kudelski | 2021-07-07 | Listed by Jito (commit 3dd6767) | Verified | [solana-labs/security-audits/spl](https://github.com/solana-labs/security-audits/tree/master/spl) |
| SPL stake pool | Neodyme | 2021-10-16 | Listed by Jito (commit 0a85a9a) | Verified | same |
| SPL stake pool | Quantstamp | 2021-10-22 | Listed by Jito (initial 99914c9, re-review 3b48fa0) | Verified | same |
| SPL stake pool | Neodyme | 2022-12-10; 2023-01-31; 2023-11-14 | Later reviews (not listed on Jito's page) | Verified (repo) | same |
| SPL stake pool | OtterSec | 2023-01-20 | Later review | Verified (repo) | same |
| SPL stake pool | Halborn | 2023-01-25; 2023-12-31 | Later reviews | Verified (repo) | same |
| SPL stake pool | Certora | 2025-09-15 | Formal verification | Verified (repo) | same |
| StakeNet: Steward | OtterSec | Assessed 19 Jun–29 Jul 2024; report dated 28 Oct 2024, **marked "DRAFT"** | 5 findings incl. one high-risk (validator state desynchronisation) | Verified | [PDF](https://github.com/jito-foundation/stakenet/blob/master/security-audits/jito_steward_audit.pdf) |
| StakeNet: Validator History | OtterSec | Assessed 1 Jan–7 Feb 2024; report dated 10 Feb 2024, **marked "DRAFT"** | 5 findings | Verified | [PDF](https://github.com/jito-foundation/stakenet/blob/master/security-audits/jito_validator_history_audit.pdf) |
| Stake Deposit Interceptor | Offside Labs | Nov 2024 (v0.1) | Interceptor program (time-decaying deposit fee) | Verified | [repo folder](https://github.com/jito-foundation/stake-deposit-interceptor/tree/master/security-audits) |
| Stake Deposit Interceptor | Certora | 24 Nov–13 Dec 2024; fix re-verification 24 Dec 2024 | Formal verification | Verified | same |
| Jito–Coinbase integration | Certora | 10–19 Mar 2026 (v0.3) | Commit c120888 | Verified (scope beyond title Not verified) | same |
| Jito Restaking / Vault | OtterSec 2024-10-25; Certora 2024-10-29 and 2024-12-23; Offside 2024-11-20 | — | Restaking and vault programs (not part of JitoSOL's stake pool) | Verified (README table) | [restaking README](https://github.com/jito-foundation/restaking#security-audits) |

**Caveats.**
- Jito's own page lists only the three 2021 SPL audits. Which SPL program version is currently deployed at `SPoo1...`, and which later audit covers that version, is **Not verified**.
- The two StakeNet reports are marked "DRAFT". Whether final versions exist is **Not verified**.
- Jito's SECURITY.md points to an Immunefi programme ([link](https://immunefi.com/bug-bounty/jito/information/)), but that page returned HTTP 404 on the research date. Bounty status: **Not verified**.

### B.2 Incident verification

| # | Incident (as in note 04) | Date | Amount | Cause | Made whole? | Status | Primary sources |
|---|---|---|---|---|---|---|---|
| 1 | Kiln API compromise → SwissBorg SOL Earn | 8 Sep 2025 | "over 192,000 SOL"; "≈$41M" (SwissBorg) | "compromise of a GitHub access token belonging to a Kiln infrastructure engineer", used to inject a payload into the Kiln Connect API that changed stake-account authority during unstaking (Kiln, SwissBorg). Kiln exited ETH validators and rotated "all service account credentials and access keys" | SwissBorg: "No breach of SwissBorg. Balances remain safe, redemptions paused, recovery ongoing." No explicit statement on full compensation was found in the pages read | **Confirmed** (make-whole Not verified) | [SwissBorg (updated 17 Nov 2025)](https://swissborg.com/blog/swissborg-security-update-kiln-breach), [Kiln (7 Oct 2025)](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information) |
| 2 | Aave CAPO oracle misconfiguration | 10 Mar 2026 | 34 accounts; about 10,938 wstETH liquidated (USD figure of about $26–27M is derived, not checked against a primary) | CAPO snapshot ratio and timestamp misaligned under on-chain rate limits. The wstETH rate was depressed about 2.85% on the Ethereum Core and Prime instances | **Yes.** No protocol bad debt. Reimbursement AIP for 512.19 ETH executed and distributed. Net DAO cost was initially about 358 ETH, then **reduced to 316.94 WETH** after further searcher and builder recoveries. Forum commenters raised a lack of per-user accounting and one payment possibly about 20 WETH short (community comment, Not verified) | **Confirmed** (update: net cost lower than note 04) | [Post-mortem (Chaos Labs, 10 Mar 2026)](https://governance.aave.com/t/post-mortem-exchange-rate-misallignment-on-wsteth-core-and-prime-instances/24269), [Reimbursement AIP (TokenLogic, 11 Mar 2026)](https://governance.aave.com/t/direct-to-aip-wsteth-capo-oracle-incident-user-reimbursement/24275) |
| 3 | Kelp rsETH exploit → Aave WETH shortfall | 18 Apr 2026 | 116,500 rsETH released from the Ethereum-side OFT adapter. Of this, 89,567 rsETH was deposited on Aave (one address supplied 53,000 rsETH and borrowed 52,460 WETH on Core). Shortfall about 163,183 ETH initially, about 75,081 ETH residual after recoveries | Forged LayerZero cross-chain packet through a 1-of-1 DVN configuration (LlamaRisk analysis on Aave forum). Kelp/LayerZero root-cause attribution itself: Not verified | **Partly, and still in progress as of the latest primary read (1 Jun 2026).** On 24 Apr 2026 the coverage plan (14,570 ETH donations, up to 30,000 ETH Mantle credit facility, 25,000 ETH from Aave DAO) was an **ARFC with visible community opposition**, not an approved decision. On 6 May 2026 the attacker positions were liquidated by AIP#478: 106,993 rsETH recovered (89,567 from Aave and 17,426 from Compound) of about 112,103 unbacked. The remaining ~5,211 rsETH "is to be covered by the DeFi United coalition's committed ETH". WETH was unfrozen. An Arbitrum AIP to release 30,000 ETH reached quorum. Whether the DAO's 25,000 ETH was approved, and when remediation finished, is Not verified | **Discrepancy** (note 04 presents the coverage package as settled; it was a proposal and was later superseded by the recovery path) | [Incident thread](https://governance.aave.com/t/rseth-incident-2026-04-18/24481), [LlamaRisk report (20 Apr)](https://governance.aave.com/t/rseth-incident-report-april-20-2026/24580), [Funding ARFC (24 Apr)](https://governance.aave.com/t/arfc-rseth-incident-funding-update/24740), [WETH unfreeze AIP (9 May)](https://governance.aave.com/t/direct-to-aip-weth-unfreeze-and-ltv-restoration-across-aave-v3-instances/24878), [Aave Labs May update](https://governance.aave.com/t/al-development-update-may-2026/25013) |
| 4 | Stream Finance / xUSD → Morpho curators | Nov 2025 | Note 04: about $93M disclosed loss; about $0.7M direct bad debt in one Morpho vault | Not verified from Stream or Morpho primary sources. Morpho's October and November 2025 "Morpho Effect" posts do not mention it. A third-party RFC on the Morpho forum (Sigma Labs, Jun 2026) describes curators routing USDC into recursive xUSD loops and "an estimated $285M–$700M ... at risk across Morpho, Euler, and Silo". That is a different metric and not a primary source | Not verified | **Not verified** | [Morpho Effect Nov 2025](https://morpho.org/blog/morpho-effect-november-2025) (silent), [Morpho forum RFC (third party)](https://forum.morpho.org/t/rfc-a-user-centric-defi-collateral-transparency-framework-phase-1/2301) |
| 5a | Hyperliquid HLP: ETH whale liquidation | 12 Mar 2025 | About $4M (press) | Whale withdrew margin; HLP absorbed liquidation | Not verified | **Not verified** (cited Defiant article body did not load; no Hyperliquid primary read) | [The Defiant](https://thedefiant.io/news/defi/whale-s-nine-figure-eth-liquidation-costs-hyperliquid-usd4-million) |
| 5b | Hyperliquid HLP: JELLYJELLY | 26 Mar 2025 | Peak unrealised HLP P&L of −$13.5M (press) | Short squeeze on illiquid market. Validators delisted; settled at $0.0095 | Hyperliquid statement as quoted in press: "All users apart from flagged addresses will be made whole from the Hyper Foundation." This concerns affected *users*, not necessarily HLP depositors. HLP's final realised result: Not verified | **Not verified** (press only) | [Yahoo/CoinDesk syndication](https://sg.finance.yahoo.com/news/hyperliquid-delists-jelly-vault-squeezed-160020190.html) |
| 5c | Hyperliquid HLP: POPCAT | 12–13 Nov 2025 | $4.9M (press) | About $3M split over 19 wallets built a $20–30M long, then pulled a supporting bid | Not reported | **Not verified** (press only). Minor discrepancy: The Block reports deposits and withdrawals "paused for maintenance" with **no Hyperliquid statement linking the pause to POPCAT**. Note 04 places the pause in the POPCAT row as an impact | [CoinDesk](https://www.coindesk.com/markets/2025/11/13/peak-degen-warfare-alleged-popcat-manipulation-hits-hyperliquid-with-usd4-9m-loss), [The Block](https://www.theblock.co/news/defi/2025-11-12-hyperliquid-pauses-deposits-withdrawals-popcat-trading-scheme-speculation-378606) |

**HLP primary-data attempt.** Hyperliquid's public info API (`vaultDetails` for HLP, `0xdfc2...f303`) confirms the vault is "Hyperliquidity Provider (HLP)". Its all-time P&L series has only about 100 points since May 2023, which is too coarse to show or rule out single-day losses. The event figures therefore stay press-sourced.

**Corrections and updates to note 04 suggested by this addendum** (for the editor of note 04; note 04 was not changed):
1. rsETH: describe the 24 Apr coverage package as a *proposal*. Add the May 2026 recovery facts (liquidation by AIP#478, 106,993 rsETH recovered, DeFi United covering the remainder). Mark the final outcome as still being confirmed. The 116,500 rsETH figure can be upgraded from press to the Aave forum (LlamaRisk).
2. Aave CAPO: the net DAO cost fell to about 316.94 WETH after later recoveries.
3. Kiln: the root cause is now Verified at Kiln's own post as well as SwissBorg's. SwissBorg Member compensation remains Not verified.
4. HLP POPCAT: the pause was not officially linked to the event.
5. Rocket Pool and Jito "Audits" cells can now cite B.1.

---

## C. Open questions

**For providers** (only after Cyclone/AlphaWave approve engagement; no contact made)
1. **Alchemy Pay:** current merchant agreement and prohibited-business list; merchant-of-record entity per region; fee schedule; whether a "network marketing" platform can pass KYB on full disclosure.
2. **Meld:** does each routed provider run its own KYB on the integrating app, or rely on Meld's? Can some providers decline Helm while others serve it? Does the ToS exclusivity clause bar a parallel Onramper contract? What are Meld's fees? Does Privy's Meld integration run under Privy's Meld agreement or the app's own?
3. **Mercuryo:** subscription-fee amount; merchant of record; position on MLM platforms under the business terms; country list.
4. **Ramp Network:** does the 2022 restricted-industries list still apply?
5. **MoonPay:** partner agreement and prohibited list; whether "certain multi-level marketing programs" is assessed at partner level.
6. **Guardarian / Unlimit Crypto (Stable):** integration docs, merchant of record, fees. For Unlimit: which entity operates the product after the redirect.

**For legal counsel**
7. Does a provider's silence on MLM in public terms (Meld, Mercuryo business, Guardarian) materially change the likelihood of approval? Note that the "any activity prohibited by ... card scheme" clauses (Mercuryo EEA) import card-network MLM rules indirectly.
8. Same items as note 03 §10 (compensation-plan characterisation; separate-entity structures).

**Yield, technical and due diligence**
9. Rocket Pool: is Saturn 1 live on mainnet, and do the Saturn 1 audit reports cover the deployed commit?
10. Jito: which SPL stake-pool version is deployed at `SPoo1...`, and are final (non-draft) StakeNet audit reports available?
11. SwissBorg: were affected SOL Earn users fully compensated, and from what source?
12. Aave rsETH: was the 25,000 ETH DAO contribution approved? Is the remediation complete, with all WETH suppliers whole?
13. Stream/xUSD and Hyperliquid HLP: obtain primary statements (Stream disclosure, Morpho or curator posts, Hyperliquid announcements) before using figures in client-facing risk disclosures.

---

## D. Evidence limitations

- No web-search queries were available (session quota exhausted). Coverage of providers was limited to official URLs that could be reached directly. Kado was not researched, and Guardarian's integration docs were not located.
- **HTTP 403:** Mercuryo business page, `rocketpool.net` (security page and audit PDFs), `jito.network` docs, Consensys Diligence audit page, Incrypted.
- **HTTP 404:** Jito's Immunefi page.
- **JavaScript-only (unreadable):** Alchemy Pay legal pages, `stable.com`.
- **Wayback Machine:** temporarily offline during research.
- Rocket Pool audit dates and scopes come from the protocol's Immunefi listing and docs. The report PDFs themselves were not read.
- Hyperliquid incident figures are press-only. Exact numbers vary by outlet.
- Fees are as published on the research date and may change. No provider was contacted, and no account was created.
