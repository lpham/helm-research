# Executive summary and recommended direction

## Purpose

AlphaWave intends to offer a crypto-based financial product through its established multi-level marketing (MLM) network. This report identifies the fastest credible way to build a first release from existing software. It covers MLM and CRM vendors, wallet and custody infrastructure, fiat on-ramps, Yield Product options and compliance tooling, and it recommends an architecture, a cost envelope and a 30-day scope.

The research was desk-based and conducted on 6 October 2026. No vendor was contacted and no account was opened. Every material claim is labelled as verified, a vendor claim, a working assumption or not verified (see section 12).

## Recommended direction

**Primary: a modular architecture (Option 2).** AlphaWave buys each core capability from a specialist and Cyclone integrates them behind one Member experience and one admin back office:

- **MLM core:** a headless commission engine and Sponsor Tree. MLM Soft is the lead candidate, with Exigo as the alternative to demonstrate side by side.
- **Member wallets:** Privy embedded wallets, owned by the Member, with no Privy features that depend on Stripe or Bridge.
- **Operator treasury:** a separate wallet with multi-person approval for Commission payouts.
- **Ledger and back office:** owned by Cyclone. The ledger is the single financial source of truth.
- **Compliance tooling:** tiered KYC (Sumsub or Didit) and sanctions screening of every wallet address from day one.
- **Customer operations:** a SaaS helpdesk (Zendesk or Freshdesk) linked to the back office, with CRM deferred.
- **Yield Product:** a provider-neutral adapter built now, switched on later, with Privy Earn (Morpho or Aave vaults) as the shortest route.

**Fallback: the same modular design with different components.** A Stripe-independent wallet stack, Turnkey with Alchemy Smart Wallets or ZeroDev Kernel, replaces Privy for Member wallets, and Fireblocks, Cobo or a Safe multisig runs the treasury. Because Privy is owned by Stripe, this alternative should be tested in parallel from week 1. Exigo or Epixel replaces MLM Soft if the lead candidate fails its demonstration or security due diligence. The integrated white-label option (Option 1) is not recommended for real funds because no candidate documents custody, signing authority or a genuine yield source.

**QUANT (Option 3)** is treated as a Phase 2 integration for algorithmic trading only. Its engine is not a dependency of the first release, and no Member funds are exposed to it in that release.

## Headline findings

1. **No MLM vendor offers a genuine Yield Product.** Every "staking" or "investment plan" feature found is an operator-set percentage displayed on a dashboard, with no named protocol behind it. A Yield Product must therefore come from outside the MLM software.
2. **Stripe, and almost every major fiat on-ramp, prohibits MLM businesses.** Stripe lists "Multilevel marketing services offering commission or recruitment-based sales" and "Cryptocurrency mining and staking" as prohibited (updated 22 September 2026). Coinbase, Transak, Banxa, Ramp and Bridge carry similar prohibitions. **Release 1 should accept crypto Deposits only**; fiat is a gated Phase 2 item.
3. **Privy fits the wallet requirement technically, but not through its Stripe-backed features.** Its fiat, custodial-wallet and KYC features run on Bridge, a Stripe company whose terms prohibit MLM. Its core wallet, policy engine and Earn features are usable, subject to Privy's written acceptance of the business model and an Enterprise quotation.
4. **Custody depends on who controls signing, not on labels.** Embedded wallets with a platform-held signer are a hybrid model, and an operator-run vault is custodial. Global AML standards test control in the same way.
5. **The assumption that crypto Deposits need no KYC is not supported.** The client's own compensation plan requires KYC for leadership ranks, on-ramps impose KYC, and Commission payouts always leave an operator-controlled treasury. Tiered KYC is the planning base case, pending legal advice.
6. **The commission base is the most consequential open business question.** Crypto-MLM software most commonly pays Commissions on Members' Deposits or on calculated returns, which are the patterns regulators associate with Ponzi and pyramid schemes. Paying Commissions from platform fee revenue, such as a fee on real yield, is structurally safer, and MLM Soft's documentation shows it can calculate on such amounts. The previous subscription-based plan is superseded and the client must confirm the new base.

## Can real funds be accepted within 30 days?

**No. A real-funds launch within 30 days is not supported by the evidence.** The gating items are outside engineering control:

- legal characterisation of the compensation plan, custody model and KYC thresholds;
- written acceptance of the MLM model by the wallet, MLM and verification vendors;
- a defined commission base and Yield Product terms;
- an independent security test of the money-handling paths.

**The closest credible milestone at day 30** is a complete end-to-end system on test networks (signup, Sponsor Tree, wallets, Deposits, withdrawals, Commission calculation and treasury payouts, KYC tiers, admin approvals and helpdesk), plus vendor contracts and the legal questions in progress. A controlled real-funds pilot is realistic roughly **10–14 weeks** from start if legal answers arrive within four to six weeks (consultant estimate).

## Indicative cost (external software and services)

| Item | Low | Base | High |
|---|--:|--:|--:|
| One-time (setup, security testing) | $32,000 | $65,000 | $100,000 |
| Monthly operating (pilot scale) | $2,900 | $8,200 | $17,800 |
| Indicative 12-month total | $67,000 | $163,000 | $314,000 |

Implementation effort is about **9 person-months** for the 30-day milestone and about **22 person-months** cumulatively to a controlled pilot. Cyclone's rates are contracted, so effort is shown in person-months only. Section 7 gives the breakdown and the evidence status of each figure.

## What can be decided now, and what needs more work

| Status | Items |
|---|---|
| **Decide now** | Modular architecture direction. Crypto-only Deposits in Release 1. Separate operator treasury with multi-person approval. Cyclone-owned ledger as the financial source of truth. Helpdesk before CRM. Web-first delivery. No Member funds exposed to QUANT in Release 1. No display-only "ROI" modules. |
| **Needs vendor demonstration or quotation** | MLM Soft and Exigo scripted demos against Helm test cases. Privy Enterprise pricing and written acceptance of the MLM model. Turnkey with Alchemy or ZeroDev technical spike as the Stripe-independent wallet alternative. Treasury vendor (Privy key quorum, Cobo or Fireblocks). KYC vendor pricing. Helpdesk trial. |
| **Needs technical due diligence** | MLM Soft security evidence (none published). Privy policy-engine configuration and fee-wrapper audit status. Vault selection criteria for a future Yield Product. QUANT engine, custody and controls (Phase 2). |
| **Needs legal confirmation** | Commission base. Custody classification of the hybrid wallet model. KYC thresholds and Travel Rule. Yield Product characterisation. Target jurisdictions and the operating entity. |
