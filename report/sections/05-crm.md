# CRM and customer operations

## Recommendation in brief

**For the first 30 days, use a dedicated SaaS helpdesk, not a CRM suite.** Customer operations at this stage are ticket handling: questions about Deposits and withdrawals, verification problems, Commission disputes, access and security. The helpdesk is the inbox; the Cyclone-built admin back office is where agents look things up and where operational actions happen. The two are linked by deep links and a read-only sidebar keyed on the Member ID.

Salesforce and Odoo, which AlphaWave has discussed previously, are assessed on equal terms. Both are better suited to a later CRM phase than to the 30-day helpdesk.

## Options compared

| | Zendesk Suite Professional | Freshdesk Omni Enterprise | Intercom Expert | Salesforce Service Cloud | Odoo (Enterprise apps) |
|---|---|---|---|---|---|
| List price, per agent per month (annual) | $115 | $119 | $132 | $195 (Core), $395 (Advanced) | Varies by billing country; quote |
| Custom objects (link to Member ID, wallet, KYC status) | Up to 30 | Yes | 15 on all plans (claim) | Yes, extensive | Yes (Studio) |
| SLAs and escalation | Yes | Yes | Expert plan | Yes (entitlements) | Yes |
| Approvals | Ticket approvals | Yes | Limited | Yes | Approvals app |
| Audit log | Enterprise tier (quote) | Included | Plan to confirm | Yes; Shield for field history | Yes |
| SSO | Yes | Yes | Expert plan | Yes | Yes |
| Telegram | Via integration | Marketplace app | **Native** (claim) | Custom build | Third-party modules (needs Odoo.sh or self-hosting) |
| Data residency | Free data-location add-on (US, EEA, UK, JP, AU) | Regional data centres | Regional hosting | Hyperforce regions | Hosting choice |
| Implementation effort (estimate) | 0.75–2.5 person-months | 0.75–2.5 | 0.75–2.5 | 3–5 | 2–3 |
| Fit for the 30-day milestone | **Good** | **Good** | Good if chat-led | Poor (effort) | Fair (effort, API on Custom plan only) |

Sources (prices seen 6 October 2026, verified on vendor pages): [Zendesk pricing](https://www.zendesk.com/pricing/), [Freshdesk Omni pricing](https://www.freshworks.com/freshdesk/omni/pricing/), [Intercom pricing](https://www.intercom.com/pricing), [Salesforce Service Cloud pricing](https://www.salesforce.com/service/pricing/), [Odoo editions](https://www.odoo.com/page/editions), [Odoo pricing](https://www.odoo.com/pricing).

Additional notes:

- **Odoo:** Helpdesk, Knowledge, Approvals and Studio are Enterprise-only, and the external API requires the Custom plan (verified). The USD price depends on the billing country: $13.40–$16.40 per user was shown for the research location, and a third party reports $49–$61 in the United States (not verified). Odoo also licenses every internal user, including back-office staff, whereas SaaS helpdesks license agents only. ISO 27001 and SOC 2 evidence could not be retrieved.
- **Salesforce:** the strongest case management, audit options and residency, at the highest licence and administration cost. Financial Services Cloud ($325–$700 per user) is not justified at this stage.
- **Intercom:** the only option with native Telegram, which suits community-led MLM support. Its AI agent costs $0.99 per resolved outcome on top of seats.

## System boundaries: CRM, helpdesk, back office and ledger

No CRM or helpdesk holds authoritative financial data.

| System | Source of truth for | Must not own or do | Agent access |
|---|---|---|---|
| Financial ledger | Balances, Deposits, withdrawals, Commission payouts, reconciliation state | Conversations; manual edits | None directly; only through back-office commands |
| MLM platform | Sponsor Tree, plan versions, Commission calculations and explanations | Payout execution; tickets | Read-only views via the back office |
| Verification provider | KYC status, evidence, sanctions results | Being copied into the helpdesk | Status only; evidence for the compliance role |
| Admin back office (Cyclone) | Operational actions: withdrawal hold, approval and retry; account freeze; address-change review; Commission adjustment requests; admin audit log | Messaging; SLA tracking | Role-scoped; any financial action needs a second approver |
| Helpdesk | Conversations, tickets, SLA timers, knowledge base, macros | Balances, wallet secrets, KYC documents, approval of funds movements, Sponsor Tree changes | All agents; cases store reference IDs only |
| CRM (later) | Relationship context: leaders, pipelines, segments, campaigns | Authoritative balances or Commission figures | Member-success staff |

Design rules:

1. The helpdesk stores **references, not values**. Member status is fetched live from the back office.
2. Helpdesk approvals are for non-financial decisions only. Every funds movement is approved in the back office with maker-checker control.
3. Agents never request private keys or seed phrases; macros, the knowledge base and inbound filters enforce this.
4. Cases are created automatically from the back office (stuck withdrawal, KYC rejection, Commission dispute) with a back-office reference.

## Minimum viable setup for 30 days

- **Tool:** one helpdesk chosen after a one-week scripted trial of Zendesk Suite Professional and Freshdesk Omni Enterprise, or Intercom if chat and Telegram will dominate.
- **People:** three to five agents for a controlled pilot, one support lead and a quarter of a helpdesk administrator's time. Finance and compliance approvers work in the back office.
- **Channels:** email and in-app chat. Telegram and WhatsApp only after verified accounts and a security review.
- **Case types:** Deposit, withdrawal, KYC, Commission dispute, Sponsor Tree or referral, account access, security or phishing.
- **Queues and SLAs:** security and withdrawal cases at the highest priority; separate queues for funds, verification and Commissions.
- **Knowledge base:** 20–40 articles reviewed by compliance, including wrong-network Deposits, network fees, verification steps, how and when Commissions are paid, and security warnings. No financial advice.
- **AI agent:** off, or restricted to approved knowledge with forced escalation on funds and verification topics.
- **Effort:** about 1.5 person-months (range 0.75–2.5) and two to three weeks elapsed once procurement is complete.

| Monthly licence cost (estimate from list prices) | 5 agents | 15 agents |
|---|--:|--:|
| Low (Freshdesk Omni Growth or Zendesk Suite Team) | $145–$275 | $435–$825 |
| Base (Zendesk Suite Professional or Freshdesk Omni Enterprise) | $575–$595 | $1,725–$1,785 |
| High (Zendesk Enterprise, or Salesforce Service Core with messaging) | about $1,350+ | about $4,050+ |

Usage-based AI and messaging fees are additional.

## Expansion path

- **Months 2–4: harden the helpdesk.** Add Telegram and WhatsApp, upgrade to the tier with audit logs and custom roles if not bought initially, add QA scoring and multilingual content, and enable a knowledge-restricted AI agent.
- **Months 4–9: add a CRM layer if the business case exists**, for leader relationship management, market onboarding pipelines and campaign segmentation. Options: the helpdesk vendor's own CRM (simplest); Odoo if AlphaWave also wants ERP functions (estimated 3–6 person-months); or Salesforce if scale and partner portals justify it (estimated 4–8 person-months plus 0.5–1 FTE administrator).
- **Later: consolidation.** If Salesforce or Odoo becomes the CRM, decide whether to migrate support into it; budget 2–4 person-months.
