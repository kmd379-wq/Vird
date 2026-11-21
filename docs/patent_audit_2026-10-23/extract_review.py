import json, re, zipfile, xml.etree.ElementTree as ET
from pathlib import Path
from pypdf import PdfReader
BASE=Path(__file__).resolve().parent
records=json.loads((BASE/'STARTUP_INVENTORY.json').read_text(encoding='utf-8'))
out=BASE/'extracted';out.mkdir(exist_ok=True)
texts=[]
for row in records:
    if row['status']!='imported_new':continue
    p=Path(row['imported_path']); text=''; meta={}
    try:
        if p.suffix.lower()=='.pdf':
            pdf=PdfReader(p);meta['pages']=len(pdf.pages)
            text='\n\n'.join(f'[PAGE {i+1}]\n'+(pg.extract_text() or '') for i,pg in enumerate(pdf.pages))
        elif p.suffix.lower()=='.docx':
            with zipfile.ZipFile(p) as z:
                root=ET.fromstring(z.read('word/document.xml'))
                text='\n'.join(''.join(el.itertext()) for el in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
        elif p.suffix.lower() in {'.txt','.md','.json','.csv'}:
            text=p.read_text(encoding='utf-8-sig',errors='replace')
        else:continue
        target=out/(row['sha256'][:12]+'.txt');target.write_text(text,encoding='utf-8')
        texts.append({'source':row['source_path'],'extracted':str(target),'characters':len(text),**meta})
    except Exception as e:texts.append({'source':row['source_path'],'error':str(e)})
for p in (BASE/'evidence'/'Ali_original_drafts_2026-10-15').glob('*'):
    if p.suffix=='.pdf':
        reader=PdfReader(p);text='\n\n'.join(f'[PAGE {i+1}]\n'+(pg.extract_text() or '') for i,pg in enumerate(reader.pages));meta={'pages':len(reader.pages)}
    elif p.suffix=='.docx':
        with zipfile.ZipFile(p) as z:
            root=ET.fromstring(z.read('word/document.xml'));text='\n'.join(''.join(t.text or '' for t in el.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')) for el in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
        meta={}
    else:continue
    target=out/(p.stem+'.txt');target.write_text(text,encoding='utf-8');texts.append({'source':str(p),'extracted':str(target),'characters':len(text),**meta})
(BASE/'EXTRACTION_INDEX.json').write_text(json.dumps(texts,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'extracted':sum('extracted' in r for r in texts),'errors':sum('error' in r for r in texts),'ali':[x for x in texts if 'ALI_NPPA1' in x['source']]},ensure_ascii=True))
