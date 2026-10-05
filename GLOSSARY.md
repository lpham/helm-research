# Helm

Helm is Cyclone's research and architecture project for an MLM-distributed crypto financial platform: members deposit fiat or crypto, hold it as crypto, and access yield, while the MLM network earns commissions.

## Parties

**Cyclone**:
The implementation company that leads the technology, authors the research and integrates purchased core software.
_Avoid_: Vendor, agency

**QUANT**:
An associated trading company whose algorithmic trading engine is a later-phase integration, not a core dependency.
_Avoid_: Partner platform, the engine

## Product

**Yield Product**:
Any product that offers members a return on deposited assets, whatever the underlying mechanism.
_Avoid_: Staking (as a generic term), earn, saving

**Staking**:
Locking a proof-of-stake asset to secure a network in return for protocol rewards, either directly (native) or through a protocol that issues a tradable receipt token (liquid).
_Avoid_: Yield, interest

**Deposit**:
Funds a member adds to the platform, arriving as crypto or as fiat converted to crypto.
_Avoid_: Investment, top-up

## Network

**Member**:
A person registered on the platform with a position in the Sponsor Tree.
_Avoid_: User, affiliate, distributor

**Sponsor Tree**:
The permanent genealogy recording which Member introduced each Member; the only tree in the plan.
_Avoid_: Downline tree, placement tree, binary tree

**Commission**:
A payment to a Member calculated from activity in their Sponsor Tree under a versioned compensation plan.
_Avoid_: Bonus (as a generic term), reward, earnings

**Subscription**:
A superseded commissionable product from an earlier version of the compensation plan; no longer the commission base.
_Avoid_: Using it to mean the current commission base
