# Task 2: AI Tool-Building Challenge - Customer 360 Insight Tool

---

## 1. Problem Solved

**Problem:** In a growing company, customer information is scattered across multiple systems — CRM (Zoho), support tickets, emails, Slack conversations, and internal notes. When a sales or growth team member needs to understand a customer's situation quickly, they have to check 4-5 different tools. This leads to:
- Missed signals (urgent tickets, negative sentiment)
- Slow response times
- Inconsistent customer experience
- Lost revenue from missed up-sell opportunities

**Solution:** A single-page web tool that aggregates data from 4 sources (CRM, Support Tickets, Emails, Slack notes) into a unified 360° customer view. It automatically:
- Summarizes account context
- Highlights risks (urgent tickets, negative email sentiment)
- Identifies opportunities (expansion signals, referrals, high-value accounts)
- Recommends the next best action with priority levels

---

## 2. Tool / Prototype

**File:** `index.html` — a self-contained HTML file. Open it directly in any browser. No installation, no server, no dependencies.

**How to run:**
1. Open `index.html` in Chrome, Firefox, Safari, or Edge
2. Select a customer from the dropdown
3. View the unified 360° dashboard

---

## 3. Screenshots

*(No screenshots needed — the tool is a single HTML file that works offline. To generate screenshots:)*
1. Open `index.html` in a browser
2. Select "Acme Corp" from the dropdown
3. Take a screenshot showing all 6 cards (Summary, CRM, Tickets, Emails, Signals, Actions)

---

## 4. Dummy Data Used

### Source 1: CRM Data (Zoho)
- 15 customers with fields: ID, Name, Stage, Deal Value, Owner, Company Size, Industry, Status, Last Contact Date
- Stages covered: Discovery, Qualified, Proposal Sent, Negotiation, Closed Won, Closed Lost
- Industries: SaaS, FinTech, Healthcare, Manufacturing, Defense, Technology, Biotech, etc.

### Source 2: Support Tickets
- 15 tickets with fields: Ticket ID, Customer Name, Issue Description, Priority (Urgent/High/Medium/Low), Status (Open/Closed), Created Date, Support Agent
- Realistic scenarios: Integration failures, billing discrepancies, SSO login issues, compliance reports

### Source 3: Email History
- 15 emails with fields: Email ID, Customer Name, Sender, Subject, Sentiment (Positive/Neutral/Negative), Date
- Sentiment is analyzed programmatically in the tool to flag risks

### Source 4: Slack/Internal Notes (Bonus)
- 5 internal notes from channels: #sales, #support, #engineering, #product
- Contains real-world signals like "upsell opportunity" or "customer frustration"

---

## 5. Prompts, Logic, Workflow & Tools Used

### Tools Used
- **Claude (AI Assistant):** Designed the architecture, wrote the complete HTML/CSS/JS code, created realistic dummy data
- **Plain HTML/CSS/JavaScript:** Zero-dependency implementation. Runs in any browser
- **No frameworks, no build tools, no APIs** — just a single file that works instantly

### Logic & Workflow

```
User selects a customer
        │
        ▼
┌─────────────────────────────────────────────┐
│            AGGREGATION LAYER                │
│  ┌──────────┐ ┌──────────┐ ┌─────────────┐  │
│  │ CRM Data │ │ Tickets  │ │   Emails    │  │
│  │  (Zoho)  │ │ (Zendesk)│ │  (Gmail)   │  │
│  └────┬─────┘ └────┬─────┘ └──────┬──────┘  │
│       └────────────┼──────────────┘         │
│                    ▼                        │
│           Combined Customer View            │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│           ANALYSIS ENGINE                   │
│  • Count open/urgent tickets               │
│  • Detect negative email sentiment         │
│  • Identify pipeline stage                 │
│  • Check for expansion/referral signals    │
│  • Flag high-value accounts                │
│  • Parse Slack intelligence                │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│            OUTPUT GENERATION                │
│  • Account Summary (risk badge + KPIs)     │
│  • CRM Detail View                         │
│  • Ticket List (priority-coded)           │
│  • Email History (sentiment-coded)        │
│  • Signals & Risks (categorized cards)    │
│  • Next Best Actions (prioritized list)   │
└─────────────────────────────────────────────┘
```

### Key Logic: Signal Detection

