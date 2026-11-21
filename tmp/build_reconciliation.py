from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from email.message import EmailMessage
from email.policy import SMTP
import json
base=Path(r"C:/Users/kmd37/Projects/vird/docs/patent_attorney_tracker/Replies_2026-10-24")
pdf=base/"PBK_Kozin_Reconciliation_21828_EN.pdf"
s=getSampleStyleSheet()
s.add(ParagraphStyle(name="BodyCustom",fontName="Helvetica",fontSize=10,leading=14,spaceAfter=8))
s.add(ParagraphStyle(name="CellCustom",fontName="Helvetica",fontSize=8,leading=10))
s.add(ParagraphStyle(name="SmallCustom",fontName="Helvetica",fontSize=8.5,leading=11,spaceAfter=6))
s["Title"].fontName="Helvetica-Bold";s["Title"].fontSize=19;s["Title"].leading=23
story=[]
def p(t,style="BodyCustom"): return Paragraph(t,s[style])
def add(t,style="BodyCustom"): story.append(p(t,style))
def table(data,widths):
 t=Table([[p(str(c),"CellCustom") for c in row] for row in data],colWidths=widths,repeatRows=1)
 t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#e8edf1")),("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#bfc6cc")),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
 story.append(t);story.append(Spacer(1,10))
add("Statement of reconciliation of personally funded patent expenses","Title")
add("As of 25 October 2026 | Draft for review and confirmation","SmallCustom")
add("<b>Parties:</b> Mikhail Kozin and PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO, licence No. 38769.")
add("This statement records patent-related payments personally funded by Mikhail Kozin for review against PBK's accounting records in connection with the proposed assignment of interests in US provisional patent applications PPA 1-10 and associated priority rights.")
add("<b>Reconciled payment total: USD 21,828.</b> Schedule A forms part of this statement. The amount is the corrected payment total submitted by Mikhail Kozin; PBK's recognition of a payable and any assignment-based settlement remain subject to its accounting and corporate review.")
table([["Category","USD"],["PPA 1-10 preparation and filing, including NDA work within the PPA 4 payment","10,828"],["Three patent searches","4,600"],["Advance for unfinished preparation of NPPA 1","6,400"],["TOTAL","21,828"]],[420,91])
add("Corrections and work status","Heading2")
add("<b>PPA 10:</b> Mikhail Kozin confirms that the first payment attempt through the first bank failed and one payment of USD 765 succeeded after another invoice was issued. The failed attempt is excluded. The earlier total of USD 22,593 is reduced by USD 765. This adjustment does not represent a refund.")
add("Records show invoices 00624 and 00620 and document dates of 1 and 6 August 2026. The clarification does not independently identify the final bank settlement date or allocate the failed attempt to a particular invoice. Accordingly, Schedule A records both document references and only one USD 765 payment.","SmallCustom")
add("<b>NPPA 1:</b> USD 6,400 is an advance for preparation and filing work combining PPA 3-7. Ali Shalchi supplied a work report, but the work was not completed, as confirmed by Mikhail Kozin. The reported scope corresponds to the advance according to Mikhail Kozin; this is not confirmation of a completed filing.")
add("Basis and confirmation","Heading2")
add("Based on retained invoices and receipts, correspondence with Ali Shalchi, saved USPTO filing records and Mikhail Kozin's clarification of 25 October 2026. Separate unverified bank or platform charges, currency conversion and unpaid future services are excluded. No rights transfer, set-off, release or acknowledgement of satisfactory completion is effected by this statement.","SmallCustom")
add("Mikhail Kozin: ____________________  Date: ______________","SmallCustom")
add("For PBK, following accounting review: ____________________","SmallCustom")
add("Name and capacity: ____________________  Date: ______________","SmallCustom")
story.append(PageBreak())
add("Schedule A Payment register","Title")
add("All amounts in USD. Dates are receipt dates unless otherwise noted.","SmallCustom")
rows=[
["09 Dec 2025","00419","PPA 1 - initial payment","891","11 Dec 2025"],
["10 Dec 2025","00426","PPA 1 - balance and additional work","777","11 Dec 2025"],
["13 Dec 2025","00430","Produce Vision patent search","1,100","Not a filing"],
["15 Dec 2025","00432","PPA 2","1,600","19 Dec 2025"],
["19 Dec 2025","00438","PPA 3","800","23 Dec 2025"],
["04 Jan 2026","00443","PPA 4 and NDA","900","06 Jan 2026"],
["12 Jan 2026","00449","PPA 5","800","13 Jan 2026"],
["15 Jan 2026","00453","PPA 6","865","16 Jan 2026"],
["03 Feb 2026","00460","PPA 7","965","04 Feb 2026"],
["25 Apr 2026","00524","Prior-art search - two agreed groups","1,000","Not a filing"],
["19 May 2026","SLPC1","Patent search - six features; direct payment","2,500","Not a filing"],
["08 Jun 2026","SLPC2","PPA 8; direct payment","1,500","14 Jun 2026"],
["30 Jun 2026","00610","PPA 9","965","07 Jul 2026"],
["01 / 06 Aug 2026*","00624 / 00620","PPA 10 - one successful payment","765","04 Aug 2026"],
["09 Sep 2026","00654","NPPA 1 - advance; work unfinished","6,400","Filing not confirmed"],
["TOTAL","","15 payments included","21,828",""]]
assert sum(float(r[3].replace(",","")) for r in rows[:-1])==21828
table([["Payment / record date","Invoice","Purpose","USD","USPTO filing date"]]+rows,[77,65,201,55,113])
add("* PPA 10: both document dates are retained; only one successful payment is counted. See the clarification on page 1.","SmallCustom")
add("PPA 1 total: USD 1,668 (USD 1,318 plus USD 350 for additional work). PPA 4 includes NDA work without an agreed separate allocation. PPA 6 is matched through the receipt and filing correspondence.","SmallCustom")
add("Payment channels: USD 17,828 through UpCounsel and USD 4,000 directly. Ali's receipt of the NPPA 1 funds on 14 September does not represent another payment.","SmallCustom")
add("Filing dates come from saved USPTO Patent Center records, not the later issue dates of filing receipts. This schedule is a payment reconciliation, not an independent bank audit or confirmation that all charged work was completed.","SmallCustom")
def footer(c,d):
 c.setFont("Helvetica",8);c.drawString(42,25,"PBK and Mikhail Kozin | Reconciliation as of 25 October 2026")
 c.drawRightString(A4[0]-42,25,str(d.page))
