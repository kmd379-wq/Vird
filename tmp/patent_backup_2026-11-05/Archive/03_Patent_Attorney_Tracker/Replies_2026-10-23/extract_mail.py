from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime
from zoneinfo import ZoneInfo
import json,re
B=Path(__file__).resolve().parent
class TextParser(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,t,a):
        if t in ['style','script']:self.skip+=1
        if t in ['p','div','br','li','tr','h1','h2']:self.parts.append('\n')
        if t in ['td','th']:self.parts.append(' | ')
    def handle_endtag(self,t):
        if t in ['style','script']:self.skip=max(0,self.skip-1)
        if t in ['p','div','li','tr']:self.parts.append('\n')
    def handle_data(self,s):
        if not self.skip:self.parts.append(s)
def flatten(m):
    plain=[];html=[]
    def walk(p):
        c=p.get('body',{}).get('content')
        if c:
            if p.get('mime_type')=='text/plain':plain.append(c)
            if p.get('mime_type')=='text/html':html.append(c)
        for q in p.get('parts') or []:walk(q)
    walk(m.get('payload',{}))
    if plain:return '\n'.join(plain)
    parser=TextParser();parser.feed('\n'.join(html));return re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+','\n\n',unescape(''.join(parser.parts)))
for path in B.glob('*_MESSAGE.json'):
    m=json.loads(path.read_text(encoding='utf-8'));text=flatten(m).replace('\r\n','\n')
    (B/(m['id']+'_ORIGINAL.txt')).write_text(text,encoding='utf-8')
    if m['id']=='1a1650509ffc7b44':text=text.split('From:\n')[0].split('From: Mikhail')[0]
    if m['id']=='1a16761e9a1e0385':text=text.split('On Thu,')[0]
    (B/(m['id']+'_READABLE.txt')).write_text(text,encoding='utf-8')
    print(m['id'],len(text))
