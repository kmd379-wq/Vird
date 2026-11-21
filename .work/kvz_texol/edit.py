import json,re,sys
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt
from lxml import etree
src,out,edits=sys.argv[1:]
a=json.load(open(edits,encoding='utf8'))
d=Document(src)
refs={'A':'А','B':'Б','C':'В','D':'Г','E':'Д','F':'Е','G':'Ж','H':'З','I':'И'}
def translate(s):
 for k,v in sorted(a['replace'].items(),key=lambda x:-len(x[0])): s=s.replace(k,v)
 s=re.sub(r'(Приложени[еяюим]+) ([A-I])',lambda m:m[1]+' '+refs[m[2]],s)
 return s

def settext(p,s):
 if p.text==s:return
 if p.runs:
  p.runs[0].text=s
  for r in p.runs[1:]:r.text=''
 else:p.add_run(s)

for i,p in enumerate(d.paragraphs):settext(p,a['paras'].get(str(i),translate(p.text)))
for ti,t in enumerate(d.tables):
 for ri,row in enumerate(t.rows):
  for ci,c in enumerate(row.cells):
   s=a['tables'][str(ti)][ri][ci]
   settext(c.paragraphs[0],s)
   for p in c.paragraphs[1:]:p._element.getparent().remove(p._element)
for s in d.sections:
 for story in [s.header,s.footer,s.first_page_header,s.first_page_footer,s.even_page_header,s.even_page_footer]:
  for p in story.paragraphs:settext(p,translate(p.text))
  for t in story.tables:
   for row in t.rows:
    for c in row.cells:
     for p in c.paragraphs:settext(p,translate(p.text))
for el in list(d.element.iter(qn('w:lang'))):
 el.set(qn('w:val'),'ru-RU')
for el in list(d.element.iter(qn('w:commentRangeStart')))+list(d.element.iter(qn('w:commentRangeEnd')))+list(d.element.iter(qn('w:commentReference'))):el.getparent().remove(el)
d.core_properties.author=''
d.core_properties.last_modified_by=''
d.core_properties.title='Договор КВЗ — TEXOL о техническом сопровождении'
d.core_properties.subject='Техническое сопровождение и контроль соблюдения КД/ТД'
d.core_properties.comments=''
d.save(out)
print(out)
print('LATIN REMAINS:')
for p in d.paragraphs:
 if re.search('[A-Za-z]',p.text):print(p.text)
print('HEADERS/FOOTERS:')
for s in d.sections:
 for story in [s.header,s.footer]:print([p.text for p in story.paragraphs])
print('TABLES',len(d.tables))
