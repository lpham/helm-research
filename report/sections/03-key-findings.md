# Key findings and constraints

## "Staking" covers six different mechanisms

The client material uses "staking" for any product that pays a return on deposited crypto. The mechanisms behind that word differ in risk, custody and regulatory profile. This report uses **Yield Product** as the umbrella term and reserves **Staking** for native and liquid proof-of-stake staking.

| Category | Examples | Where the return comes from | Platform must control funds? | Liquidity | Main risks |
|---|---|---|---|---|---|
| Native Staking | ETH validators via Kiln, Figment or Coinbase; SOL or HYPE delegation | Protocol rewards for securing a network | No, if each Member's wallet signs | Chain unbonding periods; HYPE has a 1-day lockup and a 7-day queue | Token price, slashing, provider compromise |
| Liquid Staking | Lido stETH, Rocket Pool rETH, Jito JitoSOL | The same protocol rewards, via a tradable receipt token | No | Market sale (price may deviate) or protocol queue | Receipt-token depeg, smart contract |
| Lending | Aave; Morpho vaults curated by Steakhouse or Gauntlet | Interest paid by borrowers who post crypto collateral | No, if supplied from Member wallets | Usually instant, limited by available liquidity | Smart contract, oracle, bad debt, curator error |
| Trading vault | Hyperliquid HLP and user vaults | Trading profit and loss | No (depositor holds a vault share) | HLP 4-day lockup; user vaults 1 day | **Loss of principal**, market manipulation |
| Operator-managed program | Custodial "earn" programmes; a QUANT-run strategy | Whatever the operator does with pooled funds | **Yes** | Set by operator terms; can be suspended | Operator failure, commingling, highest regulatory sensitivity |
| Return calculator | MLM software "staking", "ROI" or "daily return" plans | **None.** A number credited in a database | Operator holds funds | Depends on new Deposits | Ponzi and pyramid dynamics; not a Yield Product |

