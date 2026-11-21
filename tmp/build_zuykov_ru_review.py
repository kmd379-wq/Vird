from pathlib import Path
import json,zipfile,io,re,shutil,hashlib,xml.etree.ElementTree as ET
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
from xml.sax.saxutils import escape
root=Path(r'C:/Users/kmd37/Projects/vird')
out=root/'docs/patent_attorney_tracker/ZUYKOV_RU_PRICING_2026-10-26'
pack=out/'RU_REVIEW';pack.mkdir(exist_ok=True)
cfg=json.loads((root/'tmp/zuykov_pricing_ru.json').read_text(encoding='utf-8'))
z=zipfile.ZipFile(root/'docs/patent_attorney_tracker/ZUYKOV_PACKAGE_2026-10-23/ZUYKOV_PPA1-10_ALI_NPPA1_REVIEW.zip')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def docxtext(data):
 x=ET.fromstring(zipfile.ZipFile(io.BytesIO(data)).read('word/document.xml'))
 return '\n'.join(''.join(p.itertext()) for p in x.findall('.//w:p',ns))
records=[]
numbers=['63/938,244','63/945,513','63/947,909','63/955,179','63/959,439','63/961,839','63/975,643','64/090,283','64/106,825','64/125,577']
dates=['11.12.2025','19.12.2025','23.12.2025','06.01.2026','13.01.2026','16.01.2026','04.02.2026','14.06.2026','07.07.2026','04.08.2026']
for n in range(1,11):
 paths=[x for x in z.namelist() if f'/PPA_{n:02}/' in x]
 doc=next(x for x in paths if x.endswith('.docx'))
 text=docxtext(z.read(doc)); pdfs=[x for x in paths if x.lower().endswith('.pdf') and '/SPEC_' in x and 'APP.FILE' not in x]
 pages=sum(len(PdfReader(io.BytesIO(z.read(x))).pages) for x in pdfs)
 figs=[x for x in paths if 'FIGURE' in x.upper()]
 figpages=sum(len(PdfReader(io.BytesIO(z.read(x))).pages) for x in figs)
 records.append({'n':n,'number':numbers[n-1],'date':dates[n-1],'words':len(text.split()),'pages':pages,'figure_pages':figpages,'source':doc,'sha256':hashlib.sha256(z.read(doc)).hexdigest()})
ali=next(x for x in z.namelist() if x.endswith('/ALI_NPPA1_Draft_Spec.docx'))
aliwords=len(docxtext(z.read(ali)).split())
ru_src=Path(r'C:/Start-up/23.08.2026.документы на патенты/23.08.2026. 1 пакет документов для патента/Папка PPA#3,#4,#5,#6')
ru_dir=pack/'02_Русские_тексты_PPA_3-7';ru_dir.mkdir(exist_ok=True)
ru_counts=[]
for n in range(3,8):
 p=next(p for p in ru_src.glob('*.docx') if f'PPA#{n}' in p.name and 'яз' in p.name)
 txt=docxtext(p.read_bytes())
 assert len(re.findall('[А-Яа-я]',txt))>100
 shutil.copyfile(p,ru_dir/f'PPA_{n:02}_Русский_текст.docx')
 (ru_dir/f'PPA_{n:02}_Русский_текст.txt').write_text(txt,encoding='utf-8-sig')
 ru_counts.append((n,len(txt.split())))
diag=pack/'03_Схемы_архитектуры_PPA_3-7';diag.mkdir(exist_ok=True)
for n in range(3,8):
 p=root/f'assets/figures/ppa3456/PPA{n}_ARCH_RU.svg'
 raw=p.read_bytes()
 try: svg=raw.decode('utf-8')
 except UnicodeDecodeError: svg=raw.decode('cp1251')
 svg=''.join(c for c in svg if ord(c)>=32 or c in '\n\r\t')
 ET.fromstring(svg)
 (diag/f'PPA_{n:02}_Архитектура_RU.svg').write_text(svg,encoding='utf-8')
