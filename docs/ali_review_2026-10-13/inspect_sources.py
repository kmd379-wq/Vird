from pathlib import Path
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image,ImageOps,ImageDraw
import json,re
root=Path(__file__).parent
qa=root/'qa';qa.mkdir(exist_ok=True)
records=[]
for p in sorted((root/'originals').rglob('*.pdf')):
    if p.name.startswith('._'):continue
    d=pdfium.PdfDocument(str(p))
    for i,page in enumerate(d):
        im=page.render(scale=1.2).to_pil(); dest=qa/(p.stem+f'_{i+1}.png');im.save(dest)
        records.append(dest)
for k in range(0,len(records),6):
    sheet=Image.new('RGB',(1500,1550),'#dddddd');draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(records[k:k+6]):
        im=Image.open(p);im.thumbnail((485,720));x=(j%3)*500;y=(j//3)*775
        sheet.paste(im,(x,y+35));draw.text((x+5,y+5),p.stem,fill='black')
    sheet.save(qa/f'sources_{k//6+1}.jpg')
reg=[]
for n in range(1,11):
    p=root/'extracted'/f'PPA#{n} Patent Center Index.txt';t=p.read_text(encoding='utf8')
    num=re.search(r'(\d{2}/\d{3},\d{3})',t).group(1)
    title=t.split('| -:',1)[1].split('PRIVATE VIEW')[0].strip().replace('\n',' ')
    date=re.search(r'\(c\) date\s*(\d{2}/\d{2}/\d{4})',t).group(1)
    reg.append(dict(ppa=n,number=num,date=date,title=title,source=p.name))
(root/'registry.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(reg,ensure_ascii=False,indent=2))