SimpleDocTemplate(str(pdf),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=35,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
letter=(base/"UAE_ADVISER_REQUEST_EN.txt").read_text(encoding="utf-8-sig")
old="The register records 16 payments personally funded by me, totalling USD 22,593. This includes an advance of USD 6,400 paid to Ali Shalchi. I confirm that the scope of work in his submitted report corresponds to that advance; this payment is not to be treated as disputed for purposes of this review."
new="Please use the attached Statement of Reconciliation and Schedule A, which record 15 payments personally funded by me, totalling USD 21,828, replacing the earlier total of USD 22,593. For PPA #10, the first payment attempt through the first bank failed; one payment of USD 765 succeeded after another invoice was issued. Only one payment is included.\n\nThe total consists of USD 10,828 for PPA #1-10 and associated NDA work, USD 4,600 for patent searches, and USD 6,400 advanced to Ali Shalchi for preparation and filing work on NPPA #1. Ali supplied a work report, but did not complete that work. I confirm that the reported scope corresponds to the advance; this amount is not being treated as disputed for this review. Please record it as an advance for unfinished work, not as payment for a completed filing."
assert old in letter
letter=letter.replace(old,new).replace("I will provide the draft documents with the application schedule, Michael's comments and the payment register with supporting records. Please identify any further materials needed beyond those already in your records.","Attached: PBK_Kozin_Reconciliation_21828_EN.pdf (Statement of Reconciliation and Schedule A). Please review and confirm or amend the reconciliation against PBK's records.\n\nI will provide the draft assignment documents, application schedule, Michael's comments and supporting payment records as needed. Please identify any further materials required beyond those already in your records.")
(base/"UAE_ADVISER_REQUEST_EN.txt").write_text(letter,encoding="utf-8")
(base/"UAE_ADVISER_EMAIL_UPDATED_21828_EN.txt").write_text(letter,encoding="utf-8")
msg=EmailMessage(policy=SMTP)
msg["Subject"]=letter.splitlines()[0].removeprefix("Subject: ")
msg["X-Unsent"]="1"
msg.set_content(letter.split("\n\n",1)[1])
msg.add_attachment(pdf.read_bytes(),maintype="application",subtype="pdf",filename=pdf.name)
(base/"UAE_ADVISER_EMAIL_WITH_ATTACHMENT_EN.eml").write_bytes(bytes(msg))
print(pdf)

