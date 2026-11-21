from pathlib import Path
import json, html, zipfile

BASE=Path(__file__).resolve().parent
OUT=BASE/'PCT_ONLY_OUTREACH_2026-10-27'
OUT.mkdir(exist_ok=True)
reg=json.loads((BASE.parent/'patent_audit_2026-10-23/VERIFIED_PPA_REGISTRY.json').read_text(encoding='utf-8-sig'))
registry='\n'.join(f"PPA #{r['ppa']}: {r['number']} — {r['filing_iso']} — {r['title']}" for r in reg)

ru='''Мы приняли решение в первую очередь подготовить и подать две международные заявки PCT от имени PBK. Просим подготовить проект договора с фиксированным объёмом услуг, стоимостью и календарным графиком. Отдельные одновременные национальные подачи в США и России, а также национальные фазы в первоначальный объём не включаем. PPA №10 остаётся отдельным проектом и в эти две заявки не входит.

Остальные ранее обсуждавшиеся этапы проекта сохраняются: мы планируем приступить к их выполнению после подачи обеих PCT. Их объём, стоимость и сроки будут согласованы отдельно с учётом применимых сроков. На данном этапе просим заключить договор на подготовку и подачу PCT с предусмотренным международным сопровождением; это не означает отказа от дальнейшей работы по проекту.

1. Состав заявок и сроки

PCT №1 — Modular Cabinet Platform, PPA №3–7: модульная архитектура торгового шкафа, реконфигурируемый каркас, самовыравнивание, сменные секции, совместная обработка сигналов датчиков при извлечении товара, токенизированный/биометрический доступ и подключаемые тепловые и жидкостные модули. Рабочая ранняя дата — 23.12.2025; контрольная дата — 23.12.2026. Желаемая дата подачи — 03.12.2026.

PCT №2 — AI Pricing & Retail Intelligence Platform, PPA №1, 2, 8, 9: динамическое ценообразование с учётом срока годности, свежести и порчи; биометрический контроль доступа к ограниченным товарам; контроль качества продукции, проверенная обратная связь и управление взаимодействием с поставщиками. Рабочая ранняя дата — 11.12.2025; контрольная дата — 11.12.2026. Желаемая дата подачи — 28.11.2026. Эта группа требует первоочередного внимания по срокам.

Группировка — исходное задание для вашей оценки. Просим проверить даты по официальным документам, поддержку приоритета и единство изобретения. Если требуются изменения состава заявок, заранее объясните причины и влияние на стоимость и сроки. Не предполагается, что любое новое описание или рисунок автоматически получает раннюю дату PPA.

2. Имеющиеся материалы

Имеются поданные описания PPA, рисунки в составе соответствующих подач, официальные квитанции и индексы USPTO, рабочий реестр и дополнительные пояснения. По группе №1 имеется подготовленный Ali Shalchi редактируемый английский проект описания NPPA №1 с формулой и рефератом, а также PDF из 22 листов рисунков. Это незавершённые рабочие материалы, не подтверждение подачи NPPA. Просим использовать пригодную работу после проверки и адаптировать её для PCT. Ali прекратил представительство; его участие в новой работе не предполагается.

По группе №2 требуется подготовить полный комплект на основе четырёх PPA; завершённого проекта, аналогичного группе №1, нет. По имеющейся предварительной проверке в тексте PPA №9 упоминаются FIG. 1–8, но рисунки в поданной версии не обнаружены. Просим проверить это и включить необходимые рисунки в объём и смету, разграничив иллюстрирование исходного раскрытия и новые сведения.

Просим подтвердить, какие материалы вы уже получили, и одним перечнем указать недостающее для окончательного расчёта. Дополнительные схемы следует отличать от фактически поданных рисунков. Сведения о других связанных подачах, публичных раскрытиях, продажах и предшествующем поиске не следует считать отсутствующими без уточнения: задайте конкретные вопросы, если эти сведения необходимы.

3. Заявитель и личные сведения

Планируемый заявитель — PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO, Дубай, ОАЭ, лицензия №38769. PBK указана заявителем в имеющемся реестре предварительных заявок; просим проверить документы для выбранного порядка подачи. Адрес по уставу: IFZA Business Park, DDP, PO Box 342001, Dubai, UAE. Я подтверждаю, что устав на 51 странице является действующей редакцией; я единственный участник компании. В корпоративных материалах я указан генеральным менеджером; необходимые актуальные подтверждения полномочий прошу перечислить.

Лицензия действует до 10.12.2026; её продлением занимается обслуживающая компания в Дубае. Имеются лист реквизитов, лицензия и устав; укажите, что ещё необходимо и как безопасно передать документы.

Я — Михаил Дмитриевич Козин, в патентных материалах Mikhail Kozin, единственный изобретатель по десяти PPA. Гражданин России, постоянно проживаю в Шардже, ОАЭ, имею Emirates ID более трёх лет и являюсь налоговым резидентом ОАЭ. Имею постоянный ВНЖ Испании более 25 лет, недвижимость там; семья проводит там большую часть времени, я также часто бываю в Испании. Имею 17 международных патентов в машиностроении. Эти личные сведения следует отличать от правоспособности PBK как заявителя. Копии удостоверений личности предоставлю по конкретному запросу через согласованный безопасный канал.

Относительно принадлежности прав прошу указать конкретно необходимые документы и подтверждения. Если требуется моё заявление, подготовьте его для подписи. Предложите необходимый объём проверки и укажите, включён ли он в цену. Не требую от вас исходить из непроверенного юридического вывода о достаточности имеющихся документов.

4. Услуга под ключ и представитель

Прошу включить подготовку описания, формулы, реферата и рисунков; проверку согласованности и поддержки приоритетов; подготовку заявления и приоритетных документов, включая DAS, где применимо; окончательную проверку, фактическую подачу, организацию оплаты пошлин и контроль уведомлений.

Назовите ответственного специалиста, его организацию и регистрационный номер. Укажите получающее ведомство, допустимые поисковые органы и рекомендуемый вариант с обоснованием и стоимостью. Подтвердите право конкретного представителя действовать именно для PBK при выбранной схеме. Предлагаемый язык подачи — английский, русский перевод необходим для моего обсуждения и согласования.

Я не буду самостоятельно юридически проверять комплект, заполнять ePCT или отправлять заявки. Предпочтителен один основной исполнитель, который организует привлечённого представителя и отвечает по договору за порученные ему действия. Если необходим отдельный договор PBK с представителем, организуйте его подготовку и чётко распределите обязанности, стоимость и ответственность между исполнителями. Необходимые лично мои подписи на договоре, доверенности или заявлениях прошу заранее перечислить и подготовить документы.

5. Обсуждение, переводы и правки

Моя роль — пояснить работу изобретения, указать пропущенные элементы, важные технические особенности и деловые приоритеты. Юридический текст, формулу и проверку английской редакции готовит исполнитель. Прошу включить два консолидированных раунда моих замечаний по каждой полной заявке и одно письменное обсуждение стратегии формулы.

Обсуждения и мои замечания будут на русском. Перевод проектов, вопросов и пояснений на русский, а также внесение моих замечаний в английскую редакцию должны входить в согласованную фиксированную стоимость. Исправление ошибок исполнителя или привлечённых им специалистов и формальных недостатков по их вине не расходует клиентские раунды и не оплачивается дополнительно. Новые материалы или изменение объёма по моей инициативе оплачиваются только после отдельного письменного согласования.

6. Договор, календарь и полная стоимость

До аванса прошу направить проект договора и отдельный расчёт по каждой PCT: фиксированные гонорары, рисунки, переводы, представитель, пошлины подачи и поиска, приоритетные документы, комиссии платформы и банков, налоги и прочие расходы. Укажите включённые услуги и исключения. По переменным расходам дайте обоснованный диапазон и основания изменения; профессиональные услуги прошу оценить фиксированно, а не только тарифом «от».

По каждому платежу: сумма и валюта, получатель, назначение, дата либо событие оплаты, соответствующий результат работы и статус суммы — фиксированная или предварительная. Нужны три итога: сколько оплачивается при начале, сколько до каждой подачи и сколько позднее. Оплата — только по официальным счетам организаций; пошлины и расходы третьих лиц отражаются отдельно с подтверждением оплаты. Дополнительные работы и превышения согласованных сумм требуют моего письменного согласия.

Просим дать календарные даты начала, первого полного проекта, обоих раундов обсуждения, окончательного согласования и фактической подачи, а также сроки материалов и ответов с моей стороны. Укажите резерв до контрольных дат, порядок предупреждения о риске задержки и договорную ответственность за нарушение сроков по вине исполнителя. Если желаемые даты 28.11 и 03.12 недостижимы, сразу предложите конкретный безопасный график.

7. Завершение этапов

Подготовка и подача завершены после подачи обеих PCT и передачи по каждой: полного фактически поданного комплекта с русским переводом; официального подтверждения международного номера и установленной даты подачи; поданных приоритетных сведений; подтверждений всех пошлин, подлежащих оплате на этом этапе; краткого отчёта об оставшихся действиях и сроках. Не должно оставаться уже сообщённых ведомством формальных недостатков, устранение которых входит в обязанности исполнителя.

Включите сопровождение уведомлений получающего и поискового ведомств до получения отчёта международного поиска и письменного заключения, их передачу с пояснениями и рекомендациями на русском. Эта часть завершается после передачи указанных документов и рекомендаций по обеим заявкам. Отдельно обозначьте, включаются ли содержательные ответы, дополнительные поиски при отсутствии единства и процедуры главы II; дополнительные платные действия — только по отдельному согласованию. Обязанность бесплатно исправлять ошибки исполнителя сохраняется после окончания этапа. Выдача патентов и национальные фазы в текущий результат не входят.

Просим подтвердить возможность работы на этих условиях, предложить договор, расчёт и график и сообщить дату, когда вы их предоставите. Если предварительная оценка платная, сначала укажите её фиксированную или предельную стоимость, результат и срок. Настоящее письмо не является принятием договора, разрешением на платную работу или поручением на подачу.

С уважением,
Михаил Козин

Справочный перечень PPA (даты в формате ГГГГ-ММ-ДД; сверить с официальными документами; №10 вне текущего объёма):
{registry}
'''

