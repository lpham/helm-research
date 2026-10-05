# 04 — Yield Product options

- **Workstream:** Yield Product (Project Helm, client AlphaWave)
- **Author:** Cyclone research
- **Research date:** 2026-10-06
- **Status:** Research note, input to the client report (sections 3, 6, 9 of `research-brief.md`). Not legal advice; jurisdiction-neutral.

**Evidence labels used throughout**

- **Verified:** confirmed in a primary source (protocol docs, audit repository, governance forum, official vendor docs, or regulator publication) linked at the claim.
- **Vendor claim:** stated by the vendor or protocol about itself (marketing page, press release, self-reported certification), not independently checked.
- **Not verified:** secondary or press source only, or could not be confirmed in a primary source on the research date.

No APY figures are given as facts. Rates on every option below are variable and change daily. The report should describe *where yield comes from*, not quote a number.

---

## 1. Summary

1. **"Staking" in the client material covers at least six different mechanisms.** They have different risk, custody and regulatory profiles. Following the brief (section 3) and `GLOSSARY.md`, this note uses **Yield Product** as the umbrella term and keeps **Staking** for native and liquid proof-of-stake staking only. Stablecoin lending (Aave, Morpho), Hyperliquid HLP and curated vaults are *not* Staking.
2. **For a stablecoin-denominated Yield Product, over-collateralised lending is the most credible underlying mechanism.** Aave and Morpho vaults curated by risk managers such as Steakhouse or Gauntlet are the main examples. The yield comes from interest paid by borrowers who post crypto collateral. Large regulated platforms already integrate these mechanisms: Coinbase via Morpho; Kraken and Deel via Privy and Morpho. (Morpho and Privy materials, Verified in part; see section 4.)
3. **Privy, the base-case wallet, ships a native "Earn" API.** It can deposit into Morpho, Aave and Veda vaults from embedded wallets. It includes an on-chain fee wrapper that pays the platform a share of the yield: up to 50% for Morpho and up to 100% for Aave (**Verified**, [Privy docs](https://docs.privy.io/wallets/actions/earn/revenue-sharing)). This is the shortest path to "plug yield in later" without changing the wallet architecture.
4. **Hyperliquid HLP is a trading vault, not Staking.** It earns from market making, liquidations and a share of fees. Members can lose money in it: three loss events of about USD 4–13M each are documented for 2025. Native HYPE Staking is a separate product, with a 1-day delegation lockup and a 7-day unstaking queue (**Verified**, [Hyperliquid docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking)). Hyperliquid trading integration provides neither by default.
5. **Native and liquid Staking are mature but carry volatile-asset exposure.** A Member holding staked ETH or SOL carries the token's price risk; the product is not a dollar yield. Institutional staking providers (Kiln, Figment, Coinbase CDP, Chorus One, Blockdaemon) provide APIs that build unsigned transactions for the platform's own signer. That works with Fireblocks-style MPC and, in principle, with embedded wallets.
6. **Third-party providers are a real operational risk.** In September 2025 a compromised Kiln API was used to steal about USD 41M of SOL from SwissBorg's operator-managed Earn program (**Verified**, [SwissBorg](https://swissborg.com/blog/swissborg-security-update-kiln-breach)). In April 2026 the Kelp rsETH bridge exploit left Aave with a WETH shortfall that needed DAO treasury funds, donations and a credit facility to cover (**Verified**, [Aave governance](https://governance.aave.com/t/arfc-rseth-incident-funding-update/24740)). "Blue-chip" does not mean risk-free.
7. **The platform can earn revenue from yield without taking custody.** It can take an on-chain fee-on-yield through ERC-4626 fee wrappers (Privy, Kiln DeFi, Aave Earn vaults, Morpho Vault V2) or through reward-split contracts (Coinbase Staking onchain billing). Whether paying MLM **Commissions** out of, or based on, Yield Product Deposits is acceptable is a high-sensitivity legal question for counsel (section 8).
8. **Red flag:** MLM-software "staking/ROI plan" modules that credit a fixed daily percentage, with no underlying protocol, are display-only calculators. Regulators have described this pattern as the hallmark of Ponzi and pyramid schemes (HyperFund, Forsage). They are unacceptable as a Yield Product (section 9).
9. **Recommendation for Release 1:** no real-funds yield. Build a **yield-adapter seam** in the ledger: a position sub-ledger, reconciliation against on-chain share balances, and a fee-accrual model. Prototype it against a Privy Earn sandbox or testnet vault, or display-only data from a real vault, clearly labelled. Choose a provider in a later phase after legal confirmation (section 7).

---

## 2. Taxonomy

The brief requires six categories to be kept apart. The table maps each to examples and its main properties. "Custody needed" asks whether the platform must hold or control Member assets in order to use the option.

| Category | Examples | Yield source | Custody needed by platform? | Liquidity / withdrawal | Main risks |
|---|---|---|---|---|---|
| **Native staking** | ETH validators via Coinbase CDP Dedicated ETH, Kiln, Figment; SOL delegation; HYPE delegation | Protocol rewards (issuance + fees/MEV) for securing a PoS chain | No. The provider builds a transaction; the asset owner's wallet signs. A platform running an omnibus wallet does hold custody. | Chain-specific exit/unbonding: ETH exit queue; SOL about 1 epoch; HYPE 1-day lockup + 7-day queue | Token price; slashing; validator downtime; provider API compromise (Kiln 2025) |
| **Liquid staking** | Lido stETH/wstETH, Rocket Pool rETH, Jito JitoSOL, Kinetiq kHYPE | Same protocol rewards, minus protocol fee; holder gets a tradable receipt token | No (token sits in the Member's wallet) | Instant via secondary market (price may deviate); protocol withdrawal queue (Lido: days; longer in stress) | Depeg of receipt token; smart contract; slashing; oracle use of the LST in lending markets |
| **Lending (over-collateralised)** | Aave v3/v4, Morpho vaults (Steakhouse, Gauntlet, Sentora), Spark, Compound | Interest paid by borrowers who post crypto collateral, net of reserve factor or curator fee | No when supplied from Member wallets; yes if pooled from an omnibus wallet | Usually instant, but **only up to available liquidity**; high utilisation can delay exits | Smart contract; oracle; bad debt from collateral failure (rsETH 2026); curator misallocation (Stream/xUSD 2025); liquidity crunch |
| **Trading vault** | Hyperliquid HLP; Hyperliquid user vaults; Veda strategy vaults (multi-protocol) | Trading P&L: market making, liquidations, funding, strategy returns | No (on Hyperliquid each depositor holds a vault share) | HLP 4-day lockup; user vaults 1 day; slippage on withdrawal | **Principal loss**; market manipulation (JELLY, POPCAT); counterparty/strategy; venue centralisation |
| **Operator-managed yield program** | SwissBorg Earn, Kraken/Coinbase custodial products, CeFi lenders (Celsius history), a QUANT-run strategy | Whatever the operator does with pooled Member funds (staking, lending, trading, rehypothecation) | **Yes.** The operator pools and controls assets. | Set by operator terms; can be suspended | Operator insolvency or fraud; commingling; third-party provider compromise; highest regulatory sensitivity |
| **Return calculator / display module** | MLM software "staking", "ROI" or "daily return" plans | **None.** The return is a number credited in a database. | Funds are held by operator; no underlying product | Depends on new Deposits | Ponzi/pyramid dynamics; misrepresentation; not a Yield Product |

---

## 3. Lending

### 3.1 Aave (v3 and v4)

**What it is.** Aave is a pooled, over-collateralised lending protocol. Suppliers deposit assets and receive aTokens. Borrowers post collateral and pay variable interest.

- **Yield source.** "Supplier yields are funded by borrower interest net of the reserve factor." Rates rise with pool utilisation. Liquidations rely on oracle prices and the Health Factor. **Verified:** [Aave v3 overview](https://aave.com/docs/aave-v3/overview).
- **v4 status.** Aave V4 launched on Ethereum mainnet on **30 March 2026** with a Hub-and-Spoke design. A Liquidity Hub holds assets; Spokes connect to it with their own collateral types, risk parameters and liquidation rules. There are three launch Hubs (Core, Prime, Plus), all with deliberately conservative supply and borrow caps. **Verified:** [Aave blog, "Aave V4 is Live on Ethereum"](https://aave.com/blog/aave-v4-live-ethereum).
  - Later expansion to Avalanche: **Vendor claim** ([Aave blog](https://aave.com/blog/aave-v4-live-avalanche)).
  - The launch blog does not state whether or when V3 will be wound down; V3 markets remain the main venue. Integration partners such as Privy and Kiln still target V3 (see 3.4, section 6).
- **V4 audits.** Year-long programme (March 2025 to February 2026). Manual audits by ChainSecurity, Trail of Bits and Blackthorn; formal verification by Certora; independent researchers; a Sherlock public contest. No high-severity findings were reported. **Vendor claim** (Aave's own summary): [Aave "Security by Design"](https://aave.com/blog/aave-v4-security-by-design), [V4 launch blog](https://aave.com/blog/aave-v4-live-ethereum).
- **V3 audits.** Reports are published in the DAO repository. Examples:
  - v3.3: StErMi 2024-10-22; Certora 2024-11-07
  - v3.4: Enigma Dark 2025-05-13; Certora and StErMi 2025-06-11
  - v3.5: Certora 2025-07-14; ABDK and StErMi 2025-07-17

  **Verified:** [aave-dao/aave-v3-origin/audits](https://github.com/aave-dao/aave-v3-origin/tree/main/audits). Bug bounty: [Immunefi](https://immunefi.com/bug-bounty/aave/information/).
- **Backstop.** "Umbrella" replaced the legacy Safety Module in June 2025. Stakers of aTokens or GHO can be slashed automatically to cover bad debt in specific assets. **Not verified** in primary docs for the launch date; see [Aave help: Umbrella](https://aave.org/help/umbrella/umbrella) and the [Aave X announcement](https://x.com/aave/status/1930630754255479080).
- **Aave Horizon (permissioned market).** Launched **26 August 2025** on Aave v3.3.
  - Only qualified institutions may supply tokenised real-world-asset (RWA) collateral, such as Superstate USTB/USCC and Centrifuge JRTSY/JAAA.
  - *Anyone* may supply stablecoins (USDC, RLUSD, GHO) for those institutions to borrow.
  - So stablecoin suppliers earn from institutional borrowers who post tokenised Treasuries or credit funds as collateral.

  **Verified:** [Aave blog, Horizon launch](https://aave.com/blog/horizon-launch). Later deposit figures (about USD 600M in January 2026, then lower) are **Not verified** (press).
- **Embedding for fintechs.** Aave Labs offers "Aave Earn / Simple Earn" ERC-4626 vaults on top of v3. A vault manager can set a performance fee on yield only, not principal. **"When a performance fee is set, 50% of that fee is automatically allocated to Aave Labs."** **Verified:** [Aave Earn vaults docs](https://aave.com/docs/aave-v3/vaults/overview). AaveKit SDKs and API: [Aave docs](https://aave.com/docs/aave-v3/smart-contracts/vaults).

**Incidents relevant to risk disclosure (2026).**

- **10 March 2026, CAPO oracle misconfiguration.** The wstETH/stETH exchange-rate cap was set about 2.85% below market on the Ethereum Core and Prime instances. About 10,938 wstETH of E-Mode positions in 34 accounts were wrongly liquidated. There was no protocol bad debt, and users were reimbursed (about 512 ETH; net DAO cost about 358 ETH). **Verified:** [post-mortem](https://governance.aave.com/t/post-mortem-exchange-rate-misallignment-on-wsteth-core-and-prime-instances/24269), [reimbursement AIP](https://governance.aave.com/t/direct-to-aip-wsteth-capo-oracle-incident-user-reimbursement/24275). *Lesson:* oracle and configuration risk hits borrowers directly. Stablecoin suppliers were not the affected party here.
- **18 April 2026, Kelp rsETH bridge exploit.** About 116,500 rsETH (about USD 292M) was stolen through Kelp's LayerZero bridge setup. The attacker posted stolen rsETH on Aave V3 and borrowed WETH and wstETH. The Guardian froze rsETH and wrsETH across V3 deployments and disabled new supply and borrow on V4, and froze WETH on several networks as a precaution.
  - Shortfall: about 163,183 ETH initially, reduced to a residual of about 75,081 ETH after recoveries.
  - Coverage: about 14,570 ETH in donations, up to 30,000 ETH from a Mantle credit facility, and 25,000 ETH from the Aave DAO treasury (proposal dated 24 April 2026).

  **Verified:** [incident thread](https://governance.aave.com/t/rseth-incident-2026-04-18/24481), [funding ARFC](https://governance.aave.com/t/arfc-rseth-incident-funding-update/24740). Exploit mechanics and attribution: **Not verified** (press: [The Block](https://www.theblock.co/news/defi/2026-04-20-kelp-dao-shifts-blame-layerzero-398204), [CoinDesk](https://www.coindesk.com/tech/2026/04/19/2026-s-biggest-crypto-exploit-kelp-dao-hit-for-usd292-million-with-wrapped-ether-stranded-across-20-chains)).

  *Lesson:* in a pooled market, a collateral asset failing elsewhere can create bad debt that suppliers of *other* assets are exposed to. Whether suppliers lose principal then depends on governance and backstops. A stablecoin Yield Product needs exposure limits and an incident runbook (freeze new Deposits, communicate to Members, handle withdrawal queues).

### 3.2 Morpho (Markets, Vaults V1 / V2)

**What it is.** Morpho Markets (formerly Morpho Blue) are immutable, isolated lending markets, each with one collateral asset, one loan asset, an oracle and a liquidation LTV. Morpho Vaults are ERC-4626 vaults run by third-party **curators**, who decide which markets receive Deposits and how much.

- **Yield source.** Interest from borrowers in the markets the vault allocates to, minus any curator performance or management fee.
- **Vault V2 risk model.** Launched in late September 2025 (Keyrock USDC vault first; dates from [Morpho blog](https://morpho.org/blog/morpho-vaults-v2-a-new-standard-for-asset-curation/), **Vendor claim**). Verified features ([Morpho docs, Vault V2](https://docs.morpho.org/learn/concepts/vault-v2/)):
  - Roles: Owner, Curator (adapters, caps, fees), Allocator (executes allocations), Sentinel (can de-risk and revoke).
  - Absolute and relative caps on risk identifiers.
  - Configurable timelocks (0 to 3 weeks) on potentially harmful curator actions.
  - Fees: performance fee up to 50% of yield; management fee up to 5% of assets.
  - **In-kind redemption via `forceDeallocate`.** A depositor can exit into the underlying positions even when the vault is illiquid, with a penalty of up to 2%.
  - Optional "gates" (access control on deposits, withdrawals and transfers), useful for allow-listed Member-only vaults.
- **Audits.**
  - Morpho Blue: OpenZeppelin and Spearbit (October 2023), Cantina contest (November–December 2023).
  - MetaMorpho (Vaults V1): OpenZeppelin and Spearbit (November 2023).
  - Vault V2: Spearbit (2025-05-19), Zellic (2025-07-15), Cantina contest (2025-07-15), ChainSecurity and Blackthorn (2025-09-15), Spearbit (2025-11-08), Certora (2025-12-15).

  **Verified:** [Morpho audits page](https://docs.morpho.org/get-started/resources/audits/).
- **Curators.** Steakhouse Financial, Gauntlet, Sentora, MEV Capital, Re7 and others. Curators are not custodians, but they decide what collateral the vault is exposed to. Curator fees vary by vault and can change; read them from the vault page or on-chain at integration time.
- **Fintech adoption.**
  - Coinbase offers USDC lending through Morpho vaults curated by Steakhouse on Base, using Coinbase Smart Wallet, passkeys and Magic Spend. Morpho reports a "Core" vault (blue-chip collateral) and a "High Yield" vault (launched June 2026, including Ethena-linked collateral). **Vendor claim:** [Morpho, Coinbase story](https://morpho.org/stories/coinbase/); corroborated by [CoinDesk, 18 September 2025](https://www.coindesk.com/business/2025/09/18/coinbase-adds-usdc-lending-with-morpho-and-steakhouse-financial).
  - Any fee Coinbase takes on yield: **Not verified**.
  - Kraken and Deel embed Morpho through Privy. Morpho says more than USD 500M of Deposits have been routed this way, mostly from Kraken. **Vendor claim:** [Morpho, Privy story](https://morpho.org/stories/privy-and-morpho-power-embedded-finance-for-fintechs).
- **Incident: Stream Finance / xUSD (November 2025).** Stream disclosed about USD 93M of losses and froze withdrawals. Its xUSD token depegged, and Elixir's deUSD, heavily lent to Stream, collapsed.
  - Several curators (notably MEV Capital and Re7) had exposure through permissionless Morpho and Euler markets.
  - Morpho's co-founder reported that only one of about 320 vaults had direct xUSD bad debt (about USD 0.7M), and that wider stress came from simultaneous withdrawals hitting isolated-market liquidity.
  - **Not verified** (press / secondary): [Protos](https://protos.com/stream-finance-meltdown-winners-and-losers-in-defi-risk-curator-reckoning/), [CryptoRank summary](https://cryptorank.io/news/feed/dd09a-morpho-co-founder-illiquidity-in-defi-vault), [Chorus One curator report](https://chorus.one/reports-research/defi-curators-in-2025-navigating-chaos-building-resilience).
  - *Lesson:* with Morpho, **curator selection is the main risk decision.** The platform should allow only vaults with conservative collateral (e.g., "Prime"-type vaults limited to BTC, ETH and major stablecoins), timelocks and a Sentinel, and monitor allocations continuously.

### 3.3 Spark / Sky, Compound (brief)

- **Sky Savings Rate (sUSDS) and Spark.** These are protocol-set savings rates on Sky's stablecoin. Their yield comes from the Sky protocol's collateral and RWA income. Privy lists "Sky Savings" as a recipe. **Verified (listing only):** [Privy yield overview](https://docs.privy.io/recipes/yield/overview). Mechanism detail not researched in depth: **Not verified**.
- **Compound v3.** Single-borrowable-asset markets. Kiln DeFi has test vaults on Compound v3 (Arbitrum). **Verified (listing):** [Kiln integration guide](https://docs.api.kiln.fi/docs/kiln-defi-integrate).

### 3.4 Lending: assessment for Helm

| Criterion | Aave v3 (direct or Earn vault) | Morpho curated vault |
|---|---|---|
| Yield source | Borrower interest, pooled | Borrower interest, isolated markets chosen by curator |
| Liquidity | Instant up to available liquidity | Instant up to vault liquidity; in-kind exit (V2) |
| Main risks | Pooled contagion (rsETH 2026), oracle config | Curator misallocation (xUSD 2025), market illiquidity |
| Audits | Extensive, published (above) | Extensive, published (above) |
| Custody needed | No (Member wallet holds aTokens or vault shares) | No (Member wallet holds vault shares) |
| Platform fee mechanism | Aave Earn vault performance fee (50% shared with Aave Labs); Privy wrapper up to 100% | Vault V2 performance fee; Privy wrapper up to 50% |
| Fit | Good default | Good, if limited to conservative curated vaults |

---

## 4. Hyperliquid

**Framing.** Hyperliquid is an L1 running a perpetuals and spot order book (HyperCore) plus an EVM (HyperEVM, live since 18 February 2025, **Not verified**: secondary sources). It offers three things that are often mixed up:

- a **trading venue**, which QUANT may connect to; QUANT's engine is out of scope here (Phase 2);
- **vaults**, including HLP, which are trading vaults;
- **native HYPE Staking**.

Integrating with Hyperliquid for trading **does not provide** Staking. HLP is **not** Staking.

### 4.1 HLP (Hyperliquidity Provider)

- **What it is.** A community-owned protocol vault. It "employs multiple market-making strategies, performs liquidations, and supplies USDC to the Earn program", and earns "a portion of trading fees". **Verified:** [Hyperliquid docs, Protocol vaults](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/protocol-vaults).
- **Yield source.** Trading P&L (market-making spread, liquidation profits, fee share, interest on USDC supplied to Earn). It is not protocol issuance, and **principal is at risk.**
- **Lockup.** "The deposit lock-up period is 4 days. This means you can withdraw 4 days after your most recent deposit." So each new Deposit resets the clock. **Verified:** [Protocol vaults](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/protocol-vaults).
- **Audits.** Hyperliquid's audits page lists only Zellic reviews of the legacy Ethereum bridge contract and Circle's own review of its HyperEVM contracts. **No public audit of the HyperCore matching engine, HLP logic or consensus is listed.** **Verified:** [Hyperliquid audits](https://hyperliquid.gitbook.io/hyperliquid-docs/audits).
- **Documented drawdown and loss events.** All **Not verified** (press); each was widely reported.

| Date | Event | HLP impact | Source |
|---|---|---|---|
| 12 March 2025 | Whale with about 50x ETH long withdrew margin to trigger liquidation; HLP absorbed position | About USD 4M loss; Hyperliquid then changed leverage/margin rules | [The Defiant](https://thedefiant.io/news/defi/whale-s-nine-figure-eth-liquidation-costs-hyperliquid-usd4-million) |
| 26 March 2025 | JELLYJELLY: trader shorted and then pumped spot; liquidation passed the short to HLP | Unrealised loss peaked at about USD 12–13.5M. Validators voted to delist; market settled at a set price; Hyper Foundation said it would make non-flagged users whole | [Yahoo/CoinDesk syndication](https://sg.finance.yahoo.com/news/hyperliquid-delists-jelly-vault-squeezed-160020190.html), [Incrypted](https://incrypted.com/en/hyperliquid-loop-jellyjelly-manipulations-12-million-losses-and-questions-of-decentralization/) |
| 12–13 November 2025 | POPCAT: about USD 3M spread over 19 wallets built a USD 20–30M long and pulled the supporting bid | About USD 4.9M bad debt absorbed by HLP; deposits and withdrawals paused for "maintenance" | [CoinDesk](https://www.coindesk.com/markets/2025/11/13/peak-degen-warfare-alleged-popcat-manipulation-hits-hyperliquid-with-usd4-9m-loss), [The Block](https://www.theblock.co/news/defi/2025-11-12-hyperliquid-pauses-deposits-withdrawals-popcat-trading-scheme-speculation-378606) |

- **Governance note.** The JELLY outcome was decided by validators intervening to delist and settle the market. That protects HLP, but it shows discretionary intervention on a venue described as decentralised (brief section 3: "A 'DeFi' label does not establish decentralization").

### 4.2 User vaults

- Any trader ("leader") can run a vault. Depositors share P&L, the leader takes a **10% profit share**, and the depositor lockup is **1 day**. "There may be some slippage as you withdraw and open positions are closed." **Verified:** [Hyperliquid docs, For vault depositors (legacy)](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/for-vault-depositors-legacy).
- These are discretionary trading strategies. Offering a selected user vault to Members would be an operator-selected trading product, with high sensitivity and principal risk.
- HyperEVM vaults can follow ERC-4626 while trading on HyperCore through CoreWriter and precompiles. **Verified (high-level):** [Hyperliquid docs, Vaults](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults).

### 4.3 Native HYPE Staking

All facts in this subsection are **Verified:** [Hyperliquid docs, Staking](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking).

- Delegators stake HYPE to validators. A validator needs 10k HYPE self-delegation to be active.
- **Delegation lockup is 1 day.** Moving from staking back to spot goes through a **7-day unstaking queue**, with at most five pending withdrawals per address.
- Rewards come from "the future emissions reserve". The rate scales inversely with the square root of total staked HYPE. Rewards accrue each minute, are paid daily and auto-compound.
- "There is currently no automatic slashing implemented." Jailing exists for poor performance.
- Validator commission cannot be raised unless the new rate is at most 1%.
- **Assessment.** This is genuine native Staking, but the Member is exposed to HYPE price, a single-ecosystem token. It is not a dollar yield. Institutional providers such as Chorus One list Hyperliquid among supported networks (**Vendor claim**, [Chorus One SDK](https://sdk.chorus.one/)).
- **Liquid staking variants.** Kinetiq kHYPE is reported as audited by Pashov, Zenith, Code4rena and Spearbit in 2025. **Not verified:** secondary source only ([QuillAudits blog](https://www.quillaudits.com/blog/staking/kinetiq-liquid-staking-on-hyperliquid)).

### 4.4 HyperCore portfolio-margin "Earn"

- Portfolio-margin accounts earn interest on idle borrowable assets. Stablecoin borrow rate = 0.05 + 4.75 × max(0, utilisation − 0.8) APY. Caps include a 1B USDC global supply cap and a 250M per-user supply cap. **Verified (as documented; parameters may change):** [Hyperliquid docs, Portfolio margin](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/portfolio-margin).
- This is a lending-type yield inside a trading venue. It is untested as a retail Yield Product venue and depends on unaudited core components.

---

## 5. Liquid staking

| Protocol | Yield source | Fee | Withdrawal / liquidity | Risks | Audits |
|---|---|---|---|---|---|
| **Lido stETH / wstETH** (Ethereum) | ETH consensus + execution rewards | 10% of staking rewards, split between node operators and the DAO treasury (**Verified**, [Lido integration guide](https://docs.lido.fi/guides/lido-tokens-integration-guide); module splits: [Lido protocol fee](https://lido.fi/how-lido-works/protocol-fee)) | Secondary market (instant; price can deviate) or protocol queue: request, finalisation by daily oracle report, claim. FIFO; time depends on queue size, validator exit rate and buffer (**Verified**, [Lido withdrawals](https://lido.fi/how-lido-works/withdrawals)). "Bunker mode" slows finalisation in mass-slashing scenarios ([Accounting oracle spec](https://docs.lido.fi/guides/oracle-spec/accounting-oracle/)). Requests are 100 wei to 1,000 stETH each and cannot be cancelled (**Verified**, integration guide). | Smart contract; slashing; stETH discount to ETH; integrator pitfalls (stETH rebases, 1–2 wei rounding; prefer wstETH for accounting) | Long, continuous record; recent entries include Certora, MixBytes, Composable Security and Cyfrin in March–April 2026, and Lido V3 / stVaults audits by Certora, Consensys Diligence and MixBytes (**Verified**, [Lido audits](https://docs.lido.fi/security/audits/)) |
| **Rocket Pool rETH** (Ethereum) | ETH rewards via decentralised node operators | Node operator commission. ETH-only minipools 5%, boostable (**Not verified**: Rocket Pool Medium, [Saturn upgrades](https://medium.com/rocket-pool/rocket-pools-saturn-upgrades-8f1eee0b55ce)) | Burn rETH against the deposit pool / buffer when liquid, otherwise secondary market. A protocol withdrawal queue using EIP-7002 triggerable exits is proposed in **RPIP-71, status Draft** (**Verified**, [RPIP-71](https://rpips.rocketpool.net/RPIPs/RPIP-71)) | Thinner liquidity than stETH; smart contract; slashing | Not researched in this pass (**Not verified**) |
| **Jito JitoSOL** (Solana) | SOL staking rewards + MEV tips distributed to stakers | About 4% of rewards as management fee + 0.1% on direct unstake (**Vendor claim**, from Jito docs search excerpt; [Jito general FAQs](https://www.jito.network/docs/jitosol/faqs/general-faqs/) returned HTTP 403 to automated fetch) | Instant via DEX, or delayed unstake of up to about 1 epoch (about 2 days) (**Vendor claim**, same source; [Unstaking overview](https://www.jito.network/docs/jitosol/get-started/unstaking-jitosol-flow/unstaking-overview/)) | MEV dependency; smart contract (SPL stake-pool based); SOL price | Not researched in this pass (**Not verified**) |

**Assessment.** Liquid staking is the cleanest non-custodial "Staking" option, and it fits embedded wallets because the receipt token sits in the Member's wallet. But the Member's balance moves with ETH or SOL prices. If AlphaWave's Members expect a stable-value Yield Product, liquid staking is a secondary option. A "Staking" label on a stablecoin lending product would misdescribe it.

---

## 6. Native staking and staking-as-a-service (institutional)

The common integration model across providers: the provider runs validators and exposes an API that **builds unsigned staking transactions**. The asset owner's signer (Fireblocks, an MPC wallet, or an embedded wallet) signs them, and the API broadcasts. The provider does not take custody of principal. That changes if the platform runs an omnibus wallet and stakes on behalf of Members: then the *platform* is the custodian and the product becomes an operator-managed program.

| Provider | Integration model | Custody compatibility | Fees | SOC 2 / ISO | Notes |
|---|---|---|---|---|---|
| **Kiln** | Kiln Connect API/SDK, no-code Widget, Kiln DeFi ERC-4626 vaults, white-label "Onchain" ETH staking; 30+ PoS networks (**Vendor claim**, [kiln.fi](https://www.kiln.fi/)) | Lists Fireblocks, Ledger Enterprise, BitGo and others as integrations (**Vendor claim**) | Kiln DeFi: integrator sets deposit and/or rewards fees, minted as vault shares (**Verified**, [Kiln DeFi FAQ](https://docs.kiln.fi/v1/kiln-products/defi/kiln-defi-faq)); Kiln's own commission is visible as GRR minus NRR in the API (**Verified**, [integration guide](https://docs.api.kiln.fi/docs/kiln-defi-integrate)); commercial terms by quotation | SOC 2 Type II (**Vendor claim**, [kiln.fi](https://www.kiln.fi/)) | **September 2025 incident:** a compromised engineer GitHub token let attackers inject a payload into the Kiln Connect API, which reassigned SwissBorg SOL stake accounts; about USD 41M stolen. Kiln emergency-exited its ETH validators and rotated keys (**Verified**, [SwissBorg](https://swissborg.com/blog/swissborg-security-update-kiln-breach)). Kiln DeFi audits: Quantstamp (February 2024), Spearbit (March 2024); USD 500k bounty since 9 September 2024 (**Verified**, [Kiln DeFi audits](https://docs.kiln.fi/v1/kiln-products/defi/security/audits-and-bug-bounty)) |
| **Figment** | Staking API builds ready-to-sign transactions per protocol, plus a broadcast endpoint and transaction decoder (**Verified**, [Figment docs](https://docs.figment.io/docs/transaction-decoder)) | Documented Fireblocks signing flow: contract_call for ETH, program_call for SOL, raw signing for others (**Verified**, [Figment, signing with Fireblocks](https://docs.figment.io/docs/signing-transactions-with-the-fireblocks-api)); WalletConnect-compatible wallets via app (**Vendor claim**) | Quotation required | SOC 2 Type II and ISO 27001 (**Vendor claim**; reports not reviewed) | Large institutional client base (**Vendor claim**) |
| **Coinbase (CDP Staking API / Prime)** | CDP Staking API for non-custodial platforms; Prime staking for custodial Prime clients ([Prime staking docs](https://docs.cdp.coinbase.com/prime/concepts/staking)) | Dedicated ETH: "End-users are always in custody of their funds"; validators are dedicated, not commingled; 32 ETH increments (**Verified**, [CDP Dedicated ETH](https://docs.cdp.coinbase.com/staking/staking-api/protocols/dedicated-eth/overview)) | Dedicated ETH standard commission 8%. **Onchain billing:** a reward-split contract as fee recipient divides execution-layer rewards between integrator, user and Coinbase under a "Reward Distribution Plan" (**Verified**, same page) | Coinbase corporate attestations not reviewed for this product (**Not verified**) | Most relevant model for "platform fee on Staking rewards" without custody |
| **Chorus One** | SDK (non-custodial; networks incl. Ethereum, Solana, TON, Hyperliquid, Monad) (**Vendor claim**, [sdk.chorus.one](https://sdk.chorus.one/)); iFrame staking widget for fintechs, 12 networks at launch, September 2025 (**Vendor claim**, [press release](https://www.globenewswire.com/news-release/2025/09/30/3158843/0/en/Chorus-One-Introduces-Plug-and-Play-Staking-Widget-for-FinTech-and-DeFi-Platforms.html)) | Non-custodial design (**Vendor claim**) | Quotation required; revenue share not disclosed | ISO 27001:2022 (**Vendor claim**); SOC 2 described as "compliant" (**Not verified**) | — |
| **Blockdaemon** | Staking API + reporting API; "Earn Stack" (June 2025) combining staking and DeFi, with Aave as a core integration (**Vendor claim**, [PR Newswire](https://www.prnewswire.com/news-releases/blockdaemon-launches-earn-stack-to-help-institutional-clients-offer-secure-and-compliant-staking-and-defi-solutions-302486040.html)) | Fireblocks one-click staking (**Vendor claim**, [Blockdaemon blog](https://www.blockdaemon.com/blog/fireblocks-clients-get-one-click-staking-with-blockdaemon)) | Quotation required | SOC 2 Type II, SOC 1 Type I, ISO 27001 (**Vendor claim**, [Trust Center](https://www.blockdaemon.com/trust-center)) | — |

**SOC 2 caution.** Every SOC 2 or ISO claim above is self-reported. Before any selection, obtain the report under NDA and check its scope (which systems), period and exceptions. A SOC 2 report on validator operations says nothing about an API's software supply chain, which is exactly what failed in the Kiln incident.

---

## 7. Integration patterns: embedded wallets vs custodial

### 7.1 Pattern A — Member-held positions in embedded wallets (Privy base case)

```
Member embedded wallet (Privy)  --deposit-->  ERC-4626 fee wrapper  -->  Morpho / Aave / Veda vault  -->  borrowers / strategy
        ^ holds vault shares                    | fee shares -> Platform admin wallet
Platform ledger: mirrors share balance per Member, reconciles to chain; never the source of truth for the position
```

- **How.** The Privy Earn API deposits, withdraws and reads positions "with a single API call per operation". Privy handles ERC-20 approval and deposit, and can sponsor gas. Configuration in the Privy Dashboard: choose a vault, choose the fee share (0–50% Morpho, 0–100% Aave), and set an admin wallet. Exchange or cold wallets cannot be the admin wallet, and Privy cannot reassign it later. **Verified:** [Privy Earn overview](https://docs.privy.io/wallets/actions/earn/overview), [setup](https://docs.privy.io/wallets/actions/earn/setup), [revenue sharing](https://docs.privy.io/wallets/actions/earn/revenue-sharing).
- **Providers via Privy.**
  - Self-serve: Morpho (Sentora, Gauntlet, Steakhouse vaults listed), Aave USDC on Base. Veda and Kamino by arrangement.
  - Recipes: Ethena, Sky, Jupiter, Dolomite, Yield.xyz and others.
  - **Verified:** [setup](https://docs.privy.io/wallets/actions/earn/setup), [yield recipes](https://docs.privy.io/recipes/yield/overview).
  - Veda's vault stack (also behind Kraken DeFi Earn) became available to Privy developers on 2 June 2026; developers "set their own fee on top" (**Not verified**: press, [The Block](https://www.theblock.co/amp/post/403277/veda-brings-the-vault-stack-behind-kraken-defi-earn-to-privys-2000-plus-developer-teams)).
- **Custody characterisation, for counsel and due diligence.** Privy states that "Privy does not control DeFi vaults or underlying protocols" (**Verified**, revenue-sharing page). However:
  - Privy "automations" can auto-deposit a wallet's *full balance* into Earn. For wallets with an owner, attaching an automation needs an authorization signature. For **ownerless** wallets it does not (**Verified**, [Privy automations](https://docs.privy.io/wallets/automations/earn-deposits)).
  - Whether the platform has unilateral control over Member wallets depends on how ownership, authorization keys and policies are configured. Per the brief, smart or embedded wallets do **not** by themselves establish a non-custodial model. **Open question** (section 10).
- **Pros.** No pooling. Each Member's position is on-chain and individually redeemable. The fee is enforced on-chain. It matches the base-case wallet.
- **Cons.** Gas and chain choice (Base, Ethereum). A per-Member vault exposure needs monitoring. Fee wrappers are additional contracts that need their own audit evidence (audit status of Privy's fee wrapper: **Not verified**).

### 7.2 Pattern B — Provider-built transactions signed by the Member wallet (Staking)

The Staking API (Figment, Coinbase CDP, Kiln Connect, Chorus One SDK) returns an unsigned transaction. The embedded wallet or MPC signer signs, and the provider broadcasts.

Works for:

- native ETH (32 ETH validators, so practical only for pooled or partial products);
- SOL delegation, which is per-wallet and fits embedded wallets well;
- HYPE delegation.

Revenue model: a provider reward-split contract, e.g. Coinbase onchain billing, or a commercial rebate by quotation.

### 7.3 Pattern C — Omnibus / MPC custody (fallback)

```
Member Deposits -> Platform omnibus wallet (Fireblocks/MPC) -> vault or staking provider
Platform ledger = source of truth for each Member's share of pooled position
```

- **How.** The platform deposits pooled funds into a vault or Staking provider from its custody account. Fireblocks integrations exist for Figment, Blockdaemon and Kiln (**Vendor claims**, above).
- **Implication.** The platform (or its operating entity) controls Member assets and decides allocation, so this becomes an **operator-managed yield program** in the taxonomy. It needs:
  - an internal sub-ledger with pro-rata share accounting;
  - daily reconciliation of vault shares to the ledger;
  - segregation or commingling disclosures;
  - liquidity buffers for withdrawals;
  - the highest level of legal review.

  SwissBorg's Earn programme is a real-world example of this pattern; there the provider API compromise affected pooled Member funds.

### 7.4 Architecture seam to build in Release 1 (no real-funds yield)

- `YieldAdapter` interface (deposit / withdraw / position / accrued yield / fee accrued / status), with implementations per provider: Privy Earn, Kiln DeFi, a direct ERC-4626 vault, a Staking API. The ERC-4626 standard gives a common `deposit`, `redeem`, `convertToAssets` surface for most lending vaults.
- **Ledger.** Record Yield Product positions as *shares*, not balances. Value them by on-chain `convertToAssets` with a recorded timestamp, and label freshness (PRD P2-007, P2-009). Never credit yield from a configured rate.
- **Controls.** Per-vault exposure caps, vault allow-list with curator criteria, kill switch (stop new Deposits; withdraw-only mode), incident runbook, Member disclosures per category.
- **Release 1 demo.** Read-only display of a real vault's live data from chain or provider API, marked as "illustrative, not available", or a testnet or sandbox flow. Do **not** show projected returns computed by the platform (section 9).

---

## 8. How platforms take a fee on yield (commission source)

| Mechanism | How it works | Custody needed? | Evidence |
|---|---|---|---|
| **ERC-4626 fee wrapper (Privy Earn)** | Wrapper skims an app-set percentage of yield as shares to the app's admin wallet. Morpho fees accrue directly as shares; Aave fees accumulate in the contract and are collected via endpoint; Veda claims and sends on a schedule | No | **Verified**, [Privy revenue sharing](https://docs.privy.io/wallets/actions/earn/revenue-sharing) |
| **Kiln DeFi vault fees** | Integrator-set deposit fee and/or rewards fee; rewards fee minted as extra vault shares, so collected fees keep earning until withdrawn; third-party recipients supported | No | **Verified**, [Kiln DeFi FAQ](https://docs.kiln.fi/v1/kiln-products/defi/kiln-defi-faq) |
| **Aave Earn vault performance fee** | Manager-set fee on yield only, not principal; 50% of the fee goes to Aave Labs | No | **Verified**, [Aave Earn vaults](https://aave.com/docs/aave-v3/vaults/overview) |
| **Morpho Vault V2 curator fees** | A platform acting as vault owner or curator can set a performance fee (≤50%) and management fee (≤5%). This makes the platform a curator, with risk-management responsibility | No (but higher responsibility) | **Verified**, [Morpho Vault V2](https://docs.morpho.org/learn/concepts/vault-v2/) |
| **Staking reward split** | Split contract set as validator fee recipient divides execution-layer rewards between integrator, user and provider | No | **Verified**, [Coinbase CDP Dedicated ETH](https://docs.cdp.coinbase.com/staking/staking-api/protocols/dedicated-eth/overview) |
| **Spread / off-chain fee in an omnibus program** | Platform pays Members less than it earns on pooled funds | **Yes** | Pattern C; most sensitive |

**Sensitivity note (no legal conclusion).**

- Taking a fee on yield is ordinary for wallets and fintechs, e.g. Kraken via Privy and Morpho.
- Two features combined need explicit legal review:
  - (a) the platform *selects* the yield source and *earns* from it;
  - (b) MLM **Commissions** are calculated on Yield Product Deposits or on yield.
- Regulators in several jurisdictions have treated interest-bearing crypto programs as securities or investment offerings; see the SEC's Celsius action on its "Earn Interest Program" ([SEC press release 2023-133](https://www.sec.gov/newsroom/press-releases/2023-133)). Recruitment-linked returns are central to pyramid-scheme analysis; see section 9.
- The compensation plan should be designed so that no Commission depends on Members' Yield Product Deposits until counsel has confirmed the structure.

---

## 9. Red flag: return-calculator "staking/ROI plan" modules

**What they are.** Many MLM software vendors sell "ROI", "daily ROI" or "staking plan" modules. These credit a configured percentage (daily, weekly or monthly) to a Member's internal balance. Examples: [Fenizo "Investment MLM software"](https://fenizomlmsoft.com/investment-mlm-plan-software/), [Solidale "ROI based MLM software"](https://solidaletech.com/roi-based-mlm-software/), [DNG "Daily ROI Plan Crypto Demo"](https://play.google.com/store/apps/details?id=com.dng.DailyROICryptocurrencyPlan&hl=en_US). These are **Vendor claims**; the pages are cited only to show the product type exists.

**Why they are unacceptable as a Yield Product.**

1. **No yield source.** The module computes a number. Nothing is lent, staked or traded. Payouts can only come from other Members' Deposits or from operator capital. That is the defining mechanism of a Ponzi scheme: "pays existing investors with funds collected from new investors" ([Investor.gov, Ponzi scheme](https://www.investor.gov/protect-your-investments/fraud/types-fraud/ponzi-scheme); [SEC/OIEA alert, Ponzi schemes using virtual currencies](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/investor-7)).
2. **Fixed or "guaranteed" rates are a recognised fraud red flag.** Real DeFi and Staking yields are variable. SEC/CFTC staff cite "high guaranteed returns" with "little or no risk" as warning signs ([Investor.gov / CFTC alert](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/investor-alert-watch-out-fraudulent-digital-asset-and-crypto-trading-websites)).
3. **Enforcement precedents combine exactly these features with MLM.** All **Verified**, regulator sources:
   - **HyperFund (SEC, 29 January 2024).** "Membership" packages promised 0.5–1% per day, supposedly from crypto mining, plus a referral system. The SEC alleged no real revenue source beyond investor funds; more than USD 1.7B raised ([SEC 2024-11](https://www.sec.gov/newsroom/press-releases/2024-11)).
   - **Forsage (SEC, August 2022).** Smart-contract-based pyramid scheme. "Fraudsters cannot circumvent the federal securities laws by focusing their schemes on smart contracts and blockchains" ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)).
4. **Ledger integrity.** Crediting unbacked returns makes the ledger diverge from on-chain assets. That breaks the reconciliation requirement (brief section 4; PRD P2-009) and creates an unfunded liability.

**Rule for vendor evaluation.** An MLM vendor's "staking" feature is acceptable only if it is an interface onto an identified external protocol or provider, with on-chain positions reconcilable per Member. A calculator-only module is grounds to treat the feature as absent and, if marketed as yield, as an exclusion signal (brief section 4: "Whether the feature executes an underlying product or only displays calculated returns").

---

## 10. Risks (cross-cutting)

| Risk | Where it bites | Mitigation |
|---|---|---|
| Smart contract | All on-chain options; fee wrappers | Allow-list audited contracts only; get audit reports for any wrapper; exposure caps |
| Oracle / configuration | Lending (Aave CAPO, March 2026); curated vaults (xUSD hard-coded pricing, 2025) | Prefer conservative markets; monitor; incident runbook |
| Pooled contagion / bad debt | Aave pools (rsETH, April 2026) | Diversify; caps; watch governance alerts |
| Curator / strategy | Morpho vaults, Veda, Hyperliquid user vaults | Curator due diligence; "Prime"-type vaults; timelock and Sentinel present |
| Liquidity | Lending at high utilisation; LST queues; HLP 4-day lockup; HYPE 7-day queue | Disclose exit terms per product; keep withdraw-only mode; no instant-liquidity promises |
| Principal loss from trading | HLP, user vaults, any QUANT strategy | Keep out of Release 1 and any "savings" framing |
| Depeg | Stablecoins (USDC, USDT, USDe), LSTs | Limit to major stablecoins; disclose |
| Third-party provider / API compromise | Staking APIs (Kiln, September 2025), wallet infra | Verify transaction contents before signing (transaction decoders); signing policies; vendor security review beyond SOC 2 |
| Venue centralisation / governance intervention | Hyperliquid (JELLY settlement), Aave Guardian freezes | Disclose; treat as counterparty-like risk |
| Regulatory | Any Yield Product, more so with pooling, operator selection, fee-on-yield and Commissions | Legal confirmation before real funds (brief section 8) |

---

## 11. Open questions

**For the client**

1. Which mechanism is meant by "staking": a stable-value return on stablecoins (lending), Staking of a volatile token, or exposure to QUANT trading? The answer changes the product category and its risk disclosures.
2. Should the Yield Product be offered to all Members, or allow-listed per jurisdiction? Morpho V2 gates and Kiln geofencing support this.
3. Is fee-on-yield intended as a platform revenue line? Is any Commission intended to be linked to Yield Product Deposits?

**For vendors (do not contact during research; list for the due diligence phase)**

4. Privy: audit reports for the Earn fee-wrapper contracts; Privy pricing for Earn; exact control model for ownerless vs owned wallets and authorization keys; supported chains for production vaults.
5. Kiln / Figment / Blockdaemon / Chorus One: SOC 2 Type II report scope and period; post-September-2025 API supply-chain controls (Kiln); revenue-share terms; embedded-wallet (non-Fireblocks) signing support.
6. Coinbase CDP: availability of onchain billing for Solana and partial ETH, and eligibility by jurisdiction.

**For legal counsel**

7. Characterisation of each category (lending vault access, Staking, trading vault, operator-managed program) in the target jurisdictions. Does the platform-controlled fee wrapper or vault curation change that characterisation?
8. Does linking MLM Commissions to Yield Product activity raise pyramid or investment-contract concerns in the target jurisdictions?
9. Disclosure requirements for variable returns, lockups and principal-loss risk.

**Technical due diligence**

10. QUANT: if it proposes a "staking/yield" product, which category in the taxonomy does it fall in, who holds the assets, and where is the on-chain evidence? (Not evaluated here per scope.)
11. Chain choice for Release 2 yield (Base vs Ethereum mainnet vs Solana): gas cost per Member action against vault availability.

---

## 12. Evidence limitations

- Search budget was exhausted before Rocket Pool and Jito audit histories were researched. Those cells are marked **Not verified**.
- Some vendor pages (Coinbase blog, Jito docs) returned HTTP 403 to automated fetching. Claims sourced from search excerpts of official pages are labelled **Vendor claim**.
- Hyperliquid loss events are documented from reputable press, not from Hyperliquid primary disclosures. Exact figures vary by source.
- No SOC 2 reports were obtained. All certification statements are vendor claims.
- APYs, curator fees and protocol parameters change frequently. Re-check at integration time.
