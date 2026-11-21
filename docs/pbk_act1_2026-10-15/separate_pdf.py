from pathlib import Path
import re,json
from datetime import datetime
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader
base=Path(__file__).resolve().parent;source=base/'assignment_execution';out=base/'pdf_signing';out.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','C:/Windows/Fonts/arialbd.ttf'))
r=(source/'01_PBK_Corporate_Resolution_EN_RU.md').read_text(encoding='utf8')
a=(source/'02_Patent_Assignment_EN_RU.md').read_text(encoding='utf8')
company='PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO'
en_sig='Mikhail Kozin\n\nSignature __________________________\n\nDate: 15 October 2026'
ru_sig='Михаил Козин\n\nПодпись __________________________\n\nДата: 15 октября 2026 года'
ren='# PBK Corporate Resolution 1\n\nDate of adoption: 15 October 2026.\n\nCompany: '+company+'. Licence No. 38769. IFZA Dubai. Registered office: IFZA Business Park, DDP, P.O. Box 342001, Dubai, United Arab Emirates.\n\n'
ren+=r.split('## Part I Sole shareholder written ordinary resolution')[1].split('Sole shareholder:')[0].join(['## Part I Sole shareholder written ordinary resolution',''])
ren+='\n\nSole shareholder\n\n'+en_sig+'\n\n## Part II Sole director implementation decision\n\n'+r.split('## Part II Sole director implementation decision')[1].split('## Часть II')[0].strip()+'\n\nDirector / General Manager\n\n'+en_sig
rru='# Корпоративное решение PBK №1\n\nДата принятия: 15 октября 2026 года.\n\nКомпания: '+company+'. Лицензия №38769. Свободная зона IFZA, Дубай, ОАЭ. Зарегистрированный офис: IFZA Business Park, DDP, почтовый ящик 342001, Дубай, Объединённые Арабские Эмираты.\n\n'
rru+='## Часть I Письменное решение единственного участника\n\n'+r.split('## Часть I Русская редакция решения участника')[1].split('Подпись в Части I выше')[0].strip()+'\n\nЕдинственный участник\n\n'+ru_sig
rru+='\n\n## Часть II Решение единственного директора об исполнении\n\n'+r.split('## Часть II Решение единственного директора об исполнении')[1].split('Director / Директор:')[0].strip()+'\n\nДиректор\n\n'+ru_sig
ren+='\n\nThe separately prepared English and Russian versions record the same resolution. English controls inconsistencies, subject to mandatory law.'
rru+='\n\nОтдельно подготовленные английская и русская редакции отражают одно решение. При расхождениях применяется английский текст с учётом обязательных норм.'
aen=a.split('---PAGE---')[0].replace('\n\nДоговор уступки патентных прав №1','')
aen=aen.replace('Prepared 15 October 2026. Effective on the date of the last party signature below, after adoption of Corporate Resolution No. 1 and confirmation of the signatory\'s authority. No retrospective transfer is intended.','Dated 15 October 2026. Effective upon execution by both parties on 15 October 2026, after adoption of Corporate Resolution No. 1 and confirmation of the signatory’s authority. No retrospective transfer is intended.')
aru='# Договор уступки патентных прав №1\n\n'+a.split('## Русская редакция')[1].split('---PAGE---')[0].strip()
aru=aru.replace('Подготовлено 15 октября 2026 года. Договор действует с даты последней подписи сторон после принятия корпоративного решения №1 и подтверждения полномочий подписанта. Передача задним числом не предусматривается.','Дата договора: 15 октября 2026 года. Договор вступает в силу при подписании обеими сторонами 15 октября 2026 года после принятия корпоративного решения №1 и подтверждения полномочий подписанта. Передача задним числом не предусматривается.')
aen=aen.replace('The English and Russian texts constitute one instrument; English controls an inconsistency subject to mandatory law.','The separately prepared English and Russian versions express the same agreement and do not effect two transfers. English controls an inconsistency subject to mandatory law.')
aru=aru.replace('Английская и русская редакции составляют один документ; при расхождениях применяется английская редакция с учётом обязательных норм.','Отдельно подготовленные английская и русская редакции выражают один договор и не оформляют две уступки. При расхождениях применяется английская редакция с учётом обязательных норм.')
aen+='\n\n## Signatures\n\nFor '+company+'\n\nDirector / General Manager\n\n'+en_sig+'\n\nPersonally as assignee and settling creditor\n\n'+en_sig+'\n\n---PAGE---\n\n## Schedule A Assigned applications\n\n'
aru+='\n\n## Подписи сторон\n\nЗа '+company+'\n\nДиректор\n\n'+ru_sig+'\n\nЛично как приобретатель и кредитор\n\n'+ru_sig+'\n\n---PAGE---\n\n## Приложение А Передаваемые заявки\n\n'
reg=json.loads((base.parent/'ali_review_2026-10-13/registry.json').read_text(encoding='utf8'))
old=(base.parent/'pbk_execution_2026-10-14/02_Assignment_RU.md').read_text(encoding='utf8')
translations=re.findall(r'Перевод названия: (.+)',old)
assert len(translations)==10
for i,x in enumerate(reg):
 aen+=f'PPA #{x["ppa"]} — US {x["number"]}\nFiling date: {datetime.strptime(x["date"],"%m/%d/%Y").strftime("%d %B %Y")}\n{x["title"].replace("AI- DRIVEN","AI-DRIVEN")}\n\n'
 aru+=f'Предварительная заявка №{x["ppa"]} — US {x["number"]}\nДата подачи: {datetime.strptime(x["date"],"%m/%d/%Y").strftime("%d.%m.%Y")}\n{translations[i]}\n\n'
