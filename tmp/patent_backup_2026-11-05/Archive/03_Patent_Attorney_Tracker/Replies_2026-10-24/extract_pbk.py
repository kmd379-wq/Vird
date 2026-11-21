from pathlib import Path
import zipfile,json
from pypdf import PdfReader
p=Path(__file__).parent
src=Path(r'C:\Start-up\Attorney_Review_2026-10-22\Patent_Review_Part_5_of_5.zip')
with zipfile.ZipFile(src) as z:
 for n in z.namelist():
  if n.startswith('Ownership/') and n.endswith('.pdf'):
   dest=p/Path(n).name
   dest.write_bytes(z.read(n))
   r=PdfReader(dest)
   dest.with_suffix('.txt').write_text('\n'.join('[PAGE %d]\n%s'%(i+1,x.extract_text()) for i,x in enumerate(r.pages)),encoding='utf-8')
   print(dest.name,len(r.pages))