Sources: [Hyperliquid staking](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking), [Hyperliquid protocol vaults](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/protocol-vaults), [Aave v3 overview](https://aave.com/docs/aave-v3/overview), [Cloud MLM investment plan](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/).

Key points for AlphaWave:

- **For a dollar-denominated product, over-collateralised stablecoin lending is the most credible mechanism.** Interest comes from borrowers, and the Member's position stays in the Member's wallet. Morpho states that Coinbase, Kraken and Deel embed Morpho vaults (vendor claim).
- **Hyperliquid HLP is a trading vault, not Staking.** Press reports document three loss events in 2025 of about $4 million, $12–13.5 million (unrealised) and $4.9 million (not verified against Hyperliquid disclosures). Hyperliquid's published audits cover only its legacy bridge, not the matching engine or HLP logic ([audits page](https://hyperliquid.gitbook.io/hyperliquid-docs/audits), verified).
- **Third-party providers carry real operational risk.** In September 2025 a compromised Kiln API was used to steal about $41 million of SOL from SwissBorg's operator-managed programme ([SwissBorg](https://swissborg.com/blog/swissborg-security-update-kiln-breach), verified). In March 2026 an Aave oracle misconfiguration wrongly liquidated 34 accounts; users were reimbursed from the DAO ([post-mortem](https://governance.aave.com/t/post-mortem-exchange-rate-misallignment-on-wsteth-core-and-prime-instances/24269), verified). In April 2026 the Kelp rsETH bridge exploit left Aave with a large WETH shortfall. A coverage package was proposed and contested; in May most of the unbacked rsETH was recovered through liquidations, with a coalition of protocols committed to cover the remainder ([incident thread](https://governance.aave.com/t/rseth-incident-2026-04-18/24481), [Aave Labs May update](https://governance.aave.com/t/al-development-update-may-2026/25013); final completion not verified).
- **Return-calculator modules are unacceptable as a Yield Product.** The SEC's Forsage action concerned this kind of design ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)).

## Payment providers prohibit MLM

The team's concern about Stripe is justified, and the issue is industry-wide rather than specific to Stripe.

- **Stripe** lists "Pyramid schemes" and "Multilevel marketing services offering commission or recruitment-based sales" as **prohibited** businesses, as well as "Cryptocurrency mining and staking" (page updated 22 September 2026). Its Crypto Onramp merchant terms (§5.4) bind the integrating platform to that list, and Stripe may suspend access without notice. Verified: [Stripe prohibited and restricted businesses](https://stripe.com/legal/restricted-businesses), [Crypto Onramp merchant terms](https://stripe.com/legal/crypto-onramp/merchant-terms).
- **Bridge** (a Stripe company that powers Privy's fiat and custodial features) lists "multi-level marketing" among prohibited activities in §2.1.1 of its [Developer Agreement](https://www.bridge.xyz/legal/developer-agreement). Verified.

| Provider | MLM wording found in terms | Evidence status |
|---|---|---|
| Stripe (incl. Crypto Onramp) | "Multilevel marketing services offering commission or recruitment-based sales"; "Pyramid schemes" | Verified |
| Bridge (Stripe) | "multi-level marketing" | Verified |
| Coinbase Developer Platform | "Multi-level Marketing: Pyramid schemes, network marketing, and referral marketing programs" | Verified (archived copy) |
| Transak | "Multi-level marketing" | Verified |
| Banxa | "Multi-level marketing: pyramid schemes, network marketing, and referral marketing programs" | Verified (December 2024 terms) |
| Ramp Network | "multi-level marketing" among restricted partner industries | Verified (2022 source; current terms to be confirmed) |
| MoonPay | Consumer terms bar "certain multi-level marketing programs"; partner terms not public | Partly verified |
| Mercuryo | "Ponzi or pyramid schemes" | Verified |
| Privy | No MLM wording; prohibits misrepresenting "the nature of the business" | Verified |
| Onramper (aggregator) | No MLM wording; underlying providers' terms still apply | Verified (absence) |

No provider reviewed publishes a positive statement that it accepts MLM businesses. Any acceptance would have to come as written approval after full disclosure of the model.

**Consequences:**

- **Release 1 accepts crypto Deposits only.** Members transfer crypto from a wallet or exchange they already use. This path cannot be switched off by an on-ramp partner. It does not remove KYC or AML obligations.
- **A fiat on-ramp is a gated Phase 2 item.** It requires counsel's characterisation of the compensation plan, full disclosure of the MLM model during provider review, and written approval from at least two providers or from an aggregator plus two underlying providers.
- **Direct fiat acceptance** (taking card or bank payments and converting) brings licensing, chargebacks, safeguarding and three-way reconciliation, and belongs to a later phase.

## Custody is determined by control, not by labels

A model is non-custodial only if no party other than the Member can move the Member's assets without the Member's approval of each action. Embedded wallets, multi-party computation (MPC) and smart accounts are mechanisms; who holds signing authority decides the classification.

| Model | Who can sign | Classification towards Members |
|---|---|---|
| Privy embedded wallet, Member-owned, no platform signer | Member, with Privy's enclave share | Non-custodial (dependent on the vendor) |
| Privy embedded wallet with a platform signer limited by policy | Member, or the platform within the policy | **Hybrid** |
| Platform signer with broad permissions | Effectively the platform | Custodial in substance |
| Key quorum requiring both Member and platform | Both | Non-custodial for outflows, with a platform veto |
| Operator MPC vault (Fireblocks, Cobo, BitGo) | Operator, co-signed by the vendor | **Custodial** (the operator is the custodian) |
| Licensed third-party custodian | Custodian on operator instruction | Custodial (third-party) |

Vendors that market MPC vaults as "self-custody" mean self-custody for the business, not for its customers. **Commission payouts require an operator treasury in every model, and that treasury is always custodial.** The design choice concerns where Member Deposits sit.

Regulators apply the same test. The FATF counts any business with "control" over virtual assets as a virtual asset service provider (VASP), including shared or multi-signature control ([FATF 2021 guidance](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html), paragraphs 72–76). FinCEN treats a provider as a money transmitter "regardless of the label the person applies to itself" ([FIN-2019-G001](https://www.fincen.gov/sites/default/files/2019-05/FinCEN%20Guidance%20CVC%20FINAL%20508.pdf), §4.2). The EU MiCA definition of custody covers controlling "the means of access" to crypto-assets ([MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), Art. 3(1)(17)). These are examples; which regime applies is for counsel.

## KYC: three scenarios

The client's assumption that crypto Deposits need no KYC cannot be confirmed from the software side. For VASPs, the FATF threshold for occasional transactions is USD/EUR 1,000 and the Travel Rule applies (FATF guidance, paragraph 146). The EU Transfer of Funds Regulation, for example, covers transfers to self-hosted wallets and has no minimum amount for crypto ([TFR](https://eur-lex.europa.eu/eli/reg/2023/1113/oj)).

| | A: KYC at onboarding | **B: Tiered KYC (base case)** | C: Crypto only, no KYC |
|---|---|---|---|
| Member experience | Document and liveness check before any Deposit | Light checks at signup; full check triggered by thresholds (Deposits, first withdrawal, Commission earned, Yield Product access) | Wallet signup only |
| Tooling | Identity verification, AML screening, wallet screening, case management | As A, plus a tier engine and threshold logic in the ledger | Wallet screening only |
| Fiat on-ramp | Provider still runs its own KYC | Same | Route effectively closed |
| Commission payouts | Payee identity known | Full KYC before payouts above a threshold | Payouts to anonymous wallets; sanctions, duplicate-account and clawback risk |
| Vendor and banking access | Easiest to explain | Explainable with counsel-approved thresholds | May block custody, banking and payment relationships |
| Reversibility | Can be relaxed later | Thresholds can be tuned | Hard to tighten after launch |

**Whatever the scenario, every Deposit source address, withdrawal address and payout address should be screened against sanctions lists from day one.** The free [Chainalysis sanctions oracle](https://go.chainalysis.com/chainalysis-oracle-docs.html) is the minimum. Build the identity gates into Release 1 even before thresholds are set; adding KYC after Members have deposited is harder than switching on a tier that already exists.

## Commission base: what the software actually supports

The compensation plan overview pays Commissions on subscription sales. That model is superseded, and the new base has not been defined. Rather than propose a base from first principles, the research examined what real MLM software supports.

| Base | Evidence from vendors | Status | Observation |
|---|---|---|---|
| Product orders | Exigo, ByDesign, DirectScale organise around orders and products | Verified (docs) | Default for enterprise platforms; a non-product base needs synthetic orders |
| Deposit ("investment") amount | Hybrid MLM: "Commissions are earned when a recruit makes an initial investment"; Cloud MLM: "daily percentage returns based on individual member investments" | Verified (as described) | **The most common base in crypto-MLM software.** Rewards funded by new Deposits are the structural pattern behind Ponzi and pyramid concerns |
| Calculated "ROI" | Hybrid MLM: "whenever a recruit's investment generates ROI" | Verified (as described) | The "ROI" is itself an operator-set number, not protocol yield |
| Entry or package fee | ARM MLM "Forsage clone": "Pay 0.5 ETH to join" | Verified (as described) | The pattern the SEC alleged in the Forsage case |
| Trading activity | Epixel: "new trader registration or ... the first trade" | Vendor claim | Relevant only if trading is integrated later |
| Arbitrary platform amount, such as fee revenue | MLM Soft: plan properties flagged as volume or bonus can be "set by API request" | Verified (vendor docs); needs a demo | The only route found to a **platform fee revenue** base |

Sources: [Hybrid MLM](https://www.hybridmlm.io/investment-mlm-plan/), [Cloud MLM](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/), [ARM MLM](https://www.armmlm.com/tron-smart-contract-mlm-software/), [Epixel](https://www.epixelmlmsoftware.com/cryptocurrency-trading-mlm-software), [MLM Soft plan properties](https://help.mlmsoft.net/hc/en-us/articles/39249705385235-Plan-properties-configuration).

**A non-custodial source of fee revenue exists.** Privy Earn deposits a Member's funds into Morpho or Aave vaults and lets the platform take up to 50% (Morpho) or up to 100% (Aave) of the **yield only**; Members keep the principal and can withdraw at any time ([Privy revenue sharing](https://docs.privy.io/wallets/actions/earn/revenue-sharing), verified). A plan in which Commissions are a capped share of realised platform fee revenue, held for a period before payout, is structurally the lowest-risk option found. It is still a matter for legal counsel, because both choosing the yield source and paying Commissions linked to it raise questions in several jurisdictions (see the SEC's action concerning Celsius's "Earn Interest Program", [SEC 2023-133](https://www.sec.gov/newsroom/press-releases/2023-133)).

The client must confirm the base before the compensation plan can be configured or tested (section 11).
