import json,hashlib,zipfile,csv
from pathlib import Path
from pypdf import PdfReader
B=Path(__file__).resolve().parent
data=json.loads((B/'STARTUP_INVENTORY.json').read_text(encoding='utf-8'))
backups={hashlib.sha256(p.read_bytes()).hexdigest():str(p) for p in (B/'before_revision').rglob('*') if p.is_file()}
for row in data:
    if row['status']=='existing_identical' and row['sha256'] in backups:
        old=backups[row['sha256']]
        if old not in row['existing_project_paths']: row['existing_project_paths'].append(old)
(B/'STARTUP_INVENTORY.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
with (B/'STARTUP_INVENTORY.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader()
    for row in data:w.writerow({**row,'existing_project_paths':' | '.join(row['existing_project_paths'])})
errors=[]
for row in data:
    copies=[Path(row['imported_path'])] if row.get('imported_path') else [Path(x) for x in row['existing_project_paths']]
    if not any(p.exists() and p.stat().st_size==row['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'] for p in copies): errors.append(row['source_path'])
registry=json.loads((B/'VERIFIED_PPA_REGISTRY.json').read_text(encoding='utf-8'))
assert len(registry)==10
assert len(PdfReader(B/'REVISION_REPORT_RU.pdf').pages)==4
assert len(PdfReader(B/'evidence/Ali_original_drafts_2026-10-15/ALI_NPPA1_Draft_Figures.pdf').pages)==22
with zipfile.ZipFile(B/'RECOVERED_ALI_DRAFTS_FOR_REVIEW.zip') as z:
    assert z.testzip() is None
    assert len(z.namelist())==3
assert not errors, errors
result={'checked_startup_file_references':len(data),'verified_registry_rows':10,'report_pages':4,'ali_drawing_pages':22,'handoff_archive_entries':3,'missing_or_changed_copies':errors}
(B/'VERIFICATION_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result))