aru+='Названия приведены в русском переводе; идентификация заявок осуществляется по официальным номерам США и датам подачи. Исходные английские названия приведены в английской редакции договора.'
for key,text in [('01_Corporate_Resolution_RU',rru),('02_Corporate_Resolution_EN',ren),('03_Patent_Assignment_RU',aru),('04_Patent_Assignment_EN',aen)]:
 ru=key.endswith('RU')
 if ru:
  text=text.replace('директор / General Manager','директор').replace('директора / General Manager','директора').replace('Михаил Козин / Mikhail Kozin','Михаил Козин').replace('Flat 503, Plot 70, Sharjah Main City, United Arab Emirates','квартира 503, участок 70, Шарджа, Объединённые Арабские Эмираты').replace('email','электронная почта').replace('USD','долларов США')
  text=text.replace('зарегистрированный офис IFZA Business Park, DDP, P.O. Box 342001, Dubai, United Arab Emirates','зарегистрированный офис IFZA Business Park, DDP, почтовый ящик 342001, Дубай, Объединённые Арабские Эмираты')
 styles={'Normal':ParagraphStyle('Normal',fontName='Arial',fontSize=11,leading=13,spaceAfter=7), 'Title':ParagraphStyle('Title',fontName='ArialBold',fontSize=17,leading=21,spaceAfter=14), 'Heading':ParagraphStyle('Heading',fontName='ArialBold',fontSize=12,leading=15,spaceBefore=10,spaceAfter=8,keepWithNext=True)}
 story=[]
 blocks=re.split(r'\n\s*\n',text.strip())
 for b in blocks:
  if b=='---PAGE---':story.append(PageBreak());continue
  sty='Normal'
  if b.startswith('## '):b=b[3:];sty='Heading'
  elif b.startswith('# '):b=b[2:];sty='Title'
  st=styles[sty]
  if b in ['Mikhail Kozin','Михаил Козин','Director / General Manager','Директор','Sole shareholder','Единственный участник','Personally as assignee and settling creditor','Лично как приобретатель и кредитор'] or b.startswith(('For PBK','За PBK','Signature _','Подпись _')):
   st=ParagraphStyle('sign',parent=st,keepWithNext=True)
  story.append(Paragraph(escape(b).replace('\n','<br/>'),st))
 def footer(c,d):
  c.setFont('Arial',8);c.drawString(45,22,('15 октября 2026 года' if ru else '15 October 2026'));c.drawRightString(567,22,str(d.page))
 SimpleDocTemplate(str(out/(key+'.pdf')),pagesize=letter,leftMargin=45,rightMargin=45,topMargin=40,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
 (out/(key+'.txt')).write_text(text,encoding='utf8')
 pdf=PdfReader(out/(key+'.pdf'));alltext='\n'.join(p.extract_text() for p in pdf.pages)
 assert ('22 593' in alltext or '22,593' in alltext)
 if 'Assignment' in key:
  assert all(x['number'] in alltext for x in reg)
 if not ru:assert not re.search('[А-Яа-я]',alltext)
 print(key,len(pdf.pages))
