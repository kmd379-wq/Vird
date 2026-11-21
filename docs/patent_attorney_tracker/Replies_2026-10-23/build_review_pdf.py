import re
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from pypdf import PdfReader
B=Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont('ReviewArial',r'C:\Windows\Fonts\arial.ttf'));pdfmetrics.registerFont(TTFont('ReviewArialBold',r'C:\Windows\Fonts\arialbd.ttf'))
pdfmetrics.registerFontFamily('ReviewArial',normal='ReviewArial',bold='ReviewArialBold',italic='ReviewArial',boldItalic='ReviewArialBold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='ReviewBody',fontName='ReviewArial',fontSize=10.5,leading=15,spaceAfter=8))
styles.add(ParagraphStyle(name='ReviewTitle',fontName='ReviewArialBold',fontSize=20,leading=25,spaceAfter=14,textColor=colors.HexColor('#164f53')))
styles.add(ParagraphStyle(name='ReviewH2',fontName='ReviewArialBold',fontSize=15,leading=19,spaceBefore=16,spaceAfter=9,keepWithNext=True))
styles.add(ParagraphStyle(name='ReviewH3',fontName='ReviewArialBold',fontSize=12,leading=16,spaceBefore=11,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='ReviewBullet',fontName='ReviewArial',fontSize=10.5,leading=15,leftIndent=13,firstLineIndent=-10,spaceAfter=6))
def markup(s):
    s=escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'https://[^\s<>]+',lambda m:f'<link href="{m.group(0)}" color="#235b74">{m.group(0)}</link>',s)
    return s
story=[]
for block in (B.parent/'REPLIES_2026-10-23_RU.md').read_text(encoding='utf-8').split('\n\n'):
    block=block.strip()
    if not block:continue
    if block.startswith('### '):story.append(Paragraph(markup(block[4:]),styles['ReviewH3']))
    elif block.startswith('## '):story.append(Paragraph(markup(block[3:]),styles['ReviewH2']))
    elif block.startswith('# '):story.append(Paragraph(markup(block[2:]),styles['ReviewTitle']))
    elif block.startswith('- ') or re.match(r'\d+\. ',block):
        for line in block.splitlines():story.append(Paragraph(markup(line),styles['ReviewBullet']))
    else:story.append(Paragraph(markup(block.replace('\n',' ')),styles['ReviewBody']))
def footer(c,d):
    c.setFont('ReviewArial',8);c.setFillColor(colors.HexColor('#626c72'));c.drawString(48,25,'23.10.2026 | Переписка по PPA / NPPA / PCT | Конфиденциально');c.drawRightString(A4[0]-48,25,str(d.page))
out=B/'MAIL_REVIEW_2026-10-23_RU.pdf'
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=44,title='Новые патентные письма - перевод и анализ 23.10.2026',author='Mikhail Kozin / working review').build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(out)
for page in reader.pages:assert len(page.extract_text())>80
print('Pages:',len(reader.pages));print('Bytes:',out.stat().st_size)