| Condition | Signal Type | Action |
|-----------|------------|--------|
| Urgent tickets open | 🔴 Risk | Call customer immediately |
| Negative email sentiment | 🔴 Risk | Schedule check-in call |
| >2 open tickets | 🟡 Risk | Review with support team |
| High deal value (>₹2L) | 🟢 Opportunity | Assign senior team member |
| Expansion/referral mentioned | 🟢 Opportunity | Follow up on expansion leads |
| Slack intelligence available | 🟢 Opportunity | Incorporate internal context |
| Negotiation stage | 🟢 Opportunity | Action all open tickets before closing |

---

## 6. Example Input & Output

### Input: Selecting "Acme Corp"

**Raw data from 4 sources combined:**
```
CRM:  Acme Corp | Negotiation | ₹1,20,000 | Priya S. | SaaS | Active
Tickets: 
  - TKT-101: Integration failure (High, Open)
  - TKT-102: Billing discrepancy (Urgent, Open)
  - TKT-115: QBR scheduling (Medium, Open)
Emails:
  - "Concerned about recent billing changes" (Negative)
  - "Pricing discussion for Q3 renewal" (Neutral)
Slack:
  - "Acme CFO mentioned frustration with current vendor lock-in" (#sales)
  - "Acme power user — using 90% of premium features" (#product)
```

### Output: 360° Dashboard View

```
┌─────────────────────────────────────────────────────┐
│ 📋 ACCOUNT SUMMARY                                  │
│ Acme Corp  🔴 At Risk  |  Negotiation  |  SaaS      │
│ Owner: Priya S. | ₹120K | Last: 2026-07-05          │
│ ┌──────┐ ┌──────┐ ┌──────────┐                     │
│ │  3   │ │  2   │ │Negotiation│                     │
│ │Open  │ │Emails│ │  Stage   │                     │
│ │Tickets│ │     │ │          │                     │
│ └──────┘ └──────┘ └──────────┘                     │
├─────────────────────────────────────────────────────┤
│ ⚠️ SIGNALS & RISKS                                  │
│ 🔴 1 Urgent open ticket(s)                         │
│ ⚠️ High open ticket volume (3)                     │
│ 📉 Negative email sentiment detected               │
│ 💬 Slack intelligence available                    │
├─────────────────────────────────────────────────────┤
│ 🎯 NEXT BEST ACTION                                 │
│ 🔴 HIGH: Call immediately about TKT-102 (billing)  │
│ 🟡 MEDIUM: Schedule check-in for billing concerns  │
│ 🟢 LOW: Review open tickets with support team      │
└─────────────────────────────────────────────────────┘
```

---

## 7. How I Would Improve This With More Time

### Improvement 1: Real API Integration
- Connect to actual Zoho CRM API, Gmail API, and Zendesk/Jira APIs for live data
- Add OAuth authentication flow
- Implement webhook listeners for real-time updates

### Improvement 2: Machine Learning Sentiment Analysis
- Replace keyword-based sentiment detection with a proper ML model (e.g., using TensorFlow.js or an API like OpenAI/Gemini)
- Add topic extraction to automatically categorize customer concerns (e.g., "pricing", "integration", "support quality")
- Predict churn probability based on combined signals

### Improvement 3: Collaboration Features
- Add team notes/annotations on each customer view
- Create shareable links for specific customer dashboards
- Add task assignment — "assign this next action to [team member]"
- Integration with Slack — push daily digest of risky accounts to a channel

### Improvement 4: Historical Trends
- Track how signals change over time (e.g., "this customer had 0 tickets last month, now has 5")
- Add trend arrows and alerts for sudden changes
- Weekly summary email for key accounts

### Improvement 5: Mobile & Offline Support
- Progressive Web App (PWA) with service worker for offline access
- Push notifications for urgent signals
- Touch-optimized interface for field sales teams

---

## Summary

| Requirement | Status |
|------------|--------|
| 1. Data from 3+ sources | ✅ 4 sources (CRM, Tickets, Emails, Slack) |
| 2. Combined into one view | ✅ 6-card dashboard |
| 3. Summarize key context | ✅ Account summary with risk badge |
| 4. Highlight risks/opportunities | ✅ Automated signal detection |
| 5. Recommend next action | ✅ Prioritized action list |
| 6. Simple output format | ✅ Clean web UI, no login needed |
| Dummy data | ✅ 15 customers, 50+ records |
| Complete documentation | ✅ This document |