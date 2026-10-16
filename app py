import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="FF ULTIMATE - EVERYTHING", page_icon="🔥", layout="wide")
components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Russo+One&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;font-family:Orbitron}
body{background:#060e06;overflow:hidden}
#canvas{width:100vw;height:100vh;display:block}
#top{position:absolute;top:0;left:0;right:0;height:82px;background:linear-gradient(180deg,#000 0%,rgba(0,0,0,0.7) 60%,transparent);display:flex;justify-content:space-between;padding:8px 10px;color:#fff;z-index:20}
.box{background:rgba(0,0,0,0.75);border:1.5px solid rgba(255,255,255,0.25);border-radius:10px;padding:5px 9px;text-align:center;min-width:72px}
#hpWrap{width:100%;height:12px;background:#1a1a1a;border-radius:6px;border:1px solid #fff;overflow:hidden}
#hpFill{height:100%;background:linear-gradient(90deg,#00ff88,#00ffcc);width:100%;transition:0.25s}
#skillRow{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:20}
.skill{width:64px;height:64px;border-radius:16px;border:3px solid #fff;background:radial-gradient(#222,#000);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;position:relative;box-shadow:0 5px 18px #000}
.skill.active{border-color:#00ffcc;box-shadow:0 0 22px #00ffcc}
.cd{position:absolute;inset:0;background:rgba(0,0,0,0.78);border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:18px;display:none}
.joy{position:absolute;bottom:16px;width:138px;height:138px;background:radial-gradient(rgba(255,255,255,0.2),rgba(255,255,255,0.04));border-radius:70px;border:2px solid rgba(255,255,255,0.28);backdrop-filter:blur(7px);z-index:20}
#joyMove{left:12px} #joyAim{right:108px;width:106px;height:106px;bottom:26px}
.stick{position:absolute;width:60px;height:60px;background:radial-gradient(#fff,#aaa);border-radius:30px;left:39px;top:39px;box-shadow:0 5px 14px #000}
#stickAim{width:46px;height:46px;left:30px;top:30px;background:radial-gradient(#ff4444,#880000)}
.btn{position:absolute;z-index:20;border:none;font-weight:900;color:#fff;text-shadow:1px 1px 3px #000;box-shadow:0 6px 20px rgba(0,0,0,0.7)}
#fireBtn{bottom:128px;right:14px;width:104px;height:104px;background:radial-gradient(#ff5050,#990000);border-radius:52px;border:3px solid #fff;font-size:23px}
#glooBtn{bottom:18px;right:12px;width:90px;height:54px;background:linear-gradient(180deg,#00eaff,#0077ff);border-radius:12px;border:2px solid #fff;font-size:11px}
#grenadeBtn{bottom:18px;right:112px;width:52px;height:52px;background:radial-gradient(#88ff00,#448800);border-radius:26px;border:2px solid #fff;font-size:18px}
#emoteBtn{bottom:78px;right:112px;width:52px;height:26px;background:rgba(0,0,0,0.7);border-radius:8px;border:1px solid #ffcc00;color:#ffcc00;font-size:9px}
#shop{position:absolute;top:88px;right:8px;width:122px;background:rgba(0,0,0,0.8);border-radius:12px;border:1.5px solid #ffcc00;padding:7px;color:#fff;font-size:9px;z-index:20}
#feed{position:absolute;top:90px;left:8px;color:#ffcc00;font-size:10px;z-index:20;line-height:13px;max-width:180px}
#mini{position:absolute;top:88px;right:138px;width:108px;height:108px;background:rgba(0,0,0,0.8);border:2px solid #fff;border-radius:12px;z-index:20}
#select{position:absolute;inset:0;background:radial-gradient(ellipse at center,#123212,#000);z-index:100;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;padding:14px;overflow-y:auto}
.card{width:148px;height:198px;background:rgba(255,255,255,0.07);border:2px solid rgba(255,255,255,0.2);border-radius:18px;margin:6px;padding:10px;text-align:center;cursor:pointer}
.card.sel{border-color:#00ffcc;background:rgba(0,255,204,0.18);box-shadow:0 0 28px #00ffcc}
.petRow{display:flex;gap:8px;margin-top:12px}
.petCard{width:92px;height:86px;background:rgba(255,255,255,0.06);border:2px solid #555;border-radius:12px;text-align:center;padding:6px;cursor:pointer;font-size:9px}
.petCard.sel{border-color:#ffaa00;box-shadow:0 0 15px #ffaa00}
#vehicleBar{position:absolute;bottom:140px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,0.7);border-radius:20px;padding:6px 14px;color:#00ffcc;font-size:11px;z-index:20;display:none}
</style>
</head>
<body>
<div id="select">
<h1 style="font-family:Russo One;font-size:30px;color:#00ffcc;text-shadow:0 0 18px #00ffcc;letter-spacing:2px">FREE FIRE ULTIMATE</h1>
<p style="font-size:11px;opacity:0.8;margin:6px 0">EVERYTHING EDITION - Choose Character + Pet</p>
<div style="display:flex;flex-wrap:wrap;justify-content:center;max-width:700px" id="charList"></div>
<p style="margin:14px 0 6px;font-size:11px;color:#ffcc00">CHOOSE PET (Bonus)</p>
<div class="petRow" id="petList"></div>
<button id="goBtn" style="margin-top:18px;padding:14px 50px;background:linear-gradient(90deg,#00ffcc,#0088ff);border:none;border-radius:30px;font-size:19px;font-weight:900;color:#000;box-shadow:0 0 30px #00ffcc">DROP IN BERMUDA 🔥</button>
<div style="margin-top:12px;font-size:9px;opacity:0.5;text-align:center;max-width:360px;line-height:12px">Includes: 8 Guns, Gloo, Grenade, Airdrop Plane, Vehicle, Landmine, Launchpad, Medkit, Vest/Helm Lv3, Emotes, Rank Heroic</div>
</div>

<div id="top">
<div class="box"><div style="font-size:8px;opacity:0.6">ALIVE</div><div id="alive" style="font-size:20px">13</div><div id="rank" style="font-size:9px;color:#ffaa00">BRONZE I</div></div>
<div class="box"><div style="font-size:8px">GUN</div><div id="gunName" style="font-size:12px;color:#00ffcc">FIST</div><div id="ammo" style="font-size:10px">∞</div></div>
<div class="box"><div id="hpWrap"><div id="hpFill"></div></div><div style="font-size:8px;margin-top:3px">VEST <span id="vestTxt">0</span> HELM <span id="helmTxt">0</span> <span id="petBonus"></span></div></div>
</div>
<div id="feed"></div>
<div id="shop"><b style="color:#ffcc00">SHOP / LOOT</b><div id="lootTxt" style="margin-top:4px"></div><div style="margin-top:6px;border-top:1px solid #555;padding-top:4px"><div id="invTxt"></div></div></div>
<canvas id="mini"></canvas>
<div id="vehicleBar">🚗 IN VEHICLE - Joystick to Drive | FIRE to Exit</div>
<div class="joy" id="joyMove"><div class="stick" id="stickMove"></div></div>
<div class="joy" id="joyAim"><div class="stick" id="stickAim"></div></div>
<button class="btn" id="fireBtn">FIRE</button>
<button class="btn" id="glooBtn">GLOO<br><span id="glooCnt">4</span></button>
<button class="btn" id="grenadeBtn">💣</button>
<button class="btn" id="emoteBtn">EMOTE</button>
<div id="skillRow">
<div class="skill" id="skillMain"><div id="sIcon" style="font-size:22px">🎧</div><div id="sName" style="font-size:7px">ALOK</div><div class="cd" id="sCd">0</div></div>
<div class="skill" id="medBtn"><div style="font-size:20px">💊</div><div style="font-size:7px">MEDKIT</div><div class="cd" id="medCd">0</div></div>
</div>
<canvas id="canvas"></canvas>
<script>
const canvas=document.getElementById('canvas'), ctx=canvas.getContext('2d');
const mcanvas=document.getElementById('mini'), mctx=mcanvas.getContext('2d');
canvas.width=innerWidth; canvas.height=innerHeight; mcanvas.width=108; mcanvas.height=108;

const chars=[
{id:'alok',icon:'🎧',name:'ALOK',desc:'Heal Aura +5HP/s<br>10 sec',color:'#00ffcc',skill:'Drop The Beat'},
{id:'chrono',icon:'🛡️',name:'CHRONO',desc:'Dome Shield 600HP<br>6 sec',color:'#00aaff',skill:'Time Turner'},
{id:'kelly',icon:'🏃',name:'KELLY',desc:'Dash +35% Speed<br>4 sec',color:'#ffaa00',skill:'Dash'},
{id:'wukong',icon:'🌿',name:'WUKONG',desc:'Bush Camo Invis<br>9 sec',color:'#88ff00',skill:'Camouflage'},
{id:'dj_alok2',icon:'⚡',name:'HAYATO',desc:'Armor +10% when<br>HP low',color:'#ff4444',skill:'Bushido'},
{id:'moco',icon:'🎯',name:'MOCO',desc:'Tag Enemy 5 sec<br>See thru wall',color:'#ff00ff',skill:'Hacker Eye'},
{id:'skyler',icon:'🌊',name:'SKYLER',desc:'Break Gloo + Heal<br>9HP each',color:'#00ffaa',skill:'Riptide Rhythm'},
{id:'chrono2',icon:'🔥',name:'K',desc:'EP +500%<br>Team EP',color:'#ffff00',skill:'Master Of All'}
];
const pets=[
{id:'none',icon:'❌',name:'No Pet',bonus:''},
{id:'falco',icon:'🦅',name:'Falco',bonus:'+25% Glide + Loot'},
{id:'shiba',icon:'🐶',name:'Shiba',bonus:'+Mushroom Sense'},
{id:'panda',icon:'🐼',name:'Detective Panda',bonus:'+10HP per Kill'},
{id:'otter',icon:'🦦',name:'Otto',bonus:'+Medkit Extra'}
];

let selChar='alok', selPet='falco';
const charList=document.getElementById('charList'), petList=document.getElementById('petList');
chars.forEach(c=>{
  let d=document.createElement('div'); d.className='card'+(c.id==selChar?' sel':''); d.innerHTML=`<div style="font-size:36px">${c.icon}</div><b style="color:${c.color}">${c.name}</b><br><span style="font-size:9px;line-height:11px">${c.desc}</span><div style="margin-top:7px;background:${c.color};color:#000;border-radius:6px;padding:3px;font-size:9px;font-weight:900">${c.skill}</div>`;
  d.onclick=()=>{selChar=c.id; document.querySelectorAll('.card').forEach(x=>x.classList.remove('sel')); d.classList.add('sel');};
  charList.appendChild(d);
});
pets.forEach(p=>{
  let d=document.createElement('div'); d.className='petCard'+(p.id==selPet?' sel':''); d.innerHTML=`<div style="font-size:28px">${p.icon}</div><b>${p.name}</b><br><span style="font-size:8px">${p.bonus}</span>`;
  d.onclick=()=>{selPet=p.id; document.querySelectorAll('.petCard').forEach(x=>x.classList.remove('sel')); d.classList.add('sel');};
  petList.appendChild(d);
});

let game=false, player, bullets=[], enemies=[], buildings=[], loots=[], glooWalls=[], particles=[], vehicles=[], mines=[], launchpads=[], grenades=[], plane={x:-500,y:300,active:true,speed:6,dropTimer:0}, killFeed=[], cam={x:1000,y:1000}, shake=0, joyM={x:0,y:0}, joyA={x:0,y:0}, skillReady=true, skillCD=0, medCD=0, glooCount=4, grenadeCount=3, inVehicle=null, rankScore=0, kills=0;

let guns={
fist:{name:'FIST',dmg:22,rate:350,ammo:0,range:38,color:'#fff'},
mp40:{name:'MP40',dmg:24,rate:85,ammo:40,range:380,color:'#ffaa00',icon:'🔫'},
m1887:{name:'M1887',dmg:19*6,rate:580,ammo:8,range:260,color:'#ff4444',icon:'💥'},
awm:{name:'AWM',dmg:95,rate:1300,ammo:5,range:950,color:'#00ffcc',icon:'🎯'},
ak:{name:'AK',dmg:40,rate:145,ammo:30,range:520,color:'#ff8800',icon:'🔥'},
ump:{name:'UMP',dmg:27,rate:108,ammo:32,range:460,color:'#aaaaff',icon:'⚡'},
scar:{name:'SCAR',dmg:32,rate:125,ammo:30,range:580,color:'#00ff88',icon:'✦'},
groza:{name:'GROZA',dmg:36,rate:95,ammo:30,range:500,color:'#ff00ff',icon:'☠️'},
};

function resetWorld(){
  player={x:1000,y:1000,angle:0,hp:100,maxHp:100,vest:0,helm:0,gun:guns.fist,ammo:0,reserve:120,shield:0,speed:1,invis:0,tagged:0,ep:0,vestLevel:0,helmLevel:0};
  if(selPet=='falco'){player.x=1000+Math.random()*100; glooCount=5;}
  if(selPet=='otter') glooCount=4;
  bullets=[]; enemies=[]; buildings=[]; loots=[]; glooWalls=[]; particles=[]; vehicles=[]; mines=[]; launchpads=[]; grenades=[];
  // Map - Bermuda 2.0
  for(let i=0;i<28;i++) buildings.push({x:Math.random()*2400,y:Math.random()*2400,w:65+Math.random()*135,h:65+Math.random()*115});
  buildings.push({x:900,y:900,w:240,h:240,type:'clock'}); buildings.push({x:1500,y:600,w:180,h:180,type:'factory'});
  // Loots
  let types=['mp40','m1887','awm','ak','ump','scar','groza','vest2','vest3','helm2','helm3','medkit','gloo','grenade','mine','launchpad'];
  for(let i=0;i<48;i++){let t=types[Math.floor(Math.random()*types.length)]; loots.push({x:Math.random()*2400,y:Math.random()*2400,type:t,taken:false});}
  // Enemies
  for(let i=0;i<12;i++) enemies.push({x:Math.random()*2400,y:Math.random()*2400,hp:100,angle:0,gun:Object.keys(guns)[1+Math.floor(Math.random()*7)],cd:0,vest:Math.floor(Math.random()*3),helm:Math.floor(Math.random()*3),tagged:0});
  // Vehicles
  vehicles.push({x:600,y:600,w:80,h:45,hp:1000,occupied:false,speed:0,angle:0});
  vehicles.push({x:1600,y:1400,w:80,h:45,hp:1000,occupied:false,speed:0,angle:0});
  // Launchpads & mines
  launchpads.push({x:1100,y:500,w:60,h:60}); launchpads.push({x:1800,y:1100,w:60,h:60});
  for(let i=0;i<6;i++) mines.push({x:Math.random()*2400,y:Math.random()*2400,armed:true,triggered:false});
  plane={x:-600,y:300+Math.random()*800,active:true,speed:5.5+Math.random()*2,dropTimer:0};
  glooCount= selPet=='falco'?5:4; grenadeCount=3; kills=0; rankScore=0;
}

function setupJoy(joyId, stickId, out){
  const joy=document.getElementById(joyId), stick=document.getElementById(stickId);
  let act=false;
  joy.addEventListener('touchstart', e=>act=true);
  joy.addEventListener('touchmove', e=>{
    if(!act) return;
    let r=joy.getBoundingClientRect(), t=e.touches[0], cx=r.left+r.width/2, cy=r.top+r.height/2;
    let dx=t.clientX-cx, dy=t.clientY-cy, d=Math.hypot(dx,dy), m=r.width/2-12;
    if(d>m){dx=dx/d*m; dy=dy/d*m;}
    stick.style.left=(r.width/2-stick.offsetWidth/2+dx)+'px'; stick.style.top=(r.height/2-stick.offsetHeight/2+dy)+'px';
    out.x=dx/m; out.y=dy/m;
  });
  const end=()=>{act=false; stick.style.left='39px'; stick.style.top='39px'; if(stickId=='stickAim'){stick.style.left='30px'; stick.style.top='30px'} out.x=0; out.y=0;};
  joy.addEventListener('touchend', end); joy.addEventListener('touchcancel', end);
}
setupJoy('joyMove','stickMove',joyM); setupJoy('joyAim','stickAim',joyA);

document.getElementById('goBtn').onclick=()=>{document.getElementById('select').style.display='none'; resetWorld(); game=true; document.getElementById('sIcon').innerText=chars.find(c=>c.id==selChar).icon; document.getElementById('sName').innerText=chars.find(c=>c.id==selChar).name; document.getElementById('petBonus').innerText= pets.find(p=>p.id==selPet).bonus;};

function isBlocked(x,y){for(let b of [...buildings,...glooWalls]) if(x>b.x && x<b.x+b.w && y>b.y && y<b.y+b.h) return true; return false;}
function addFeed(t){killFeed.unshift(t); if(killFeed.length>5) killFeed.pop(); document.getElementById('feed').innerHTML=killFeed.join('<br>');}
function shoot(){
  if(!game) return;
  if(Date.now()- (shoot.last||0) < player.gun.rate) return; shoot.last=Date.now();
  if(player.gun!=guns.fist && player.ammo<=0){addFeed('RELOAD!'); return;}
  if(player.gun!=guns.fist) player.ammo--;
  let spread=0.14, pellets=player.gun.name=='M1887'?6:1;
  for(let p=0;p<pellets;p++){let a=player.angle+(Math.random()-0.5)*spread; bullets.push({x:player.x+Math.cos(player.angle)*34,y:player.y+Math.sin(player.angle)*34,vx:Math.cos(a)*20,vy:Math.sin(a)*20,owner:'player',dmg:player.gun.dmg/(pellets>1?pellets:1),life:75,gun:player.gun.name});}
  shake=player.gun.name=='AWM'?16:7;
  for(let i=0;i<10;i++) particles.push({x:player.x+Math.cos(player.angle)*38,y:player.y+Math.sin(player.angle)*38,vx:Math.cos(player.angle)*(3+Math.random()*5)+(Math.random()-0.5)*3,vy:Math.sin(player.angle)*(3+Math.random()*5)+(Math.random()-0.5)*3,life:9,color:i<5?'#ffff00':'#ff8800',s:2+Math.random()*3});
  if(navigator.vibrate) navigator.vibrate(30);
}
document.getElementById('fireBtn').addEventListener('touchstart', e=>{e.preventDefault(); shoot()});
document.getElementById('fireBtn').addEventListener('mousedown', shoot);

document.getElementById('glooBtn').onclick=()=>{
  if(glooCount<=0) return; glooCount--; document.getElementById('glooCnt').innerText=glooCount;
  let gx=player.x+Math.cos(player.angle)*85, gy=player.y+Math.sin(player.angle)*85;
  glooWalls.push({x:gx-36,y:gy-36,w:72,h:72,hp:500,max:500});
};
document.getElementById('grenadeBtn').onclick=()=>{
  if(grenadeCount<=0) return; grenadeCount--;
  grenades.push({x:player.x,y:player.y,vx:Math.cos(player.angle)*9,vy:Math.sin(player.angle)*9,life:90,owner:'player'});
  addFeed('💣 GRENADE!');
};
document.getElementById('emoteBtn').onclick=()=>{
  let emotes=['💃','🕺','😎','🔥','👑']; let e=emotes[Math.floor(Math.random()*emotes.length)];
  for(let i=0;i<18;i++) particles.push({x:player.x,y:player.y-20,vx:(Math.random()-0.5)*4,vy:-2-Math.random()*3,life:40,color:'#ffcc00',s:6,text:e});
  addFeed('Emote: '+e);
};
document.getElementById('skillMain').onclick=()=>{
  if(!skillReady) return; skillReady=false; skillCD= chars.find(c=>c.id==selChar).id=='alok'?32: chars.find(c=>c.id==selChar).id=='chrono'?40: chars.find(c=>c.id==selChar).id=='kelly'?18: chars.find(c=>c.id==selChar).id=='wukong'?38: 30;
  let ch=chars.find(c=>c.id==selChar);
  if(selChar=='alok'){player.hp=Math.min(player.maxHp,player.hp+50); player.speed=1.35; setTimeout(()=>player.speed=1,5000); addFeed('🎧 ALOK: +50 HP + SPEED!'); for(let i=0;i<30;i++) particles.push({x:player.x+(Math.random()-0.5)*140,y:player.y+(Math.random()-0.5)*140,vx:0,vy:-1.2,life:35,color:'#00ffcc',s:4});}
  else if(selChar=='chrono'){player.shield=650; glooWalls.push({x:player.x-90,y:player.y-90,w:180,h:180,hp:650,max:650,isDome:true}); addFeed('🛡️ CHRONO DOME!');}
  else if(selChar=='kelly'){player.speed=2.4; setTimeout(()=>player.speed=1,4000); addFeed('🏃 KELLY SUPER DASH!');}
  else if(selChar=='wukong'){player.invis=540; addFeed('🌿 WUKONG INVISIBLE 9s');}
  else if(selChar=='dj_alok2'){player.maxHp=150; player.hp=Math.min(150,player.hp+20); addFeed('⚡ HAYATO: ARMOR +20');}
  else if(selChar=='moco'){enemies.forEach(en=>{if(Math.hypot(en.x-player.x,en.y-player.y)<600) en.tagged=300}); addFeed('🎯 MOCO: TAGGED ENEMIES!');}
  else if(selChar=='skyler'){glooWalls.forEach(w=>{if(Math.hypot(w.x-player.x,w.y-player.y)<250) w.hp-=400}); player.hp=Math.min(player.maxHp,player.hp+40); addFeed('🌊 SKYLER: BREAK GLOO + HEAL');}
  else if(selChar=='chrono2'){player.ep+=100; player.hp=Math.min(player.maxHp,player.hp+30); addFeed('🔥 K: EP + HP!');}
  document.getElementById('sCd').style.display='flex';
};
document.getElementById('medBtn').onclick=()=>{
  if(medCD>0) return; if(player.hp>=player.maxHp) return;
  medCD=8; player.hp=Math.min(player.maxHp,player.hp+ (selPet=='otter'?90:75));
  if(selPet=='panda') player.hp=Math.min(player.maxHp,player.hp+10);
  addFeed('💊 MEDKIT USED');
  document.getElementById('medCd').style.display='flex';
};

function loop(){
  if(!game){requestAnimationFrame(loop); return;}
  // Cooldowns
  if(!skillReady){skillCD-=0.016; document.getElementById('sCd').innerText=Math.ceil(skillCD); if(skillCD<=0){skillReady=true; document.getElementById('sCd').style.display='none';}}
  if(medCD>0){medCD-=0.016; document.getElementById('medCd').innerText=Math.ceil(medCD); if(medCD<=0){document.getElementById('medCd').style.display='none';}}

  // Vehicle enter/exit
  if(inVehicle){
    inVehicle.angle=Math.atan2(joyM.y,joyM.x);
    if(Math.hypot(joyM.x,joyM.y)>0.2){inVehicle.x+=Math.cos(inVehicle.angle)*8; inVehicle.y+=Math.sin(inVehicle.angle)*8; player.x=inVehicle.x; player.y=inVehicle.y;}
    if(Math.hypot(joyA.x,joyA.y)>0.8){inVehicle.occupied=false; inVehicle=null; document.getElementById('vehicleBar').style.display='none';}
  } else {
    let mx=joyM.x, my=joyM.y, sp=5.8*player.speed;
    let nx=player.x+mx*sp, ny=player.y+my*sp;
    if(!isBlocked(nx,player.y)) player.x=nx;
    if(!isBlocked(player.x,ny)) player.y=ny;
    // Enter vehicle
    vehicles.forEach(v=>{if(Math.hypot(player.x-v.x,player.y-v.y)<60 && !v.occupied && Math.hypot(joyM.x,joyM.y)<0.1 && Math.hypot(joyA.x,joyA.y)>0.8){v.occupied=true; inVehicle=v; document.getElementById('vehicleBar').style.display='block';}});
  }

  if(Math.hypot(joyA.x,joyA.y)>0.28) player.angle=Math.atan2(joyA.y,joyA.x);
  cam.x+=(player.x-cam.x)*0.13; cam.y+=(player.y-cam.y)*0.13;

  // Plane Airdrop
  if(plane.active){
    plane.x+=plane.speed; plane.dropTimer++;
    if(plane.dropTimer>180+Math.random()*200){loots.push({x:plane.x,y:plane.y+80,type:['awm','groza','vest3','helm3','gloo'][Math.floor(Math.random()*5)],taken:false,isAirdrop:true}); plane.dropTimer=0; addFeed('✈️ AIRDROP FALLING!');}
    if(plane.x>2600) plane.active=false;
  }

  // Safe zone shrink
  let safeR=1000 - Date.now()/1400; safeR=Math.max(170,safeR);
  if(Math.hypot(player.x-1200,player.y-1200)>safeR){player.hp-=0.45; if(player.vest>0) player.hp-=0.15;}

  // Loot pickup + mines + launchpad
  let near=[];
  loots.forEach(l=>{
    if(!l.taken && Math.hypot(player.x-l.x,player.y-l.y)<48){
      if(l.type=='medkit'){player.hp=Math.min(player.maxHp,player.hp+75); addFeed('💊 MEDKIT');}
      else if(l.type.startsWith('vest')){let lvl=l.type=='vest2'?2:3; if(lvl>player.vestLevel){player.vestLevel=lvl; player.vest=lvl; player.maxHp=lvl==2?125:lvl==3?150:100; addFeed('🦺 VEST LV'+lvl);}}
      else if(l.type.startsWith('helm')){let lvl=l.type=='helm2'?2:3; if(lvl>player.helmLevel){player.helmLevel=lvl; player.helm=lvl; addFeed('🪖 HELM LV'+lvl);}}
      else if(l.type=='gloo'){glooCount=Math.min(6,glooCount+1); document.getElementById('glooCnt').innerText=glooCount; addFeed('🧱 GLOO +1');}
      else if(l.type=='grenade'){grenadeCount=Math.min(5,grenadeCount+1); addFeed('💣 GRENADE +1');}
      else if(l.type=='mine'){mines.push({x:player.x+Math.cos(player.angle)*70,y:player.y+Math.sin(player.angle)*70,armed:true,owner:'player'}); addFeed('💣 MINE PLACED');}
      else if(l.type=='launchpad'){launchpads.push({x:player.x,y:player.y,w:60,h:60}); addFeed('🚀 LAUNCHPAD');}
      else {player.gun=guns[l.type]; player.ammo=player.gun.ammo; addFeed('🔫 '+player.gun.name); if(selPet=='falco') player.ammo+=Math.floor(player.ammo*0.25);}
      l.taken=true; if(selPet=='panda'){rankScore+=10;}
    }
    if(!l.taken && Math.hypot(player.x-l.x,player.y-l.y)<190) near.push((guns[l.type]?guns[l.type].name:l.type.toUpperCase()));
  });
  mines.forEach(m=>{
    if(!m.triggered && Math.hypot(player.x-m.x,player.y-m.y)<30 && m.owner!='player'){m.triggered=true; player.hp-=60; shake=18; addFeed('💥 MINE! -60 HP'); for(let i=0;i<20;i++) particles.push({x:m.x,y:m.y,vx:(Math.random()-0.5)*10,vy:(Math.random()-0.5)*10,life:20,color:'#ff4400',s:4});}
    enemies.forEach(en=>{if(!m.triggered && Math.hypot(en.x-m.x,en.y-m.y)<30){m.triggered=true; en.hp-=80; for(let i=0;i<20;i++) particles.push({x:m.x,y:m.y,vx:(Math.random()-0.5)*10,vy:(Math.random()-0.5)*10,life:20,color:'#ff4400',s:4});}});
  });
  mines=mines.filter(m=>!m.triggered);
  launchpads.forEach(lp=>{if(Math.hypot(player.x-lp.x,player.y-lp.y)<45){player.x+=Math.cos(player.angle)*120; player.y+=Math.sin(player.angle)*120; addFeed('🚀 LAUNCHPAD!'); for(let i=0;i<15;i++) particles.push({x:lp.x,y:lp.y,vx:(Math.random()-0.5)*4,vy:-3-Math.random()*4,life:25,color:'#00eaff',s:3});}});

  // Grenades
  grenades.forEach(g=>{
    g.x+=g.vx; g.y+=g.vy; g.vx*=0.98; g.vy*=0.98; g.life--;
    if(g.life<=0){for(let i=0;i<25;i++) particles.push({x:g.x,y:g.y,vx:(Math.random()-0.5)*12,vy:(Math.random()-0.5)*12,life:22,color:'#ff6600',s:5}); 
      if(Math.hypot(player.x-g.x,player.y-g.y)<110) player.hp-= g.owner=='player'?20:55;
      enemies.forEach(en=>{if(Math.hypot(en.x-g.x,en.y-g.y)<110) en.hp-=65;});
      g.dead=true;
    }
  });
  grenades=grenades.filter(g=>!g.dead);

  // Bullets
  bullets.forEach(b=>{
    b.x+=b.vx; b.y+=b.vy; b.life--;
    let hit=false;
    [...buildings,...glooWalls].forEach(w=>{if(b.x>w.x && b.x<w.x+w.w && b.y>w.y && b.y<w.y+w.h){hit=true; if(w.hp!==undefined){w.hp-=b.dmg; if(w.hp<=0) w.dead=true;} b.life=0;}});
    if(!hit && b.owner=='player'){
      enemies.forEach((en,i)=>{
        if(Math.hypot(b.x-en.x,b.y-en.y)<27){
          let dmg=b.dmg * (en.vest?0.7:1); en.hp-=dmg; b.life=0;
          for(let k=0;k<8;k++) particles.push({x:en.x,y:en.y,vx:(Math.random()-0.5)*7,vy:(Math.random()-0.5)*7,life:15,color:'#ff2222',s:3});
          if(en.hp<=0){enemies.splice(i,1); kills++; rankScore+=100; if(selPet=='panda') player.hp=Math.min(player.maxHp,player.hp+10); addFeed('💀 KILL +'+b.gun); if(kills==12){addFeed('🏆 BOOYAH! HEROIC!');}}
        }
      });
    } else if(b.owner!='player' && Math.hypot(b.x-player.x,b.y-player.y)<30 && player.invis<=0){
      let dmg=b.dmg * (player.vest?0.65:1) * (player.helm?0.8:1);
      if(player.shield>0){player.shield-=dmg; dmg=0; if(player.shield<=0){player.shield=0; addFeed('🛡️ SHIELD BROKE');}}
      player.hp-=dmg; b.life=0; shake=13;
      if(player.hp<=0){alert('ELIMINATED! Rank: '+document.getElementById('rank').innerText+' | Kills: '+kills); location.reload();}
    }
  });
  bullets=bullets.filter(b=>b.life>0); glooWalls=glooWalls.filter(w=>!w.dead);

  // Enemies AI with moco tag
  enemies.forEach(en=>{
    if(en.cd>0) en.cd--;
    if(en.tagged>0) en.tagged--;
    let dist=Math.hypot(en.x-player.x,en.y-player.y);
    if(dist<600){
      en.angle=Math.atan2(player.y-en.y,player.x-en.x);
      if(dist>150){
        let tx=en.x+Math.cos(en.angle)*1.7, ty=en.y+Math.sin(en.angle)*1.7;
        if(!isBlocked(tx,en.y)) en.x=tx;
        if(!isBlocked(en.x,ty)) en.y=ty;
      }
      if(en.cd==0 && dist<420 && player.invis<=0){
        let gd=guns[en.gun];
        bullets.push({x:en.x+Math.cos(en.angle)*30,y:en.y+Math.sin(en.angle)*30,vx:Math.cos(en.angle)*16,vy:Math.sin(en.angle)*16,owner:'enemy',dmg:gd.dmg*0.55,life:70});
        en.cd=gd.rate/16;
      }
    }
  });

  // DRAW
  ctx.save();
  if(shake>0){ctx.translate((Math.random()-0.5)*shake,(Math.random()-0.5)*shake); shake*=0.87;}
  ctx.translate(canvas.width/2-cam.x, canvas.height/2-cam.y);

  ctx.fillStyle='#132213'; ctx.fillRect(cam.x-1300,cam.y-1000,2600,2000);
  ctx.fillStyle='rgba(255,255,255,0.03)'; for(let i=0;i<400;i++) ctx.fillRect((i*173)%2400,(i*97)%2400,2,2);

  // Safe zone
  ctx.beginPath(); ctx.arc(1200,1200,safeR,0,Math.PI*2); ctx.strokeStyle='#00ffff'; ctx.lineWidth=4; ctx.setLineDash([26,16]); ctx.stroke(); ctx.setLineDash([]); ctx.fillStyle='rgba(0,255,255,0.045)'; ctx.fill();

  // Buildings
  buildings.forEach(b=>{
    ctx.fillStyle='rgba(0,0,0,0.5)'; ctx.fillRect(b.x+10,b.y+10,b.w,b.h);
    ctx.fillStyle=b.type=='clock'?'#4a3720':b.type=='factory'?'#333':'#2e2e2e'; ctx.fillRect(b.x,b.y,b.w,b.h);
    ctx.fillStyle='rgba(255,255,255,0.14)'; ctx.fillRect(b.x,b.y,b.w,8);
    ctx.strokeStyle='#000'; ctx.lineWidth=2; ctx.strokeRect(b.x,b.y,b.w,b.h);
  });

  // Plane
  if(plane.active){
    ctx.fillStyle='#ddd'; ctx.fillRect(plane.x-60,plane.y-15,120,20);
    ctx.fillStyle='#fff'; ctx.fillRect(plane.x+30,plane.y-25,30,8);
    ctx.fillStyle='rgba(255,255,0,0.6)'; ctx.fillRect(plane.x-10,plane.y+10,20,30);
  }

  // Launchpads
  launchpads.forEach(lp=>{ctx.fillStyle='#00eaff'; ctx.fillRect(lp.x,lp.y,lp.w,lp.h); ctx.fillStyle='#fff'; ctx.font='10px Orbitron'; ctx.fillText('LAUNCH',lp.x+4,lp.y+18);});

  // Mines
  mines.forEach(m=>{ctx.fillStyle=m.owner=='player'?'#00ff00':'#ff0000'; ctx.beginPath(); ctx.arc(m.x,m.y,8,0,Math.PI*2); ctx.fill();});

  // Loots glow + airdrop smoke
  loots.forEach(l=>{
    if(l.taken) return;
    let col=guns[l.type]?guns[l.type].color: l.type.includes('vest')?'#00ff00':l.type.includes('helm')?'#8888ff':l.type=='medkit'?'#ff00ff':l.type=='gloo'?'#00eaff':'#ffff00';
    ctx.shadowColor=col; ctx.shadowBlur=l.isAirdrop?28:16; ctx.fillStyle=col; ctx.fillRect(l.x-11,l.y-11,22,22); ctx.shadowBlur=0;
    if(l.isAirdrop){ctx.fillStyle='rgba(255,255,255,0.5)'; ctx.fillRect(l.x-2,l.y-80,4,80);}
    ctx.fillStyle='#fff'; ctx.font='900 9px Orbitron'; ctx.fillText((guns[l.type]?guns[l.type].name:l.type.toUpperCase()),l.x-18,l.y-16);
  });

  // Gloo
  glooWalls.forEach(w=>{
    if(w.isDome){ctx.fillStyle='rgba(0,200,255,0.18)'; ctx.beginPath(); ctx.arc(w.x+w.w/2,w.y+w.h/2,w.w/2,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#00eaff'; ctx.lineWidth=3; ctx.stroke();}
    else {ctx.fillStyle='rgba(0,230,255,0.92)'; ctx.fillRect(w.x,w.y,w.w,w.h); ctx.strokeStyle='#fff'; ctx.lineWidth=2; ctx.strokeRect(w.x,w.y,w.w,w.h); ctx.fillStyle='#000'; ctx.fillRect(w.x,w.y,w.w,7*(w.hp/w.max));}
  });

  // Vehicles
  vehicles.forEach(v=>{
    ctx.fillStyle=v.occupied?'#ffaa00':'#555'; ctx.save(); ctx.translate(v.x+v.w/2,v.y+v.h/2); ctx.rotate(v.angle); ctx.fillRect(-v.w/2,-v.h/2,v.w,v.h); ctx.fillStyle='#222'; ctx.fillRect(-v.w/2+10,-v.h/2+8,18,10); ctx.fillRect(v.w/2-28,-v.h/2+8,18,10); ctx.restore();
  });

  // Enemies
  enemies.forEach(en=>{
    ctx.save(); ctx.translate(en.x,en.y); ctx.rotate(en.angle);
    ctx.fillStyle='rgba(0,0,0,0.4)'; ctx.beginPath(); ctx.ellipse(0,8,20,12,0,0,Math.PI*2); ctx.fill();
    ctx.fillStyle='#7a0000'; ctx.fillRect(-16,-12,32,24);
    ctx.fillStyle='#444'; ctx.beginPath(); ctx.arc(10,0,9,0,Math.PI*2); ctx.fill();
    ctx.fillStyle='#111'; ctx.fillRect(17,-4,30,8);
    if(en.tagged>0){ctx.strokeStyle='#ff00ff'; ctx.lineWidth=3; ctx.strokeRect(-20,-20,40,40);}
    ctx.restore();
    ctx.fillStyle='#000'; ctx.fillRect(en.x-22,en.y-32,44,7); ctx.fillStyle=en.hp>50?'#0f0':'#f00'; ctx.fillRect(en.x-22,en.y-32,en.hp*0.44,7);
  });

  // Player + Pet
  if(player.invis<=0 || Math.floor(Date.now()/120)%2==0){
    ctx.save(); ctx.translate(player.x,player.y); ctx.rotate(player.angle);
    if(player.shield>0){ctx.strokeStyle='rgba(0,200,255,0.85)'; ctx.lineWidth=5; ctx.beginPath(); ctx.arc(0,0,42,0,Math.PI*2); ctx.stroke();}
    ctx.fillStyle='rgba(0,0,0,0.45)'; ctx.beginPath(); ctx.ellipse(0,10,22,14,0,0,Math.PI*2); ctx.fill();
    let chCol=chars.find(c=>c.id==selChar).color; ctx.fillStyle=chCol; ctx.fillRect(-18,-13,36,26);
    ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(12,0,10,0,Math.PI*2); ctx.fill();
    ctx.fillStyle='#222'; ctx.beginPath(); ctx.arc(12,0,11,Math.PI,Math.PI*2); ctx.fill();
    let gCol=player.gun.color||'#222'; ctx.fillStyle=gCol; ctx.fillRect(20,-5,38,10); ctx.fillStyle='#111'; ctx.fillRect(52,-3,18,6);
    ctx.restore();
    // Pet follow
    if(selPet!='none'){
      let petX=player.x-Math.cos(player.angle)*38, petY=player.y-Math.sin(player.angle)*38;
      ctx.font='20px Arial'; ctx.fillText(pets.find(p=>p.id==selPet).icon, petX-10, petY-10);
    }
  }

  bullets.forEach(b=>{ctx.strokeStyle=b.owner=='player'?'rgba(255,255,0,0.75)':'rgba(255,90,90,0.75)'; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(b.x-b.vx*2.5,b.y-b.vy*2.5); ctx.lineTo(b.x,b.y); ctx.stroke(); ctx.fillStyle=b.owner=='player'?'#ffff00':'#ff9999'; ctx.beginPath(); ctx.arc(b.x,b.y,4,0,Math.PI*2); ctx.fill();});
  grenades.forEach(g=>{ctx.fillStyle='#88ff00'; ctx.beginPath(); ctx.arc(g.x,g.y,7,0,Math.PI*2); ctx.fill();});
  particles.forEach(p=>{
    p.x+=p.vx; p.y+=p.vy; p.life--; p.vx*=0.92; p.vy*=0.92;
    ctx.globalAlpha=p.life/30; if(p.text){ctx.font='18px Arial'; ctx.fillStyle='#fff'; ctx.fillText(p.text,p.x,p.y);} else {ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.s,0,Math.PI*2); ctx.fill();}
    ctx.globalAlpha=1;
  });
  particles=particles.filter(p=>p.life>0);
  ctx.restore();

  // Minimap
  mctx.clearRect(0,0,108,108); mctx.fillStyle='#132213'; mctx.fillRect(0,0,108,108);
  mctx.strokeStyle='#0ff'; mctx.lineWidth=1; mctx.beginPath(); mctx.arc(52,52,safeR*0.043,0,Math.PI*2); mctx.stroke();
  buildings.forEach(b=>{mctx.fillStyle='#555'; mctx.fillRect(b.x*0.043,b.y*0.043,b.w*0.043,b.h*0.043)});
  loots.forEach(l=>{if(!l.taken){mctx.fillStyle=l.isAirdrop?'#f00':'#ff0'; mctx.fillRect(l.x*0.043,l.y*0.043,2,2)}});
  glooWalls.forEach(w=>{mctx.fillStyle='#0ef'; mctx.fillRect(w.x*0.043,w.y*0.043,w.w*0.043,w.h*0.043)});
  vehicles.forEach(v=>{mctx.fillStyle='#ffaa00'; mctx.fillRect(v.x*0.043,v.y*0.043,4,3)});
  mctx.fillStyle='#f00'; enemies.forEach(en=>{if(en.tagged>0){mctx.fillStyle='#f0f'} mctx.fillRect(en.x*0.043,en.y*0.043,3,3); mctx.fillStyle='#f00';});
  mctx.fillStyle='#0f8'; mctx.beginPath(); mctx.arc(player.x*0.043,player.y*0.043,4,0,Math.PI*2); mctx.fill();
  if(plane.active){mctx.fillStyle='#fff'; mctx.fillRect(plane.x*0.043,plane.y*0.043,6,2);}

  // UI updates
  document.getElementById('alive').innerText=enemies.length+1;
  document.getElementById('gunName').innerText=player.gun.name;
  document.getElementById('ammo').innerText=player.gun==guns.fist?'∞':player.ammo+' / '+player.reserve;
  document.getElementById('hpFill').style.width=(player.hp/player.maxHp*100)+'%';
  document.getElementById('vestTxt').innerText=player.vestLevel;
  document.getElementById('helmTxt').innerText=player.helmLevel;
  document.getElementById('lootTxt').innerHTML=near.slice(0,5).join('<br>')||'No loot';
  document.getElementById('invTxt').innerHTML=`GLOO ${glooCount} | 💣 ${grenadeCount}<br>Kills ${kills} | Score ${rankScore}`;
  let ranks=['BRONZE I','BRONZE II','SILVER I','SILVER II','GOLD I','GOLD IV','PLATINUM','DIAMOND','HEROIC','GRANDMASTER'];
  document.getElementById('rank').innerText=ranks[Math.min(9,Math.floor(rankScore/250))];

  if(player.invis>0) player.invis--;
  if(enemies.length==0 && game){addFeed('🏆 BOOYAH! YOU ARE HEROIC!'); game=false; setTimeout(()=>{alert('BOOYAH! HEROIC RANK! Kills: '+kills+' | Score: '+rankScore); location.reload()},800);}

  requestAnimationFrame(loop);
}
loop();
</script>
</body>
</html>
""", height=850)
