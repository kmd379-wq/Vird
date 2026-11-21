from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
import re

base=Path(__file__).parent
pdfmetrics.registerFont(TTFont('ArialReview',r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialReviewBold',r'C:\Windows\Fonts\arialbd.ttf'))
pdfmetrics.registerFontFamily('ArialReview',normal='ArialReview',bold='ArialReviewBold')
styles={
 'body':ParagraphStyle('body',fontName='ArialReview',fontSize=10,leading=14,spaceAfter=8,splitLongWords=True),
 'heading':ParagraphStyle('heading',fontName='ArialReviewBold',fontSize=13,leading=17,spaceBefore=14,spaceAfter=9,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='ArialReviewBold',fontSize=19,leading=24,spaceAfter=15),
}
story=[]
for i,p in enumerate(base.joinpath('REVIEW_MICHAEL_PBK_RU.txt').read_text(encoding='utf-8').split('\n\n')):
 kind='title' if i==0 else 'heading' if re.match(r'^\d+\. [^\n]+$',p) or p.startswith('Официальные источники') else 'body'
 story.append(Paragraph(escape(p).replace('\n','<br/>'),styles[kind]))
def footer(c,d):
 c.setFont('ArialReview',8);c.setFillColor(colors.HexColor('#555555'))
 c.drawString(42,25,'MICHAEL / PBK · 24.10.2026 · Для обсуждения, не для подписи')
 c.drawRightString(553,25,str(d.page))
out=base/'REVIEW_MICHAEL_PBK_RU.pdf'
SimpleDocTemplate(str(out),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=44,title='Michael / PBK: стоимость и подготовка уступки',author='Обзор документов для Михаила Козина').build(story,onFirstPage=footer,onLaterPages=footer)
from pypdf import PdfReader
r=PdfReader(out)
print(f'Created {out.name}: {len(r.pages)} pages')
assert len(PdfReader(base/'Kozin_Scope_and_Fee_Proposal_2026-10-23.pdf').pages)==18
assert 15250+2100+800+7050==25200
assert 15250+2100+1600+8300==27250
assert 26450+2000+500==28950
assert 27250+4000+1500==32750
