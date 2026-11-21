import csv, hashlib, json, shutil, collections
from pathlib import Path
from datetime import datetime

ROOT = Path(r'C:\Users\kmd37\Projects\vird')
SOURCE = Path(r'C:\Start-up')
OUT = Path(__file__).resolve().parent
SKIP = {'.git','node_modules','.venv','venv','.next'}
def files(root):
    import os
    for parent, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP and Path(parent,d).resolve() != OUT.resolve()]
        for name in names:
            yield Path(parent,name)
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()
existing=collections.defaultdict(list)
for p in files(ROOT):
    try: existing[(p.stat().st_size,digest(p))].append(str(p))
    except OSError: pass
rows=[]
new={}
errors=[]
for p in files(SOURCE):
    try:
        stat=p.stat(); sha=digest(p); key=(stat.st_size,sha)
        found=existing.get(key,[])
        row={'relative_path':str(p.relative_to(SOURCE)),'source_path':str(p),'bytes':stat.st_size,'sha256':sha,'modified':datetime.fromtimestamp(stat.st_mtime).isoformat(timespec='seconds'),'existing_project_paths':found,'status':'existing_identical' if found else 'missing_in_project','imported_path':None}
        if not found:
            if key in new:
                row['imported_path']=new[key];row['status']='duplicate_of_new_copy'
            else:
                # Copy document/evidence formats; preserve originals and avoid copying executables/caches.
                if p.suffix.lower() in {'.pdf','.doc','.docx','.txt','.md','.json','.csv','.xlsx','.xls','.zip','.png','.jpg','.jpeg','.svg','.eml','.html','.htm'}:
                    target=OUT/'source_additions'/p.relative_to(SOURCE)
                    target.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copy2(p,target)
                    assert digest(target)==sha
                    new[key]=str(target);row['imported_path']=str(target);row['status']='imported_new'
                else: row['status']='indexed_only'
        rows.append(row)
    except Exception as e: errors.append({'path':str(p),'error':str(e)})
(OUT/'STARTUP_INVENTORY.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (OUT/'STARTUP_INVENTORY.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader()
    for row in rows: writer.writerow({**row,'existing_project_paths':' | '.join(row['existing_project_paths'])})
summary={'source':'C:\\Start-up','files':len(rows),'total_bytes':sum(r['bytes'] for r in rows),'unique_content':len(set(r['sha256'] for r in rows)),'status_counts':dict(collections.Counter(r['status'] for r in rows)),'imported_unique_bytes':sum(r['bytes'] for r in rows if r['status']=='imported_new'),'errors':errors}
(OUT/'INVENTORY_SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=True))
