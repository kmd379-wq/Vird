from pathlib import Path
import json,re,shutil
from datetime import datetime
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pypdf import PdfReader

base=Path(__file__).resolve().parent
out=base/'revised';out.mkdir(exist_ok=True)
reg=json.loads((base.parent/'ali_review_2026-10-13/registry.json').read_text(encoding='utf8'))
old=(base/'01_Act_1_2026-10-15_RU.md').read_text(encoding='utf8')
parties=next(p for p in old.split('\n\n') if p.startswith('PBK ENGINEERING'))
data=[('00419',891,'09.12.2025','Услуги поверенного — 75% Service Fees; название задания Conduct Patent Search. Номер PPA не указан.'),('00426',777,'10.12.2025','Услуги поверенного — 297 USD; Filing fees — 130 USD и 350 USD. Название задания Conduct Patent Search. Номер PPA не указан.'),('00432',1600,'15.12.2025','Filing fees — расходы на подачу по обозначению счёта; номер PPA не указан.'),('00438',800,'19.12.2025','Filing fees; номер PPA не указан.'),('00443',900,'04.01.2026','Filing fees; номер PPA не указан.'),('00449',800,'12.01.2026','Filing fees; номер PPA не указан.'),('00453',865,'15.01.2026','Filing fees; номер PPA не указан.'),('00460',965,'03.02.2026','Filing fees; номер PPA не указан.'),('SLPC2',1500,'08.06.2026','PPA №8 — назначение подтверждено письмом Ali от 09.10.2026; в счёте имеются обозначения PPA и NPPA.'),('00610',965,'30.06.2026','Filing fees по PPA №9.'),('00624',765,'01.08.2026','Filing fees по PPA №10.'),('00620',765,'06.08.2026','Filing fees по PPA №10; второй документально подтверждённый платёж по этой заявке.')]
assert sum(x[1] for x in data)==11593
def money(n):return f'{n:,.2f}'.replace(',',' ').replace('.',',')+' USD'
def applications():
 return '\n\n'.join(f'PPA №{x["ppa"]} — US {x["number"]}; дата подачи {datetime.strptime(x["date"],"%m/%d/%Y").strftime("%d.%m.%Y")}.\n{x["title"].replace("AI- DRIVEN","AI-DRIVEN")}' for x in reg)
sign='''За PBK: Михаил Козин / Mikhail Kozin, директор / General Manager.

Подпись _____________________ Дата подписи _____________________

Козин лично: Михаил Козин / Mikhail Kozin.

Подпись _____________________ Дата подписи _____________________'''
limits='''Все перечисленные операции подтверждены квитанциями либо письменным подтверждением получателя. Платежи перечислялись UpCounsel по счетам Ali Shalchi и непосредственно Shalchi Law; поступление денег на счёт PBK настоящим актом не удостоверяется.

Общая сумма отражает исходные платежи, принятые для сверки финансирования портфеля. Она не является установленной стоимостью подачи всех десяти заявок или окончательным долгом PBK перед Козиным. Возвраты и возмещения полностью не сверены; их отсутствие не утверждается.

Назначение Filing fees воспроизведено из счетов и не означает, что вся сумма является государственной пошлиной USPTO. Две оплаты по PPA №10 включены как факты платежей; необходимость двух начислений требует сверки. По счетам без номера PPA распределение между заявками не устанавливается.'''
act=f'''# Двусторонний акт № 1
## О подтверждённых платежах по патентному портфелю

Дата составления: 15 октября 2026 года. Новая редакция для рассмотрения и подписания.

{parties}

## 1 Общая сумма и предмет акта

Стороны фиксируют перечень 12 документально подтверждённых платежей Козина на общую сумму 11 593,00 USD (одиннадцать тысяч пятьсот девяносто три доллара США 00 центов) для сверки финансирования патентного портфеля PPA №1–10. Из них 10 093,00 USD оплачено через UpCounsel и 1 500,00 USD непосредственно Shalchi Law.

PBK при подписании принимает перечисленные подтверждения к сверке расходов, заявленных Козиным как финансирование в интересах компании. Подробные даты, счета и документы приведены в Реестре финансирования — приложении №1 к настоящему акту.

## 2 За что перечислены средства

1. Услуги поверенного — 891,00 USD по счёту 00419 и 297,00 USD в составе счёта 00426; всего 1 188,00 USD. Оба счёта связаны с заданием Conduct Patent Search; конкретные PPA в них не указаны.

2. Расходы с обозначением Filing fees без номера заявки — 480,00 USD в составе счёта 00426 и 5 930,00 USD по счетам 00432, 00438, 00443, 00449, 00453, 00460; всего 6 410,00 USD.

3. Платёж за PPA №8 по SLPC Invoice №2 — 1 500,00 USD; назначение письменно подтверждено Ali.

4. Filing fees по PPA №9, счёт 00610 — 965,00 USD.

5. Filing fees по PPA №10, счета 00624 и 00620 — по 765,00 USD каждый, всего 1 530,00 USD.

ИТОГО: 1 188,00 + 6 410,00 + 1 500,00 + 965,00 + 1 530,00 = 11 593,00 USD. Каждая оплата включена один раз.

---PAGE---

## 3 Перечень всех предварительных заявок

Перечень определяет состав портфеля. Само включение заявки в этот перечень не устанавливает сумму расходов по ней. Названия приведены в исходной английской редакции для точной идентификации.

{applications()}

---PAGE---

## 4 Подтверждения и пределы сверки

{limits}

В итог не включены отдельно обозначенные патентные поиски по счетам 00430, 00524 и SLPC Invoice №1, а также аванс NPPA по счёту 00654. Квитанция USPTO по PPA №1 на 65,00 USD приложена для сверки и повторно к итогу не прибавлена.

Приложение №1 — Реестр финансирования к акту №1 от 15.10.2026, содержащий все 12 платежей и перечень десяти PPA. Подтверждающие документы — 26 файлов в папке Evidence. Акт не передаёт патентные права, не подтверждает завершение услуг и не отменяет требований о сверке или возврате средств.

## 5 Подписи сторон

Проект предназначен для подписания после действительного корпоративного одобрения полномочий на заинтересованную сделку. Ранее подготовленный проект решения не подтверждает принятие такого решения. При подписании после 15.10.2026 стороны указывают фактическую дату подписи.

{sign}
'''
fund='''# Реестр финансирования
## Приложение № 1 к двустороннему акту № 1

Дата составления: 15 октября 2026 года. Стороны: PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO и Михаил Козин / Mikhail Kozin лично.

Общая сумма подтверждённых исходных платежей — 11 593,00 USD. Всего 12 операций: 11 оплат через UpCounsel на 10 093,00 USD и один прямой платёж Shalchi Law на 1 500,00 USD.

## 1 Список платежей и оплаченных услуг

Даты оплаты приведены по квитанциям и подтверждению Ali. Даты SENT — даты отправки счетов. В выгрузке CSV даты UTC иногда относятся к соседнему дню; это не дополнительные операции.
'''
for i,(inv,amount,date,desc) in enumerate(data,1):
 if inv!='SLPC2':
  txt=PdfReader(base/'Evidence'/f'Invoice_{inv}.pdf').pages[0].extract_text()
  sent=re.search(r'SENT\s+([^\n]+)',txt)[1].strip()
  sent=datetime.strptime(sent,'%m/%d/%Y').strftime('%d.%m.%Y') if sent!='-' else 'не указана'
  evidence=f'Invoice_{inv}.pdf и Receipt_{inv}.pdf'; extra=f'Дата отправки счёта: {sent}. Получатель: UpCounsel по счёту Ali Shalchi.'
 else:evidence='SLPC Invoice#2.pdf и Ali_2026-10-09_email_EN.txt';extra='Получатель: Shalchi Law напрямую; перевод Santander.'
 fund+=f'\n\n### {i} Счёт {inv}\n\nОплачено {date} — {money(amount)}. {extra}\nЗа что оплачено: {desc}\nПодтверждение: {evidence}.\n'
