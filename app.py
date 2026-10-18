import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="NEON STRIKE HD", page_icon="🔥", layout="wide")
components.html("""
<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;user-select:none}
body{background:#000;overflow:hidden;width:100vw;height:100vh}
#gameWrapper{position:fixed;inset:0;width:100vw;height:100vh;background:#000;display:flex;align-items:center;justify-content:center}
#canvas{width:100%;height:100%;display:block;object-fit:cover;background:#0e1a0e}
/* IF PHONE IS VERTICAL, ROTATE GAME 90DEG SO IT'S ALREADY SIDEWAYS */
@media (orientation: portrait){
  #gameWrapper{width:100vh;height:100vw;top:50%;left:50%;transform:translate(-50%,-50%) rotate(90deg);transform-origin:center center}
  #canvas{width:100vh;height:100vw}
  #lobby{width:100vh !important;height:100vw !important}
}
#lobby{position:absolute;inset:0;background:linear-gradient(105deg,#000 0%,#0a1e0a 35%,#122412 70%);z-index:50;display:flex;color:#fff}
#lobbyLeft{flex:1.6;padding:18px;display:flex;flex-direction:column;justify-content:space-between;background:radial-gradient(circle at 30% 40%,rgba(0,255,150,0.18),transparent 60%)}
#lobbyRight{flex:1;background:rgba(5,5,5,0.88);border-left:2.5px solid #00ff9d;padding:12px;overflow:auto}
.charBig{width:180px;height:280px;margin:20px auto;background:linear-gradient(180deg,rgba(0,255,150,0.18) 0%,rgba(0,0,0,0.8) 100%);border:2.5px solid #00ff9d;border-radius:24px;box-shadow:0 0 30px #00ff9d, inset 0 0 20px rgba(0,255,150,0.2);display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
.charBig::before{content:'';position:absolute;bottom:-12px;width:80%;height:14px;background:radial-gradient(ellipse,rgba(0,0,0,0.8),transparent);border-radius:50%}
.lobbyBtn{padding:13px;background:linear-gradient(90deg,#00ff9d,#00c3ff);border:none;border-radius:12px;font-weight:900;color:#000;font-size:15px;cursor:pointer;box-shadow:0 0 20px rgba(0,255,157,0.6);width:100%;letter-spacing:1px}
.card{background:rgba(255,255,255,0.07);border:1.5px solid rgba(255,255,255,0.15);border-radius:12px;padding:8px;margin:4px;cursor:pointer;transition:0.2s}
.card.sel{border-color:#00ff9d;background:rgba(0,255,157,0.18);box-shadow:0 0 12px rgba(0,255,157,0.4)}
#ui{position:absolute;inset:0;pointer-events:none;z-index:20}
.joy{position:absolute;bottom:14px;width:128px;height:128px;background:radial-gradient(circle,rgba(255,255,255,0.14) 0%,rgba(255,255,255,0.02) 70%);border-radius:50%;border:2px solid rgba(255,255,255,0.25);pointer-events:auto}
#jM{left:14px} #jA{right:108px;width:96px;height:96px;bottom:18px}
.stick{position:absolute;width:56px;height:56px;background:radial-gradient(#fff,#bbb);border-radius:50%;left:36px;top:36px;box-shadow:0 4px 10px #000}
#sA{width:42px;height:42px;left:27px;top:27px;background:radial-gradient(#ff5a5a,#900)}
.btn{position:absolute;pointer-events:auto;border:none;font-weight:900;color:#fff;box-shadow:0 4px 12px #000}
#fire{bottom:108px;right:10px;width:94px;height:94px;background:radial-gradient(circle at 30% 30%,#ff6a6a,#a00);border-radius:50%;border:3.5px solid #fff;font-size:18px}
#gloo{bottom:10px;right:10px;width:84px;height:48px;background:linear-gradient(#00eaff,#0077ff);border-radius:12px;border:2.5px solid #fff;font-size:11px}
#skills{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);display:flex;gap:10px;pointer-events:auto}
.skill{width:60px;height:60px;border-radius:14px;border:2.5px solid #fff;background:radial-gradient(#222,#000);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;position:relative}
</style></head><body>
<div id="gameWrapper">
<canvas id="canvas"></canvas>

<div id="lobby">
<div id="lobbyLeft">
<div style="display:flex;justify-content:space-between"><div><b style="color:#00ff9d;font-size:20px;letter-spacing:2px">NEON STRIKE</b><div style="font-size:9px;opacity:0.6;letter-spacing:1px">FREE FIRE MAX • BERMUDA HD • v3</div></div><div style="text-align:right;font-size:12px">💎 1245<br><span style="color:#ffcc00">🪙 89340</span></div></div>
<div class="charBig" id="bigBox"><div id="bigIcon" style="font-size:82px;filter:drop-shadow(0 0 12px #00ff9d)">🎧</div><div id="bigName" style="font-size:20px;font-weight:900;color:#00ff9d;margin-top:6px;letter-spacing:1px">ALOK</div><div id="bigSkill" style="font-size:10px;background:#00ff9d;color:#000;padding:4px 10px;border-radius:20px;margin-top:6px;font-weight:900">DROP THE BEAT</div><div style="font-size:10px;opacity:0.7;margin-top:8px" id="bigDesc">Heal 50HP + 5HP/s aura</div></div>
<div style="display:flex;gap:8px"><button class="lobbyBtn" style="flex:1.5;background:#fff;color:#000;border:none" id="startBtn">▶ PLAY • BERMUDA</button><button class="lobbyBtn" style="flex:0.5;background:rgba(255,255,255,0.12);color:#fff;border:1px solid #fff">VAULT</button></div>
</div>
<div id="lobbyRight">
<div style="font-size:10px;color:#ffcc00;margin-bottom:6px;letter-spacing:1px">SELECT CHARACTER - NO DOTS</div>
<div id="cGrid" style="display:grid;grid-template-columns:1fr 1fr;gap:6px"></div>
<div style="font-size:10px;color:#ffcc00;margin:10px 0 6px">PET • RANK HEROIC</div>
<div id="pGrid" style="display:flex;gap:6px;flex-wrap:wrap"></div>
<div style="margin-top:12px;background:rgba(0,255,157,0.08);border:1px solid rgba(0,255,157,0.2);border-radius:10px;padding:10px;font-size:9px;line-height:13px">HD FEATURES:<br>• Auto sideways - no rotate screen<br>• Real shadows + building textures<br>• Muzzle flash + bullet trails<br>• Gloo walls with HP bar</div>
</div>
</div>

<div id="ui" style="display:none">
<div style="position:absolute;top:0;left:0;right:0;height:52px;display:flex;justify-content:space-between;padding:8px 12px;color:#fff"><div style="display:flex;gap:8px"><div style="background:rgba(0,0,0,0.7);border-radius:10px;padding:5px 12px;text-align:center"><div style="font-size:8px;opacity:0.6">ALIVE</div><div id="alive" style="font-size:18px;font-weight:900">13</div></div><div style="background:rgba(0,0,0,0.7);border-radius:10px;padding:5px 10px"><div id="gunName" style="font-size:12px;color:#00ff9d;font-weight:900">FIST</div><div id="ammo" style="font-size:10px">∞</div></div></div><div style="background:rgba(0,0,0,0.7);border-radius:10px;padding:5px 10px"><div style="width:100px;height:12px;background:#222;border-radius:6px;border:1.5px solid #fff;overflow:hidden"><div id="hpFill" style="height:100%;background:linear-gradient(90deg,#00ff88,#00ffcc);width:100%"></div></div><div style="font-size:8px;margin-top:3px">VEST <span id="vest">0</span> • PET <span id="petI"></span></div></div></div>
<div class="joy" id="jM"><div class="stick" id="sM"></div></div>
<div class="joy" id="jA"><div class="stick" id="sA"></div></div>
<button class="btn" id="fire">FIRE</button>
<button class="btn" id="gloo">GLOO<br><span id="gCnt">4</span></button>
<div id="skills"><div class="skill" id="sk"><div id="skIc" style="font-size:22px">🎧</div><div style="font-size:7px">SKILL</div><div id="skCd" style="position:absolute;inset:0;background:rgba(0,0,0,0.78);border-radius:12px;display:none;align-items:center;justify-content:center;font-size:16px;font-weight:900">0</div></div><div class="skill" id="med"><div style="font-size:20px">💊</div><div style="font-size:7px">MED</div></div></div>
</div>
</div>

<script>
const canvas=document.getElementById('canvas'), ctx=canvas.getContext('2d');
function resize(){canvas.width=canvas.clientWidth*2; canvas.height=canvas.clientHeight*2; ctx.scale(2,2)} // HD
setTimeout(resize,100); addEventListener('resize',()=>{ctx.setTransform(1,0,0,1,0,0); resize()});
const W=()=>canvas.clientWidth, H=()=>canvas.clientHeight;

const chars=[{id:'alok',ic:'🎧',n:'ALOK',sk:'DROP THE BEAT',d:'Heal 50HP + aura'}, {id:'chrono',ic:'🛡️',n:'CHRONO',sk:'TIME TURNER',d:'Dome 600HP'}, {id:'kelly',ic:'🏃',n:'KELLY',sk:'DASH',d:'35% Speed 4s'}, {id:'wukong',ic:'🌿',n:'WUKONG',sk:'CAMOUFLAGE',d:'Invisible 9s'}, {id:'hayato',ic:'⚡',n:'HAYATO',sk:'BUSHIDO',d:'Armor when low'}, {id:'moco',ic:'🎯',n:'MOCO',sk:'HACKER EYE',d:'Tag enemies'}];
const pets=[{id:'falco',ic:'🦅',n:'Falco'},{id:'panda',ic:'🐼',n:'Panda'},{id:'otter',ic:'🦦',n:'Otto'},{id:'shiba',ic:'🐶',n:'Shiba'}];
let selC='alok', selP='falco';
const cGrid=document.getElementById('cGrid'), pGrid=document.getElementById('pGrid');
chars.forEach(c=>{let d=document.createElement('div'); d.className='card'+(c.id==selC?' sel':''); d.innerHTML=`<div style="font-size:28px">${c.ic}</div><b style="font-size:11px;color:#00ff9d">${c.n}</b><div style="font-size:8px;opacity:0.8">${c.d}</div>`; d.onclick=()=>{selC=c.id; document.querySelectorAll('#cGrid .card').forEach(x=>x.classList.remove('sel')); d.classList.add('sel'); upd()}; cGrid.appendChild(d)});
pets.forEach(p=>{let d=document.createElement('div'); d.className='card sel'; d.style.width='72px'; d.innerHTML=`<div style="font-size:22px">${p.ic}</div><div style="font-size:8px">${p.n}</div>`; d.onclick=()=>{selP=p.id; upd()}; pGrid.appendChild(d)});
function upd(){let c=chars.find(x=>x.id==selC); document.getElementById('bigIcon').innerText=c.ic; document.getElementById('bigName').innerText=c.n; document.getElementById('bigSkill').innerText=c.sk; document.getElementById('bigDesc').innerText=c.d}
upd();

let game=false, player, bullets=[], enemies=[], buildings=[], loots=[], gWalls=[], parts=[], cam={x:1000,y:1000}, shake=0, jM={x:0,y:0}, jA={x:0,y:0}, skReady=true, skCD=0, gCount=4;
let guns={fist:{n:'FIST',dmg:22,rate:350,col:'#fff',ammo:0}, mp40:{n:'MP40',dmg:24,rate:85,col:'#ffaa00',ammo:40}, m1887:{n:'M1887',dmg:110,rate:580,col:'#ff4444',ammo:8}, awm:{n:'AWM',dmg:95,rate:1200,col:'#00ffff',ammo:5}, ak:{n:'AK',dmg:40,rate:140,col:'#ffaa00',ammo:30}, ump:{n:'UMP',dmg:27,rate:108,col:'#aaccff',ammo:32}};

function reset(){
 player={x:1000,y:1000,ang:0,hp:100,max:100,vest:0,gun:guns.fist,ammo:0,speed:1,inv:0,shd:0};
 bullets=[]; enemies=[]; buildings=[]; loots=[]; gWalls=[]; parts=[];
 for(let i=0;i<26;i++) buildings.push({x:Math.random()*2400,y:Math.random()*2400,w:70+Math.random()*120,h:70+Math.random()*110, col:`hsl(${30+Math.random()*20},15%,${18+Math.random()*8}%)`});
 buildings.push({x:900,y:900,w:240,h:240,col:'#1a1a1a'});
 let ts=['mp40','m1887','awm','ak','ump','med','gloo']; for(let i=0;i<40;i++){let t=ts[Math.floor(Math.random()*ts.length)]; loots.push({x:Math.random()*2400,y:Math.random()*2400,t,took:false})}
 for(let i=0;i<12;i++) enemies.push({x:Math.random()*2400,y:Math.random()*2400,hp:100,ang:0,g:Object.keys(guns)[1+Math.floor(Math.random()*5)],cd:0});
 gCount=4; document.getElementById('gCnt').innerText=gCount;
}
function setJoy(jID,sID,out){
 const j=document.getElementById(jID), s=document.getElementById(sID); let act=false;
 const mv=(e)=>{if(!act) return; let r=j.getBoundingClientRect(), t=e.touches?e.touches[0]:e, cx=r.left+r.width/2, cy=r.top+r.height/2, dx=t.clientX-cx, dy=t.clientY-cy, d=Math.hypot(dx,dy), m=r.width/2-14; if(d>m){dx=dx/d*m; dy=dy/d*m;} s.style.left=(r.width/2-s.offsetWidth/2+dx)+'px'; s.style.top=(r.height/2-s.offsetHeight/2+dy)+'px'; out.x=dx/m; out.y=dy/m;}
 const end=()=>{act=false; s.style.left='36px'; s.style.top='36px'; if(sID=='sA'){s.style.left='27px'; s.style.top='27px'} out.x=0; out.y=0}
 j.addEventListener('touchstart',e=>{act=true; mv(e)}); j.addEventListener('touchmove',mv); j.addEventListener('touchend',end); j.addEventListener('touchcancel',end);
}
setJoy('jM','sM',jM); setJoy('jA','sA',jA);
document.getElementById('startBtn').onclick=()=>{document.getElementById('lobby').style.display='none'; document.getElementById('ui').style.display='block'; reset(); game=true; document.getElementById('skIc').innerText=chars.find(c=>c.id==selC).ic; document.getElementById('petI').innerText=pets.find(p=>p.id==selP).ic};

function shoot(){if(!game) return; if(Date.now()-(shoot.l||0) < player.gun.rate) return; shoot.l=Date.now(); if(player.gun!=guns.fist && player.ammo<=0) return; if(player.gun!=guns.fist) player.ammo--; let spr=0.12, pel=player.gun.n=='M1887'?6:1; for(let p=0;p<pel;p++){let a=player.ang+(Math.random()-0.5)*spr; bullets.push({x:player.x+Math.cos(player.ang)*36,y:player.y+Math.sin(player.ang)*36,vx:Math.cos(a)*21,vy:Math.sin(a)*21,own:'p',dmg:player.gun.dmg/(pel>1?pel:1),life:78});} shake=player.gun.n=='AWM'?16:7; for(let i=0;i<12;i++) parts.push({x:player.x+Math.cos(player.ang)*40,y:player.y+Math.sin(player.ang)*40,vx:Math.cos(player.ang)*(4+Math.random()*5)+(Math.random()-0.5)*4,vy:Math.sin(player.ang)*(4+Math.random()*5)+(Math.random()-0.5)*4,life:10,col:'#ffcc00',s:2+Math.random()*3});}
document.getElementById('fire').addEventListener('touchstart',e=>{e.preventDefault(); shoot()}); document.getElementById('fire').addEventListener('mousedown',shoot);
document.getElementById('gloo').onclick=()=>{if(gCount<=0) return; gCount--; document.getElementById('gCnt').innerText=gCount; let gx=player.x+Math.cos(player.ang)*88, gy=player.y+Math.sin(player.ang)*88; gWalls.push({x:gx-38,y:gy-38,w:76,h:76,hp:500,mx:500})};
document.getElementById('sk').onclick=()=>{if(!skReady) return; skReady=false; skCD=30; let c=selC; if(c=='alok'){player.hp=Math.min(player.max,player.hp+50); player.speed=1.35; setTimeout(()=>player.speed=1,5000); for(let i=0;i<28;i++) parts.push({x:player.x+(Math.random()-0.5)*150,y:player.y+(Math.random()-0.5)*150,vx:0,vy:-1.2,life:35,col:'#00ff9d',s:5});} else if(c=='chrono'){player.shd=650; gWalls.push({x:player.x-90,y:player.y-90,w:180,h:180,hp:650,mx:650,dome:true});} else if(c=='kelly'){player.speed=2.4; setTimeout(()=>player.speed=1,4000);} else if(c=='wukong'){player.inv=540;} else if(c=='moco'){enemies.forEach(en=>{if(Math.hypot(en.x-player.x,en.y-player.y)<650) en.tag=300});} document.getElementById('skCd').style.display='flex';};
document.getElementById('med').onclick=()=>{if(player.hp<player.max){player.hp=Math.min(player.max,player.hp+35); for(let i=0;i<10;i++) parts.push({x:player.x,y:player.y,vx:(Math.random()-0.5)*3,vy:-2,life:20,col:'#0f0',s:3});}};

function loop(){
 if(!game){requestAnimationFrame(loop); return}
 if(!skReady){skCD-=0.016; document.getElementById('skCd').innerText=Math.ceil(skCD); if(skCD<=0){skReady=true; document.getElementById('skCd').style.display='none';}}
 let sp=6*player.speed, nx=player.x+jM.x*sp, ny=player.y+jM.y*sp; let blk=false; [...buildings,...gWalls].forEach(b=>{if(nx>b.x && nx<b.x+b.w && player.y>b.y && player.y<b.y+b.h) blk=true; if(player.x>b.x && player.x<b.x+b.w && ny>b.y && ny<b.y+b.h) blk=true;}); if(!blk){player.x=nx; player.y=ny;}
 if(Math.hypot(jA.x,jA.y)>0.28) player.ang=Math.atan2(jA.y,jA.x);
 cam.x+=(player.x-cam.x)*0.13; cam.y+=(player.y-cam.y)*0.13;
 let safe=1000-Date.now()/1400; safe=Math.max(170,safe); if(Math.hypot(player.x-1200,player.y-1200)>safe) player.hp-=0.45;
 loots.forEach(l=>{if(!l.took && Math.hypot(player.x-l.x,player.y-l.y)<50){if(l.t=='med') player.hp=Math.min(player.max,player.hp+75); else if(l.t=='gloo'){gCount=Math.min(6,gCount+1); document.getElementById('gCnt').innerText=gCount;} else {player.gun=guns[l.t]; player.ammo=player.gun.ammo||30;} l.took=true;}});
 bullets.forEach(b=>{b.x+=b.vx; b.y+=b.vy; b.life--; let hit=false; [...buildings,...gWalls].forEach(w=>{if(b.x>w.x && b.x<w.x+w.w && b.y>w.y && b.y<w.y+w.h){hit=true; if(w.hp!==undefined){w.hp-=b.dmg; if(w.hp<=0) w.dead=true;} b.life=0;}}); if(!hit && b.own=='p'){enemies.forEach((en,i)=>{if(Math.hypot(b.x-en.x,b.y-en.y)<28){en.hp-=b.dmg; b.life=0; for(let k=0;k<9;k++) parts.push({x:en.x,y:en.y,vx:(Math.random()-0.5)*7,vy:(Math.random()-0.5)*7,life:16,col:'#ff2222',s:3}); if(en.hp<=0) enemies.splice(i,1);}});} else if(b.own!='p' && Math.hypot(b.x-player.x,b.y-player.y)<32 && player.inv<=0){let d=b.dmg; if(player.shd>0){player.shd-=d; d=0; if(player.shd<=0) player.shd=0;} player.hp-=d; b.life=0; shake=14; if(player.hp<=0){alert('ELIMINATED! TRY AGAIN'); location.reload();}}});
 bullets=bullets.filter(b=>b.life>0); gWalls=gWalls.filter(w=>!w.dead);
 enemies.forEach(en=>{if(en.cd>0) en.cd--; let dist=Math.hypot(en.x-player.x,en.y-player.y); if(dist<620){en.ang=Math.atan2(player.y-en.y,player.x-en.x); if(dist>150){let tx=en.x+Math.cos(en.ang)*1.8, ty=en.y+Math.sin(en.ang)*1.8; let bl=false; [...buildings,...gWalls].forEach(b=>{if(tx>b.x && tx<b.x+b.w && en.y>b.y && en.y<b.y+b.h) bl=true;}); if(!bl) en.x=tx; bl=false; [...buildings,...gWalls].forEach(b=>{if(en.x>b.x && en.x<b.x+b.w && ty>b.y && ty<b.y+b.h) bl=true;}); if(!bl) en.y=ty;} if(en.cd==0 && dist<440 && player.inv<=0){let gd=guns[en.g]; bullets.push({x:en.x+Math.cos(en.ang)*32,y:en.y+Math.sin(en.ang)*32,vx:Math.cos(en.ang)*16,vy:Math.sin(en.ang)*16,own:'e',dmg:gd.dmg*0.55,life:70}); en.cd=gd.rate/16;}} if(en.tag>0) en.tag--;});
 // DRAW HD
 ctx.save(); if(shake>0){ctx.translate((Math.random()-0.5)*shake,(Math.random()-0.5)*shake); shake*=0.87;} ctx.translate(W()/2-cam.x, H()/2-cam.y);
 ctx.fillStyle='#0f1a0f'; ctx.fillRect(cam.x-1400,cam.y-1100,2800,2200);
 // grass texture dots
 ctx.fillStyle='rgba(255,255,255,0.03)'; for(let i=0;i<120;i++){let gx=(cam.x-1400)+Math.random()*2800, gy=(cam.y-1100)+Math.random()*2200; ctx.fillRect(gx,gy,2,2);}
 // safe zone
 ctx.beginPath(); ctx.arc(1200,1200,safe,0,Math.PI*2); ctx.strokeStyle='#00ffcc'; ctx.lineWidth=3.5; ctx.setLineDash([28,16]); ctx.stroke(); ctx.setLineDash([]);
 // buildings HD
 buildings.forEach(b=>{
  ctx.fillStyle='rgba(0,0,0,0.45)'; ctx.fillRect(b.x+8,b.y+8,b.w,b.h);
  ctx.fillStyle=b.col; ctx.fillRect(b.x,b.y,b.w,b.h);
  ctx.fillStyle='rgba(255,255,255,0.12)'; ctx.fillRect(b.x,b.y,b.w,10);
  ctx.strokeStyle='rgba(0,0,0,0.8)'; ctx.lineWidth=2.2; ctx.strokeRect(b.x,b.y,b.w,b.h);
  // windows
  ctx.fillStyle='rgba(120,200,255,0.25)'; for(let wx=b.x+10;wx<b.x+b.w-18;wx+=22){for(let wy=b.y+16;wy<b.y+b.h-14;wy+=20){ctx.fillRect(wx,wy,12,10);}}
 });
 loots.forEach(l=>{if(l.took) return; let col=guns[l.t]?guns[l.t].col:l.t=='med'?'#ff44ff':l.t=='gloo'?'#00eaff':'#ffcc00'; ctx.shadowColor=col; ctx.shadowBlur=18; ctx.fillStyle=col; ctx.beginPath(); ctx.roundRect(l.x-12,l.y-12,24,24,6); ctx.fill(); ctx.shadowBlur=0; ctx.fillStyle='#000'; ctx.font='14px Arial'; ctx.fillText(l.t=='med'?'💊':l.t=='gloo'?'🧱':guns[l.t]?guns[l.t].n[0]:'?', l.x-6, l.y+5);});
 gWalls.forEach(w=>{if(w.dome){ctx.fillStyle='rgba(0,200,255,0.16)'; ctx.beginPath(); ctx.arc(w.x+w.w/2,w.y+w.h/2,w.w/2,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#00eaff'; ctx.lineWidth=3; ctx.stroke(); ctx.fillStyle='#fff'; ctx.font='10px Arial'; ctx.fillText(Math.floor(w.hp), w.x+w.w/2-10, w.y+w.h/2);} else {ctx.fillStyle='rgba(0,230,255,0.92)'; ctx.fillRect(w.x,w.y,w.w,w.h); ctx.strokeStyle='#fff'; ctx.lineWidth=2; ctx.strokeRect(w.x,w.y,w.w,w.h); ctx.fillStyle='rgba(0,0,0,0.35)'; ctx.fillRect(w.x,w.y,w.w,8);}});
 enemies.forEach(en=>{ctx.save(); ctx.translate(en.x,en.y); ctx.rotate(en.ang); ctx.fillStyle='#6e0000'; ctx.beginPath(); ctx.roundRect(-17,-14,34,28,6); ctx.fill(); ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(12,0,11,0,Math.PI*2); ctx.fill(); ctx.fillStyle='#222'; ctx.fillRect(19,-4,32,8); ctx.fillRect(19,-10,10,20); if(en.tag>0){ctx.strokeStyle='#ff00ff'; ctx.lineWidth=3; ctx.strokeRect(-22,-22,44,44);} ctx.restore(); ctx.fillStyle='#000'; ctx.fillRect(en.x-24,en.y-36,48,8); ctx.fillStyle='#00ff66'; ctx.fillRect(en.x-24,en.y-36,en.hp*0.48,8);});
 if(player.inv<=0 || Math.floor(Date.now()/100)%2==0){
  ctx.save(); ctx.translate(player.x,player.y); ctx.rotate(player.ang);
  if(player.shd>0){ctx.strokeStyle='rgba(0,200,255,0.9)'; ctx.lineWidth=5; ctx.beginPath(); ctx.arc(0,0,46,0,Math.PI*2); ctx.stroke();}
  ctx.fillStyle=selC=='alok'?'#00ff9d':selC=='chrono'?'#00aaff':selC=='kelly'?'#ffaa00':selC=='wukong'?'#88ff44':'#ffaa66'; ctx.beginPath(); ctx.roundRect(-20,-15,40,30,8); ctx.fill();
  ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(14,0,11,0,Math.PI*2); ctx.fill();
  ctx.fillStyle=player.gun.col; ctx.beginPath(); ctx.roundRect(22,-6,42,12,4); ctx.fill(); ctx.fillStyle='#111'; ctx.fillRect(56,-4,20,8);
  ctx.restore();
  let petX=player.x-Math.cos(player.ang)*42, petY=player.y-Math.sin(player.ang)*42; ctx.font='22px Arial'; ctx.fillText(pets.find(p=>p.id==selP).ic, petX-11, petY-8);
 }
 bullets.forEach(b=>{ctx.strokeStyle=b.own=='p'?'rgba(255,255,80,0.85)':'rgba(255,90,90,0.85)'; ctx.lineWidth=3.5; ctx.beginPath(); ctx.moveTo(b.x-b.vx*2.8,b.y-b.vy*2.8); ctx.lineTo(b.x,b.y); ctx.stroke(); ctx.fillStyle=b.own=='p'?'#ffee00':'#ff9999'; ctx.beginPath(); ctx.arc(b.x,b.y,4.5,0,Math.PI*2); ctx.fill();});
 parts.forEach(p=>{p.x+=p.vx; p.y+=p.vy; p.life--; p.vx*=0.92; p.vy*=0.92; ctx.globalAlpha=p.life/30; ctx.fillStyle=p.col; ctx.beginPath(); ctx.arc(p.x,p.y,p.s,0,Math.PI*2); ctx.fill(); ctx.globalAlpha=1;}); parts=parts.filter(p=>p.life>0);
 ctx.restore();
 document.getElementById('alive').innerText=enemies.length+1; document.getElementById('gunName').innerText=player.gun.n; document.getElementById('ammo').innerText=player.gun==guns.fist?'∞':player.ammo+' / ∞'; document.getElementById('hpFill').style.width=(player.hp/player.max*100)+'%'; document.getElementById('vest').innerText=player.vest||0;
 if(player.inv>0) player.inv--;
 if(enemies.length==0 && game){game=false; setTimeout(()=>{alert('BOOYAH! 🏆 YOU WIN - NEON STRIKE CHAMPION!'); location.reload()},500);}
 requestAnimationFrame(loop);
}
loop();
</script></body></html>
""", height=820)
