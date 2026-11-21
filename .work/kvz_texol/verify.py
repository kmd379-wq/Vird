from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree
from pathlib import Path
import sys,re
p=Path(sys.argv[1]); tmp=p.with_suffix('.tmp.docx')
with ZipFile(p) as z, ZipFile(tmp,'w',ZIP_DEFLATED) as out:
 for info in z.infolist():
  b=z.read(info.filename)
  if info.filename=='docProps/app.xml':
   root=etree.fromstring(b)
   for el in list(root):
    if etree.QName(el).localname in ['HeadingPairs','TitlesOfParts','Manager','Company','HyperlinkBase','Pages','Words','Characters','Lines','Paragraphs','CharactersWithSpaces','TotalTime']:
     root.remove(el)
   b=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
  out.writestr(info,b)
tmp.replace(p)
with ZipFile(p) as z:
 assert z.testzip() is None
 for n in z.namelist():
  if n.endswith('.xml'):
   root=etree.fromstring(z.read(n)); text=' '.join(root.itertext())
   assert not re.search(r'OZTM|ОЗТМ|Осипович|Беларус|Левченко|Чолоян|3905031160|390601001|40702810232580003712|044030786',text,re.I),n
print('Проверка ZIP, XML и удаления исходных имён и реквизитов пройдена.')
print('Размер файла:',p.stat().st_size)
