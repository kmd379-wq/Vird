import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=new URL('.',import.meta.url);
const data=JSON.parse(await fs.readFile(new URL('data.json',dir),'utf8'));
const wb=Workbook.create();
const headers=['ID','Компания / поверенный','Страна','Контактное лицо','Канал / адрес','Статус','Последний ответ','Что отправили мы','NDA','Выкладка задач','Технические материалы','Срок ответа','Следующий шаг','Финансовая позиция'];
function col(i){let s='';for(i++;i;i=Math.floor((i-1)/26))s=String.fromCharCode(65+(i-1)%26)+s;return s;}
function sheet(name,heads,rows,widths,title,note){
const s=wb.worksheets.add(name);s.showGridLines=false;
s.getRange('A2:F2').merge();s.getRange('A2').values=[[title]];
s.getRange('A3:H3').merge();s.getRange('A3').values=[[note]];
s.getRange('A2').format.font={name:'Arial',size:16,bold:true};
s.getRange('A3').format.font={name:'Arial',size:10,color:'#526070'};
s.getRange('A3:H3').format.wrapText=true;s.getRange('A3:H3').format.rowHeight=32;
s.getRange('A5:'+col(heads.length-1)+(rows.length+5)).values=[heads,...rows];
const all=s.getRange('A5:'+col(heads.length-1)+(rows.length+5));all.format.font={name:'Arial',size:11};all.format.wrapText=true;all.format.verticalAlignment='top';
all.format.rowHeight=name==='Журнал писем'?95:125;
s.getRange('A5:'+col(heads.length-1)+'5').format.fill='#E5EBF0';s.getRange('A5:'+col(heads.length-1)+'5').format.font={bold:true};s.getRange('A5:'+col(heads.length-1)+'5').format.rowHeight=40;
widths.forEach((w,i)=>s.getRange(col(i)+'5:'+col(i)+(rows.length+5)).format.columnWidth=w);
s.freezePanes.freezeRows(5);
const table=s.tables.add('A5:'+col(heads.length-1)+(rows.length+5),true,name==='Реестр'?'Candidates':name==='Финансы'?'Finance':name==='Единые вопросы'?'Questions':'MailLog');
table.style='TableStyleLight1';
s.getRange('A5:'+col(heads.length-1)+'5').format.fill='#243746';
s.getRange('A5:'+col(heads.length-1)+'5').format.font={name:'Arial',size:11,bold:true,color:'#FFFFFF'};
if(name==='Финансы') s.getRange('D6:F'+(rows.length+5)).setNumberFormat('#,##0');
return s;}
const keys=['id','name','country','person','contact','status','reply','sent','nda','tasks','materials','due','next','finance'];
sheet('Реестр',headers,data.rows.map(r=>keys.map(k=>r[k])),[13,32,20,31,32,27,53,53,36,48,30,20,44,58],'Патентные поверенные — единый реестр','Обновлено 22.10.2026. Только PPA №1–10 / NPPA / PCT / уступка. Финансовая позиция — последняя графа.');
const finances=[
['PATENTUS','RUB','Поиск / РФ / PCT — отдельные позиции',85000,150000,220000,'Не уточнены','Не уточнены','Не уточнён','Не получена','21.10.2026','Письмо 1a15e1404e984422','Цены «от», не складывать без согласования объёма'],
['Darryl Scott','USD','Уступка + NPPA; PCT не подтверждён',null,null,null,'400 — по контексту, не проверено','Разница 360 — требует пояснения','3645 — по контексту','Не получена','20.10.2026','docs/PATENT_CONTEXT_UNIFIED_RU.md, строки 63–71','4500 услуги / 5260 сумма — не подтверждено оригиналом'],
['Anthony Whittington / IdeaParlor Legal P.C.','USD','Историческая оценка; 22.10 отказ',null,null,null,'Не включены','Не уточнены','Не уточнён','Не получена','21.10.2026','Письмо 1a15f0c01788bb4a','ОТКАЗ 22.10.2026. Прежние 7250 USD недействующее предложение'],
['Ken Emanuelson','USD','Подача готовой заявки — тариф сайта 1200; подготовка отдельно',null,null,null,'Не включены','Не уточнены','Не уточнён','Не получена','21.10.2026','https://emanuelsonfirm.com/pricing/','Не индивидуальная смета; услуги иностранных коллег отдельно. Договоры почасово.'],
...data.rows.filter(r=>!['patentus','scott','ali','anthony','ken'].includes(r.id)).map(r=>[r.name,'Не указана',r.status==='Отказ'?'Отказ':r.tasks,null,null,null,'Не получены','Не получены','Не получен',r.status==='Отказ'?'Не применимо':'Не получена','21.10.2026','См. журнал писем',r.finance]),
['Ali Shalchi','USD','Историческая оплата, не кандидат',null,null,null,'Не относится к новой смете','Не относится','6400 — исторический аванс','Не применимо','20.10.2026','История переписки; письмо об отказе','Отдельный учёт прежних платежей; не сравнивать с новыми ценами']
];
sheet('Финансы',['Компания','Валюта','Объём предложения','Поиск от','Заявка РФ от','PCT от','Пошлины','Налоги / платформа','Аванс','Итоговая полная смета','Дата сведений','Источник','Условия сравнения'],finances,[32,15,53,18,18,18,32,35,34,28,20,48,62],'Финансовое сравнение предложений','Разные объёмы и валюты не суммируются. Пустые суммы означают отсутствие цены, а не ноль. Итоговый рейтинг пока невозможен.');
const ev=[...data.events].sort((a,b)=>new Date(a.date)-new Date(b.date));
const dateFmt=new Intl.DateTimeFormat('ru-RU',{timeZone:'Europe/Madrid',dateStyle:'short',timeStyle:'short'});
sheet('Журнал писем',['Дата и время — Мадрид','Компания','Направление','Тема','Выдержка / содержание','Вложения','Источник Gmail','ID письма'],ev.map(e=>[dateFmt.format(new Date(e.date)),data.rows.find(r=>r.id===e.company)?.name,e.direction,e.subject,e.summary,e.attachment,e.url,e.id]),[25,34,18,64,84,20,45,24],'История переписки с кандидатами','18–22.10.2026. Выдержки из писем; оригиналы доступны по ссылкам. Автоответ не означает согласия вести дело.');
const candidates=data.rows.filter(r=>r.questionnaire);
sheet('Единые вопросы',['Компания','Расширение задания','1 Объём','2 Команда','3 PCT полномочия','4 Приоритеты','5 График','6 Материалы Ali','7 NDA','8 Страхование / рекомендации','9 Смета','10 Условия начала','Запрошенный срок ответа','Цена NPPA2'],candidates.map(r=>[r.name,r.plannedScope,...r.questionnaire,'22.10.2026 — не согласован',r.nppa2Quote]),[34,48,39,39,42,39,39,40,42,43,48,43,28,42],'Одинаковые 10 вопросов — NPPA №1 + №2','Старые ответы; новые региональные запросы отправлены. 10 региональных писем отправлены. Подписанных NDA и общей сметы нет.');
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Реестр!A5:F8',tableMaxRows:4,tableMaxCols:6,maxChars:1500})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?',options:{useRegex:true,maxResults:10},summary:'Ошибки'})).ndjson);
await fs.mkdir(new URL('../../outputs/patent_tracker/',dir),{recursive:true});
const out=new URL('../../outputs/patent_tracker/PATENT_ATTORNEYS_REGISTER_RU.xlsx',dir);
await (await SpreadsheetFile.exportXlsx(wb)).save(out.pathname.replace(/^\/(\w:)/,'$1'));
for(const [s,r,f] of [['Реестр','L6:N8','registry'],['Единые вопросы','A5:D9','questions']]){
const b=await wb.render({sheetName:s,range:r,scale:1,format:'png'});await fs.writeFile(new URL(f+'.png',dir),new Uint8Array(await b.arrayBuffer()));}
console.log('Saved '+out.pathname);