en='''We have decided to prioritize the preparation and filing of two international PCT applications in PBK's name. Please provide a draft engagement agreement with a fixed scope, fees and a dated schedule. Separate simultaneous US and Russian national filings and national-phase entries are not part of this initial scope. PPA #10 remains a separate project and is not included in these two applications.

The other previously discussed stages of the project remain planned: we intend to proceed with them after both PCT applications have been filed. Their scope, fees and schedule will be agreed separately, taking applicable deadlines into account. At this stage, we are requesting an engagement for PCT preparation and filing with the specified international-phase support; this does not mean that we are abandoning the subsequent project work.

1. Applications and dates

PCT #1 — Modular Cabinet Platform, PPAs #3–7: reconfigurable cabinet chassis, self-leveling, modular bays, sensor-fusion retrieval, tokenized/biometric access, and plug-in thermal/fluid processing modules. Working earliest priority date: December 23, 2025; control deadline: December 23, 2026. Requested filing date: December 3, 2026.

PCT #2 — AI Pricing & Retail Intelligence Platform, PPAs #1, #2, #8 and #9: expiration-, freshness- and spoilage-based dynamic pricing, biometric-gated restricted-goods functions, produce quality control, verified feedback and supplier governance. Working earliest priority date: December 11, 2025; control deadline: December 11, 2026. Requested filing date: November 28, 2026. This group is more urgent in terms of timing.

This grouping is the starting point for your assessment. Please verify dates against official records, priority support and unity of invention. Explain any necessary regrouping and its cost and timing implications before proceeding. New descriptions or figures are not assumed automatically to benefit from a provisional filing date.

2. Available materials

Available materials include the filed PPA specifications, drawings included in the respective filings, USPTO receipts and indexes, a working register, and supplementary explanations. For Group 1, Ali Shalchi prepared an editable English NPPA #1 draft specification with claims and abstract and a 22-sheet drawing PDF. These are unfinished working drafts, not evidence that an NPPA has been filed. Please retain useful work after review and adapt it for PCT. Ali has ended his representation; his participation in new work should not be assumed.

Group 2 needs a complete application prepared from four PPAs; there is no completed draft comparable to Group 1. A preliminary review indicated that PPA #9 refers to FIG. 1–8, but drawings were not located in the filed version. Please verify this and include necessary drawing work in your scope and budget, distinguishing illustration of the original disclosure from new subject matter.

Please confirm which materials you have received and provide one consolidated list of anything missing for a final quote. Supplementary diagrams must be distinguished from filed drawings. Do not assume that no related filings, public disclosures, sales or prior-art searches exist; ask specific questions where this information is needed.

3. Applicant and personal information

The proposed applicant is PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO, Dubai, UAE, trade licence No. 38769. PBK is identified as applicant in our provisional filing register; please verify the documents for the proposed filing route. The registered address in the Memorandum is IFZA Business Park, DDP, PO Box 342001, Dubai, UAE. I confirm that the 51-page Memorandum and Articles is the current version and that I am the sole shareholder. Corporate materials identify me as General Manager; please specify any current evidence of authority needed.

The licence expires on December 10, 2026. Renewal is being handled by my Dubai corporate services provider. An address sheet, licence and Memorandum are available. Please specify any other documents required and a secure transfer method.

I am Mikhail Dmitrievich Kozin, named Mikhail Kozin in the patent records, and the sole inventor in the ten PPAs. I am a Russian citizen, principally resident in Sharjah, UAE, have held an Emirates ID for over three years and am a UAE tax resident. I have held Spanish permanent residence for over 25 years and own property there; my family spends most of its time there and I also spend substantial time in Spain. My engineering background includes 17 international patents in mechanical engineering. Please distinguish these personal circumstances from PBK's eligibility as applicant. Identity documents can be supplied upon a specific request through an agreed secure channel.

Please specify exactly which ownership documents and confirmations you need. If a declaration from me is required, prepare it for signature. Propose the necessary review scope and state whether it is included in your fee. You should not rely on an unverified legal conclusion that the current documents are sufficient.

4. End-to-end service and representation

Please include preparation of the description, claims, abstract and drawings; consistency and priority-support checks; preparation of the request and priority documents, including DAS where applicable; final checks, actual filing, arranging official-fee payments and monitoring notices.

Identify the responsible practitioner, firm and registration number, proposed receiving Office, competent search authorities and your recommended option with reasons and costs. Confirm the specific representative's eligibility to act for PBK under that arrangement. English is the proposed filing language, with Russian translations for my discussion and approval.

I will not personally conduct legal checks, complete ePCT forms or submit applications. I prefer one lead service provider who arranges an authorized representative and accepts contractual responsibility for the tasks delegated to them. If a separate PBK engagement with the representative is needed, arrange its preparation and clearly allocate duties, fees and responsibility. Identify and prepare documents genuinely requiring my personal signature, such as the engagement agreement, powers of attorney or factual declarations.

5. Discussions, translations and revisions

My role is to explain how the invention works, identify omissions, important technical features and business priorities. The service provider prepares the legal text and claims and checks the English version. Please include two consolidated client revision rounds for each complete application and one written discussion of claim strategy.

My discussions and comments will be in Russian. Russian translations of drafts, questions and explanations, and incorporation of my comments into the English text, must be included in the agreed fixed fee. Correction of errors by the provider or its specialists and formal deficiencies attributable to them must not consume client revision rounds or attract additional fees. New material or a scope change at my request requires separate written agreement before additional paid work.

6. Agreement, schedule and full cost breakdown

Before an advance payment, please provide the draft engagement and a separate calculation for each PCT: fixed professional fees, drawings, translations, representative, filing and search fees, priority documents, platform and bank charges, taxes and other expenses. Identify inclusions and exclusions. For variable expenses give a reasoned range and adjustment basis; please quote fixed professional fees rather than only starting rates.

For every payment, specify amount and currency, payee, purpose, payment date or trigger, corresponding deliverable, and whether fixed or estimated. Please show totals payable at commencement, before each filing, and subsequently. Payment will be against official invoices issued by the relevant organizations; official fees and third-party costs must be separately itemized with payment evidence. Extra work and increases require my prior written agreement.

Give calendar dates for commencement, first complete drafts, both revision rounds, final approval and actual filing, together with deadlines for my materials and responses. Identify the contingency margin, warning procedure for delay risks, and contractual responsibility for missed deadlines attributable to the provider. If November 28 and December 3 are not achievable, immediately propose a specific safe alternative schedule.

7. Completion and deliverables

Preparation and filing are complete once both PCTs have been filed and I have received for each: the complete filed package and Russian translation; official confirmation of the international application number and established international filing date; priority particulars as filed; evidence of all official fees due at that stage; and a brief report of outstanding actions and dates. No already-notified formal deficiencies within the provider's responsibilities should remain unresolved.

Include monitoring of receiving-Office and searching-authority notices through receipt of the international search report and written opinion, and delivery of those documents with explanations and recommendations in Russian. This part ends when those documents and recommendations have been delivered for both applications. Separately identify whether substantive responses, additional unity-related searches and Chapter II procedures are included; extra paid action requires separate approval. The obligation to correct provider errors free of charge survives completion. Patent grants and national phases are outside the current deliverables.

Please confirm whether you can work on these terms and provide the engagement, cost breakdown and schedule, stating when these will be available. If an initial assessment is chargeable, first specify its fixed or capped fee, deliverables and timing. This message does not accept an engagement, authorize paid work or instruct a filing.

Kind regards,
Mikhail Kozin

Reference PPA list (dates YYYY-MM-DD; subject to verification against official records; #10 outside current scope):
{registry}
'''

