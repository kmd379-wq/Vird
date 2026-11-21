import fs from 'node:fs/promises';
const dir=new URL('.',import.meta.url),d=JSON.parse(await fs.readFile(new URL('data.json',dir),'utf8')),sent=JSON.parse(await fs.readFile(new URL('sent_regional.json',dir),'utf8'));
const folder=new URL('NPPA2_Outreach_2026-10-21/SENT/',dir);await fs.mkdir(folder,{recursive:true});
let log='ОТПРАВЛЕНО — 10 писем\nGmail подтвердил SENT. Доставка/прочтение адресатами и отображение в интерфейсе UpCounsel отдельно не подтверждены.\n\n';
for(const s of sent){if(!s.result.label_ids?.includes('SENT'))throw Error('Not sent');
const r=d.rows.find(r=>r.id===s.key);const url='https://mail.google.com/mail/u/0/#sent/'+s.result.id;
const summary='Согласованный региональный запрос: '+r.plannedScope.replace(/Черновик\./g,'')+' Единые 10 вопросов, NDA, сроки и раздельная смета; ответ запрошен к 22.10.';
if(!d.events.some(e=>e.id===s.result.id)){d.events.push({id:s.result.id,company:s.key,date:s.date,direction:'Исходящее',subject:s.subject,summary,url,attachment:'Нет'});r.outgoing++;}
r.sent+='; '+s.date.slice(0,10)+': отправлен региональный запрос из 10 вопросов, группы1/2 и отдельная опция PCT';r.plannedScope=r.plannedScope.replace('Черновик.','Отправлено.');r.next='Ожидать ответ на региональное задание и смету; запросили к 22.10.2026';r.nppa2Quote=r.nppa2Quote.replace('не получена','не получена — запрос отправлен');
await fs.writeFile(new URL(s.key+'.txt',folder),'ОТПРАВЛЕНО\nДата UTC: '+s.date+'\nКому: '+s.to+'\nТема: '+s.subject+'\nGmail: '+url+'\n\n'+s.body);
log+=r.name+'\n'+s.date+'\n'+url+'\n\n';}
d.questionnaire.status='Отправлено 10 региональных писем; 4 иных иностранных кандидата приостановлены';
await fs.writeFile(new URL('data.json',dir),JSON.stringify(d,null,2));await fs.writeFile(new URL('SEND_CONFIRMATION_RU.txt',folder),log);await fs.copyFile(new URL('sent_regional.json',dir),new URL('receipts.json',folder));
console.log('10 sent copies saved; events '+d.events.length);
