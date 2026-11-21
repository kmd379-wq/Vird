import fs from 'node:fs/promises';
const dir=new URL('.',import.meta.url);
const d=JSON.parse(await fs.readFile(new URL('data.json',dir),'utf8'));
const u=JSON.parse(await fs.readFile(new URL('update_2026-10-21_evening.json',dir),'utf8'));
d.rows=d.rows.map(r=>({...r,...u.updates[r.id]}));
for(const e of u.events)if(!d.events.some(x=>x.id===e.id))d.events.push(e);
for(const r of d.rows){r.incoming=d.events.filter(e=>e.company===r.id&&e.direction==='Входящее').length;}
await fs.writeFile(new URL('data.json',dir),JSON.stringify(d,null,2));
const path='C:/Users/kmd37/.cursor/projects/c-Users-kmd37-Projects-vird/canvases/patent-attorney-tracker.canvas.tsx';
let c=await fs.readFile(path,'utf8');
c=c.replace(/const DATA=.*;\nexport default/,()=> 'const DATA='+JSON.stringify(d)+';\nexport default');
await fs.writeFile(path,c);
console.log('Updated '+d.events.length+' messages');