# Candidate-specific openings: facts are sourced in the local audit and Gmail reads.
people=[
('01_John_Moetteli','John Moetteli / Da Vinci Partners','moetteli@davincipartners.com','assistant@davincipartners.com','1a17489855cddb75',
'Уважаемый господин Moetteli!\n\nБлагодарю за подтверждение проверки конфликта и предложения о представительстве. Подтверждаю, что я не нахожусь в санкционном списке. Теперь основной вариант — подача от PBK. Прошу сначала оценить представительство для этой компании через надлежащего партнёра. Если вы всё же считаете необходимым созаявителя, представьте отдельный вариант договора с точной долей/территорией, фиксированной ценой обратного перехода, сроком исполнения по моему требованию, ограничением самостоятельных действий созаявителя и всеми расходами. Это просьба о предложении, а не согласие передать права или назначить созаявителя. Если подготовка оценки платная, согласуем её цену до начала.\n\n',
'Dear Mr. Moetteli,\n\nThank you for confirming conflict clearance and outlining representation options. I confirm that I am not on a sanctions list. The principal proposal is now filing in PBK\'s name. Please first assess representation for that company through an eligible partner. If you still consider a co-applicant necessary, please provide a separate contractual option specifying the exact share/territory, fixed reassignment price, timing upon my request, restrictions on unilateral action by the co-applicant, and all costs. This requests a proposal; it does not authorize a transfer or appointment of a co-applicant. Any chargeable assessment must be priced and approved before work starts.\n\n'),
('02_Scott_Polk','Darryl Scott / Daniel Polk','6adafa577e44923f53980189-6adafa577344950001c8ee3c@msgs.upcounsel.com','','1a16761e9a1e0385',
'Уважаемые Darryl и Daniel!\n\nБлагодарю за предварительную оценку проекта №1 и предложение привлечь представителя ОАЭ. Прошу превратить этот вариант в конкретное предложение: назвать представителя, определить его роль, общую цену и распределение ответственности. Пять частей технического пакета были направлены вам 22 октября; подтвердите комплектность и отдельно наличие последних проектов Ali. Отдельный NDA не ставлю условием: прошу подтвердить профессиональную конфиденциальность сведений как моих, так и PBK, включая доступ сотрудников и внешних специалистов.\n\n',
'Dear Darryl and Daniel,\n\nThank you for your initial assessment of Group 1 and the suggestion to involve a UAE representative. Please turn that option into a concrete proposal identifying the representative, role, total fee and allocation of responsibility. Five parts of the technical review package were sent to you on October 22; please confirm completeness and separately confirm receipt of Ali\'s latest drafts. I am not making a separate NDA a condition; please confirm professional confidentiality for both my information and PBK\'s, including access by employees and outside specialists.\n\n'),
('03_Ken_Emanuelson','Ken Emanuelson','6ad8f1244c02967b16232afb-6ad8f1247344950001c8e25b@msgs.upcounsel.com','','1a15f6dfe860e30f',
'Уважаемый Ken!\n\nБлагодарю за готовность лично работать над проектом. Теперь прошу оценить именно две PCT, включая подготовку, а не только подачу готового комплекта по тарифу сайта. Пять частей пакета были направлены 22 октября; подтвердите получение и наличие последних проектов Ali. Для ясности: 11 и 23 декабря 2025 года — ранние даты подачи PPA, а декабрь 2026 года — контрольные сроки следующей подачи. Отдельный NDA не ставлю условием; прошу подтвердить профессиональную конфиденциальность информации моей и PBK, включая сотрудников и внешних специалистов.\n\n',
'Dear Ken,\n\nThank you for your willingness to handle the matter personally. Please now quote specifically for two PCT applications, including preparation rather than only filing a completed package at a website rate. Five parts of the package were sent on October 22; please confirm receipt and availability of Ali\'s latest drafts. For clarity, December 11 and 23, 2025 are the earliest provisional filing dates; December 2026 dates are the subsequent-filing control deadlines. I do not require a separate NDA; please confirm professional confidentiality covering my information and PBK\'s, including employees and outside specialists.\n\n'),
('04_Niq_Howard','Niq Howard','6ade002093195a03ac38c347-6ade00207344950001c8f74d@msgs.upcounsel.com','','1a1733085364a375',
'Уважаемый Niq!\n\nБлагодарю за пояснения о предварительном анализе и конфиденциальности. Новое первоочередное задание — две PCT от имени PBK, а не отдельная работа по уступке десяти PPA. Ваш прежний расчёт 300 USD за заявку на уступку не следует считать ценой настоящего задания. Понимаю, что проверка конфликта и оценка у вас платные: прежде чем оформлять найм, прошу назвать ставку, предельную сумму, срок и результат этого предварительного этапа, а также регистрационный номер ответственного поверенного. Укажите, можете ли вы организовать весь новый объём с уполномоченным представителем. Отдельный NDA не требуется при подтверждённой профессиональной конфиденциальности моей информации и PBK.\n\n',
'Dear Niq,\n\nThank you for clarifying your preliminary-review and confidentiality terms. The new immediate scope is two PCT applications in PBK\'s name, rather than a standalone assignment of ten PPAs. Your earlier USD 300-per-application assignment quote should not be treated as a quote for this scope. I understand that your conflict check and assessment are chargeable: before hiring, please specify the hourly rate, capped amount, timing and deliverables of that initial stage and the responsible attorney\'s registration number. Please confirm whether you can arrange the entire revised scope with an authorized representative. A separate NDA is not required if professional confidentiality for both my information and PBK\'s is confirmed.\n\n'),
('05_Zuykov','Зуйков и партнёры / Надежда Краснянская','krasnyanskaya@zuykov.com','patent@zuykov.com','1a1785de93756e2c',
'Уважаемая Надежда!\n\nБлагодарю за предварительные тарифы и подтверждение получения русского пакета 26 октября (PC34749RU00). Просьба пересчитать задание на две PCT, без одновременных российских подач. Нужна фиксированная цена всего объёма, а не цена «от» за объект. Учтите переданные материалы и сообщите одним списком, чего не хватает. В прежнем предложении упоминалась подача через Роспатент: прошу проверить подходящий порядок именно для PBK — компании ОАЭ, назвать полномочного представителя, получающее ведомство и доступный поисковый орган. Расчёт пошлин должен соответствовать заявителю-компании. Указанные вами 15 рабочих дней относятся к проекту: просим также зафиксировать даты обсуждения и фактической подачи. По ранее обсуждавшемуся NDA прошу сообщить результат согласования защиты сведений PBK и моих сведений. Вся переписка и расчёт нужны на русском.\n\n',
'Dear Ms. Krasnyanskaya,\n\nThank you for your preliminary rates and confirmation of receipt of the Russian package on October 26 (PC34749RU00). Please revise the scope to two PCTs without simultaneous Russian filings, quoting a fixed total rather than starting rates per subject. Please identify missing materials in one list. Your earlier proposal referred to filing through Rospatent; please verify a suitable route specifically for PBK, a UAE company, and identify the eligible representative, receiving Office and competent search authority. Official fees must reflect the corporate applicant. Your 15-working-day period concerns a draft; please also specify review and actual-filing dates. Please update us on the previously discussed NDA protection for both PBK and me. Correspondence and the quotation are requested in Russian.\n\n'),
('06_PATENTUS','PATENTUS / Никита Гензер','n.genzer@patentus.ru','','1a1689ac89678880',
'Уважаемый Никита!\n\nБлагодарю за предложение 220 000 рублей за одну PCT без переводов, пошлин и иностранных коллег. Прошу подготовить окончательный совокупный расчёт двух PCT по новому заданию ниже, включив необходимую подготовку и русский перевод в фиксированную стоимость услуг. Одновременные российские заявки сейчас не заказываем. Укажите безопасный способ передачи полного технического пакета и завершения ранее обсуждавшегося соглашения о конфиденциальности для меня и PBK. Не предполагаю, что полный комплект уже находится у вас. Прошу назвать ответственного поверенного и представителя для подачи от PBK.\n\n',
'Dear Mr. Genzer,\n\nThank you for quoting RUB 220,000 per PCT excluding translations, official fees and foreign associates. Please provide a final aggregate calculation for the two PCTs under the scope below, including necessary preparation and Russian translations within fixed professional fees. We are not ordering simultaneous Russian applications. Please identify a secure method to supply the complete technical package and complete the previously discussed confidentiality arrangement covering both PBK and me. I do not assume that you already have the complete package. Please identify the responsible practitioner and the representative eligible to file for PBK.\n\n'),
('07_Sojuzpatent','Союзпатент','info@sojuzpatent.com','','1a15dd4ac509169c',
'Уважаемые коллеги!\n\nБлагодарю за подтверждение получения прежнего запроса. Уточняю первоочередной объём: две PCT от PBK. Просим назначить ответственного специалиста и подтвердить готовность подготовить договор, полную смету и календарь. Укажите, какие материалы необходимы для расчёта и как их безопасно передать; наличие у вас полного пакета пока не предполагаем.\n\n',
'Dear colleagues,\n\nThank you for acknowledging our earlier inquiry. The immediate scope is now two PCTs in PBK\'s name. Please appoint a responsible practitioner and confirm whether you can provide an engagement agreement, full quotation and schedule. Identify the materials needed for pricing and a secure transfer channel; we do not assume you already hold the full package.\n\n'),
('08_ARS_Patent','АРС-Патент / Павел Мишуров','office@ars-patent.com','fadeev@ars-patent.com','1a1530a49d719c3b',
'Уважаемый Павел, уважаемые коллеги!\n\nВ автоответе Кирилла Осипова было указано, что запрос передаётся Павлу Мишурову. Просим подтвердить, кто может рассмотреть его сейчас, с учётом декабрьских сроков. Первоначальный объём изменён: прежде всего две PCT от PBK, подробности ниже. Просим назвать недостающие материалы, безопасный канал передачи и срок подготовки договора, сметы и графика.\n\n',
'Dear Mr. Mishurov and colleagues,\n\nMr. Osipov\'s out-of-office reply stated that the inquiry would be forwarded to Mr. Mishurov. Please confirm who can consider it now given the December deadlines. The initial scope has changed to prioritizing two PCTs for PBK as detailed below. Please identify missing materials, a secure transfer channel and when you can provide the agreement, quote and schedule.\n\n')]

