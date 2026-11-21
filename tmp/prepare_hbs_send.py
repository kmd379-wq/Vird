from pathlib import Path
import json, base64
base=Path(r'C:/Users/kmd37/Projects/vird/docs/patent_attorney_tracker/Replies_2026-10-24')
text=(base/'UAE_ADVISER_EMAIL_UPDATED_21828_EN.txt').read_text(encoding='utf-8')
text=text.replace('Dear colleagues,','Dear Salah and Myriam,')
old='Please confirm what is covered by our existing service arrangement, the fee for additional work and the completion timeline. Additional paid services require prior agreement. The target is a signing-ready package in the first half of November 2026.'
new='As we are working to a tight deadline, please complete the requested review and prepare the necessary documents within two days of receiving this email. Please confirm promptly that you can meet this deadline and immediately identify any missing documents needed from me.\n\nPlease confirm whether this work is covered by our annual service fee. If any part falls outside our annual service arrangement, please provide the scope and cost in writing in advance and obtain my written approval before starting any additional chargeable work.'
assert old in text
text=text.replace(old,new)
subject='Urgent: PBK patent rights assignment - two-day request and USD 21,828 reconciliation'
body=text.split('\n\n',1)[1]
(base/'HBS_EMAIL_FINAL_EN.txt').write_text('To: Salah Azaiez <salah@dubai-investissement.com>, Myriam Razim <myriam@hbsdubai.com>\nSubject: '+subject+'\n\n'+body,encoding='utf-8')
print(json.dumps({'subject':subject,'body':body,'pdf':base64.urlsafe_b64encode((base/'PBK_Kozin_Reconciliation_21828_EN.pdf').read_bytes()).decode().rstrip('=')}))
