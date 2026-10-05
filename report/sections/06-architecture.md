# Architecture options and fund flows

Three approaches were compared, as the brief requires. Every option shares one principle: **the Cyclone-owned platform ledger is the single financial source of truth.** The MLM software calculates Commissions, the wallet layer executes transfers, and the helpdesk and any CRM store references only.

## Option 1: Integrated white-label MLM platform

A single vendor (Epixel or Cloud MLM) provides the Member portal, compensation engine, internal e-wallet, crypto gateway and admin panel. Cyclone white-labels and customises it.

![Option 1: architecture and fund flow. The vendor's software holds balances and executes payouts; custody sits with an undocumented or custodial gateway.](figures/opt1-integrated){width=100%}

| Aspect | Assessment |
|---|---|
| Who controls assets | The vendor's gateway, or a custodial processor such as CoinPayments. Signing authority is not documented by any candidate. |
| Who provides the financial product | The vendor's "ROI/staking" module, which only calculates returns. **It must be disabled**, leaving no Yield Product. |
| Who processes withdrawals | The vendor's software, through its gateway. |
| Sources of truth | Identity, genealogy, balances, transactions and Commissions all sit inside the vendor database. |
| Buy, configure, build | Buy and configure the vendor package; customise the portal; build little. |
| Path to fiat | Through the vendor's gateway partners, which face the same MLM prohibitions as section 3.2. |
| Replaceability | Low. Balances, genealogy and payouts are tied to one vendor. Cloud MLM's source licence mitigates this but shifts security responsibility to Cyclone. |
| Complexity and timeline | Fastest visible portal (weeks), but the controls gap cannot be closed by configuration. |
| Material risks | Undocumented custody; unverified "smart contract" claims; expired or inconsistent ISO claims; vendor marketing that promises returns. |
| Conditions before real funds | Vendor proof of custody model, contract addresses and audits; current security attestation; replacement of the gateway with an AlphaWave-controlled wallet layer, at which point the option becomes Option 2. |

**Assessment: not recommended for real funds.** It is useful only as a fallback source of a Member portal or comp engine within Option 2.

## Option 2: Modular architecture (recommended)

AlphaWave buys a headless MLM core, a wallet layer, verification tooling and a helpdesk, and Cyclone builds the Member app, admin back office, ledger and integration layer.

![Option 2: high-level architecture. Cyclone builds the application layer and ledger; specialist components are purchased.](figures/opt2-architecture){width=100%}

![Option 2: fund flow. Member Deposits stay in Member-owned wallets; Commission payouts leave a separate operator treasury under multi-person approval; a later Yield Product keeps vault shares in the Member's wallet and pays the platform a share of yield only.](figures/opt2-fundflow){width=100%}

| Aspect | Assessment |
|---|---|
| Who controls assets | **Member Deposits:** the Member, through a Privy embedded wallet. If a narrowly scoped platform signer is added for vault deposits, the model is hybrid. **Treasury:** the operator, with quorum approval. |
| Who provides the financial product | Release 1: none with real funds. Later: a named lending or Staking protocol through the yield adapter (for example Privy Earn into Morpho or Aave vaults). |
| Who processes withdrawals | The Member signs withdrawals from their own wallet. Commission payouts are executed by the operator treasury after maker-checker approval. |
| Sources of truth | Identity status: verification provider (evidence) and platform identity service (decision record). Genealogy and Commission calculation: MLM core. Balances and transactions: platform ledger, reconciled to the chain. Commission payouts: ledger. |
| Buy | MLM core (MLM Soft or Exigo); wallet infrastructure (Privy); treasury tooling (Privy key quorum, Cobo or Fireblocks); KYC and screening (Sumsub or Didit, Chainalysis oracle); chain indexer or RPC provider; helpdesk. |
| Configure | Compensation plan; wallet policies; KYC tiers; helpdesk queues and SLAs. |
| Build | Member web app; admin back office; ledger and reconciliation; integration layer with idempotent event handling, webhook retries and feature gates; yield adapter interface. |
| Path to fiat | A provider-neutral funding interface allows an on-ramp to be added in Phase 2 once providers approve the model in writing. |
| Replaceability | High. Each component sits behind a Cyclone interface: the MLM engine receives events and returns Commission results; the wallet layer executes signed transfers; the yield adapter abstracts providers. QUANT can be added or removed without touching the core. Privy supports key export, giving Members an exit path. |
| Complexity and timeline | Highest integration effort of the three, but every piece is standard. About 9 person-months to the 30-day milestone and about 22 to a controlled pilot. |
| Material risks | MLM Soft security evidence; Privy's acceptance of the MLM model and Enterprise pricing; classification of the hybrid signer; gas costs for per-Member wallets; Commission clawbacks cannot be enforced on-chain once paid. |
| Conditions before real funds | See section 8.2. |

Key design rules for Option 2:

- **Separate the treasury from Member wallets.** Treasury signing keys never sit on the same server as any platform signer used with Member wallets.
- **Any platform signer is policy-restricted** to approved vault methods with amount caps and expiry, and can never transfer to a non-Member address. It is held in a hardware security module or key management service.
- **Deposits are detected twice**: by the wallet provider's webhooks and by an independent indexer, de-duplicated on chain, transaction hash and log index, with per-chain confirmation thresholds.
- **Commission calculation is separate from payout.** The MLM core emits payout instructions; the ledger records them; the treasury executes approved batches; clawbacks are applied before payout, which favours a hold period.
- **No Privy features that depend on Stripe or Bridge**: no fiat accounts, custodial wallets, fiat payouts or Stripe on-ramp.

## Option 3: QUANT integration in Phase 2

QUANT's trading engine is optional and is not part of the first release. If AlphaWave later offers algorithmic trading, the integration should keep the engine away from Members' core balances.

![Option 3: QUANT integration in Phase 2. Members opt in to a separate, capped trading account; QUANT receives only a trade-only key; Cyclone enforces limits and a kill switch.](figures/opt3-quant){width=100%}

| Aspect | Assessment |
|---|---|
| Who controls assets | The Member, through a separate trading account they opt into and fund with a capped amount. QUANT never holds withdrawal authority. |
| Who provides the financial product | QUANT's strategy, executed on Hyperliquid. This is a trading product with loss of principal possible, not Staking. |
| Who processes withdrawals | The Member, from their own Hyperliquid account back to their core wallet. |
| Sources of truth | Positions and P&L on Hyperliquid, mirrored in a separate sub-ledger. |
| Buy, configure, build | Integrate QUANT's engine; build the opt-in flow, risk monitor, limits and kill switch; configure Hyperliquid trade-only keys. |
| Path to fiat | As Option 2. |
| Replaceability | High if QUANT only sends orders through a trade-only key: another strategy provider can replace it. Hyperliquid documents agent (API) wallets that can place orders but not withdraw; this must be confirmed in due diligence (not verified in this research). |
| Complexity and timeline | Phase 2; depends on due diligence of QUANT's engine, security and operations. |
| Material risks | Strategy losses; venue manipulation (see HLP incidents); Hyperliquid's matching engine has no published audit; operator-selected trading products carry high regulatory sensitivity. |
| Conditions before real funds | Independent technical due diligence of QUANT; written risk limits and kill-switch tests; legal characterisation of the product; Member disclosures; QUANT never receives a signer over core Member wallets. |

**Release 1 restriction:** no Member funds are exposed to QUANT's engine, and no delegated signer is issued to QUANT.

## Wallet layer: Privy and a Stripe-independent alternative

Privy is the base case because it combines embedded wallets, smart accounts, a policy engine and a yield API in one product. Its ownership is the main concern: Stripe acquired Privy in June 2025, and Stripe and Bridge both prohibit MLM. Privy's own acceptable-use policy does not, and the design avoids every Privy feature that runs on Stripe or Bridge. There remains a risk that Privy's terms are later aligned with its parent's. Two independent alternatives were assessed.

| | Privy (base case) | Turnkey + Alchemy Smart Wallets (recommended alternative) | Dynamic (secondary alternative) |
|---|---|---|---|
| Ownership | Stripe (verified) | Both independent (Turnkey funding round May 2026, vendor claim) | Fireblocks, since October 2025 (verified) |
| Key model | Secure enclave plus 2-of-2 key split with the Member's login | Turnkey: keys in AWS Nitro enclaves; signing per policy-defined authenticators (vendor claim) | 2-of-2 MPC between Member device and vendor enclave (vendor claim) |
| Smart accounts | ERC-4337 and EIP-7702 (verified, docs) | Alchemy: EIP-7702 by default, Modular Account v2 (ERC-6900), audited by ChainLight and Quantstamp (vendor claim) | ERC-4337 (vendor claim); EIP-7702 not verified |
| Limits on platform actions | Off-chain policy engine in Privy's enclave (Enterprise) | Turnkey policies on amounts, recipients, contracts, chain, 7702 authorisations and Hyperliquid agent approval (verified, docs); **plus on-chain session keys** with spend, contract, function and expiry limits (verified, docs) | Delegated access share for the platform (vendor claim) |
| Built-in yield | Privy Earn: Morpho and Aave vaults with a fee on yield (verified) | None; integrate ERC-4626 vaults directly, or use Kiln DeFi vaults, which support integrator fees (verified) | None |
| Built-in on-ramps | Stripe (default), MoonPay, Meld | None core | Coinbase, Banxa (both prohibit MLM) |
| Published pricing | Free to $499/month; Enterprise quote needed (verified) | Turnkey $0.10 per signature, Pro $99/month at $0.05, Enterprise from $0.0015 (verified); Alchemy usage-based plus 8% gas fee, wallet pricing on quote | Free to $249/month, then $0.05 per user; bundled in Fireblocks Essentials at $999/month (verified) |
| SOC 2 | Type I/II (vendor claim) | Turnkey Type II (vendor claim); Alchemy not verified | Type II (vendor claim) |
| Main trade-off | Fastest integration; parent-company policy risk | More integration work; limits enforced on-chain, which is easier to evidence to counsel | Moves the parent-company question to Fireblocks, whose MLM stance is not verified |

Sources: [Privy pricing](https://www.privy.io/pricing), [Turnkey policies](https://docs.turnkey.com/concepts/policies/overview), [Turnkey pricing](https://www.turnkey.com/pricing), [Alchemy wallets](https://www.alchemy.com/docs/wallets), [Alchemy session keys](https://www.alchemy.com/docs/reference/wallet-apis-session-keys), [Kiln DeFi FAQ](https://docs.kiln.fi/v1/kiln-products/defi/kiln-defi-faq), [Fireblocks acquisition of Dynamic](https://www.fireblocks.com/blog/fireblocks-acquires-dynamic), [Dynamic pricing](https://www.dynamic.xyz/pricing).

Four further smart-account providers were assessed. None is owned by a payment company or an exchange, and none names MLM in its terms.

| Provider | What it is | Strengths for Helm | Limitations | Fit |
|---|---|---|---|---|
| **ZeroDev Kernel** (operated by Offchain Labs, the company behind Arbitrum) | Smart account (ERC-4337, ERC-7579, EIP-7702), on-chain permissions, bundler and paymaster | Platform session keys limited on-chain by contract, function, argument, expiry and rate; the private key never leaves the platform. HyperEVM listed. Earn API (beta) for Aave, Morpho and ERC-4626. Weighted multisig for a treasury. Kernel v3.x audit reports published. Plans $69 and $399/month; 8% gas premium | Offchain Labs may terminate if the relationship "would cause material harm to the reputation of Offchain" (verified). Earn is "an experimental product offered in beta" with no documented fee on yield (verified). No report found for Kernel v4 | **Co-equal alternative to Alchemy**, paired with Turnkey |
| **Openfort** | Full stack: embedded wallets, backend wallets, policy engine, paymaster, on-chain session keys | Closest to a Privy replacement on EVM networks; cheapest published entry pricing | No HyperEVM support; Hyperliquid signing is all-or-nothing; no SOC 2 evidence; its acceptable-use policy bans "Ponzi or pyramid schemes" and unlicensed "securities", the wording closest to excluding the model | Possible on EVM networks, after written clearance |
| **Para** (formerly Capsule) | Key signer (2-of-2 MPC with a share on the Member's device) | A device-held share gives the Member an independent factor | Not a smart account and no gas sponsorship; needs ZeroDev, Alchemy or Pimlico. Server-side paths are platform-controlled. HyperEVM not listed | Not preferred |
| **Pimlico** | Bundler and paymaster infrastructure only | Second paymaster for redundancy; HyperEVM listed | No EIP-7702 on HyperEVM; 10% sponsorship surcharge | Infrastructure complement |

Sources: [ZeroDev terms](https://zerodev.app/terms), [ZeroDev Kernel](https://github.com/zerodevapp/kernel), [ZeroDev session keys](https://docs.zerodev.app/smart-accounts/permissions/session-keys), [ZeroDev Earn](https://docs.zerodev.app/onramp/earn), [ZeroDev pricing](https://zerodev.app/pricing), [Openfort acceptable use](https://www.openfort.io/acceptable-use-policy), [Openfort HyperEVM](https://www.openfort.io/docs/recipes/hyperliquid/hyperevm), [Openfort pricing](https://www.openfort.io/pricing), [Para terms](https://www.getpara.com/terms-of-service), [Pimlico pricing](https://www.pimlico.io/pricing). Quotations were read through automated retrieval and should be re-checked before contracts are signed.

**Recommendation:**

- Keep Privy as the base case, conditional on its written acceptance of the business model.
- Carry **Turnkey as the signer with either Alchemy Smart Wallets or ZeroDev Kernel as the account layer** as the Stripe-independent alternative. ZeroDev is stronger on HyperEVM, DeFi tooling and published pricing; Alchemy's own terms have not yet been reviewed for comparable termination rights. Decide between them on the vendors' written answers.
- Run a **parallel technical spike of Turnkey with Alchemy Smart Wallets or ZeroDev Kernel in week 1**, covering wallet creation, a scoped session key limited to one vault and a cap, a Member-signed withdrawal and key export. Choose the wallet layer on the spike results and the vendors' written answers.
- Keep the wallet layer behind Cyclone's own interface so that a later switch does not touch the ledger, the MLM integration or the Member app. Member key export (offered by Privy and Turnkey, vendor claims) gives Members an exit path if a provider leaves.
- Coinbase Developer Platform (likely MLM prohibition), MetaMask Embedded Wallets (thinner policy documentation) and thirdweb (no SOC 2 evidence) were assessed and not recommended.

## Comparison

| Criterion | Option 1: Integrated | **Option 2: Modular** | Option 3: QUANT (Phase 2) |
|---|---|---|---|
| Custody clarity | Poor (undocumented) | **Good** (Member-owned wallets, separate treasury) | Good if trade-only keys are used |
| Genuine Yield Product path | None (display-only modules) | **Yes** (adapter to named protocols) | Trading returns, not yield |
| Controls evidence | Weak | **Mixed** (strong for Privy and verification vendors; MLM Soft unproven) | Unverified |
| Replaceability | Low | **High** | Medium |
| Effort | Lowest | **Highest** | Additional, later |
| Time to a credible real-funds pilot | Blocked by controls gaps | **10–14 weeks (estimate)** | After Option 2 is live |
| Recommendation | Not for real funds | **Primary** | Phase 2, conditional |

## Web-first delivery

**Web-first delivery is sufficient for the first release and native mobile should be deferred.** The PRD itself excludes a standalone mobile app from the first release. A responsive web app or progressive web app reaches Members on mobile browsers, and embedded wallets with passkey or email login work in the browser. Native apps add app-store review, which applies its own policies to crypto and MLM apps, plus a second release pipeline, with no gain for a controlled pilot. Mobile can follow once the product and legal position are stable.

## Recommendation: primary and fallback

- **Primary: Option 2 with MLM Soft, Privy and a quorum-approved treasury.** It is the only option that delivers clear custody boundaries, a genuine route to a Yield Product, replaceable components and a ledger AlphaWave controls.
- **Fallback: Option 2 with substitutions**, triggered by specific failures:
  - if Privy declines the business, its Enterprise terms are unacceptable, or Stripe ownership is judged too great a policy risk: the Stripe-independent wallet stack of Turnkey with Alchemy Smart Wallets or ZeroDev Kernel (section 6.4), with Fireblocks, Cobo or a Safe multisig for the treasury;
  - if MLM Soft fails its demonstration or security due diligence: Exigo (stronger controls evidence, slower) or Epixel (integrated, crypto features to be proven);
  - if counsel or the business prefers an omnibus model: Fireblocks, Cobo or a qualified custodian such as BitGo, accepting that the operator becomes custodian of Member assets with the licensing implications that follow.

The trade-off is effort for control: Option 2 needs more integration work than Option 1, in exchange for custody, data and vendor independence that Option 1 cannot provide.
