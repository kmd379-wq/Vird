from pathlib import Path
import shutil,zipfile,json,hashlib
from pypdf import PdfReader
root=Path('C:/Users/kmd37/Projects/vird')
src=Path('C:/Start-up/PPA_01-10_Проверка_2026-10-06/PPA_01-10_from_MVP_2026-10-04')
out=root/'outputs/Attorney_Review_2026-10-22';out.mkdir(parents=True,exist_ok=True)
groups=[[1,2],[3,4,5],[6,7,8,9],[10]]
manifest=[]
for idx,nums in enumerate(groups,1):
    zpath=out/f'Patent_Review_Part_{idx}_of_5.zip'
    with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
        for n in nums:
            files=sorted((src/f'PPA_{n:02d}').rglob('*'))
            for f in files:
                if not f.is_file():continue
                if f.suffix.lower() not in ['.pdf','.docx']:continue
                name=f'PPA_{n:02d}/{f.name}'
                z.write(f,name);manifest.append({'part':idx,'name':name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
extra=[
('docs/ali_submission/NPPA1_Modular_Cabinet_Platform_EN.md','Supplemental/NPPA1_Client_Memo_EN.md'),
('docs/ali_submission/NPPA1_PCT_Specification_Skeleton_EN.md','Supplemental/NPPA1_Client_Skeleton_NOT_FILED_EN.md'),
('docs/ali_submission/send/NPPA1/NPPA1_Supplemental_Figures_EN.pdf','Supplemental/NPPA1_Supplemental_Figures_EN.pdf'),
('docs/ali_review_2026-10-13/registry.json','Registry/Portfolio_Registry.json'),
('docs/ali_review_2026-10-13/originals/PBK_MOA_51_pages_previously_received.pdf','Ownership/PBK_MOA_51_pages.pdf'),
('docs/ali_review_2026-10-13/originals/PBK_Memorandum_received_2026-10-13.pdf','Ownership/PBK_Memorandum_alternate_version.pdf'),
('docs/ali_review_2026-10-13/originals/PBK_Trade_Licence_38769.pdf','Ownership/PBK_Trade_Licence.pdf')]
readme='''CONFIDENTIAL — MATERIALS FOR SCOPE AND FEE ASSESSMENT ONLY
Five independent ZIP parts, not a split archive; open each normally.
Parts 1–4: available archived PPA #1–10 file sets, including specifications, drawings where present, editable source documents, forms and receipts. These local copies require counsel verification against official records; editable files are not certified filed versions.
Part 5: client-prepared supplementary NPPA #1 memo and skeleton (NOT a completed attorney draft or filed application), supplemental figures, registry, Patent Center indexes and ownership review documents.
US scope: NPPA #1 = PPAs #3–7; NPPA #2 = PPAs #1,2,8,9; assignment/USPTO recordation. PPA #10 is supplied as portfolio background, not authorization for a third US application. Russian filings are handled separately by Russian counsel.
PCT is a separate option requiring confirmation of applicant, receiving Office, authorized representative, fees and deadlines. Russian citizenship and residence in Sharjah, UAE; do not assume the PBK-to-Kozin assignment has been completed.
Earliest reported provisional dates: group #2 December 11, 2025; group #1 December 23, 2025. Verify dates, disclosure support, ownership and all applicable filing deadlines.
Ownership PDFs dated October 15 are client-prepared review drafts. No completed execution or USPTO recordation is asserted. Two versions of the PBK memorandum are supplied for reconciliation; determine which is operative.
Known gaps: no separately identified completed nonprovisional attorney draft by Ali was located in the assembled sources. The included client skeleton must not be attributed to Ali. PPA #9 has no separate figures PDF in its archived set; please check figures within the specification and identify anything missing. The separately available PPA #1 official filing receipt is included in Part 5.
Please provide an itemized fixed fee or cap, exclusions, payment milestones, drawing/translation/associate costs, official fees and calendar milestones. Identify missing materials before giving a final quote. No paid substantive review, filing or engagement is authorized by receipt of this package.
'''
(out/'READ_FIRST_EN.txt').write_text(readme,encoding='utf8')
with zipfile.ZipFile(out/'Patent_Review_Part_5_of_5.zip','w',zipfile.ZIP_DEFLATED) as z:
    z.write(out/'READ_FIRST_EN.txt','READ_FIRST_EN.txt')
    for rel,name in extra:
        f=root/rel;z.write(f,name);manifest.append({'part':5,'name':name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
    for f in (root/'docs/ali_review_2026-10-13/originals/USPTO/Patent Center document indexes').glob('*.pdf'):z.write(f,'Registry/'+f.name)
    for f in Path('C:/Start-up/PBK_PDF_ДЛЯ_ПОДПИСИ_15-10-2026').glob('*_EN.pdf'):z.write(f,'Ownership/UNVERIFIED_EXECUTION_'+f.name)
    z.write('C:/Users/kmd37/Downloads/PPA-1 (-244) official filing receipt.pdf','Registry/PPA01_Official_Filing_Receipt.pdf')
(out/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
for zpath in out.glob('*.zip'):
    with zipfile.ZipFile(zpath) as z:assert z.testzip() is None
    print(zpath.name,zpath.stat().st_size)
print('PPA9 specification pages:',[(p.name,len(PdfReader(p).pages)) for p in (src/'PPA_09').rglob('SPEC*.pdf')])
