from pathlib import Path
import json,re,shutil
from datetime import datetime
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
base=Path(__file__).resolve().parent;out=base/'assignment_execution';out.mkdir(exist_ok=True)
company='PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO'
address='IFZA Business Park, DDP, P.O. Box 342001, Dubai, United Arab Emirates'
person='Mikhail Kozin, a citizen of the Russian Federation, residing at Flat 503, Plot 70, Sharjah Main City, United Arab Emirates'
reg=json.loads((base.parent/'ali_review_2026-10-13/registry.json').read_text(encoding='utf8'))
schedule='\n\n'.join(f'PPA #{x["ppa"]} / PPA №{x["ppa"]} — US {x["number"]}\nFiling date / Дата подачи: {datetime.strptime(x["date"],"%m/%d/%Y").strftime("%Y-%m-%d")}\n{x["title"].replace("AI- DRIVEN","AI-DRIVEN")}' for x in reg)
res=f'''# PBK Corporate Resolution 1

Корпоративное решение PBK №1

Prepared / Подготовлено: 15 October 2026 / 15 октября 2026 года. Adoption dates are the actual signature dates below / Даты принятия — фактические даты подписей ниже.

Company / Компания: {company}. Licence / Лицензия №38769. IFZA Dubai. Registered office / Зарегистрированный офис: {address}.

## Part I Sole shareholder written ordinary resolution

I, Mikhail Kozin, as the sole shareholder holding 1,000 ordinary shares representing 100% of the Company, disclose my interests as its Director / General Manager, the proposed assignee and the person who funded the patent work. Having considered the agreement and records identified below, I resolve as follows.

1. Approve Patent Rights Assignment Agreement No. 1 prepared on 15 October 2026, including its Schedule A listing all ten US provisional applications, and the related Act No. 1 and clarified payment register dated 15 October 2026 documenting 16 payments totalling USD 22,593.00.

2. For this transaction, the Company accepts all 16 payments in that clarified register as expenses funded by Mikhail Kozin for its patent project and recognises a settlement obligation to him of USD 22,593.00. This is the Company's present approval and recognition upon adoption, not an assertion that the payment receipts themselves previously established this debt. The agreed transfer value and amount discharged are USD 22,593.00 (twenty-two thousand five hundred ninety-three US dollars and zero cents). The remaining Company liability for these accepted expenses after the transfer is USD 0.00. This negotiated settlement value is not represented as an independent market valuation.

3. The commercial purpose is to settle the Company's accepted patent-project financing obligation by transferring its interest in the funded portfolio to the person who financed it. The Company retains no obligation to finance future prosecution under this transaction. The payment register includes patent searches and the unfinished NPPA work, not only provisional filing costs. Claims against Ali Shalchi, Shalchi Law and UpCounsel are not released or assigned by this resolution.

4. Solely for the decisions approving and implementing this transaction, disapply the participation restriction in Article 60.1 by ordinary resolution under Article 60.3(a), with Article 60.2, of the supplied 51-page Memorandum and Articles of Association. Use the written-resolution mechanism in Article 43. This authority is to be exercised only after confirming that these Articles are in force and that the stated shareholder and director particulars remain current; mandatory law and any required creditor or third-party consents remain applicable.

5. Expressly authorise Mikhail Kozin to execute the approved documents for the Company as Director / General Manager and separately in his personal capacity as assignee and creditor. Each capacity requires a separate signature. The interested-director approval is limited to this identified transaction. No right to sign for either party is delegated to Ali.

6. Authorise delivery of the signed agreement to Ali Shalchi for USPTO recordation against all ten applications, subject to written agreement of his scope and fee. The representative must verify the chain of title and any additional applicant-change requirements. No new PCT or nonprovisional filing, substantive prosecution or additional unapproved fees are authorised. Material changes to price, discharge or transferred rights require fresh approval.

Sole shareholder: Mikhail Kozin / Единственный участник: Михаил Козин

Signature / Подпись __________________ Actual date / Дата __________________

---PAGE---

## Часть I Русская редакция решения участника

Я, Михаил Козин, единственный участник, владеющий 1 000 обыкновенных долей, составляющих 100% капитала Компании, раскрываю свою заинтересованность как директор / General Manager, приобретатель прав и лицо, финансировавшее патентные работы. Рассмотрев указанные ниже документы, принимаю следующие решения.

1. Одобрить Договор уступки патентных прав №1, подготовленный 15 октября 2026 года, с Приложением А по всем десяти предварительным заявкам США, а также акт №1 и уточнённый реестр от 15.10.2026, содержащий 16 платежей на 22 593,00 USD.

2. Для этой сделки Компания принимает все 16 платежей уточнённого реестра как расходы, профинансированные Михаилом Козиным для её патентного проекта, и признаёт обязательство перед ним в размере 22 593,00 USD. Это признание возникает при принятии решения, а не выводится автоматически из прежних квитанций. Согласованная стоимость передачи и погашаемая сумма составляют 22 593,00 USD (двадцать две тысячи пятьсот девяносто три доллара США 00 центов). Остаток обязательства по этим расходам после передачи — 0,00 USD. Сумма является согласованной стоимостью урегулирования, а не независимой рыночной оценкой.

3. Цель сделки — погасить принятое Компанией обязательство по финансированию патентного проекта передачей принадлежащих ей прав лицу, оплатившему работы. Эта сделка не обязывает Компанию финансировать дальнейшее патентование. Реестр включает поиск и незавершённую работу по NPPA, а не только подачу предварительных заявок. Требования к Ali Shalchi, Shalchi Law и UpCounsel не прекращаются и не передаются настоящим решением.

4. Исключительно для одобрения и исполнения этой сделки снять ограничение участия директора по пункту 60.1 посредством обычного решения по пункту 60.3(a), с учётом 60.2, представленного устава на 51 странице; применить письменную процедуру пункта 43. Использовать полномочия только после подтверждения действительности этой редакции устава и актуальности сведений об участнике и директоре. Обязательные нормы и необходимые согласия кредиторов или третьих лиц сохраняются.

5. Прямо уполномочить Михаила Козина подписать документы за Компанию как директор / General Manager и отдельно лично как приобретатель и кредитор. Требуются отдельные подписи в каждом качестве. Одобрение заинтересованности ограничено данной сделкой. Ali не вправе подписываться за стороны.

6. Разрешить передачу подписанного договора Ali Shalchi для регистрации уступки в USPTO по всем десяти заявкам после письменного согласования объёма и цены его услуг. Представителю проверить происхождение прав и необходимые изменения сведений о заявителе. Новые PCT, NPPA, работа по существу и несогласованные расходы не разрешаются. Изменение цены, погашения или предмета требует нового одобрения.

Подпись в Части I выше относится к английской и русской редакциям одного решения, а не к двум разным решениям.

## Part II Sole director implementation decision

After adoption of Part I and verification of the operative Articles and my current authority, I approve execution of Agreement No. 1 on exactly the terms above under Articles 60.2, 60.3(a), 66 and 69. I will sign separately for the Company and personally, retain the signed documents with the corporate records, and record discharge of USD 22,593.00 only when the assignment becomes effective. I will not certify unverified title, consent or payment facts.

## Часть II Решение единственного директора об исполнении

После принятия Части I и проверки действующего устава и своих полномочий одобряю исполнение договора №1 на указанных условиях по пунктам 60.2, 60.3(a), 66 и 69. Подписываю отдельно за Компанию и лично, сохраняю документы в корпоративном архиве и отражаю погашение 22 593,00 USD только при вступлении уступки в силу. Непроверенные сведения о правах, согласиях и платежах не удостоверяю.

Director / Директор: Mikhail Kozin / Михаил Козин

Signature / Подпись __________________ Actual date / Дата __________________

The English and Russian texts form one bilingual instrument; English governs inconsistencies, subject to mandatory law. / Английская и русская редакции составляют один документ; при расхождениях применяется английский текст с учётом обязательных норм.
'''
en=f'''# Patent Rights Assignment Agreement 1

Договор уступки патентных прав №1

Prepared 15 October 2026. Effective on the date of the last party signature below, after adoption of Corporate Resolution No. 1 and confirmation of the signatory's authority. No retrospective transfer is intended.

## 1 Parties and transaction

Assignor: {company}, an IFZA Dubai free-zone company, licence No. 38769, registered office {address}, represented by Mikhail Kozin as Director / General Manager under Corporate Resolution No. 1 (PBK).

Assignee: {person}, acting personally; notice email kmd379@gmail.com (Kozin). Kozin executes this agreement separately in each capacity.

The parties refer to Act No. 1 and the clarified register of 16 payments dated 15 October 2026, totalling USD 22,593.00. They expressly accept those payments as Company patent-project expenses funded by Kozin and agree to settle the corresponding Company obligation on the terms below. This agreement makes the settlement agreement; it does not treat the earlier factual register as having independently established liability or valuation.

## 2 Present assignment

PBK hereby assigns, transfers and conveys to Kozin all of PBK's right, title and interest, to the extent owned by PBK, worldwide in the ten US provisional applications identified in Schedule A and the inventions disclosed in them, including all assignable rights to apply for patents and to claim priority or benefit from each listed application under the Paris Convention, PCT and applicable national or regional law.

The transfer includes PBK's assignable interests in corresponding nonprovisional, PCT, national and regional applications, continuations, divisionals, reissues, resulting patents and extensions relating to that disclosed subject matter, and assignable causes of action and recoveries for infringement of the transferred rights. PBK shall execute further instruments needed to confirm corresponding rights it later acquires in that same subject matter. Unrelated inventions, unrelated new subject matter and third-party rights are excluded.

Kozin accepts the assignment. The transfer does not alter inventorship, create a past inventor-to-PBK transfer, extend any filing deadline or establish substantive entitlement to a priority claim. Any rights already owned personally by Kozin remain his.

## 3 Consideration and discharge

PBK acknowledges and the parties settle the Company obligation for all 16 accepted payments at USD 22,593.00 (twenty-two thousand five hundred ninety-three US dollars and zero cents). The agreed consideration for the transferred rights is the discharge of that same amount. Upon this agreement becoming effective, Kozin accepts the transfer in full satisfaction of that identified obligation, which is discharged in full; its remaining balance is USD 0.00. No additional cash payment is due from Kozin under this agreement.

The figure is a negotiated settlement amount, not a representation of independent market value or of USPTO fees alone. The parties knowingly include the search payments and unfinished NPPA work described in the register. This settlement provision supersedes only the register's statements that the Company obligation and settlement amount were not yet determined; the underlying payment facts and stated uncertainties are unchanged.

No unrelated Company obligation is discharged. Claims held by Kozin against Ali Shalchi, Shalchi Law, UpCounsel or other service providers, including claims relating to non-completion, duplicate payments or refunds, remain with Kozin and are neither waived nor assigned. This agreement does not accept Ali's assertion that the USD 6,400 advance was fully earned, certify performance or promise a refund. A later service-provider refund does not revive the settled PBK obligation; the same expenditure cannot be recovered twice from PBK. No unsupported representation that no prior refunds occurred is made.

## 4 Authority and title information

Upon execution PBK confirms that the signatory is authorised by duly adopted Corporate Resolution No. 1 and that any mandatory consents needed for this transfer have been obtained. The parties disclose Kozin's personal interest and his signatures in both capacities. Confirmation of the operative Articles and current corporate authority must precede execution.

Ali stated on 9 October 2026 that PBK is listed as applicant for PPA Nos. 1–10, and on 26 September 2026 that he did not prepare or record assignments for them. These statements do not establish whether private employment, invention or other title documents exist. No representation that a complete inventor-to-PBK chain has been verified, or that no third-party rights exist, is made here. PBK transfers its actual interest; this instrument does not cure any missing third-party conveyance. PBK must disclose any known restriction before execution. No warranty of patentability, validity or freedom to operate is given.

## 5 Documents and recordation

PBK will provide copies under its control of the applications, drawings, filing records, correspondence and relevant title documents and reasonably cooperate in executing accurate confirmatory documents. Neither party may sign for the other.

After signature the parties intend that Ali Shalchi record this assignment against each Schedule A application through USPTO Assignment Center with the required cover sheet. His engagement scope and charges must first be agreed in writing. The authority is limited to recordation and separately agreed related ownership/applicant formalities. It does not authorise new PCT or NPPA filings or substantive prosecution. The parties request a copy of the filed cover sheet and the notice of recordation identifying all ten applications. Recordation is not a determination of substantive ownership; additional applicant-change or representation formalities may be required.

## 6 General provisions

Schedule A is part of this agreement. The Act and clarified register are identified financial supporting records; they need not be recorded publicly with this agreement unless legally required. This instrument and the corporate resolution govern this settlement and assignment; amendments require both parties' written signatures. Invalidity of one clause does not enlarge the assigned rights or the discharged amount.

Applicable mandatory corporate, contractual and patent laws remain controlling. No exclusive jurisdiction or arbitration agreement is created; any dispute is for a court having jurisdiction under applicable law. The English and Russian texts constitute one instrument; English controls an inconsistency subject to mandatory law. Counterparts are permitted; electronic execution is used only where legally effective for its intended purpose.

---PAGE---

## Русская редакция

Подготовлено 15 октября 2026 года. Договор действует с даты последней подписи сторон после принятия корпоративного решения №1 и подтверждения полномочий подписанта. Передача задним числом не предусматривается.

## 1 Стороны и сделка

Передающая сторона: {company}, компания свободной зоны IFZA Dubai, лицензия №38769, зарегистрированный офис {address}, в лице Михаила Козина как директора / General Manager по корпоративному решению №1 (PBK).

Приобретатель: Михаил Козин / Mikhail Kozin, гражданин Российской Федерации, адрес Flat 503, Plot 70, Sharjah Main City, United Arab Emirates, действующий лично; email kmd379@gmail.com (Козин). Козин подписывает договор отдельно в каждом качестве.

Стороны ссылаются на акт №1 и уточнённый реестр 16 платежей от 15.10.2026 на 22 593,00 USD. Стороны принимают эти платежи как расходы патентного проекта Компании, профинансированные Козиным, и согласуют погашение соответствующего обязательства на следующих условиях. Обязательство и условия урегулирования согласуются настоящим договором, а не считаются автоматически установленными прежним фактическим реестром.

## 2 Уступка прав

PBK настоящим уступает и передаёт Козину все фактически принадлежащие PBK права, правовой титул и интерес во всём мире в десяти предварительных заявках США из Приложения А и раскрытых в них изобретениях, включая передаваемые права на получение патентов и испрашивание приоритета каждой заявки по Парижской конвенции, PCT и применимому национальному или региональному праву.

Передаются интересы PBK в соответствующих NPPA, PCT, национальных и региональных, продолжающих и выделенных заявках, переизданиях, выданных патентах и продлениях, относящихся к раскрытым изобретениям, а также передаваемые требования и возмещения за нарушение этих прав. PBK оформит дополнительные документы для подтверждения соответствующих прав, приобретённых ею позднее в отношении того же предмета. Посторонние изобретения, посторонние новые материалы и права третьих лиц исключены.

Козин принимает уступку. Она не изменяет авторство, не создаёт историческую уступку от изобретателя PBK, не продлевает сроки подачи и не доказывает право на приоритет по существу. Уже принадлежащие лично Козину права сохраняются за ним.

## 3 Встречное предоставление и погашение

PBK признаёт, а стороны согласуют обязательство Компании по всем 16 принятым платежам в размере 22 593,00 USD (двадцать две тысячи пятьсот девяносто три доллара США 00 центов). Встречным предоставлением за передаваемые права является погашение этой суммы. При вступлении договора в силу Козин принимает передачу в полное погашение указанного обязательства; остаток — 0,00 USD. Дополнительная денежная оплата от Козина не требуется.

Сумма является согласованной стоимостью урегулирования, а не независимой рыночной оценкой или суммой только государственных пошлин. Стороны осознанно включают оплату поисков и незавершённой NPPA из реестра. Это условие заменяет лишь указания реестра о том, что долг Компании и сумма погашения ещё не определены; факты оплат и отмеченные неопределённости сохраняются.

Иные обязательства Компании не прекращаются. Принадлежащие Козину требования к Ali Shalchi, Shalchi Law, UpCounsel и другим исполнителям, включая незавершение работ, повторные оплаты и возвраты, сохраняются за Козиным и не передаются. Договор не означает согласия с утверждением Ali об отработке аванса 6 400 USD, приёмки услуг или обещания возврата. Последующий возврат исполнителя не восстанавливает погашенный долг PBK; повторное взыскание того же расхода с PBK исключено. Отсутствие прежних возвратов без доказательств не утверждается.

## 4 Полномочия и сведения о правах

При подписании PBK подтверждает полномочия подписанта по надлежащим образом принятому корпоративному решению №1 и получение обязательных согласий на передачу. Раскрыта заинтересованность Козина и подписание им в двух качествах. Действительность устава и актуальные полномочия должны быть подтверждены до подписания.

Ali сообщил 09.10.2026, что PBK указана заявителем PPA №1–10, а 26.09.2026 — что он не готовил и не регистрировал уступки по ним. Эти сообщения не устанавливают наличие или отсутствие частных трудовых, изобретательских и других документов о правах. Полная проверка цепочки прав от изобретателя PBK и отсутствие прав третьих лиц настоящим договором не удостоверяются. Передаются фактические права PBK; отсутствующие уступки третьих лиц не заменяются. PBK раскрывает известные ограничения до подписания. Гарантии патентоспособности, действительности и свободы использования не предоставляются.

## 5 Документы и регистрация

PBK передаёт имеющиеся у неё копии заявок, чертежей, документов подачи, переписки и документов о правах и содействует подписанию достоверных подтверждений. Стороны не вправе подписываться друг за друга.

После подписания стороны намерены поручить Ali Shalchi регистрацию уступки по всем заявкам Приложения А через USPTO Assignment Center с необходимым сопроводительным листом. Объём и цена его услуг заранее согласуются письменно. Полномочия ограничены регистрацией и отдельно согласованными формальностями об обладателе прав и заявителе; новые PCT, NPPA и работа по существу не разрешаются. Сторонам предоставляются поданный сопроводительный лист и уведомление о регистрации по всем десяти заявкам. Регистрация не устанавливает принадлежность прав по существу; могут потребоваться отдельные изменения заявителя и представительства.

## 6 Общие условия

Приложение А является частью договора. Акт и уточнённый реестр — финансовые подтверждения; без обязательного требования их не нужно публично регистрировать с договором. Договор и корпоративное решение определяют эту уступку и урегулирование; изменения подписываются обеими сторонами. Недействительность отдельного положения не расширяет права или размер погашения.

Обязательные корпоративные, договорные и патентные нормы сохраняют силу. Исключительная подсудность или арбитраж не устанавливаются; спор рассматривается судом, компетентным по применимому праву. Английская и русская редакции составляют один документ; при расхождениях применяется английская редакция с учётом обязательных норм. Допускаются отдельные экземпляры подписей; электронная подпись используется лишь там, где она юридически допустима.

---PAGE---

## Signatures Подписи сторон

The signatures below adopt both language versions and Schedule A. / Подписи относятся к обеим языковым редакциям и Приложению А.

For / За {company}

Mikhail Kozin / Михаил Козин — Director / General Manager

Signature / Подпись __________________ Actual date / Дата __________________

Personally as assignee and settling creditor / Лично как приобретатель и кредитор:

Mikhail Kozin / Михаил Козин

Signature / Подпись __________________ Actual date / Дата __________________

## Schedule A Приложение А

Applications covered by this agreement / Заявки, охваченные договором

{schedule}
'''
for name,text in [('01_PBK_Corporate_Resolution_EN_RU',res),('02_Patent_Assignment_EN_RU',en)]:
 (out/(name+'.md')).write_text(text,encoding='utf8')
 d=Document();s=d.sections[0];s.page_width=Inches(8.5);s.page_height=Inches(11);s.top_margin=s.bottom_margin=Inches(.65);s.left_margin=s.right_margin=Inches(.7)
 for n,size in [('Normal',11),('Title',18),('Heading 1',13)]:
  st=d.styles[n];st.font.name='Arial';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0);st.paragraph_format.space_after=Pt(7);st.paragraph_format.line_spacing=1.05
 for st in d.styles:
  for el in list(st.element.iter(qn('w:pBdr'))):el.getparent().remove(el)
 br=False
 for b in re.split(r'\n\s*\n',text.strip()):
  if b=='---PAGE---':br=True;continue
  style='Normal'
  if b.startswith('## '):b=b[3:];style='Heading 1'
  elif b.startswith('# '):b=b[2:];style='Title'
  p=d.add_paragraph(b,style);p.paragraph_format.keep_together=True
  if br:p.paragraph_format.page_break_before=True;br=False
  if b.startswith(('Sole shareholder:','Director /','For /','Personally as','Mikhail Kozin /')):p.paragraph_format.keep_with_next=True
 footer=s.footer.paragraphs[0];footer.text='PBK → Mikhail Kozin | 15 October 2026 | '
 fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
 for rr in footer.runs:rr.font.size=Pt(8)
 d.save(out/(name+'.docx'))