pdfmetrics.registerFont(TTFont('AR',r'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ARB',r'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('AR',normal='AR',bold='ARB')
s=getSampleStyleSheet();s.add(ParagraphStyle(name='R',fontName='AR',fontSize=10.5,leading=15,spaceAfter=9));s.add(ParagraphStyle(name='SmallR',fontName='AR',fontSize=8.5,leading=11,spaceAfter=7));s.add(ParagraphStyle(name='HR',fontName='ARB',fontSize=18,leading=22,spaceAfter=14));s.add(ParagraphStyle(name='SubR',fontName='ARB',fontSize=12,leading=16,spaceAfter=8))
story=[]
def add(t,style='R'):story.append(Paragraph(t,s[style]))
def tab(data,widths):
 t=Table([[Paragraph(escape(str(c)),s['SmallR']) for c in row] for row in data],colWidths=widths,repeatRows=1)
 t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.4,colors.lightgrey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e7edf1')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story.append(t);story.append(Spacer(1,10))
add('Материалы для расчёта стоимости патентных работ','HR')
add('Русскоязычный комплект для предварительного просмотра Михаилом Козиным. 26 октября 2026 года. Не отправлен.','SmallR')
add('Объём запроса','SubR')
add('Российская охрана технических решений по PPA №1–10: число и состав российских заявок должен предложить поверенный. Отдельная опция — две PCT: группа №1 (PPA №3–7) и группа №2 (PPA №1, №2, №8, №9). PPA №10 — самостоятельная российская группа; третья PCT не входит в основной расчёт.')
add('Состав и пределы комплекта','SubR')
add('Включены имеющиеся русские тексты PPA №3–7, пять русских схем архитектуры, реестр, технические обзоры десяти PPA, обзор работы Ali и перечень содержания 22 листов его рисунков. Обзоры составлены для оценки трудоёмкости и не являются полными переводами описаний и формул.')
add('<b>Для окончательной сметы комплект ещё требует дополнения:</b> полные русские переводы PPA №1, №2, №8, №9, №10 и проекта Ali, а также проверенные русские версии исходных рисунков. Имеющиеся русские тексты №3–7 также не удостоверены как точные переводы поданных версий. Английские оригиналы в этот русскоязычный архив не включены.')
add('Размеры исходных текстов приведены по доступным Word-файлам; объёмы страниц — по соответствующим PDF. Это оценка входных материалов, а не число страниц будущих заявок. Дублирование признаков между PPA необходимо учесть при цене.')
add('Контрольные даты: 11.12.2026 для группы №2 и 23.12.2026 для группы №1; поверенный должен проверить применимость и запланировать подачу с резервом. По PPA №10 дата подачи — 04.08.2026.')
story.append(PageBreak());add('Реестр и измеренный объём исходников','HR')
tab([['PPA','Номер США','Дата подачи','Слов Word','Страниц описания PDF','Листов отдельного файла рисунков']]+[[r['n'],r['number'],r['date'],r['words'],r['pages'],r['figure_pages']] for r in records],[32,83,73,55,108,160])
add(f'Объединённый проект Ali: {aliwords:,} слов в доступном Word-файле; отдельный PDF содержит 22 листа рисунков. Подготовка не завершена, подача NPPA №1 не подтверждена.'.replace(',', ' '))
add('Ноль отдельных листов для PPA №9 означает отсутствие такого файла в проверенном архиве, а не окончательный вывод об отсутствии любых изображений в официально поданном описании. Рисунки №1–8 перечислены в тексте.','SmallR')
add('Число слов — технический подсчёт элементов текста документа, включая заголовки и формулу. Окончательную базу оплаты переводов согласовать с исполнителем после исключения повторов.','SmallR')
for i,r in enumerate(records):
 story.append(PageBreak());add(f'PPA №{i+1}','HR');add(cfg['titles'][i],'SubR')
 add(f"Номер США: {r['number']}. Подана: {r['date']}. Доступный исходный текст: {r['words']} слов; описание PDF: {r['pages']} стр.; отдельные рисунки: {r['figure_pages']} листов.",'SmallR')
 add('Технический обзор для оценки','SubR');add(cfg['summaries'][i])
 add('Что учитывать в смете','SubR')
 add('Анализ раскрытия и его пересечений с другими PPA; выбор самостоятельных объектов; адаптация описания и формулы к российской процедуре; реферат; графика; проверка приоритетной поддержки; согласование и подача. Число независимых пунктов и будущих заявок пока не установлено.')
 add('Русские приложения','SubR')
 add('В архиве приложены ранее подготовленный русский текст и схема архитектуры. Схема является дополнительным пояснением и не подменяет исходные рисунки.' if 3<=i+1<=7 else 'В текущей редакции представлен русский технический обзор. Полный русский текст описания и формулы, а также проверенная русская графика ещё не включены.')
story.append(PageBreak());add('Незавершённый проект Ali по группе №1','HR');add(cfg['ali'])
add('Что оценить отдельно','SubR');add('Пригодность существующего описания, формулы и графики; необходимый объём переработки; объединение признаков PPA №3–7; возможное разделение аппаратных решений; завершение описания, формулы и реферата; подготовка русской версии и адаптация к каждой выбранной процедуре. Не начислять повторную стоимость общего текста при подготовке российской заявки и PCT.')
add('Это обзор проекта, не его полный русский перевод. Число слов и листов в реестре позволяет предварительно оценить объём, но само по себе не подтверждает достаточность материалов для окончательной цены.','SmallR')
story.append(PageBreak());add('Содержание рисунков проекта Ali','HR')
for i,t in enumerate(cfg['ali_figures'],1):add(f'{i}. {t}','SmallR')
add('Перечень переведён по разделу краткого описания рисунков. Это указатель, а не перевод графических листов.','SmallR')
def footer(c,d):
 c.setFont('AR',8);c.drawString(42,24,'Для просмотра • 26.10.2026 • Не отправлено');c.drawRightString(A4[0]-42,24,str(d.page))
dest=pack/'01_Досье_для_оценки_RU.pdf'
SimpleDocTemplate(str(dest),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
readme='ПАКЕТ ДЛЯ ПРЕДВАРИТЕЛЬНОГО ПРОСМОТРА. НЕ ОТПРАВЛЕН.\n\nСодержимое на русском языке. Полные имеющиеся русские тексты: PPA №3–7. Технические обзоры: PPA №1–10 и работа Ali. Обзоры не являются полными переводами.\n\nДля окончательного технического комплекта не хватает полных русских переводов PPA №1,2,8,9,10, проекта Ali и исходной графики. Имеющиеся русские тексты №3–7 требуют сопоставления с поданными версиями. Пока не представлять этот архив как полный комплект всех заявок.\n\nПовреждённые русские схемы PPA №10 с нечитаемыми подписями не включены.\n\nСогласованное письмо хранится отдельно: фраза о передаче всех материалов применима после завершения комплекта.\n'
(pack/'00_СОСТАВ_И_ГОТОВНОСТЬ_RU.txt').write_text(readme,encoding='utf-8-sig')
manifest=[]
for p in sorted(pack.rglob('*')):
 if p.is_file():manifest.append({'file':p.relative_to(pack).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(out/'INTERNAL_MANIFEST.json').write_text(json.dumps({'files':manifest,'source_statistics':records,'ali_words':aliwords,'status':'REVIEW_ONLY_INCOMPLETE_TRANSLATIONS'},ensure_ascii=False,indent=2),encoding='utf-8')
archive=out/'ZUYKOV_RU_REVIEW_2026-10-26.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as zz:
 for p in sorted(pack.rglob('*')):
  if p.is_file():zz.write(p,p.relative_to(out))
with zipfile.ZipFile(archive) as zz:assert zz.testzip() is None
print(json.dumps({'pdf':str(dest),'pages':len(PdfReader(dest).pages),'zip':str(archive),'bytes':archive.stat().st_size,'files':len(manifest),'words':sum(r['words'] for r in records),'ali_words':aliwords},ensure_ascii=False))
