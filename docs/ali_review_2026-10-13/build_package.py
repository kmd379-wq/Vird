from pathlib import Path
import json,re,html,zipfile
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
root=Path(__file__).parent
reg=json.loads((root/'registry.json').read_text(encoding='utf8'))
ru=['Автономная розничная экосистема с динамическим ценообразованием на основе ИИ и биометрическим контролем доступа к товарам с ограничениями','Система биометрического управления запасами и динамического ценообразования по свежести','Модульный интеллектуальный торговый шкаф с режимом осмотра через смарт-стекло, ручным извлечением с объединением данных датчиков и динамическим ценообразованием по качеству','Интеллектуальный торговый шкаф с токенизированным доступом и разделением платежей','Интеллектуальный торговый шкаф с токенизированным доступом и разделением платежей','Модульная розничная система с адаптивной архитектурой, ценообразованием на основе ИИ и интегрированным управлением расходными материалами','Модульная розничная система с адаптивной архитектурой, ценообразованием на основе ИИ и интегрированным управлением расходными материалами','Интеллектуальная система контроля качества и динамического ценообразования весовой плодоовощной продукции','Автономная розничная платформа с управлением на основе проверенной обратной связи','Система сквозного контроля тары']
for r in reg:
 r['title']=r['title'].replace('AI- DRIVEN','AI-DRIVEN')
 r['iso']=datetime.strptime(r['date'],'%m/%d/%Y').strftime('%Y-%m-%d')
en='\n\n'.join(f"### PPA #{r['ppa']} — US {r['number']}\nFiling date: {r['iso']}.\n\nTitle: {r['title']}." for r in reg)
rus='\n\n'.join(f"### PPA №{r['ppa']} — US {r['number']}\nДата подачи: {r['iso']}.\n\nНазвание в USPTO: {r['title']}.\n\nПеревод названия: {ru[r['ppa']-1]}." for r in reg)
for p in root.glob('0*.md'):
 t=p.read_text(encoding='utf8').replace('[[SCHEDULE_A_EN]]',en).replace('[[SCHEDULE_A_RU]]',rus)
 if p.name=='02_Assignment_EN.md' and '## Schedule A' not in t:t=t.replace('### PPA #1 —','## Schedule A — Assigned applications\n\n### PPA #1 —',1)
 if p.name=='03_Assignment_RU.md' and '## Приложение А' not in t:t=t.replace('### PPA №1 —','## Приложение А — Передаваемые заявки\n\n### PPA №1 —',1)
 t=t.replace('[street, building and apartment], Sharjah','Flat 503, Plot 70, Sharjah Main City').replace('[full address], Sharjah','Flat 503, Plot 70, Sharjah Main City')
 t=t.replace('[улица, дом и квартира], Sharjah','квартира 503, участок 70, Sharjah Main City').replace('[полный адрес], Sharjah','квартира 503, участок 70, Sharjah Main City')
 t=t.replace('а также дополнить личный адрес','а также уточнить написание района в подтверждении личного адреса')
 t=t.replace('Текущее проживание в Sharjah, UAE подтверждено Михаилом в чате; улица, дом и квартира пока не найдены в проверенных материалах.','В письме Михаила «Мой актуальный адрес» от 7 октября 2026 года найдено изображение счёта SEWA: Flat 503, Plot 70, Sharjah Main City, UAE. Эти реквизиты внесены в договор. Поле района в самом источнике напечатано «AL NABBA?AH»; его написание нужно уточнить. Al Jazzat указан как филиал (Branch), а не как район проживания. Название улицы или здания не выдумывается. Счёт за 2024 год используется вместе с подтверждением актуальности адреса самим Михаилом в октябре 2026 года, а не как новое подтверждение налогового резидентства.')
 p.write_text(t,encoding='utf8')
