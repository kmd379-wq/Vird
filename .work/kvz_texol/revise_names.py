from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree
import sys,re
src,out=sys.argv[1:]
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
fullru='Акционерное общество «Калининградский вагоностроительный завод» (АО «КВЗ»)'
pbkru='Компания «Пи-Би-Кей Инжиниринг Интеллекчуал Проперти Райтс Менеджмент — ФЗКО» («ПБК»)'
pbken='Компания PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO («PBK»)'
def edit(text):
 return text.replace(fullru,'KVZ').replace(pbkru,pbken).replace('АО «КВЗ»','KVZ').replace('КВЗ','KVZ').replace('ПБК','PBK')
with ZipFile(src) as z,ZipFile(out,'w',ZIP_DEFLATED) as o:
 for info in z.infolist():
  b=z.read(info.filename)
  if info.filename.endswith('.xml'):
   root=etree.fromstring(b)
   if info.filename.startswith('word/'):
    for p in root.xpath('//w:p',namespaces=ns):
     nodes=p.xpath('.//w:t',namespaces=ns)
     old=''.join(n.text or '' for n in nodes)
     new=edit(old)
     if new!=old and nodes:
      nodes[0].text=new
      for n in nodes[1:]:n.text=''
   elif info.filename.startswith('docProps/'):
    for n in root.iter():
     if n.text:n.text=edit(n.text)
   b=etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
  o.writestr(info,b)
with ZipFile(out) as z:
 assert z.testzip() is None
 for n in z.namelist():
  if n.endswith('.xml'):
   root=etree.fromstring(z.read(n))
   txt=' '.join(root.itertext())
   assert not re.search('КВЗ|ПБК|Пи-Би-Кей|Калининградский|ОЗТМ|OZTM|Осипович|Беларус|Левченко|Чолоян|3905031160|390601001|40702810232580003712|044030786',txt),n
from docx import Document
d=Document(out)
assert len(d.tables)==12
print('Проверка пройдена: 12 таблиц; названия компаний на английском; исходные ФИО и реквизиты отсутствуют.')
for i in [4,8,13,14,15]:print(d.paragraphs[i].text)
print('Все английские слова в основном тексте и таблицах:')
t=' '.join(p.text for p in d.paragraphs)+' '+' '.join(c.text for tb in d.tables for row in tb.rows for c in row.cells)
print(sorted(set(re.findall('[A-Za-z]+',t))))
