#!/usr/bin/env python3
"""Generate PDF for Task 1 - LinkedIn Posts"""
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(26, 26, 46)
        self.cell(0, 10, 'Volopay Growth Squad Assignment', align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, 'Task 1: Finance Content Challenge - LinkedIn Posts', align='C', new_x="LMARGIN", new_y="NEXT")
        self.line(10, self.get_y()+2, 200, self.get_y()+2)
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(26, 26, 46)
        self.ln(4)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(50, 50, 80)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def bold_text(self, text):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def italic_text(self, text):
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.set_x(self.l_margin)
        self.multi_cell(0, 5.5, '  - ' + text)

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# Title
pdf.set_font('Helvetica', 'B', 20)
pdf.set_text_color(26, 26, 46)
pdf.cell(0, 12, 'Task 1: LinkedIn Content Series', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, 'Finance Content Challenge - Volopay Growth Squad', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)

# ========== POST 1 ==========
pdf.section_title('Post 1: The Real Cost of Manual AP Processing')
pdf.sub_title('Target Audience:')
pdf.body_text('Accounts Payable (AP) teams, Controllers, Finance Managers')
pdf.sub_title('Why this topic matters:')
pdf.body_text('AP processing is a daily pain point. Most finance teams spend 40-60% of their time on manual data entry and reconciliation. This post speaks directly to the frustration and offers a practical reframe.')
pdf.ln(2)
pdf.body_text('Every morning, Sarah opens 47 invoices, 3 spreadsheets, and 2 browser tabs to do what she did yesterday. Again.')
pdf.body_text('If you are in AP, you know Sarah.')
pdf.ln(1)
pdf.bold_text('Here is what nobody tells you about manual AP processing:')
pdf.bullet('It is not just slow - it is risky. Duplicate payments, missed discounts, and data entry errors cost companies an average of 1-2% of annual revenue.')
pdf.bullet('It masks real problems. When your team is busy entering data, they do not have time to ask "why did we spend 3x on vendor X this month?"')
pdf.bullet('It burns your best people. Your sharpest finance operators get bored. They leave. And then you are training someone new to do the same manual work.')
pdf.ln(1)
pdf.body_text('What if we flipped the script?')
pdf.body_text('Instead of asking "how do we process invoices faster," ask "what would our AP team do if they had 20 hours back every week?"')
pdf.body_text('The answer is usually: negotiate better terms, catch anomalies early, improve vendor relationships.')
pdf.body_text('That is not just AP work. That is strategic finance work.')
pdf.body_text('Stop treating AP as a processing center. Start treating it as an intelligence center.')
pdf.ln(2)
pdf.italic_text('What is one manual process your team spends too much time on? Drop it below.')

# ========== POST 2 ==========
pdf.add_page()
pdf.section_title('Post 2: The Metric That Actually Predicts SaaS Burn')
pdf.sub_title('Target Audience:')
pdf.body_text('CFOs, FP&A professionals, Finance Operators')
pdf.sub_title('Why this topic matters:')
pdf.body_text('Most finance teams track burn multiple the wrong way. Leading indicators are underused in SaaS finance. This post positions the reader as someone who thinks ahead.')
pdf.ln(2)
pdf.body_text('Every CFO I know tracks burn multiple.')
pdf.body_text('But most are looking in the rearview mirror.')
pdf.ln(1)
pdf.bold_text('Here is the problem with standard burn multiple:')
pdf.bullet('It is lagging (looks at past 12 months)')
pdf.bullet('It averages out your best and worst months')
pdf.bullet('It tells you where you have been, not where you are headed')
pdf.ln(1)
pdf.bold_text('Try this instead:')
pdf.body_text('Leading Burn Ratio = (Current Month Net Burn) / (New ARR Signed This Month)')
pdf.ln(1)
pdf.bold_text('Why this works:')
pdf.bullet('It measures efficiency in real-time')
pdf.bullet('It forces you to look at your sales engine, not just your spend')
pdf.bullet('A rising ratio tells you to tighten spend BEFORE cash becomes an issue')
pdf.ln(1)
pdf.body_text('Try benchmarking your last 3 months against this. If your Leading Burn Ratio is trending up, you have a signal - not a surprise - 60 days before your board asks.')
pdf.body_text('Your FP&A team does not need more reports. They need better signals.')
pdf.ln(2)
pdf.italic_text('What is one metric you wish your board tracked?')

