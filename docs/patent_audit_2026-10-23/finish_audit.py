import csv, json, hashlib, shutil, re
from pathlib import Path
from datetime import datetime, date

ROOT=Path(r'C:\Users\kmd37\Projects\vird'); BASE=Path(__file__).resolve().parent
def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def backup(p):
    dst=BASE/'before_revision'/p.relative_to(ROOT)
    if not dst.exists():dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)

inventory=json.loads((BASE/'STARTUP_INVENTORY.json').read_text(encoding='utf-8'))
for row in inventory:
    if row['status']=='indexed_only':
        p=Path(row['source_path']);dest=BASE/'source_additions'/row['relative_path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
        assert sha(dest)==row['sha256'];row['imported_path']=str(dest);row['status']='imported_new'
write(BASE/'STARTUP_INVENTORY.json',json.dumps(inventory,ensure_ascii=False,indent=2))
with (BASE/'STARTUP_INVENTORY.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(inventory[0]));w.writeheader()
    for row in inventory:w.writerow({**row,'existing_project_paths':' | '.join(row['existing_project_paths'])})
from collections import Counter
summary=json.loads((BASE/'INVENTORY_SUMMARY.json').read_text(encoding='utf-8'))
summary['status_counts']=dict(Counter(r['status'] for r in inventory));summary['imported_unique_bytes']=sum(r['bytes'] for r in inventory if r['status']=='imported_new')
write(BASE/'INVENTORY_SUMMARY.json',json.dumps(summary,ensure_ascii=False,indent=2))

registry=json.loads((ROOT/'docs/ali_review_2026-10-13/registry.json').read_text(encoding='utf-8'))
for r in registry:
    d=datetime.strptime(r['date'],'%m/%d/%Y').date();r['filing_iso']=d.isoformat();r['filing_ru']=d.strftime('%d.%m.%Y');r['anniversary']=date(d.year+1,d.month,d.day).isoformat()
    r['group']=1 if r['ppa'] in [3,4,5,6,7] else 2 if r['ppa'] in [1,2,8,9] else 3
    index=ROOT/'docs/ali_review_2026-10-13/extracted'/r['source'];source_text=index.read_text(encoding='utf-8')
    assert r['number'] in source_text and r['date'] in source_text
    r['source_index']=str(index)
    r['source_pdf']=str(ROOT/'docs/ali_review_2026-10-13/originals/USPTO/Patent Center document indexes'/index.with_suffix('.pdf').name)
    assert Path(r['source_pdf']).exists()
write(BASE/'VERIFIED_PPA_REGISTRY.json',json.dumps(registry,ensure_ascii=False,indent=2))
with (BASE/'VERIFIED_PPA_REGISTRY.csv').open('w',encoding='utf-8-sig',newline='') as f:
    fields=['ppa','number','filing_iso','title','group','anniversary','source_pdf'];w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(registry)

old=ROOT/'docs/USPTO_PPA_FILING_REGISTRY_RU.md';backup(old)
lines=['# Реестр предварительных заявок PPA №1–10 — исправлено 23.10.2026','',
'Дата подачи берётся из поля Filing or 371(c) date в сохранённых индексах USPTO Patent Center. Дата APP.FILE.REC в имени файла — дата документа/отправки, и не заменяет дату подачи. Прежняя редакция содержала ошибочные даты; копия сохранена в docs/patent_audit_2026-10-23/before_revision/.','',
'Номера, даты и названия сверены с текстом всех десяти сохранённых индексов. Это проверка локальных копий официальных записей, а не новая онлайн-проверка состояния дел Patent Center.','',
'| PPA | Номер USPTO | Дата подачи | Точное название по индексу | Группа NPPA | Годовщина через 12 месяцев |','|---|---|---|---|---|---|']
for r in registry:lines.append(f"| №{r['ppa']} | {r['number']} | {r['filing_ru']} | {r['title']} | №{r['group']} | {r['anniversary']} |")
lines+=['','## Исправления прежних дат','',
'- PPA №2: 23.01.2026 → 19.12.2025.','- PPA №3: 29.07.2026 → 23.12.2025. Дата 29.07 относится к Filing Receipt; повторная подача в июле этим не установлена.','- PPA №4: 05.02.2026 → 06.01.2026.','- PPA №5: 13.02.2026 → 13.01.2026.','- PPA №6: 24.02.2026 → 16.01.2026.','- PPA №7: 13.03.2026 → 04.02.2026.','- Данные PPA №1, 8, 9, 10 заполнены; №8–10 имеют серию 64/, её нельзя заменять на 63/.','- Префикс 164916 не является Confirmation Number PPA №3: в индексе для неё указан 6370. Назначение префикса не установлено.','',
'## Контрольные ориентиры групп','',
'- Группа №2 (PPA №1,2,8,9): ранняя дата 11.12.2025; 12-месячная годовщина 11.12.2026.','- Группа №1 (PPA №3–7): ранняя дата 23.12.2025; 12-месячная годовщина 23.12.2026.','- Группа №3 (PPA №10): 04.08.2026; годовщина 04.08.2027.','',
'Годовщины приведены как контрольные даты по записям, не как итоговое заключение о процессуальных сроках. Поддержку каждого будущего пункта формулы, срок и порядок подачи проверяет выбранный поверенный.','',
'## Где находятся подтверждения','',
'- Официальные индексы всех 10 PPA: docs/ali_review_2026-10-13/originals/USPTO/Patent Center document indexes/.','- Извлечённый текст: docs/ali_review_2026-10-13/extracted/.','- Реестр с абсолютными путями: docs/patent_audit_2026-10-23/VERIFIED_PPA_REGISTRY.csv и .json.','- Квитанции APP.FILE.REC, ADS, acknowledgment/payment receipts и их варианты: полный указатель STARTUP_INVENTORY.csv. Их наличие не означает автоматическую комплектность поданного раскрытия.','',
'## Проверки раскрытия','',
'- PPA №9: отсутствие отдельного DRW не доказывает отсутствие рисунков в описании. По письму Ali, упомянутые FIGS. 1–8 не были поданы; сверить именно поданный текст и вложения.','- PPA №10: по письму Ali рисунки находятся на страницах 14–17 описания; отдельного DRW в индексе нет.','- Совпадение названий №6/№7 и использование общего файла рисунков по данным клиента не доказывают одинаковое раскрытие.','',
'Общий актуальный контекст: docs/PATENT_CONTEXT_UNIFIED_RU.md. Отчёт ревизии: docs/patent_audit_2026-10-23/REVISION_REPORT_RU.md.']
write(old,'\n'.join(lines)+'\n')

# Repair only the procedural/priority section of the client skeleton; preserve technical drafting.
pct=ROOT/'docs/ali_submission/NPPA1_PCT_Specification_Skeleton_EN.md';backup(pct);text=pct.read_text(encoding='utf-8')
start=text.index('# §2. CROSS-REFERENCE');end=text.index('# §3. TECHNICAL FIELD')
priority=['# §2. CROSS-REFERENCE TO RELATED APPLICATIONS','',
'**Working priority particulars verified against saved Patent Center indexes on October 23, 2026. Counsel must verify entitlement, formal requirements, applicant/successor status and filing deadlines before submission.**','',
'This application claims priority to the following U.S. provisional applications. Counsel shall adapt the statement to the filing route, complete the PCT Request or U.S. ADS, and verify disclosure support for each claimed combination.','']
for r in registry:
    if r['group']==1:
        d=datetime.strptime(r['filing_iso'],'%Y-%m-%d');priority.append(f"- PPA #{r['ppa']}: U.S. Provisional Application No. {r['number']}, filed {d.strftime('%B')} {d.day}, {d.year}, entitled \"{r['title']}\".")
priority+=['','**Counsel review:** Listing the provisional applications does not itself establish entitlement to their dates. Verify written-description and enablement support in each relied-on application, including the claimed combination. The original blanket statement that priority support is assessed only in litigation has been removed; examination may require that support to be established. No continuation-in-part relationship to a provisional application is asserted here.','',
'**Draft provenance:** This is a client-prepared framework. Ali supplied a separate attorney draft and a 22-page drawing set on October 15, 2026; originals are preserved in `docs/patent_audit_2026-10-23/evidence/Ali_original_drafts_2026-10-15/`. Use those alongside the filed provisionals. Their presence does not establish that a U.S. nonprovisional or PCT has been filed.','',
'Sources: saved Patent Center indexes; USPTO MPEP 211 and 211.05 (https://www.uspto.gov/web/offices/pac/mpep/s211.html).','\n---\n\n']
write(pct,text[:start]+'\n'.join(priority)+text[end:])

# Export the retrieved ChatGPT transcript in a readable form.
chat=json.loads((BASE/'CHATGPT_NPPA_CONTROL_SOURCE.json').read_text(encoding='utf-8'))
chatlines=['# Источник: ChatGPT «Таблица контроля NPPA»','',f"Чат: {chat['thread']['id']}. Прочитано {len(chat.get('turns',[]))} блоков; hasMore={chat.get('page',{}).get('hasMore')}. Это вся доступная инструменту выдача, не гарантия полного исторического экспорта.",'']
for turn in reversed(chat.get('turns',[])):
    for item in turn.get('items',[]):
        if item['type']=='agentMessage':chatlines+=['## Ответ ассистента','',item.get('text',''),'']
        elif item['type']=='userMessage':chatlines+=['## Пользователь','', '\n'.join(x.get('text','') for x in item.get('content',[]) if x.get('type')=='text'),'']
write(BASE/'CHATGPT_NPPA_CONTROL_READABLE_RU.md','\n'.join(chatlines))

findings=[
{'id':'F01','severity':'critical','title':'Исправлены даты подачи PPA','detail':'Старый реестр использовал даты документов APP.FILE.REC. Правильные даты восстановлены по полю Filing or 371(c) date во всех 10 индексах. Для PPA №3: 23.12.2025 вместо 29.07.2026.','source':'docs/ali_review_2026-10-13/extracted/PPA#3 Patent Center Index.txt','action':'Исправлены основной реестр и §2 клиентского PCT-каркаса.'},
{'id':'F02','severity':'critical','title':'Найден отдельный проект Ali, которого не было в пакете 22 октября','detail':'В исходном письме 15.10.2026 находятся NPPA #1 Draft Spec (covering PPA#3-7).docx (48 361 байт) и Draft Figures.pdf (544 272 байта, 22 страницы). DOCX содержит 125 пронумерованных абзацев описания, раздел CLAIMS и ABSTRACT. Это рабочий адвокатский проект, а не клиентский каркас и не подтверждение подачи.','source':'Gmail 1a1418866b36c835; evidence/Ali_original_drafts_2026-10-15/','action':'Оба оригинала скачаны и проверены по размерам, сохранены отдельно. Подготовлено дополнение для последующей передачи выбранному поверенному.'},
{'id':'F03','severity':'critical','title':'Ali окончательно отказался продолжать работу','detail':'Письмо 20.10.2026 прямо исключает возобновление NPPA №1, проверку и регистрацию уступки. Ali предлагает новому поверенному использовать уже переданные описание и чертежи.','source':'Gmail 1a15a24e3d6eac64; evidence/ALI_2026-10-20_ORIGINAL_EN.txt','action':'Контекст обновлён: ожидание согласия Ali больше не считается текущим статусом.'},
{'id':'F04','severity':'high','title':'Ранние указания отправлять каждую PPA отдельно устарели','detail':'План Ali объединяет PPA №3–7 в одну NPPA №1; «по одной заявке» относилось к NPPA. Пакеты send/PPA3…PPA7 и ранний ZIP остаются историческими материалами, а не действующей схемой новой подачи.','source':'История текущего чата и консолидированное NPPA1 memo','action':'В инструкции send добавлено предупреждение; актуальные рабочие задачи сведены в единый контекст.'},
{'id':'F05','severity':'high','title':'Сведения о кандидатах в двух чатах различаются по свежести','detail':'ChatGPT показывает Scott без ответа по состоянию на 20 октября. Локальный журнал от 22 октября содержит ответы Scott/Daniel, Ken и Michael. Anthony отказался; Michael дал раздельную предварительную смету.','source':'CHATGPT_NPPA_CONTROL_SOURCE.json; docs/patent_attorney_tracker/data.json; C:\\Start-up\\Replies_2026-10-22','action':'Сохранены обе хронологические версии; в рабочем контексте используются более поздние документированные сведения.'},
{'id':'F06','severity':'high','title':'15 писем кандидатам уже отправлены, но подтверждение получения не установлено','detail':'SEND_LOG_FINAL.json фиксирует пять частей каждому из Michael, Ken, Scott — всего 15 исходящих 22.10.2026. Это локальные записи Gmail SENT; не подтверждение прочтения или принятия поручения.','source':'C:\\Start-up\\Attorney_Review_2026-10-22\\SEND_STATUS_RU.txt и SEND_LOG_FINAL.json','action':'Учтено как ранее выполненная отправка. Новых писем в ходе ревизии не отправлено.'},
{'id':'F07','severity':'high','title':'Принадлежность прав и подписанная уступка ещё требуют подтверждения','detail':'Найдены проекты корпоративного решения, уступки и реестра финансирования; наличие проекта не доказывает подписание или recordation. Разные редакции MOA и основание прав PBK требуют сверки.','source':'docs/pbk_act1_2026-10-15/assignment_execution; docs/ali_review_2026-10-13/01_Translation_and_Review_RU.md','action':'В контексте сохранён статус проектов. Автоматическое утверждение перехода прав не добавлялось.'},
{'id':'F08','severity':'high','title':'Приоритет не гарантируется одним перечислением PPA','detail':'Прежняя формулировка «проверяется только в суде» слишком категорична. MPEP 211/211.05 предусматривает проверку права на раннюю дату при экспертизе. Нужна опора конкретной формулы в поданном раскрытии.','source':'https://www.uspto.gov/web/offices/pac/mpep/s211.html','action':'Категоричная фраза удалена из рабочего PCT-каркаса; исходные цитаты переписки сохранены как история.'},
{'id':'F09','severity':'medium','title':'Пробелы в рисунках PPA №9/№10 нельзя закрывать предположениями','detail':'Для PPA №9 нет отдельного DRW; предыдущий разбор письма Ali указывает на неподачу FIGS. 1–8. По №10 рисунки, согласно письму Ali, находятся внутри описания на страницах 14–17. Нужна сверка точных поданных версий.','source':'docs/ali_review_2026-10-13/01_Translation_and_Review_RU.md; Patent Center indexes №9/№10','action':'Пробелы включены в список незавершённых проверок; более поздние эскизы не объявлены поданными.'},
{'id':'F10','severity':'medium','title':'Финансовый итог и новая смета различаются по назначению','detail':'Рабочий реестр: 16 оплат, 22 593 USD, включая 6 400 USD за NPPA №1. По позиции Ali аванс отработан; это не акт взаимной сверки, не доказательство оплаты PCT и не текущая смета нового поверенного.','source':'docs/pbk_act1_2026-10-15/clarified/02_Реестр_всех_платежей.md','action':'Суммы перенесены с указанием источника и статуса; повторные копии не посчитаны новыми платежами.'}
]
write(BASE/'FINDINGS.json',json.dumps(findings,ensure_ascii=False,indent=2))

context=ROOT/'docs/PATENT_CONTEXT_UNIFIED_RU.md';backup(context)
orig=context.read_text(encoding='utf-8');heading='# Единый рабочий конспект: PBK, PPA №1–10, NPPA, PCT и Ali'
updates='''

## Актуализация по ревизии 23.10.2026

Этот раздел имеет приоритет перед историческими статусами конспекта от 20 октября ниже. Отчёт, оригиналы и инвентаризация: docs/patent_audit_2026-10-23/.

- Проверены 646 файлов C:\\Start-up; файлы, которых не было в проекте по контрольной сумме, сохранены в source_additions. Ничего в исходной папке не переименовано и не удалено. Это проверка состава и извлечение доступного текста, а не полная юридическая или техническая экспертиза каждого документа.
- Прочитан доступный ответ инструмента по ChatGPT «Таблица контроля NPPA», ID 977310b6-46d4-8333-a421-35a8fa3ae446: пять блоков диалога, следующей страницы нет. Его исходная выдача сохранена. Старые ID в разделе источников ниже относятся к предшествующему объединению. Программный экспорт текущего Codex-чата недоступен (thread/items/list is not supported yet); использованы видимый контекст и сохранённые документы проекта.
- Ali 20.10.2026 прямо отказался возобновлять NPPA №1 и работу по уступке. Источник заново прочитан в Gmail, ID 1a15a24e3d6eac64. Не считать его текущим исполнителем.
- Из письма Ali 15.10.2026 (ID 1a1418866b36c835) восстановлены оригинальные ALI_NPPA1_Draft_Spec.docx и ALI_NPPA1_Draft_Figures.pdf, 22 страницы чертежей. Они находятся в evidence/Ali_original_drafts_2026-10-15/. В DOCX есть описание, CLAIMS и ABSTRACT; это рабочий проект, не подтверждение подачи. Прежняя пометка пакета 22.10 «проект Ali не найден» более не актуальна.
- Реестр docs/USPTO_PPA_FILING_REGISTRY_RU.md исправлен по всем десяти индексам. В частности, PPA №3 подана 23.12.2025, а 29.07.2026 — дата документа APP.FILE.REC. Более ранние ошибочные таблицы не использовать для расчёта сроков.
- Контрольные 12-месячные годовщины: группа №2 — 11.12.2026; группа №1 — 23.12.2026; PPA №10 — 04.08.2027. Это ориентиры по сохранённым записям; применимые сроки и поддержку формулы подтверждает поверенный.
- Основные группы сохраняются: NPPA №1 = PPA №3–7; NPPA №2 = PPA №1,2,8,9; PPA №10 — отдельная тема. По отправленному заданию 22 октября США сейчас оцениваются NPPA №1/№2 и уступка; №10 передана как фон. Подача PCT и российские заявки — отдельные объёмы.
- Последние локальные сведения 22.10: Michael Bartholomew готов обсуждать США и координацию PCT, но NDA/договор и окончательная смета не согласованы; Scott работает в команде Daniel Polk, Ken также дал ответ; Anthony отказался. Подробности и оговорки о непроверенной квалификации — docs/patent_attorney_tracker/data.json и Replies_2026-10-22. Это не проверка всех новых писем после 22.10.
- Michael, Ken и Scott 22.10 отправлены по пять архивов (15 писем), согласно локальному журналу SEND_LOG_FINAL.json. Получение/прочтение и заключение договора этим не подтверждены. Найденные оригинальные проекты Ali нужно передать дополнительно при согласованном продолжении работы; в ходе этой ревизии они никому не отправлялись.
- Российские ответы: PATENTUS готов учесть частично готовые материалы, обещал уточнённую смету; «Зуйков и партнёры» запросили реквизиты для NDA; «Союзпатент» подтвердил получение; «Городисский» отказал из-за загрузки. Оценки цен — предварительные условия самих фирм, не принятые предложения.
- Реестр финансирования: 16 оплат на 22 593 USD (18 593 через UpCounsel и 4 000 напрямую), в том числе аванс 6 400 за NPPA №1. Это рабочая сверка источников; не подтверждение подписания PBK долга или оплаты PCT. Действительная уступка/recordation в изученных материалах не установлены.
- В клиентском PCT-каркасе §2 заполнен проверенными номерами и датами, убрана некорректная привязка provisional к continuation-in-part и категоричная фраза о проверке приоритета только судом. Технический текст и формула требуют работы нового поверенного. USPTO MPEP 211/211.05: https://www.uspto.gov/web/offices/pac/mpep/s211.html.

### Что остаётся открытым

1. Выбранный и нанятый поверенный, окончательная смета, NDA и календарь подготовки/подачи.
2. Сопоставление всех будущих пунктов формулы с точными поданными PPA и чертежами; отдельно проверить новые признаки адвокатского проекта.
3. Подписанная уступка PBK → Михаил, полномочия по действующей редакции устава, право на приоритет и регистрация уступки.
4. Комплектность поданных рисунков PPA №9/№10 и правильная единая нумерация новых рисунков.
5. Заявитель, получающее ведомство, уполномоченный представитель и полная стоимость PCT; различать подготовку/координацию и подачу. Источник правил представительства: https://www.wipo.int/pct/en/texts/rules/r83.html.
6. Подтверждение подачи NPPA/PCT: официального номера новой заявки и квитанции в изученных материалах нет.

## Исторический конспект от 20.10.2026
'''
if '## Актуализация по ревизии 23.10.2026' not in orig:write(context,orig.replace(heading,heading+updates,1))

report=['# Ревизия патентного проекта — 23 октября 2026','',
'Проверены C:\\Start-up, доступная история ChatGPT «Таблица контроля NPPA», контекст текущего Codex-чата и рабочие документы vird. Исходные документы Start-up сохранены. Перенесены отсутствовавшие файлы, исправлен рабочий реестр и добавлен актуальный контекст.','',
'## Что проверено и добавлено','',
f"Файлов в Start-up: {summary['files']}; различных содержимых SHA-256: {summary['unique_content']}. Совпадающих с файлами проекта: {summary['status_counts'].get('existing_identical',0)}; добавлено новых уникальных копий: {summary['status_counts'].get('imported_new',0)}; повторов новых копий учтено ссылками: {summary['status_counts'].get('duplicate_of_new_copy',0)}. Ошибок инвентаризации: {len(summary['errors'])}.",
'', 'Дополнительно из исходного письма Ali скачаны два оригинала: описание DOCX и 22-страничные чертежи PDF. Для 135 новых/восстановленных PDF, DOCX и текстовых источников выполнено извлечение текста без ошибок; для 9 позднее добавленных файлов других форматов проведён только учёт и копирование. Документы DOC старого формата, сканы и изображения не объявляются полностью прочитанными.','',
'Истории чатов технически не сливались. В этот проект добавлены сохранённый ответ ChatGPT, читабельная копия и ссылки на источники. Доступный инструмент вернул пять блоков ChatGPT и hasMore=false; полноту исторического архива это не гарантирует. Экспорт текущего Codex-чата инструментом не поддерживается; использованы видимая история и файлы проекта.','',
'## Существенные находки','']
for f in findings: report += [f"### {f['id']}. {f['title']}",'',f['detail'],'',f"**Источник:** {f['source']}",'',f"**Сделано:** {f['action']}",'']
report+=['## Номера, названия и даты заявок','', 'Полный исправленный реестр: ../USPTO_PPA_FILING_REGISTRY_RU.md; машиночитаемые данные VERIFIED_PPA_REGISTRY.csv/.json. Источник каждой записи — сохранённый официальный индекс Patent Center.','']
for r in registry:report += [f"- PPA №{r['ppa']}: {r['number']}, {r['filing_ru']}. {r['title']}."]
report+=['','## Что ещё нужно подтвердить','',
'1. Официальную подачу NPPA/PCT: номера/квитанции новой подачи в проверенном наборе не установлены.','2. Подписанную уступку, действующий устав PBK, полномочия подписанта и цепочку прав.','3. Окончательный выбор поверенного, NDA, смету и принятие ответственности за календарь.','4. Поддержку каждого будущего пункта формулы в исходных поданных PPA, включая сочетания признаков и новые рисунки.','5. Неподанные или встроенные рисунки PPA №9/№10.','6. Отдельные условия PCT: заявитель, ведомство, представитель, пошлины, приоритетные документы.','7. Получение всех пяти архивов кандидатами и передачу им восстановленного проекта Ali при согласовании.','',
'## Где читать и продолжать','',
'- PATENT_CONTEXT_UNIFIED_RU.md в docs — актуальный конспект для продолжения этого чата.','- STARTUP_INVENTORY.csv — полный список файлов, контрольные суммы и путь каждой копии.','- source_additions/ — новые для проекта исходные файлы; структура Start-up сохранена.','- evidence/ — письма Ali и его оригинальные проекты.','- CHATGPT_NPPA_CONTROL_READABLE_RU.md — содержимое доступного чтения другого чата.','- before_revision/ — версии документов до правок.','- ATTORNEY_HANDOFF_ADDENDUM_EN.txt — пояснение новому поверенному о найденных оригиналах; не отправлено.','',
'Ревизия охватывает состав файлов, данные дат/номеров и документированные статусы. Она не является построчной экспертизой всех 646 файлов, заключением о патентоспособности, действительности уступки или достаточности приоритета. Новых писем, платежей, найма и подач в ходе ревизии не выполнялось.']
write(BASE/'REVISION_REPORT_RU.md','\n'.join(report)+'\n');write(BASE/'REVISION_REPORT_RU.txt','\n'.join(report)+'\n')
write(BASE/'ATTORNEY_HANDOFF_ADDENDUM_EN.txt','''CONFIDENTIAL - ADDENDUM TO THE OCTOBER 22 REVIEW PACKAGE
Prepared October 23, 2026. Not sent.

The previous READ_FIRST_EN.txt stated that no separately identified attorney nonprovisional draft from Ali had been located. That statement is superseded by this addendum.

Two original attachments from Ali Shalchi's email of October 15, 2026 have now been recovered:
1. NPPA #1 Draft Spec (covering PPA#3-7).docx (48,361 bytes).
2. NPPA #1 Draft Figures (covering PPA#3-7).pdf (544,272 bytes; 22 drawing sheets).

These are attorney working drafts, separate from the client memo and PCT skeleton. Their contents, claim support, inventorship, drawings and priority particulars require final review; no filing is established by these files. Ali's October 20 email says he will not resume NPPA #1 or assignment work and recommends coordinated new counsel.

The corrected saved-record filing dates for group 1 are:
63/947,909 - December 23, 2025
63/955,179 - January 6, 2026
63/959,439 - January 13, 2026
63/961,839 - January 16, 2026
63/975,643 - February 4, 2026

The client-prepared skeleton is not the attorney draft. Please reconcile them with the actual filed provisional disclosures before drafting or relying on any priority date. This addendum is an internal prepared handoff note; it does not authorize paid work or filing.
''')

guide=ROOT/'docs/ali_submission/send/00_INSTRUKCIYA_OTPRAVKI_RU.md'
if guide.exists():
    backup(guide);g=guide.read_text(encoding='utf-8')
    note='''> ОБНОВЛЕНИЕ 23.10.2026: инструкция ниже историческая. Ali уточнил, что PPA №3–7 объединяются в одну NPPA №1, а не подаются по очереди отдельными NPPA. С 20.10 Ali отказался продолжать работу. Актуальные исполнители и документы: docs/PATENT_CONTEXT_UNIFIED_RU.md и docs/patent_audit_2026-10-23/REVISION_REPORT_RU.md.

'''
    if not g.startswith('> ОБНОВЛЕНИЕ 23.10.2026'):write(guide,note+g)

drafts=BASE/'evidence/Ali_original_drafts_2026-10-15'
evidence=[{'filename':p.name,'bytes':p.stat().st_size,'sha256':sha(p),'gmail_message_id':'1a1418866b36c835','local_path':str(p)} for p in drafts.iterdir() if p.is_file()]
write(BASE/'RECOVERED_ALI_FILES.json',json.dumps(evidence,ensure_ascii=False,indent=2))
import zipfile
with zipfile.ZipFile(BASE/'RECOVERED_ALI_DRAFTS_FOR_REVIEW.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in drafts.iterdir():
        if p.is_file():z.write(p,p.name)
    z.write(BASE/'ATTORNEY_HANDOFF_ADDENDUM_EN.txt','READ_FIRST_ADDENDUM_EN.txt')
print(json.dumps({'inventory':summary,'registry_rows':len(registry),'findings':len(findings),'ali_originals':len(evidence)},ensure_ascii=True))
