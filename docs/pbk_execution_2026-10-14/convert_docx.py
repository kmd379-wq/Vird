from pathlib import Path
import re
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
root=Path(__file__).parent
out=root/'DOCX';out.mkdir(exist_ok=True)
for source in sorted(root.glob('0*.md')):
 d=Document();sec=d.sections[0]
 sec.page_width=Inches(8.5);sec.page_height=Inches(11)
 sec.top_margin=sec.bottom_margin=Inches(.65)
 sec.left_margin=sec.right_margin=Inches(.7)
 for name,size in [('Normal',11),('Title',19),('Heading 1',14),('Heading 2',11.5)]:
  st=d.styles[name];st.font.name='Arial';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0)
  st.paragraph_format.space_after=Pt(7)
  st.paragraph_format.line_spacing=1.12
  st.paragraph_format.widow_control=True
  if name!='Normal':st.paragraph_format.keep_with_next=True
 for st in d.styles:
  for border in list(st.element.iter(qn('w:pBdr'))):border.getparent().remove(border)
 raw=re.sub(r'(?m)^(#{1,3} .+)\n(?!\n)',r'\1\n\n',source.read_text(encoding='utf8'))
 blocks=re.split(r'\n\s*\n',raw)
 expected=[]
 break_next=False
 for b in blocks:
  b=b.strip()
  if not b:continue
  if b=='---PAGE---':break_next=True;continue
  style='Normal'
  for prefix,s in [('### ','Heading 2'),('## ','Heading 1'),('# ','Title')]:
   if b.startswith(prefix):b=b[len(prefix):];style=s;break
  if source.name.startswith('02') and style=='Heading 1' and b.startswith('Приложение '):break_next=True
  p=d.add_paragraph(b,style)
  if break_next:p.paragraph_format.page_break_before=True;break_next=False
  if b.startswith(('Подпись:','За PBK, подпись','За PBK: ____________________')):p.paragraph_format.keep_together=True
  expected.append(b)
 if source.name.startswith('02'):
  signatures=False
  for p in d.paragraphs:
   if p.text=='Подписи':signatures=True
   if p.text.startswith('Приложение А'):signatures=False
   if signatures:p.paragraph_format.keep_with_next=True
 footer=sec.footer.paragraphs[0];footer.text='PBK — Mikhail Kozin | Проект для заполнения | '
 field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
 for run in footer.runs:run.font.name='Arial';run.font.size=Pt(8)
 d.core_properties.title=expected[0];d.core_properties.subject='Преобразование согласовываемого проекта от 14.10.2026 в DOCX'
 dest=out/source.with_suffix('.docx').name;d.save(dest)
 actual=[p.text for p in Document(dest).paragraphs if p.text.strip()]
 assert actual==expected,(source.name,'Text mismatch')
 print(dest)
