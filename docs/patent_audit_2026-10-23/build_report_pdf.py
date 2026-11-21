from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4

B=Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont('Arial',r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold',r'C:\Windows\Fonts\arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial',boldItalic='Arial-Bold')
styles=getSampleStyleSheet()
for n in ['Normal','BodyText','Heading1','Heading2','Heading3']:styles[n].fontName='Arial'
styles['BodyText'].fontSize=10;styles['BodyText'].leading=14;styles['BodyText'].spaceAfter=8
styles['Heading1'].fontSize=21;styles['Heading1'].leading=25;styles['Heading1'].spaceAfter=13;styles['Heading1'].textColor=colors.HexColor('#164f53')
styles['Heading2'].fontSize=13;styles['Heading2'].leading=17;styles['Heading2'].spaceBefore=10;styles['Heading2'].spaceAfter=7
styles.add(ParagraphStyle(name='SmallAudit',fontName='Arial',fontSize=8,leading=11,spaceAfter=6))
styles.add(ParagraphStyle(name='CellAudit',fontName='Arial',fontSize=9,leading=12))
story=[]
def p(s,style='BodyText'):return Paragraph(s,styles[style])
def add(s,style='BodyText'):story.append(p(s,style))
def section(title,body):story.extend([p(title,'Heading2'),p(body)])
def table(rows,widths):
    t=Table([[p(escape(str(c)),'CellAudit') for c in row] for row in rows],colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf0f1')),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),0.6,colors.HexColor('#a1b8bb')),('LINEBELOW',(0,1),(-1,-1),0.25,colors.HexColor('#dce2e3'))]))
    story.append(t)

add('Ревизия патентного проекта','Heading1')
add('23 октября 2026 · Start-up / Codex / ChatGPT','SmallAudit')
add('Проверены состав файлов, даты и номера PPA, история подготовки NPPA/PCT и актуальные документированные статусы. Недостающие файлы добавлены в проект. Исходная папка Start-up сохранена.')
summary=json.loads((B/'INVENTORY_SUMMARY.json').read_text(encoding='utf-8'))
table([['Учтено файлов','Уже были в проекте','Добавлено уникальных копий'],[646,364,234]],[165,165,165])
add('487 различных содержимых; ещё 48 повторов новых копий учтены ссылками. Копии сверены по SHA-256. Ошибок инвентаризации: 0.','SmallAudit')
section('1. Исправлена ошибка дат подачи','В прежнем реестре даты выпуска документов APP.FILE.REC были приняты за даты подачи. Например, PPA №3 подана <b>23.12.2025</b>, а не 29.07.2026. Источник - поле Filing or 371(c) date в сохранённом индексе Patent Center. Исправлены все десять записей и раздел приоритетов клиентского PCT-каркаса.')
section('2. Восстановлена работа Ali','Из исходного письма Ali от 15.10.2026 сохранены <b>оригинальный DOCX-проект NPPA №1</b> и <b>22-страничный комплект чертежей</b>. В DOCX есть описание, раздел CLAIMS и ABSTRACT. Это отдельная работа поверенного; клиентский меморандум и каркас PCT её не заменяют.')
section('3. Уточнён действующий статус Ali','В письме от 20.10.2026 Ali прямо отказался возобновлять NPPA №1 и работу по уступке. Он предлагает новому поверенному использовать подготовленные им проекты. Эти проекты нуждаются в проверке и завершении; их наличие не подтверждает подачу.')
add('Главный рабочий конспект обновлён: docs/PATENT_CONTEXT_UNIFIED_RU.md. История и версии до правок сохранены.','SmallAudit')
story.append(PageBreak())

add('Проверенные номера и даты','Heading1')
add('Сверено с десятью сохранёнными официальными индексами Patent Center. Состояние дел онлайн заново не проверялось.','SmallAudit')
reg=json.loads((B/'VERIFIED_PPA_REGISTRY.json').read_text(encoding='utf-8'))
rows=[['PPA','Номер USPTO','Дата подачи','Группа','Годовщина 12 мес.']]
for r in reg:rows.append([f"№{r['ppa']}",r['number'],r['filing_ru'],f"№{r['group']}",r['anniversary']])
table(rows,[38,105,100,52,200])
section('Контрольные ориентиры','Группа №2 (PPA №1,2,8,9): <b>11.12.2026</b>.<br/>Группа №1 (PPA №3-7): <b>23.12.2026</b>.<br/>PPA №10: <b>04.08.2027</b>.')
add('Это календарные годовщины по записям. Применимые процессуальные сроки, достаточность раскрытия и порядок подачи подтверждает выбранный поверенный.','SmallAudit')
section('Почему исправление важно','Формулировка старого чата о повторной подаче PPA №3 в июле не подтверждается индексом. Указание даты квитанции как даты подачи давало неверный календарь.')
add('Полные названия и источники: docs/USPTO_PPA_FILING_REGISTRY_RU.md; VERIFIED_PPA_REGISTRY.csv/.json в папке ревизии.','SmallAudit')
story.append(PageBreak())

add('Что добавлено из других материалов','Heading1')
section('Переписка и кандидаты','ChatGPT «Таблица контроля NPPA» прочитан в пределах доступной выдачи: пять диалоговых блоков, следующей страницы нет. В рабочий контекст перенесены российские ответы; более поздние локальные сведения от 22 октября сохранены отдельно от ранних статусов чата.')
table([['Участник','Последний документированный статус'],['Michael Bartholomew','Готов обсуждать США и координацию PCT; окончательные NDA, договор и смета не установлены.'],['Scott / Daniel Polk; Ken Emanuelson','Ответы и распределение ролей отражены в журнале от 22 октября; получение полного пакета не подтверждено.'],['Anthony; Городисский','Отказ от проекта / отказ из-за загрузки соответственно.'],['PATENTUS; Зуйков; Союзпатент','Уточнение сметы; реквизиты для NDA; подтверждение получения соответственно.']],[140,355])
section('Передача материалов 22 октября','Локальный журнал содержит 15 исходящих писем: по пять архивов Michael, Ken и Scott. SENT не означает прочтение, заключение договора или разрешение платной работы. В этих архивах найденная работа Ali была отмечена как ненайденная; подготовлено отдельное дополнение к передаче дела.')
section('Финансирование и уступка','Рабочий реестр указывает 16 оплат на <b>22 593 USD</b>, включая аванс <b>6 400 USD</b> за NPPA №1. Это не оплата PCT и не подтверждение подписанного долга PBK. Проекты уступки и корпоративного решения найдены; подписание и регистрация перехода прав не установлены.')
add('Цены и квалификационные заявления кандидатов сохраняются как сведения из переписки, а не независимое подтверждение статуса или принятый договор.','SmallAudit')
story.append(PageBreak())

add('Что проверить дальше','Heading1')
for title,body in [
('Выбор исполнителя','Согласовать договор, окончательную смету, NDA и календарь работы. Старые инструкции «по одной PPA за письмо» помечены как исторические: NPPA №1 объединяет пять PPA.'),
('Содержание и приоритет','Передать найденные оригиналы Ali выбранному поверенному; сопоставить каждый будущий пункт формулы с точными поданными PPA и чертежами. Формальное перечисление PPA само по себе не доказывает поддержку.'),
('Уступка PBK → Михаил','Подтвердить действующий устав, полномочия, цепочку прав, подписи и регистрацию уступки. Проект документа не равен завершённой передаче прав.'),
('Рисунки №9 и №10','Проверить точные поданные версии. Отсутствие отдельного DRW не доказывает отсутствие рисунков внутри описания; поздние рисунки нельзя считать первоначально поданными.'),
('PCT и новая подача','Определить заявителя, ведомство и уполномоченного представителя. В проверенном наборе не установлены номера или официальные квитанции новой NPPA/PCT-подачи.')]:section(title,body)
add('Где находятся результаты','Heading2')
add('Все файлы ревизии находятся в:<br/><b>C:\\Users\\kmd37\\Projects\\vird\\docs\\patent_audit_2026-10-23</b>','SmallAudit')
add('REVISION_REPORT_RU.md/.txt - подробный отчёт.<br/>STARTUP_INVENTORY.csv - все 646 файлов и пути копий.<br/>source_additions - отсутствовавшие в проекте исходники.<br/>evidence/Ali_original_drafts_2026-10-15 - оригиналы Ali.<br/>RECOVERED_ALI_DRAFTS_FOR_REVIEW.zip - готовое дополнение к передаче дела, не отправлено.','SmallAudit')
add('Пределы: проверен состав файлов, извлечён доступный текст, сверены основные сведения. Сканы и все 646 файлов не проходили полную содержательную/юридическую экспертизу. Новых писем, оплат, найма и подач не выполнялось.','SmallAudit')
add('Проверенные нормативные источники: USPTO MPEP 211/211.05 - uspto.gov/web/offices/pac/mpep/s211.html; WIPO PCT Rule 83.1bis - wipo.int/pct/en/texts/rules/r83.html.','SmallAudit')

def footer(c,d):
    c.setFont('Arial',8);c.setFillColor(colors.HexColor('#60686a'));c.drawString(49,27,'Рабочая ревизия | 23.10.2026 | конфиденциально');c.drawRightString(A4[0]-49,27,str(d.page))
out=B/'REVISION_REPORT_RU.pdf'
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=49,leftMargin=49,topMargin=43,bottomMargin=43,title='Ревизия патентного проекта 23.10.2026',author='Mikhail Kozin / working review')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
from pypdf import PdfReader
reader=PdfReader(out)
assert len(reader.pages)==4,len(reader.pages)
for i,page in enumerate(reader.pages):assert len(page.extract_text())>500,i
print(str(out));print('Verified pages:',len(reader.pages))
