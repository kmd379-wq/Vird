from pathlib import Path
import zipfile, hashlib, json

root=Path(r'C:\Users\kmd37\Projects\vird')
out=root/'docs/patent_attorney_tracker/ZUYKOV_PACKAGE_2026-10-23'
out.mkdir(exist_ok=True)
items={}
def add(name,data,source):
    if name in items:
        assert items[name][0]==data, name
    items[name]=(data,source)
for part in range(1,6):
    src=Path(r'C:\Start-up\Attorney_Review_2026-10-22')/f'Patent_Review_Part_{part}_of_5.zip'
    with zipfile.ZipFile(src) as z:
        for info in z.infolist():
            if info.is_dir(): continue
            name=info.filename
            if name.lower().endswith('read_first_en.txt'): continue
            if name=='Registry/Portfolio_Registry.json': continue
            if name=='Supplemental/NPPA1_Client_Skeleton_NOT_FILED_EN.md': continue
            add(name,z.read(info),str(src)+'::'+name)
def file(src,dest):
    p=root/src
    add(dest,p.read_bytes(),str(p))
for name in ['ALI_NPPA1_Draft_Spec.docx','ALI_NPPA1_Draft_Figures.pdf']:
    file('docs/patent_audit_2026-10-23/evidence/Ali_original_drafts_2026-10-15/'+name,'Ali_NPPA1_Originals/'+name)
for name in ['ALI_2026-10-15_ORIGINAL_EN.txt','ALI_2026-10-20_ORIGINAL_EN.txt']:
    file('docs/patent_audit_2026-10-23/evidence/'+name,'Ali_NPPA1_Originals/'+name)
for name in ['VERIFIED_PPA_REGISTRY.csv','VERIFIED_PPA_REGISTRY.json']:
    file('docs/patent_audit_2026-10-23/'+name,'Registry/'+name)
file('docs/USPTO_PPA_FILING_REGISTRY_RU.md','Registry/REGISTRY_RU.md')
file('docs/ali_submission/NPPA1_PCT_Specification_Skeleton_EN.md','Supplemental/NPPA1_Client_Skeleton_NOT_FILED_EN.md')
file('docs/ali_submission/NPPA1_Modular_Cabinet_Platform_RU.md','Supplemental/NPPA1_Client_Memo_RU.md')
for p in (root/'docs/ali_review_2026-10-13/originals/USPTO/Patent Center document indexes').glob('*.pdf'):
    add('Registry/Patent_Center/'+p.name,p.read_bytes(),str(p))
for p in (root/'docs/pbk_execution_2026-10-14').glob('*.pdf'):
    add('Ownership/UNSIGNED_REVIEW_DRAFTS/'+p.name,p.read_bytes(),str(p))
