---
title: "AlphaWave Platform: Solution Research and First-Release Architecture"
subtitle: "Prepared by Cyclone for AlphaWave"
author:
  - Cyclone
date: "Research date: 6 October 2026 · Draft v0.1"
lang: en
toc: true
toc-depth: 2
---

<!--
SKELETON. Each section lists its source notes and the points already established.
Sources: research/notes/01..07, references/ (read-only), GLOSSARY.md.
Use glossary terms: Yield Product, Staking, Deposit, Member, Sponsor Tree, Commission.
Label claims: Verified / Vendor claim / Working assumption / Not verified.
-->

# Executive summary and recommended direction

<!--
- Recommended direction (primary + fallback) in one paragraph.
- Headline findings:
  - No MLM vendor offers a real Yield Product; yield sits outside the MLM core (01).
  - Major on-ramps and Stripe prohibit MLM in partner terms; Release 1 is crypto-only (03, decision).
  - Privy fits embedded wallets; Bridge/Stripe features unusable for MLM (02).
  - KYC: no-KYC assumption unsupported; tiered KYC base case (06).
- Real-funds launch in 30 days: state plainly whether supported; closest credible milestone.
- What can be decided now / needs vendor demo or quote / needs technical DD / needs legal.
-->

# Business requirements and working assumptions

## Business context

## Requirements as understood

<!-- From brief §2 and PRD (non-binding). Release 1 scope decisions: crypto-only Deposits; Yield Product not live with real funds; QUANT integration Phase 2 only. -->

## Working assumptions

<!-- Jurisdiction-neutral; Cyclone leads technology; buy MLM core; Privy base case for wallets; tiered KYC base case for estimates; commission base pending client confirmation. -->

## Contradictions in the reference documents

<!-- PRD "final" vs non-binding; staking Phase 2 in PRD; no-KYC vs comp plan KYC for leaders; subscription base superseded; QUANT/Hyperliquid absent from client docs; comp plan "fully built" vs PRD open formulas; L2-10 rates missing vs 30% cap. -->

# Key findings and constraints

## Yield Product terminology

<!-- Six mechanisms per brief §3; taxonomy table from 04. -->

## Payment-provider acceptance of MLM

<!-- Stripe prohibited list (verified 2026-09-22); on-ramp table from 03/07. -->

## Custody is determined by control, not labels

<!-- 02 + 06: hybrid when platform holds signer; FATF/FinCEN/MiCA control test. -->

## Commission base

<!-- Evidence from 01: deposit/ROI bases common in crypto-MLM software and high-risk; event-driven engines can use platform fee revenue; Privy Earn fee wrapper as a non-custodial revenue source. Pending client confirmation and counsel. -->

# MLM platform comparison, shortlist and exclusions

## Eligibility conditions

## Vendors reviewed

## Weighted scorecard

## Shortlist

## Exclusions

# CRM and customer operations

## Options compared

## System boundaries: CRM, helpdesk, back office and ledger

## Minimum viable setup for 30 days

## Expansion path

# Architecture options and fund flows

## Option 1: Integrated white-label MLM platform

## Option 2: Modular architecture (MLM core + Privy + yield adapter + helpdesk)

## Option 3: QUANT integration in Phase 2

## Comparison

## Web-first delivery

## Recommendation: primary and fallback

# Cost, effort and 12-month operating estimates

<!-- USD. Rates are contracted: show person-months, not day rates. Focus on external software costs. Separate verified public pricing / quote required / consultant estimate. -->

## External software costs

## One-time implementation costs

## Monthly operating costs

## Indicative 12-month total cost of ownership

## Effort by workstream (person-months)

## Minimum delivery team

## Dependencies and critical path

# Proposed 30-day scope and readiness criteria

## Weekly plan

## Requirements before accepting real funds

## Controlled pilot features

## Later phases

## Readiness assessment

# Risks and due diligence requirements

# Questions for vendors, QUANT and legal counsel

## Vendors

## QUANT (Phase 2)

## Legal counsel

# Business decisions required from the Client

# Sources, research date and evidence limitations

## Research date and method

## Evidence limitations

## Sources