note='''ПАКЕТ ДЛЯ ПРОВЕРКИ ALI ПЕРЕД ПОДПИСАНИЕМ И РЕГИСТРАЦИЕЙ
15.10.2026
1. Корпоративное решение №1: сначала подпись участника в Части I, затем директора в Части II. Договор подписать после решения, отдельно за PBK и лично. Вписать фактические даты, не датировать задним числом.
2. Согласовано пользователем: 22 593 USD признаются PBK и полностью погашаются уступкой. Требования к Ali/UpCounsel не прекращаются. Приложены действующие акт и реестр; признание и погашение устанавливаются новым договором, а не переписываются как прошлый факт.
3. До подписания подтвердить у корпоративного провайдера, что 51-страничный устав действует и сведения об участнике/директоре актуальны. Проверены положения 43, 60.3(a), 66 и 69 представленного файла; актуальность этой редакции ещё не установлена. Проверить обязательные согласия и допустимость сделки по применимому корпоративному праву.
4. Ali должен проверить основание прав PBK и необходимость дополнительных документов изобретателя. Он ранее сообщил, что уступки изобретатель—PBK не оформлял. Договор передаёт только фактические права PBK и не выдумывает происхождение прав.
5. Направить Ali оба DOCX на окончательную проверку. После согласования и подписания передать сканы. Подписанный договор с Приложением А — документ для recordation; корпоративное решение — подтверждение полномочий. Финансовые материалы передавать для проверки; не включать их автоматически в публичную запись USPTO.
6. Ali подготовить cover sheet, указать все десять номеров, actual execution dates, полные имена сторон и адрес приобретателя. Отдельно проверить изменение заявителя и полномочия представителя. Получить Notice of Recordation и проверить все номера.
7. Ничего не направлено Ali и не подано в USPTO. Объём и гонорар Ali должны быть согласованы до выполнения платных действий.
Источники: https://www.uspto.gov/web/offices/pac/mpep/s301.html ; https://www.uspto.gov/web/offices/pac/mpep/s302.html
Регистрация не является решением о действительности уступки. Иностранный текст при регистрации требует подписанного перевода; пакет содержит английский договор как оригинальную подписываемую редакцию вместе с русской.
'''
(out/'00_Порядок_подписания_и_отправки.txt').write_text(note,encoding='utf8')
print(out)