# ========== POST 3 ==========
pdf.add_page()
pdf.section_title('Post 3: The Follow-Up That Closes')
pdf.sub_title('Target Audience:')
pdf.body_text('Finance Ops teams, RevOps, Sales Finance, Growth teams')
pdf.sub_title('Why this topic matters:')
pdf.body_text('The gap between signed contract and paid invoice is where cash flow dies. This post addresses a practical, cross-functional pain point that finance ops teams feel daily.')
pdf.ln(2)
pdf.body_text('The deal is signed. High fives all around.')
pdf.body_text('Then the invoice sits unpaid for 47 days.')
pdf.ln(1)
pdf.body_text('Here is what finance teams know that sales teams do not:')
pdf.ln(1)
pdf.bold_text('The collection conversation is just as important as the closing conversation.')
pdf.ln(1)
pdf.bold_text('Best practice I have seen from top finance ops teams:')
pdf.ln(1)
pdf.bullet('Send the invoice within 2 hours of signing. Not 2 days. Momentum matters. Every hour of delay costs you 0.5 days in DSO.')
pdf.bullet('Include a payment reminder schedule in the welcome email. "We will send a reminder on day 15, day 30, and day 45 - unless you want a different cadence." Sets expectations. Reduces friction.')
pdf.bullet('Call before you email. A 2-minute phone call on day 20 resolves what 6 email threads cannot. Tone is everything.')
pdf.bullet('Offer incentives for early payment. A 2% discount for payment within 10 days beats chasing invoices for 60 days. Math works every time.')
pdf.ln(1)
pdf.body_text('The best finance teams do not just track cash. They accelerate it.')
pdf.body_text('And sometimes the biggest improvement is not a new tool. It is a new conversation.')
pdf.ln(2)
pdf.italic_text('What is your best tip for getting paid faster?')

# ========== SUMMARY ==========
pdf.ln(4)
pdf.section_title('Summary')
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(40, 40, 40)
col_w = [12, 50, 68, 60]
pdf.set_fill_color(26, 26, 46)
pdf.set_text_color(255, 255, 255)
pdf.cell(col_w[0], 7, '#', border=1, align='C', fill=True)
pdf.cell(col_w[1], 7, 'Post', border=1, align='C', fill=True)
pdf.cell(col_w[2], 7, 'Target Audience', border=1, align='C', fill=True)
pdf.cell(col_w[3], 7, 'Core Topic', border=1, align='C', fill=True, new_x="LMARGIN", new_y="NEXT")

pdf.set_text_color(40, 40, 40)
rows = [
    ['1', 'Post 1', 'AP teams, Controllers', 'Cost of manual AP processing & strategic reframe'],
    ['2', 'Post 2', 'CFOs, FP&A', 'Leading Burn Ratio as predictive metric'],
    ['3', 'Post 3', 'Finance Ops, RevOps', 'Post-sale payment acceleration tactics'],
]
for i, row in enumerate(rows):
    pdf.set_font('Helvetica', '', 9)
    if i % 2 == 0:
        pdf.set_fill_color(240, 242, 245)
    else:
        pdf.set_fill_color(255, 255, 255)
    for j, cell in enumerate(row):
        pdf.cell(col_w[j], 7, cell, border=1, align='C' if j == 0 else 'L', fill=True)
    pdf.new_x = "LMARGIN"
    pdf.new_y = "NEXT"

output_path = '/Users/tejeswarreddy/Downloads/ROR Challange/volopay-submission/task-1-linkedin-posts.pdf'
pdf.output(output_path)
print(f"PDF saved to: {output_path}")