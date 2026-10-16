import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="NEON STRIKE FF LOBBY", page_icon="🔥", layout="wide")
components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, orientation=landscape">
<meta name="screen-orientation" content="landscape">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Russo+One&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;font-family:Orbitron}
body{background:#050d05;overflow:hidden}

/* FORCE LANDSCAPE PROMPT */
#rotatePrompt{position:fixed;inset:0;background:#000;z-index:9999;display:none;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center}
@media (orientation: portrait){
  #rotatePrompt{display:flex}
}
#rotateIcon{font-size:80px;animation:rot 1.5s infinite}
@keyframes rot{0%{transform:rotate(0deg)}50%{transform:rotate(90deg)}100%{transform:rotate(0deg)}}

#canvas{width:100vw;height:100vh;display:block}

/* LOBBY LIKE REAL FREE FIRE */
#lobby{position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,#1a4a1a 0%,#0a1e0a 40%,#000 100%);z-index:100;display:flex;color:#fff;overflow:hidden}
#lobbyLeft{width:68%;height:100%;position:relative;background:linear-gradient(90deg,rgba(0,0,0,0.6),transparent);padding:20px;display:flex;flex-direction:column;justify-content:space-between}
#lobbyRight{width:32%;height:100%;background:rgba(0,0,0,0.75);border-left:3px solid #00ffcc;padding:14px;overflow-y:auto}
.charPreview{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);text-align:center}
.charModel{width:160px;height:260px;background:linear-gradient(180deg,rgba(0,255,204,0.2),rgba(0,0,0,0.5));border:2px solid #00ffcc;border-radius:30px 30px 12px 12px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(0,255,204,0.4)}
.lobbyBtn{padding:12px 18px;background:linear-gradient(90deg,#00ffcc,#00aaff);border:none;border-radius:12px;font-weight:900;color:#000;font-size:14px;margin:6px 0;width:100%;box-shadow:0 0 15px #00ffcc;cursor:pointer}
.lobbyCard{background:rgba(255,255,255,0.06);border:1.5px solid rgba(255,255,255,0.15);border-radius:12px;padding:10px;margin:6px 0;cursor:pointer}
.lobbyCard.sel{border-color:#00ffcc;background:rgba(0,255,204,0.12)}
#topBar{position:absolute;top:0;left:0;right:0;height:52px;background:linear-gradient(180deg,#000,rgba(0,0,0,0.4));display:flex;justify-content:space-between;padding:6px 12px;color:#fff;z-index:20}
.joy{position:absolute;bottom:12px;width:125px;height:125px;background:radial-gradient(rgba(255,255,255,0.18),rgba(255,255,255,0.03));border-radius:63px;border:2px solid rgba(255,255,255,0.25);z-index:20}
#joyMove{left:10px} #joyAim{right:98px;width:95px;height:95px;bottom:20px}
.stick{position:absolute;width:54px;height:54px;background:radial-gradient(#fff,#aaa);border-radius:27px;left:35px;top:35px}
#stickAim{width:40px;height:40px;left:27px;top:27px;background:radial-gradient(#ff4444,#800)}
.btn{position:absolute;z-index:20;border:none;font-weight:900;color:#fff}
#fire{bottom:110px;right:8px;width:92px;height:92px;background:radial-gradient(#ff4d4d,#900);border-radius:46px;border:3px solid #fff;font-size:20px}
#gloo{bottom:8px;right:8px;width:82px;height:46px;background:linear-gradient(#00eaff,#0077ff);border-radius:10px;border:2px solid #fff;font-size:10px}
#skillRow{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:20}
.skill{width:58px;height:58px;border-radius:14px;border:2.5px solid #fff;background:radial-gradient(#222,#000);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;position:relative}
.cd{position:absolute;inset:0;background:rgba(0,0,0,0.75);border-radius:11px;display:none;align-items:center;justify-content:center;font-size:16px}
</style>
</head>
<body>
<div id="rotatePrompt">
<div id="rotateIcon">📱➡️📲</div>
<h2 style="margin-top:20px;color:#00ffcc">ROTATE YOUR PHONE SIDEWAYS!</h2>
<p style="margin-top:10px;font-size:13px;opacity:0.7">Turn your phone to landscape like real Free Fire</p>
<p style="margin-top:8px;font-size:11px;color:#ffcc00">Game is made for sideways mode</p>
</div>

<div id="lobby">
<div id="lobbyLeft">
<div style="display:flex;justify-content:space-between;align-items:center">
<div><b style="color:#00ffcc;font-size:18px">NEON STRIKE</b><div style="font-size:9px;opacity:0.6">FREE FIRE MAX • BERMUDA</div></div>
<div style="text-align:right"><div style="font-size:12px">💎 1245</div><div style="font-size:10px;color:#ffcc00">🪙 89340</div></div>
</div>

<div class="charPreview">
<div class="charModel" id="modelBox">
<div id="modelIcon" style="font-size:70px">🎧</div>
<div id="modelName" style="font-size:18px;font-weight:900;color:#00ffcc;margin-top:8px">ALOK</div>
<div id="modelSkill" style="font-size:9px;background:#00ffcc;color:#000;padding:3px 8px;border-radius:6px;margin-top:4px">DROP THE BEAT</div>
<div style="font-size:8px;margin-top:8px;opacity:0.7" id="modelDesc">Heal Aura + Team Heal</div>
</div>
<div style="margin-top:14px;display:flex;gap:8px">
<div style="background:rgba(0,0,0,0.6);border-radius:8px;padding:6px 10px;font-size:10px">Pet: <span id="modelPet">🦅 Falco</span></div>
<div style="background:rgba(0,0,0,0.6);border-radius:8px;padding:6px 10px;font-size:10px">Rank: <span style="color:#ffaa00">HEROIC</span></div>
</div>
</div>

<div style="display:flex;gap:10px">
<button class="lobbyBtn" style="background:rgba(255,255,255,0.1);color:#fff;border:1px solid #fff;width:auto">VAULT</button>
<button class="lobbyBtn" style="background:rgba(255,255,255,0.1);color:#fff;border:1px solid #fff;width:auto">STORE</button>
<button class="lobbyBtn" id="startGameBtn" style="flex:1;font-size:18px">START ▶ BERMUDA</button>
</div>
</div>

<div id="lobbyRight">
<div style="font-size:11px;color:#ffcc00;margin-bottom:8px">SELECT CHARACTER</div>
<div id="charGrid" style="display:grid;grid-template-columns:1fr 1fr;gap:6px"></div>
<div style="font-size:11px;color:#ffcc00;margin:12px 0 6px">SELECT PET</div>
<div id="petGrid" style="display:flex;gap:6px;flex-wrap:wrap"></div>
<div style="margin-top:14px;background:rgba(0,255,204,0.1);border-radius:10px;padding:10px;font-size:9px;line-height:12px">
<b style="color:#00ffcc">CONTROLS - LANDSCAPE MODE:</b><br>
• Left joystick = Move<br>
• Right joystick = Aim<br>
• FIRE = Shoot<br>
• GLOO = Build wall<br>
• Turn phone SIDEWAYS!
</div>
</div>
</div>

<div id="topBar" style="display:none">
<div style="display:flex;gap:8px">
<div style="background:rgba(0,0,0,0.7);border-radius:8px;padding:4px 8px;text-align:center"><div style="font-size:8px;opacity:0.6">ALIVE</div><div id="alive" style="font-size:16px">13</div></div>
<div style="background:rgba(0,0,0,0.7);border-radius:8px;padding:4px 8px"><div id="gunName" style="font-size:11px;color:#00ffcc">FIST</div><div id="ammo" style="font-size:9px">∞</div></div>
</div>
<div style="background:rgba(0,0,0,0.7);border-radius:8px;padding:4px 8px"><div style="width:90px;height:10px;background:#222;border-radius:5px;border:1px solid #fff"><div id="hpFill" style="height:100%;background:linear-gradient(90deg,#0f8,#0ff);width:100%"></div></div><div style="font-size:8px;margin-top:2px">VEST <span id="vestTxt">0</span> PET <span id="petTxt"></span></div></div>
</div>

<canvas id="canvas"></canvas>
<div class="joy" id="joyMove" style="display:none"><div class="stick" id="stickMove"></div></div>
<div class="joy" id="joyAim" style="display:none"><div class="stick" id="stickAim"></div></div>
<button class="btn" id="fire" style="display:none">FIRE</button>
<button class="btn" id="gloo" style="display:none">GLOO<br><span id="glooCnt">4</span></button>
<div id="skillRow" style="display:none">
<div class="skill" id="skillMain"><div id="sIcon" style="font-size:20px">🎧</div><div style="font-size:6px">SKILL</div><div class="cd" id="sCd">0</div></div>
<div class="skill" id="medBtn"><div style="font-size:18px">💊</div><div style="font-size:6px">MED</div></div>
</div>

<script>
const canvas=document.getElementById('canvas'), ctx=canvas.getContext('2d');
canvas.width=innerWidth; canvas.height=innerHeight;
const chars=[{id:'alok',icon:'🎧',name:'ALOK',skill:'DROP THE BEAT',desc:'Heal Aura +5HP/s'},{id:'chrono',icon:'🛡️',name:'CHRONO',skill:'TIME TURNER',desc:'Dome Shield 600HP'},{id:'kelly',icon:'🏃',name:'KELLY',skill:'DASH',desc:'35% Speed 4s'},{id:'wukong',icon:'🌿',name:'WUKONG',skill:'CAMOUFLAGE',desc:'Invisible 9s'},{id:'hayato',icon:'⚡',name:'HAYATO',skill:'BUSHIDO',desc:'Armor when low HP'},{id:'moco',icon:'🎯',name:'MOCO',skill:'HACKER EYE',desc:'Tag enemy 5s'}];
const pets=[{id:'falco',icon:'🦅',name:'Falco'},{id:'panda',icon:'🐼',name:'Panda'},{id:'otter',icon:'🦦',name:'Otto'},{id:'shiba',icon:'🐶',name:'Shiba'}];
let selChar='alok', selPet='falco';
const charGrid=document.getElementById('charGrid'), petGrid=document.getElementById('petGrid');
chars.forEach(c=>{
  let d=document.createElement('div'); d.className='lobbyCard'+(c.id==selChar?' sel':''); d.innerHTML=`<div style="font-size:26px">${c.icon}</div><b style="font-size:10px;color:#00ffcc">${c.name}</b><div style="font-size:8px">${c.desc}</div>`;
  d.onclick=()=>{selChar=c.id; document.querySelectorAll('.lobbyCard').forEach(x=>x.classList.remove('sel')); d.classList.add('sel'); updateModel();};
  charGrid.appendChild(d);
});
pets.forEach(p=>{
  let d=document.createElement('div'); d.className='lobbyCard sel'+(p.id==selPet?' sel':''); d.style.width='70px'; d.innerHTML=`<div style="font-size:20px">${p.icon}</div><div style="font-size:8px">${p.name}</div>`;
  d.onclick=()=>{selPet=p.id; document.querySelectorAll('#petGrid.lobbyCard').forEach(x=>x.classList.remove('sel')); d.classList.add('sel'); updateModel();};
  petGrid.appendChild(d);
});
function updateModel(){
  let c=chars.find(x=>x.id==selChar), p=pets.find(x=>x.id==selPet);
  document.getElementById('modelIcon').innerText=c.icon; document.getElementById('modelName').innerText=c.name; document.getElementById('modelSkill').innerText=c.skill; document.getElementById('modelDesc').innerText=c.desc; document.getElementById('modelPet').innerText=p.icon+' '+p.name;
}
updateModel();

let game=false, player, bullets=[], enemies=[], buildings=[], loots=[], glooWalls=[], particles=[], cam={x:1000,y:1000}, shake=0, joyM={x:0,y:0}, joyA={x:0,y:0}, skillReady=true, skillCD=0, glooCount=4;

let guns={fist:{name:'FIST',dmg:22,rate:350,ammo:0,color:'#fff'}, mp40:{name:'MP40',dmg:24,rate:85,ammo:40,color:'#ffaa00'}, m1887:{name:'M1887',dmg:115,rate:580,ammo:8,color:'#f44'}, awm:{name:'AWM',dmg:95,rate:1300,ammo:5,color:'#0ff'}, ak:{name:'AK',dmg:40,rate:145,ammo:30,color:'#fa0'}, ump:{name:'UMP',dmg:27,rate:108,ammo:32,color:'#aaf'}};

function resetWorld(){
  player={x:1000,y:1000,angle:0,hp:100,maxHp:100,vest:0,gun:guns.fist,ammo:0,speed:1,invis:0,shield:0};
  bullets=[]; enemies=[]; buildings=[]; loots=[]; glooWalls=[]; particles=[];
  for(let i=0;i<24;i++) buildings.push({x:Math.random()*2400,y:Math.random()*2400,w:65+Math.random()*130,h:65+Math.random()*110});
  buildings.push({x:900,y:900,w:220,h:220});
  let types=['mp40','m1887','awm','ak','ump','medkit','gloo']; for(let i=0;i<38;i++){let t=types[Math.floor(Math.random()*types.length)]; loots.push({x:Math.random()*2400,y:Math.random()*2400,type:t,taken:false});}
  for(let i=0;i<12;i++) enemies.push({x:Math.random()*2400,y:Math.random()*2400,hp:100,angle:0,gun:Object.keys(guns)[1+Math.floor(Math.random()*5)],cd:0});
  glooCount=4; document.getElementById('glooCnt').innerText=glooCount;
}

function setupJoy(joyId, stickId, out){
  const joy=document.getElementById(joyId), stick=document.getElementById(stickId);
  let act=false;
  joy.addEventListener('touchstart', e=>act=true);
  joy.addEventListener('touchmove', e=>{if(!act) return; let r=joy.getBoundingClientRect(), t=e.touches[0], cx=r.left+r.width/2, cy=r.top+r.height/2; let dx=t.clientX-cx, dy=t.clientY-cy, d=Math.hypot(dx,dy), m=r.width/2-12; if(d>m){dx=dx/d*m; dy=dy/d*m;} stick.style.left=(r.width/2-stick.offsetWidth/2+dx)+'px'; stick.style.top=(r.height/2-stick.offsetHeight/2+dy)+'px'; out.x=dx/m; out.y=dy/m;});
  const end=()=>{act=false; stick.style.left='35px'; stick.style.top='35px'; if(stickId=='stickAim'){stick.style.left='27px'; stick.style.top='27px'} out.x=0; out.y=0;}; joy.addEventListener('touchend', end); joy.addEventListener('touchcancel', end);
}
setupJoy('joyMove','stickMove',joyM); setupJoy('joyAim','stickAim',joyA);

document.getElementById('startGameBtn').onclick=()=>{
  document.getElementById('lobby').style.display='none';
  document.getElementById('topBar').style.display='flex';
  document.getElementById('joyMove').style.display='block'; document.getElementById('joyAim').style.display='block';
  document.getElementById('fire').style.display='block'; document.getElementById('gloo').style.display='block'; document.getElementById('skillRow').style.display='flex';
  resetWorld(); game=true; document.getElementById('sIcon').innerText=chars.find(c=>c.id==selChar).icon; document.getElementById('petTxt').innerText=pets.find(p=>p.id==selPet).icon;
  // try lock landscape
  if(screen.orientation && screen.orientation.lock){screen.orientation.lock('landscape').catch(()=>{});}
};

function shoot(){if(!game) return; if(Date.now()-(shoot.last||0) < player.gun.rate) return; shoot.last=Date.now(); if(player.gun!=guns.fist && player.ammo<=0) return; if(player.gun!=guns.fist) player.ammo--; let spread=0.13, pellets=player.gun.name=='M1887'?6:1; for(let p=0;p<pellets;p++){let a=player.angle+(Math.random()-0.5)*spread; bullets.push({x:player.x+Math.cos(player.angle)*34,y:player.y+Math.sin(player.angle)*34,vx:Math.cos(a)*20,vy:Math.sin(a)*20,owner:'player',dmg:player.gun.dmg/(pellets>1?pellets:1),life:75});} shake=player.gun.name=='AWM'?14:6; for(let i=0;i<10;i++) particles.push({x:player.x+Math.cos(player.angle)*38,y:player.y+Math.sin(player.angle)*38,vx:Math.cos(player.angle)*(3+Math.random()*5)+(Math.random()-0.5)*3,vy:Math.sin(player.angle)*(3+Math.random()*5)+(Math.random()-0.5)*3,life:9,color:'#ff0',s:2+Math.random()*3});}
document.getElementById('fire').addEventListener('touchstart', e=>{e.preventDefault(); shoot()}); document.getElementById('fire').addEventListener('mousedown', shoot);
document.getElementById('gloo').onclick=()=>{if(glooCount<=0) return; glooCount--; document.getElementById('glooCnt').innerText=glooCount; let gx=player.x+Math.cos(player.angle)*85, gy=player.y+Math.sin(player.angle)*85; glooWalls.push({x:gx-36,y:gy-36,w:72,h:72,hp:500,max:500});};
document.getElementById('skillMain').onclick=()=>{
  if(!skillReady) return; skillReady=false; skillCD=30;
  let c=chars.find(x=>x.id==selChar);
  if(selChar=='alok'){player.hp=Math.min(player.maxHp,player.hp+50); player.speed=1.35; setTimeout(()=>player.speed=1,5000); for(let i=0;i<30;i++) particles.push({x:player.x+(Math.random()-0.5)*140,y:player.y+(Math.random()-0.5)*140,vx:0,vy:-1.2,life:35,color:'#0fc',s:4});}
  else if(selChar=='chrono'){player.shield=650; glooWalls.push({x:player.x-90,y:player.y-90,w:180,h:180,hp:650,max:650,isDome:true});}
  else if(selChar=='kelly'){player.speed=2.4; setTimeout(()=>player.speed=1,4000);}
  else if(selChar=='wukong'){player.invis=540;}
  else if(selChar=='moco'){enemies.forEach(en=>{if(Math.hypot(en.x-player.x,en.y-player.y)<600) en.tagged=300});}
  document.getElementById('sCd').style.display='flex';
};

function loop(){
  if(!game){requestAnimationFrame(loop); return;}
  if(!skillReady){skillCD-=0.016; document.getElementById('sCd').innerText=Math.ceil(skillCD); if(skillCD<=0){skillReady=true; document.getElementById('sCd').style.display='none';}}
  let sp=5.8*player.speed; let nx=player.x+joyM.x*sp, ny=player.y+joyM.y*sp;
  let blocked=false; [...buildings,...glooWalls].forEach(b=>{if(nx>b.x && nx<b.x+b.w && player.y>b.y && player.y<b.y+b.h) blocked=true; if(player.x>b.x && player.x<b.x+b.w && ny>b.y && ny<b.y+b.h) blocked=true;});
  if(!blocked){player.x=nx; player.y=ny;}
  if(Math.hypot(joyA.x,joyA.y)>0.28) player.angle=Math.atan2(joyA.y,joyA.x);
  cam.x+=(player.x-cam.x)*0.13; cam.y+=(player.y-cam.y)*0.13;
  let safeR=1000 - Date.now()/1400; safeR=Math.max(170,safeR); if(Math.hypot(player.x-1200,player.y-1200)>safeR) player.hp-=0.45;
  loots.forEach(l=>{if(!l.taken && Math.hypot(player.x-l.x,player.y-l.y)<48){if(l.type=='medkit') player.hp=Math.min(player.maxHp,player.hp+75); else if(l.type=='gloo'){glooCount=Math.min(6,glooCount+1); document.getElementById('glooCnt').innerText=glooCount;} else {player.gun=guns[l.type]; player.ammo=player.gun.ammo;} l.taken=true;}});
  bullets.forEach(b=>{b.x+=b.vx; b.y+=b.vy; b.life--; let hit=false; [...buildings,...glooWalls].forEach(w=>{if(b.x>w.x && b.x<w.x+w.w && b.y>w.y && b.y<w.y+w.h){hit=true; if(w.hp!==undefined){w.hp-=b.dmg; if(w.hp<=0) w.dead=true;} b.life=0;}}); if(!hit && b.owner=='player'){enemies.forEach((en,i)=>{if(Math.hypot(b.x-en.x,b.y-en.y)<27){en.hp-=b.dmg; b.life=0; for(let k=0;k<8;k++) particles.push({x:en.x,y:en.y,vx:(Math.random()-0.5)*7,vy:(Math.random()-0.5)*7,life:15,color:'#f22',s:3}); if(en.hp<=0){enemies.splice(i,1);}}});} else if(b.owner!='player' && Math.hypot(b.x-player.x,b.y-player.y)<30 && player.invis<=0){let dmg=b.dmg; if(player.shield>0){player.shield-=dmg; dmg=0; if(player.shield<=0) player.shield=0;} player.hp-=dmg; b.life=0; shake=13; if(player.hp<=0){alert('ELIMINATED!'); location.reload();}}});
  bullets=bullets.filter(b=>b.life>0); glooWalls=glooWalls.filter(w=>!w.dead);
  enemies.forEach(en=>{if(en.cd>0) en.cd--; let dist=Math.hypot(en.x-player.x,en.y-player.y); if(dist<600){en.angle=Math.atan2(player.y-en.y,player.x-en.x); if(dist>150){let tx=en.x+Math.cos(en.angle)*1.7, ty=en.y+Math.sin(en.angle)*1.7; let blk=false; [...buildings,...glooWalls].forEach(b=>{if(tx>b.x && tx<b.x+b.w && en.y>b.y && en.y<b.y+b.h) blk=true;}); if(!blk) en.x=tx; blk=false; [...buildings,...glooWalls].forEach(b=>{if(en.x>b.x && en.x<b.x+b.w && ty>b.y && ty<b.y+b.h) blk=true;}); if(!blk) en.y=ty;} if(en.cd==0 && dist<420 && player.invis<=0){let gd=guns[en.gun]; bullets.push({x:en.x+Math.cos(en.angle)*30,y:en.y+Math.sin(en.angle)*30,vx:Math.cos(en.angle)*16,vy:Math.sin(en.angle)*16,owner:'enemy',dmg:gd.dmg*0.55,life:70}); en.cd=gd.rate/16;}} if(en.tagged>0) en.tagged--;});
  ctx.save(); if(shake>0){ctx.translate((Math.random()-0.5)*shake,(Math.random()-0.5)*shake); shake*=0.87;} ctx.translate(canvas.width/2-cam.x, canvas.height/2-cam.y);
  ctx.fillStyle='#132213'; ctx.fillRect(cam.x-1300,cam.y-1000,2600,2000);
  ctx.beginPath(); ctx.arc(1200,1200,safeR,0,Math.PI*2); ctx.strokeStyle='#0ff'; ctx.lineWidth=4; ctx.setLineDash([26,16]); ctx.stroke(); ctx.setLineDash([]);
  buildings.forEach(b=>{ctx.fillStyle='rgba(0,0,0,0.5)'; ctx.fillRect(b.x+10,b.y+10,b.w,b.h); ctx.fillStyle='#2e2e2e'; ctx.fillRect(b.x,b.y,b.w,b.h); ctx.strokeStyle='#000'; ctx.lineWidth=2; ctx.strokeRect(b.x,b.y,b.w,b.h);});
  loots.forEach(l=>{if(l.taken) return; let col=guns[l.type]?guns[l.type].color:l.type=='medkit'?'#f0f':l.type=='gloo'?'#0ef':'#ff0'; ctx.shadowColor=col; ctx.shadowBlur=16; ctx.fillStyle=col; ctx.fillRect(l.x-11,l.y-11,22,22); ctx.shadowBlur=0;});
  glooWalls.forEach(w=>{if(w.isDome){ctx.fillStyle='rgba(0,200,255,0.18)'; ctx.beginPath(); ctx.arc(w.x+w.w/2,w.y+w.h/2,w.w/2,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#0ef'; ctx.lineWidth=3; ctx.stroke();} else {ctx.fillStyle='rgba(0,230,255,0.92)'; ctx.fillRect(w.x,w.y,w.w,w.h); ctx.strokeStyle='#fff'; ctx.lineWidth=2; ctx.strokeRect(w.x,w.y,w.w,w.h);}});
  enemies.forEach(en=>{ctx.save(); ctx.translate(en.x,en.y); ctx.rotate(en.angle); ctx.fillStyle='#7a0000'; ctx.fillRect(-16,-12,32,24); ctx.fillStyle='#444'; ctx.beginPath(); ctx.arc(10,0,9,0,Math.PI*2); ctx.fill(); ctx.fillStyle='#111'; ctx.fillRect(17,-4,30,8); if(en.tagged>0){ctx.strokeStyle='#f0f'; ctx.lineWidth=3; ctx.strokeRect(-20,-20,40,40);} ctx.restore(); ctx.fillStyle='#000'; ctx.fillRect(en.x-22,en.y-32,44,7); ctx.fillStyle='#0f0'; ctx.fillRect(en.x-22,en.y-32,en.hp*0.44,7);});
  if(player.invis<=0 || Math.floor(Date.now()/120)%2==0){ctx.save(); ctx.translate(player.x,player.y); ctx.rotate(player.angle); if(player.shield>0){ctx.strokeStyle='rgba(0,200,255,0.85)'; ctx.lineWidth=5; ctx.beginPath(); ctx.arc(0,0,42,0,Math.PI*2); ctx.stroke();} ctx.fillStyle=chars.find(c=>c.id==selChar).icon=='🎧'?'#0fc':chars.find(c=>c.id==selChar).icon=='🛡️'?'#0af':chars.find(c=>c.id==selChar).icon=='🏃'?'#fa0':'#8f0'; ctx.fillRect(-18,-13,36,26); ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(12,0,10,0,Math.PI*2); ctx.fill(); let gCol=player.gun.color||'#222'; ctx.fillStyle=gCol; ctx.fillRect(20,-5,38,10); ctx.fillStyle='#111'; ctx.fillRect(52,-3,18,6); ctx.restore(); if(selPet!='none'){let petX=player.x-Math.cos(player.angle)*38, petY=player.y-Math.sin(player.angle)*38; ctx.font='20px Arial'; ctx.fillText(pets.find(p=>p.id==selPet).icon, petX-10, petY-10);}}
  bullets.forEach(b=>{ctx.strokeStyle=b.owner=='player'?'rgba(255,255,0,0.75)':'rgba(255,90,90,0.75)'; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(b.x-b.vx*2.5,b.y-b.vy*2.5); ctx.lineTo(b.x,b.y); ctx.stroke(); ctx.fillStyle=b.owner=='player'?'#ff0':'#f99'; ctx.beginPath(); ctx.arc(b.x,b.y,4,0,Math.PI*2); ctx.fill();});
  particles.forEach(p=>{p.x+=p.vx; p.y+=p.vy; p.life--; p.vx*=0.92; p.vy*=0.92; ctx.globalAlpha=p.life/30; ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.s,0,Math.PI*2); ctx.fill(); ctx.globalAlpha=1;}); particles=particles.filter(p=>p.life>0);
  ctx.restore();
  document.getElementById('alive').innerText=enemies.length+1; document.getElementById('gunName').innerText=player.gun.name; document.getElementById('ammo').innerText=player.gun==guns.fist?'∞':player.ammo+' / ∞'; document.getElementById('hpFill').style.width=(player.hp/player.maxHp*100)+'%'; document.getElementById('vestTxt').innerText=player.vest||0;
  if(player.invis>0) player.invis--;
  if(enemies.length==0 && game){game=false; setTimeout(()=>{alert('BOOYAH! 🏆'); location.reload()},500);}
  requestAnimationFrame(loop);
}
loop();
window.addEventListener('resize', ()=>{canvas.width=innerWidth; canvas.height=innerHeight;});
</script>
</body>
</html>
""", height=850)
