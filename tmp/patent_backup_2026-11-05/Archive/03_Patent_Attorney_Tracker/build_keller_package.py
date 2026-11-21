from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, hashlib

base=Path(__file__).parent
out=base/'KELLER_FULL_PACKAGE_2026-10-29'
out.mkdir(exist_ok=True)
source=base/'ZUYKOV_PACKAGE_2026-10-23/ZUYKOV_PPA1-10_ALI_NPPA1_REVIEW.zip'
readme='''CONFIDENTIAL - KELLER SCHNEIDER REVIEW - 29 OCTOBER 2026
Current scope supersedes historical instructions in underlying documents.
TWO PCT APPLICATIONS, PBK ENGINEERING INTELLECTUAL PROPERTY RIGHTS MANAGEMENT - FZCO (UAE) as applicant; sole inventor Mikhail Dmitrievich Kozin.
Group 1: PPAs 3-7, Modular Cabinet Platform; requested filing by 3 December 2026; working earliest priority 23 December 2025.
Group 2: PPAs 1,2,8,9, AI Pricing & Retail Intelligence Platform; requested filing by 28 November 2026 (earlier working day if necessary); working earliest priority 11 December 2025.
Verify all priority dates, ownership and support from original official records. PPA10 is background only, not a third PCT instruction. National filings/phases and assignment work are deferred for separate agreement.
Five independent ZIP archives: 1=PPA1-2; 2=PPA3-5; 3=PPA6-9; 4=PPA10; 5=Ali draft specification and 22-sheet drawings, supplemental client materials, official indexes, working registry and PBK corporate/ownership-review documents.
Ali drafts are unfinished work, not filed NPPAs. Client supplemental architecture and skeleton are not filed provisional figures or Ali-authored final specifications. No separate PPA9 drawings PDF was located; verify drawings against actual filing records.
PBK 51-page memorandum is confirmed current by the client. The alternate version is historical for comparison. Licence expires 10 December 2026; renewal is being arranged, not asserted completed. Assignment/resolution drafts do NOT establish executed transfer or recordation and are not instructions to transfer now.
Please treat all information of PBK and Mikhail Kozin as confidential. Complete conflict clearance before substantive review; contact us immediately if any conflict arises. Identify any outside UAE representative before sharing detailed materials with them.
Please provide a complete fixed-fee proposal per PCT and combined, official/search fees, translations, drawings, UAE representation, taxes, exclusions, payment milestones, draft engagement agreement, and calendar delivery/filing dates. No paid review, filing or other billable work is authorized without separate written agreement.
Each archive contains an inventory with SHA-256 hashes. Source content is preserved; file-level verification is not a legal completeness opinion.
'''
groups={i:[] for i in range(1,6)}
with ZipFile(source) as z:
 assert z.testzip() is None
 for name in z.namelist():
  if name.endswith('/'): continue
  rel=name.split('/',1)[1]
  if rel in ('00_READ_FIRST_RU.txt','FILE_LIST.json'): continue
  group=5
  if rel.startswith('PPA_'):
   num=int(rel[4:6]); group=1 if num<=2 else 2 if num<=5 else 3 if num<=9 else 4
  groups[group].append((rel,z.read(name)))
manifest=[]
for i,items in groups.items():
 fn=out/f'Keller_PBK_Patent_Materials_Part_{i}_of_5.zip'
 inv=[{'file':n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()} for n,b in items]
 with ZipFile(fn,'w',ZIP_DEFLATED) as z:
  for n,b in items:z.writestr(n,b)
  z.writestr('00_READ_FIRST_EN.txt',readme)
  z.writestr('FILE_INVENTORY.json',json.dumps(inv,ensure_ascii=False,indent=2))
 with ZipFile(fn) as z:assert z.testzip() is None
 manifest.append({'file':fn.name,'bytes':fn.stat().st_size,'source_files':len(items),'sha256':hashlib.sha256(fn.read_bytes()).hexdigest()})
(out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print(json.dumps(manifest))