fund+=f'''

ИТОГО ПО 12 ОПЕРАЦИЯМ: 11 593,00 USD. Плательщик во всех перечисленных операциях — Mikhail Kozin.

---PAGE---

## 2 Все заявки патентного портфеля

{applications()}

---PAGE---

## 3 Сводное назначение расходов

Услуги поверенного по счетам 00419 и 00426: 1 188,00 USD.

Filing fees без указанного номера PPA: 6 410,00 USD.

PPA №8: 1 500,00 USD; PPA №9: 965,00 USD; PPA №10: два платежа, всего 1 530,00 USD.

Общий итог: 11 593,00 USD. Из него 3 995,00 USD документально связаны с PPA №8–10. Остальные 7 598,00 USD показаны с назначениями из счетов, без предположительного распределения по PPA №1–7.

{limits}

## 4 Подтверждающие документы и подписи

Приложены Invoice и Receipt по 11 счетам: 00419, 00426, 00432, 00438, 00443, 00449, 00453, 00460, 00610, 00620, 00624 — всего 22 PDF. Дополнительно приложены SLPC Invoice#2.pdf, письмо Ali_2026-10-09_email_EN.txt, выгрузка transaction_report_2026-10-09.csv и квитанция PPA1_N417_PYMT_previously_received.pdf. Всего 26 файлов в Evidence; квитанция USPTO не увеличивает итог повторно.

Подписи подтверждают согласие с перечисленными сведениями и ограничениями сверки. Итог не является подтверждением окончательного долга PBK или оценкой передаваемых патентных прав.

{sign}
'''
for name,text in [('01_Act_1_Revised_RU',act),('02_Funding_Register_Revised_RU',fund)]:
 (out/(name+'.md')).write_text(text,encoding='utf8')
 d=Document();s=d.sections[0];s.page_width=Inches(8.5);s.page_height=Inches(11);s.top_margin=s.bottom_margin=Inches(.65);s.left_margin=s.right_margin=Inches(.7)
 for n,size in [('Normal',11),('Title',18),('Heading 1',13),('Heading 2',11)]:
  st=d.styles[n];st.font.name='Arial';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0);st.paragraph_format.space_after=Pt(7);st.paragraph_format.line_spacing=1.05
 for st in d.styles:
  for el in list(st.element.iter(qn('w:pBdr'))):el.getparent().remove(el)
 br=False
 for b in re.split(r'\n\s*\n',text.strip()):
  if b=='---PAGE---':br=True;continue
  style='Normal'
  for pre,sty in [('### ','Heading 2'),('## ','Heading 1'),('# ','Title')]:
   if b.startswith(pre):b=b[len(pre):];style=sty;break
  p=d.add_paragraph(b,style);p.paragraph_format.keep_together=True
  if br:p.paragraph_format.page_break_before=True;br=False
  if b.startswith(('За PBK:','Козин лично:')):p.paragraph_format.keep_with_next=True
 footer=s.footer.paragraphs[0];footer.text='Акт №1 и реестр | Новая редакция 15.10.2026 | Проект | '
 fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
 for run in footer.runs:run.font.size=Pt(8)
 d.save(out/(name+'.docx'))
print(out)