readme='''КОНФИДЕНЦИАЛЬНО. Комплект для оценки объёма, стоимости и сроков «Зуйков и партнёры». 23.10.2026.

PPA_01–PPA_10: доступные архивные комплекты описаний, рисунков, форм и квитанций. Редактируемые документы не являются удостоверенными копиями поданной версии; сверить с официальными записями.
Ali_NPPA1_Originals: оригинальный проект Ali в Word (описание и формула), 22 листа рисунков PDF и письма передачи/прекращения работы. Это полученные результаты работы Ali, не подтверждение подачи NPPA №1. Полнота его внутреннего дела не утверждается.
Supplemental: клиентские пояснения, дополнительные рисунки и каркас PCT. Каркас НЕ является работой Ali или поданной заявкой.
Registry: проверенные номера/даты и индексы Patent Center. Дата квитанции не всегда совпадает с датой подачи.
Ownership: уставные материалы, лицензия, проекты передачи прав. Подписание и регистрация уступки PBK → Михаил не подтверждены. Две редакции устава требуют сверки. Финансовый акт — проект, не подтверждение признанного долга.

Запрашивается смета на российскую охрану по материалам PPA №1–10 (обоснованное число заявок предложить) и отдельно на две PCT:
Группа 1: PPA №3–7, Modular Cabinet Platform; использовать пригодную работу Ali.
Группа 2: PPA №1,2,8,9, AI Pricing & Retail Intelligence Platform.
PPA №10: отдельное изобретение; отдельную PCT считать только дополнительной опцией.
Контрольные даты для проверки: 11.12.2026 группа 2; 23.12.2026 группа 1. PPA №10 подана 04.08.2026.

Личные сведения по сообщению клиента: гражданин РФ, единственный изобретатель всех десяти PPA; постоянный ВНЖ Испании более 25 лет, недвижимость и семья там, значительное летнее пребывание; основное проживание Шарджа, ОАЭ; Emirates ID более трёх лет, налоговый резидент ОАЭ, инженерный бизнес. В документах заявитель PBK. Выбор заявителя PCT, полномочия представителя и подтверждающие документы необходимо проверить.

Просим полную смету и календарь к концу понедельника 26.10.2026 по московскому времени: гонорары, пошлины, рисунки, переводы, внешние специалисты, налоги, правки и сопровождение после подачи; что исключено. Если окончательная цена невозможна, дать диапазон/предел, допущения и конкретный список недостающего. Платная экспертиза, подача и регистрация уступки требуют отдельного согласования.
По PPA №9 отдельные рисунки могли отсутствовать в архивном комплекте: проверить поданную версию и необходимые дополнения. Доступные материалы не гарантируют поддержку всех признаков ранними приоритетами.
Старое сообщение о том, что проекты Ali не найдены, устарело: оригиналы включены в этот архив.
Этот комплект не содержит предложений конкурирующих поверенных и внутренних сравнительных оценок. Исходные файлы сохранены без изменения.
'''
add('00_READ_FIRST_RU.txt',readme.encode('utf-8-sig'),'Prepared for this handoff')
letter=(root/'docs/patent_attorney_tracker/Reply_Drafts_2026-10-23/01_ZUYKOV_RU.txt').read_text(encoding='utf-8-sig')
deadline='''Прошу направить к концу понедельника, 26 октября 2026 года, по московскому времени коммерческое предложение по всему запрашиваемому объёму и календарный план работ. Отдельно укажите российские заявки по материалам PPA №1–10 и две PCT по группам №1 и №2, с учётом уже выполненной Ali работы по NPPA №1. Просьба включить гонорары, пошлины, рисунки, переводы, внешних специалистов, налоги, число раундов правок, этапы оплаты и сопровождение после подачи, а также перечислить исключения. Подтвердите возможность соблюдения декабрьских сроков. Если окончательная смета пока невозможна, прошу в тот же срок дать обоснованный диапазон или предельную стоимость, допущения и список недостающего.

Для вашей оценки подготовлен единый комплект PPA №1–10, реестр и документы по правам, а также оригинальные проекты описания с формулой и 22 листов рисунков Ali по NPPA №1. Прошу сообщить удобный защищённый способ передачи архива после согласования NDA. Получение материалов не является поручением на платную работу или подачу.

'''
letter=letter.replace('С уважением,\n',deadline+'С уважением,\n')
(out/'LETTER_ZUYKOV_RU.txt').write_text(letter,encoding='utf-8-sig')
manifest=[{'path':n,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'source':s} for n,(d,s) in sorted(items.items())]
(out/'MANIFEST_INTERNAL.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
public=[{k:v for k,v in x.items() if k!='source'} for x in manifest]
add('FILE_LIST.json',json.dumps(public,ensure_ascii=False,indent=2).encode('utf-8'),'Generated manifest')
archive=out/'ZUYKOV_PPA1-10_ALI_NPPA1_REVIEW.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for n,(d,s) in items.items(): z.writestr('ZUYKOV_REVIEW/'+n,d)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for n,(d,s) in items.items(): assert z.read('ZUYKOV_REVIEW/'+n)==d
result={'files':len(items),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'verified':True}
(out/'VERIFICATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