manifest=[]
for key,name,to,cc,mid,opening_ru,opening_en in people:
    for lang,opening,common in [('RU',opening_ru,ru),('EN',opening_en,en)]:
        subject='Две PCT от PBK — проект договора, фиксированная стоимость и график' if lang=='RU' else 'Two PCT applications for PBK — engagement agreement, fixed fees and schedule'
        text=f"Кому / To: {to}\nКопия / Cc: {cc or '—'}\nТема / Subject: {subject}\n\n"+opening+common.format(registry=registry)
        (OUT/f'{key}_{lang}.txt').write_text(text,encoding='utf-8-sig')
    manifest.append(dict(key=key,name=name,to=to,cc=cc,reply_message_id=mid,status='DRAFT_NOT_SENT',kind='full',send_language='RU' if key[:2]>='05' else 'EN'))

declined=[
('09_Latscha','Silvan Latscha','latscha@lspartner.ch','1a15f67302eed5ed','Вы ранее сообщили об ограничениях представительства физического лица. Теперь предполагаемый заявитель — PBK, компания ОАЭ.','You previously explained representation limitations for an individual applicant. The proposed applicant is now PBK, a UAE company.'),
('10_Keller','Keller Schneider','j.hoppler@kellerschneider.com','1a154b9ae7a0817d','Понимаю ваш прежний отказ из-за загрузки. Если возможность участия не появилась, достаточно кратко подтвердить это.','I understand your earlier workload-related refusal. If availability has not changed, a brief confirmation is sufficient.'),
('11_Gorodissky','Городисский и Партнёры','pat@gorodissky.com','1a15876a33bcedde','Понимаю ваш прежний отказ из-за загрузки. Если возможность участия не появилась, достаточно кратко подтвердить это.','I understand your earlier workload-related refusal. If availability has not changed, a brief confirmation is sufficient.'),
('12_Patent_Boutique','Chris Rodger / Patent Boutique','chris.rodger@patent.boutique','1a1596f04c0f87df','Учитываю ваш ответ об отсутствии специалистов по электронике и программному обеспечению. Эти составляющие в проекте сохраняются.','I acknowledge that you do not have electronics/software specialists. Those aspects remain part of the project.'),
('13_Katzarov','Gilles Pfend / Katzarov','gilles.pfend@katzarov.com','1a152de173541d77','Учитываю ваш прежний отказ от представительства. Новый запрос не предполагает, что вы приняли поручение.','I acknowledge your earlier refusal to act. This new inquiry does not assume that you have accepted any engagement.'),
('14_Anthony','Anthony Whittington','awhittington@ideaparlorlaw.com','1a164a9767d138f5','Учитываю ваш повторный отказ и не направляю дополнительные технические материалы.','I acknowledge your repeated refusal and am not providing further technical materials.'),
('15_Saam','Christophe Saam','saam@patentattorneys.ch','1a152ed0ca7b4951','Учитываю сообщённый вами возможный конфликт интересов. Не прошу раскрывать его обстоятельства и не направляю технические материалы.','I acknowledge the potential conflict you identified. I am not asking you to disclose its circumstances and am not sending technical materials.')]
for key,name,to,mid,reason_ru,reason_en in declined:
    # No attempt to reverse a conflict refusal or repeat a declined technical review.
    askru='Если ваша позиция остаётся прежней, дополнительных действий не требуется.' if key.startswith(('14','15')) else 'Если при новом объёме вы можете организовать подготовку и подачу через надлежащего представителя, прошу подтвердить возможность и запросить необходимые материалы для договора, фиксированной сметы и графика. Если нет — достаточно краткого ответа; прошу не начинать платную оценку.'
    asken='If your position remains unchanged, no further action is required.' if key.startswith(('14','15')) else 'If you can arrange preparation and filing through an eligible representative under this revised scope, please confirm and identify the materials needed for an engagement agreement, fixed quotation and schedule. Otherwise a brief reply is sufficient; please do not start a paid assessment.'
    for lang,reason,ask in [('RU',reason_ru,askru),('EN',reason_en,asken)]:
        content=(f'Уважаемые коллеги!\n\n{reason}\n\nСообщаю об изменении первоочередного объёма: две PCT от имени PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO (ОАЭ): группа №1 — PPA №3–7, группа №2 — PPA №1, 2, 8, 9. Отдельные одновременные национальные заявки не включаются в текущий этап. Остальные ранее обсуждавшиеся этапы проекта сохраняются; приступить к ним планируем после подачи обеих PCT, отдельно согласовав объём, стоимость и сроки с учётом применимых сроков. Желаемые даты подачи — 03.12.2026 и 28.11.2026 соответственно; контрольные даты по рабочему реестру — 23.12.2026 и 11.12.2026, подлежащие проверке поверенным.\n\n{ask}\n\nЭто информационный запрос, не поручение и не разрешение на платную работу.\n\nС уважением,\nМихаил Козин' if lang=='RU' else f'Dear colleagues,\n\n{reason}\n\nThe immediate scope has changed to two PCTs in the name of PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO (UAE): Group 1, PPAs #3–7, and Group 2, PPAs #1, #2, #8 and #9. Separate simultaneous national applications are excluded from the current stage. The other previously discussed project stages remain planned; we intend to start them after both PCTs have been filed, with scope, fees and schedule agreed separately taking applicable deadlines into account. Requested filing dates are December 3 and November 28, 2026 respectively; working control deadlines are December 23 and December 11, 2026, subject to counsel\'s verification.\n\n{ask}\n\nThis is an informational inquiry, not an engagement or authorization for paid work.\n\nKind regards,\nMikhail Kozin')
        (OUT/f'{key}_{lang}.txt').write_text(f'To: {to}\nSubject: '+('Изменение объёма — две PCT от PBK' if lang=='RU' else 'Revised scope — two PCTs for PBK')+'\n\n'+content,encoding='utf-8-sig')
    manifest.append(dict(key=key,name=name,to=to,reply_message_id=mid,status='OPTIONAL_DRAFT_NOT_SENT',kind='prior_refusal',send_language='RU' if key.startswith('11') else 'EN'))

