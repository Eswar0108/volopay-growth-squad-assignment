# Task 3: Lead Pipeline Dashboard

## Files
- **lead_pipeline_data.csv** — Raw data (25 leads, 13 columns). Import into Google Sheets or Excel.
- **lead_pipeline_with_dashboard.xlsx** — (Optional) Pre-built dashboard with formulas, pivot tables, and charts.

---

## How to Set Up the Dashboard

### Step 1: Import Data
1. Open **Google Sheets** (recommended) or Excel
2. Import `lead_pipeline_data.csv` → **Data > Import**
3. Name the sheet: **"Raw Data"**

### Step 2: Create Pivot Tables & Summary Sheet
Create a new sheet **"Dashboard"** and use these formulas:

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Total Leads** | `=COUNTA(Raw Data!A2:A26)` | Total count |
| **Leads by Channel** | `=QUERY(Raw Data!D2:E26, "select D, count(A) group by D label count(A) ''")` | Channel breakdown |
| **Open Pipeline Value** | `=SUMIF(Raw Data!H2:H26, "Closed Won", Raw Data!I2:I26, "<>")` | Total value of active deals |
| **Leads Needing Follow-up** | `=COUNTIF(Raw Data!K2:K26, "<=" & TODAY())` | Overdue follow-ups |
| **Conversion Rate** | `=COUNTIF(Raw Data!H2:H26, "Closed Won") / COUNTA(Raw Data!H2:H26)` | Win rate % |
| **Stuck Leads** | `=COUNTIF(Raw Data!H2:H26, "Discovery")` | Most common stuck stage |
| **High Priority** | `=COUNTIFS(Raw Data!I2:I26, ">100000", Raw Data!J2:J26, "High", Raw Data!H2:H26, "<>Closed Won")` | High value, high priority open deals |
| **Channel Performance** | `=QUERY(Raw Data!D2:E26, "select D, count(A), sum(I) group by D label count(A) 'Leads', sum(I) 'Value'")` | Revenue by channel |

### Step 3: Add Conditional Formatting
1. **Priority column (J):** Highlight `High` in red, `Medium` in yellow, `Low` in green
2. **Follow-Up Date (K):** Highlight cells older than today in red (overdue)
3. **Stage (H):** Color code: Discovery=blue, Qualified=purple, Proposal Sent=orange, Negotiation=red, Closed Won=green, Closed Lost=gray

### Step 4: Add Charts
1. **Lead Source Pie Chart** — Visual breakdown of channels
2. **Pipeline Value Bar Chart** — Total deal value by stage
3. **Leads Over Time Line Chart** — Lead volume by date received
4. **Individual Performance Bar Chart** — Leads by assigned team member

---

## How a Sales Manager Should Use This Dashboard

### Daily Use (5 minutes)
1. **Open the Dashboard sheet** — see total leads, open pipeline value, and overdue follow-ups at a glance
2. **Check "Follow-ups Due"** — sort by Follow-Up Date and assign actions to team members for any overdue items
3. **Review new leads** — filter by Date Received = today to ensure no lead slips through

### Weekly Use (15 minutes)
1. **Channel Performance Review** — look at the channel performance table to see which channels are producing the most value, not just volume
2. **Stuck Lead Analysis** — identify leads that have been in "Discovery" or "Qualified" for more than 7 days and discuss with the assigned owner
3. **Pipeline Health Check** — check the open-to-closed ratio. If too many leads are in early stages, push for progression

### Monthly Use (30 minutes)
1. **Conversion Rate Trend** — track conversion rates month-over-month. A declining rate signals a problem in qualification or sales process
2. **High-Value Account Review** — pull up all leads with deal value > ₹1,00,000 and review account plans individually
3. **Team Performance** — review leads assigned vs closed per team member. Identify coaching opportunities

---

## Three Insights From the Sample Data

### Insight 1: Organic Search Drives Volume, Referral Drives Value
- **Data:** Website (Organic Search) generates the most leads (8 out of 25), but Referral leads have the highest average deal value (₹1,10,750 vs ₹1,22,250 average overall)
- **Action:** Increase referral program investment. Referral leads convert faster and have higher trust built in.

### Insight 2: "Discovery" Stage Is the Biggest Bottleneck
- **Data:** 5 out of 25 leads (20%) are stuck in Discovery stage, totaling ₹5,75,000 in pipeline value
- **Action:** Create a structured "Discovery to Qualified" workflow with specific criteria (budget identified, decision-maker engaged, timeline confirmed) to move leads through faster.

### Insight 3: Low-Priority Leads Are Being Ignored Despite High Value
- **Data:** Lead LD-004 (₹45,000, Umbrella Co) and LD-023 (₹85,000, Oscorp) are both marked "Low" priority but together represent ₹1,30,000 in potential revenue
- **Action:** Implement an "aging" rule — any lead older than 10 days auto-escalates one priority level, ensuring no lead is permanently deprioritized.

---

## Three Improvements for Real Team Use

### Improvement 1: Integrate Email & Call Logs
- **What:** Connect the spreadsheet to the team's email (Gmail/Outlook) and call logging system (like Aircall, RingCentral) so last-contact dates and notes are auto-populated
- **Why:** Manual entry leads to stale data. Auto-logging ensures the dashboard always reflects reality
- **Cost:** Low — Google Apps Script can connect to Gmail API for free

### Improvement 2: Add Lead Scoring Formula
- **What:** Add a calculated column that scores each lead based on: Deal Value (30%), Priority (25%), Industry Fit (20%), Engagement Score (15%), and Recency (10%)
- **Why:** Helps the team prioritize the right leads instead of just chasing the highest value ones. A ₹50K lead with high engagement and perfect fit may be better than a ₹2L lead with low engagement
- **Formula example:** `= (I2/100000)*30 + IF(J2="High",25,IF(J2="Medium",15,5)) + engagement_score`

### Improvement 3: Automated Slack Alerts & Weekly Digest
- **What:** Set up a Google Apps Script that:
  - Sends a **daily Slack message** at 9 AM listing all leads with follow-ups due that day
  - Sends a **weekly email digest** every Monday with pipeline KPIs to the sales manager
- **Why:** Reduces the need for the team to constantly check the sheet. The information comes to them
- **Implementation:** Google Apps Script + Slack webhook = ~2 hours to set up

---

## Answering the 8 Dashboard Questions

| # | Question | How Dashboard Answers It |
|---|----------|-------------------------|
| 1 | How many leads came in? | Total leads count (25) + trend chart over dates |
| 2 | Where did leads come from? | Pie chart by Lead Source + Channel |
| 3 | Which leads are still open? | Filter by Stage ≠ "Closed Won" or "Closed Lost" |
| 4 | Which leads need follow-up? | Follow-Up Date ≤ TODAY() filter + conditional formatting |
| 5 | Which channels perform best? | Channel Performance query (count + value by source) |
| 6 | Where are leads getting stuck? | Stage-wise count shows bottleneck (e.g., 5 in Discovery) |
| 7 | Which opportunities are high priority? | High Priority count + value query |
| 8 | What actions should the team take? | Follow-up due list + stuck lead analysis |