p=root/'04_Corporate_and_Execution_Packet_EN_RU.md'
t=p.read_text(encoding='utf8')
if '## Attached Schedule A' not in t:p.write_text(t+'\n\n## Attached Schedule A — to Document 4 / Приложение А к документу 4\n\n'+rus+'\n',encoding='utf8')
receipt=['2026-01-09','2026-01-23','2026-07-29','2026-02-05','2026-02-13','2026-02-24','2026-03-13','2026-08-06','2026-08-20','2026-09-18']
docs=['APP.TEXT 7; SPEC 5; CLM 2; DRW 4; TR.PROV 3; MES.GIB 2; ABST 1; N417 2; ADS 5; N417.PYMT 2; SCORE 1','SPEC 7; ADS 5; N417 2; MES.GIB 2; DRW 3; N417.PYMT 2; TR.PROV 3; SCORE 1','APP.TEXT 12; DRW 4; SPEC 7; CLM 5; ABST 1; TR.PROV 3; ADS 5; MES.GIB 2; N417 2; N417.PYMT 2; SCORE 1','ADS 5; N417.PYMT 2; DRW 4; TR.PROV 3; SPEC 12; MES.GIB 2; N417 2; SCORE 1','N417 2; ADS 5; MES.GIB 2; TR.PROV 3; N417.PYMT 2; SPEC 12; DRW.NONBW 4; SCORE 1','ADS 5; MES.GIB 2; TR.PROV 3; SPEC 8; N417 2; N417.PYMT 2; DRW.NONBW 1; DRW 3; SCORE 1','ADS 5; SPEC 9; MES.GIB 2; TR.PROV 3; DRW 4; N417 2; N417.PYMT 2; SCORE 1','ADS 5; MES.GIB 2; DRW 7; SPEC 14; N417.PYMT 2; TR.PROV 3; N417 2','ADS 5; SPEC 19; N417 2; TR.PROV 3; MES.GIB 2; N417.PYMT 2','ADS 5; MES.GIB 2; TR.PROV 3; SPEC 17; N417 2; N417.PYMT 2']
gloss={'APP.TEXT':'структурированный текст заявки','SPEC':'описание изобретения','CLM':'формула изобретения','DRW':'чёрно-белые линейные чертежи','DRW.NONBW':'чертежи иной категории, не только чёрно-белые линейные','TR.PROV':'сопроводительный лист предварительной заявки SB16','MES.GIB':'удостоверение статуса микропредприятия по критерию дохода','ABST':'реферат','N417':'электронное подтверждение приёма документов','ADS':'информационный лист заявки','N417.PYMT':'электронное подтверждение оплаты пошлины','SCORE':'сопутствующая запись репозитория SCORE; содержание проверяется по самому документу'}
out=['# Реестр PPA №1–10 и перевод индексов USPTO','Источник: десять Patent Center Index PDF из архива Ali от 9 октября 2026 года. Это перевод содержательных реквизитов и списка документов, без элементов навигации сайта. Даты подачи записаны как ГГГГ-ММ-ДД. Русские названия — рабочий перевод, официальные английские названия сохранены.','Индексы показывают наличие документов, но не содержат сами описания, чертежи или квитанции. Размер файла в KB не является суммой пошлины. Статус в снимках: «Передано из предварительной обработки, ещё не распределено»; это не проверка текущего статуса на дату подготовки отчёта.']
for i,r in enumerate(reg):
 out += [f"## PPA №{r['ppa']} — {r['number']}",f"Дата подачи: {r['iso']}. Название: {r['title']}.",f'Перевод: {ru[i]}.',f'Уведомление о подаче APP.FILE.REC: {receipt[i]}, 3 страницы. В ту же дату: WELCOME.LET — приветственное письмо руководства USPTO, 1 страница; OA.EMAIL — уведомление электронной почтой, 1 страница. Это даты выдачи документов, а не новые даты приоритета.']
 for item in docs[i].split('; '):
  code,n=item.split(' ');out.append(f'- {code}: {gloss[code]}; страниц: {n}.')
 if i==0:out.append('Отдельно найдена ранее полученная квитанция N417.PYMT: 65 USD, 11 декабря 2025 года. Она сохранена в папке оригиналов. Не прибавлять пошлину повторно к счёту, уже включающему её.')
 if i==8:out.append('Отдельных DRW в индексе нет. Ali 6 октября сообщил, что FIGS. 1–8 не были поданы; описание рисунков не заменяет сами рисунки.')
 if i==9:out.append('Отдельных DRW в индексе нет. По письму Ali от 6 октября, FIGS. 1–4 находятся на страницах 14–17 SPEC. Проверять по поданному SPEC.')
(root/'05_Registry_and_Index_Translation_RU.md').write_text('\n\n'.join(out),encoding='utf8')
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialB','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='ArialB',italic='Arial',boldItalic='ArialB')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyX',fontName='Arial',fontSize=10.2,leading=14.4,spaceAfter=7,splitLongWords=True))
for n,size in [('TitleX',20),('H2X',14),('H3X',11.5)]:styles.add(ParagraphStyle(name=n,fontName='ArialB',fontSize=size,leading=size*1.25,spaceBefore=12,spaceAfter=8,keepWithNext=True))
def footer(c,d):
 c.saveState();c.setFont('Arial',8);c.setFillColor(colors.HexColor('#666666'));c.drawString(43,25,'PBK / Mikhail Kozin • 13.10.2026 • Draft / Проект');c.drawRightString(A4[0]-43,25,str(d.page));c.restoreState()
qa=root/'qa'/'final';qa.mkdir(parents=True,exist_ok=True)
imgs=[];counts={}
for p in sorted(root.glob('0*.md')):
 story=[]
 raw=p.read_text(encoding='utf8')
 raw=re.sub(r'(?m)^(#{1,3} .+)\n(?!\n)',r'\1\n\n',raw)
 for block in re.split(r'\n\s*\n',raw):
  block=block.strip()
  if not block:continue
  style='BodyX'
  if block.startswith('# '):style='TitleX';block=block[2:]
  elif block.startswith('## '):style='H2X';block=block[3:]
  elif block.startswith('### '):style='H3X';block=block[4:]
  if p.name.startswith(('02_','03_')) and style=='H2X' and block.startswith(('Schedule ','Приложение ')):story.append(PageBreak())
  txt=html.escape(block).replace('\n','<br/>')
  txt=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',txt)
  story.append(Paragraph(txt,styles[style]))
 pdf=p.with_suffix('.pdf');SimpleDocTemplate(str(pdf),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=38,bottomMargin=43,title=p.stem,author='Prepared for Mikhail Kozin').build(story,onFirstPage=footer,onLaterPages=footer)
 counts[pdf.name]=len(PdfReader(str(pdf)).pages)
 doc=pdfium.PdfDocument(str(pdf))
 for i,page in enumerate(doc):
  dest=qa/(p.stem+f'_{i+1:02}.png');page.render(scale=1.3).to_pil().save(dest);imgs.append(dest)
for k in range(0,len(imgs),4):
 sheet=Image.new('RGB',(1600,2300),'#dddddd');draw=ImageDraw.Draw(sheet)
 for j,p in enumerate(imgs[k:k+4]):
  im=Image.open(p);im.thumbnail((785,1090));x=(j%2)*800;y=(j//2)*1150;sheet.paste(im,(x,y+35));draw.text((x+5,y+8),p.stem,fill='black')
 sheet.save(qa/f'contact_{k//4+1:02}.jpg')
(root/'pdf_page_counts.json').write_text(json.dumps(counts,indent=2),encoding='utf8')
print(json.dumps(counts,indent=2))