notes='''ПИСЬМА КАНДИДАТАМ — 27.10.2026. ВСЕ ЧЕРНОВИКИ, НЕ ОТПРАВЛЕНЫ.

Откройте 00_Письма_на_русском.html в браузере. Там весь русский текст каждого письма. Отдельные TXT можно открыть Блокнотом и копировать в почту. EN — версии для иностранных адресатов; российским фирмам — RU.

01–08: полные запросы договора, расчёта и графика для открытых обсуждений. У Союзпатента есть только подтверждение получения, у АРС — автоответ; это не согласие вести дело.
09–15: отдельные короткие варианты для ранее отказавшихся. Рекомендуется не включать их автоматически в общую отправку. Anthony повторно отказал; Christophe Saam сообщил возможный конфликт — для них только информационные уведомления, без просьбы изучать материалы. Они не являются действующими кандидатами.
Michael: согласованное письмо уже отправлено 27.10, message id 1a17d37d48ee342e; новое дублирующее письмо не подготовлено.
Ali: прежнее представительство прекращено; в новую рассылку кандидатов не включён. Консультанты Дубая не подменяются патентными поверенными.
PATENTICA, Isler & Pedrazzini, BOHEST, Rentsch: ответов по проверенному журналу и поиску не найдено, поэтому не включены в категорию ответивших.

Важное: условия бесплатного исправления ошибок, переводов и представительства являются запросом клиента, а не уже принятыми обязательствами кандидатов. Пересылка цен и заключений Michael не предусмотрена. Подача от PBK и приоритеты подлежат проверке новым исполнителем. Письма не подтверждают подписание уступок или завершение продления лицензии.

Полные технические архивы и корпоративные документы к черновикам автоматически не прикреплялись. В письмах запрашивается перечень недостающего; нельзя утверждать, что всем получателям ранее передан полный пакет. ZIP настоящей папки предназначен только пользователю: он содержит персональные варианты для конкурирующих кандидатов, его нельзя направлять одному кандидату целиком.

Основания: актуальные чтения Gmail 27.10 и локальные отчёты 22–27.10; официальный рабочий реестр VERIFIED_PPA_REGISTRY.json. Поиск Gmail иногда возвращал RATE_LIMIT_EXCEEDED; более узкие повторные запросы выполнены успешно. Свежее повторное чтение отказа Keller не удалось; его краткий статус взят из сохранённого журнала. Квитанции USPTO заново не извлекались: номера и даты перенесены из проверенного реестра 23.10 с просьбой кандидату подтвердить их.

Перед отправкой: выбрать адресатов и подтвердить тексты; проверить свежий Reply-To (особенно UpCounsel) и отсутствие нового ответа. Отправлять только персональное письмо и согласованные материалы этого получателя. manifest.json содержит ссылки на сообщения для проверки.
'''
(OUT/'00_Порядок_использования_RU.txt').write_text(notes,encoding='utf-8-sig')
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
for lang in ['RU','EN']:
    filename='00_Письма_на_русском.html' if lang=='RU' else '00_Letters_in_English.html'
    title='Письма кандидатам: сначала две PCT — черновики' if lang=='RU' else 'PCT-first outreach — drafts, not sent'
    contents=''.join(f'<li><a href="#{p["key"]}">{html.escape(p["name"])}</a></li>' for p in manifest)
    sections=''.join(f'<section id="{p["key"]}"><h2>{html.escape(p["name"])}</h2><p class="status">'+('Полное письмо' if p['kind']=='full' else 'Ранее отказал: отдельный необязательный вариант')+'</p><pre>'+html.escape((OUT/f'{p["key"]}_{lang}.txt').read_text(encoding='utf-8-sig'))+'</pre></section>' for p in manifest)
    page=f'<!doctype html><html lang="{lang.lower()}"><meta charset="utf-8"><title>{title}</title><style>body{{max-width:1000px;margin:40px auto;padding:24px;font:17px/1.6 Arial;color:#172434;background:#f4f6f8}}section{{background:white;padding:32px;margin:32px 0;border-radius:10px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit}}a{{color:#125eab}}.status{{color:#9b420c}}@media print{{section{{break-before:page}}body{{background:white;margin:0;padding:0}}}}</style><h1>{title}</h1><p>27.10.2026 — Не отправлено. Общий файл предназначен только для просмотра пользователем.</p><ul>{contents}</ul>{sections}</html>'
    (OUT/filename).write_text(page,encoding='utf-8')
archive=BASE/'PCT_ONLY_OUTREACH_2026-10-27.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in OUT.iterdir():
        if p.is_file():z.write(p,OUT.name+'/'+p.name)
assert len(list(OUT.glob('*_RU.txt')))==16
assert len(manifest)==15
assert all((OUT/f'{p["key"]}_EN.txt').exists() for p in manifest)
assert all('63/938,244' in (OUT/f'{p["key"]}_RU.txt').read_text(encoding='utf-8-sig') for p in manifest if p['kind']=='full')
print(json.dumps({'folder':str(OUT),'full_letters':8,'optional_short_letters':7,'languages':['RU','EN'],'zip':str(archive),'sent':False},ensure_ascii=False))
