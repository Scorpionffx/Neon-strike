import streamlit as st, streamlit.components.v1 as comps
st.set_page_config(page_title="NEON STRIKE HUMAN", layout="wide")
comps.html("""
<!DOCTYPE html><html><head>
<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=no">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;user-select:none;font-family:Arial Black}
body{background:#000;overflow:hidden}
#wrap{position:fixed;inset:0;width:100vw;height:100vh}
canvas{width:100%;height:100%;display:block}
@media(orientation:portrait){#wrap{width:100vh;height:100vw;left:50%;top:50%;transform:translate(-50%,-50%) rotate(90deg)}}

/* REAL FF LOBBY */
#lobby{position:absolute;inset:0;background:radial-gradient(ellipse at center,#0f2a3a 0%,#050a14 70%,#000 100%);z-index:10;display:flex;color:#fff}
#lLobby{flex:1.1;padding:14px;display:flex;flex-direction:column;justify-content:space-between;background:linear-gradient(90deg,rgba(0,0,0,0.6),transparent)}
#rLobby{width:34%;background:rgba(0,0,0,0.85);border-left:3px solid #ffcc00;padding:10px;overflow:auto}
.human{width:190px;height:420px;margin:0 auto;position:relative;filter:drop-shadow(0 0 25px rgba(255,204,0,0.4))}
.head{position:absolute;top:0;left:50%;transform:translateX(-50%);width:72px;height:72px;background:#ffdbac;border-radius:50%;border:3px solid #000;z-index:3}
.head::before{content:'';position:absolute;top:-8px;left:-5px;width:84px;height:28px;background:#111;border-radius:20px 20px 5px 5px}
.face{position:absolute;top:22px;left:50%;transform:translateX(-50%);width:50px;height:32px}
.eye{position:absolute;top:5px;width:8px;height:8px;background:#000;border-radius:50%} .eye.l{left:8px} .eye.r{right:8px}
.torso{position:absolute;top:68px;left:50%;transform:translateX(-50%);width:110px;height:130px;background:linear-gradient(180deg,#111 0%,#222 100%);border-radius:18px;border:2px solid #000;z-index:2}
.torso::after{content:'NEON';position:absolute;top:42px;left:50%;transform:translateX(-50%);color:#ffcc00;font-size:10px;letter-spacing:2px}
.arm{position:absolute;top:76px;width:34px;height:90px;background:#ffdbac;border:2px solid #000;border-radius:12px;z-index:1}
.arm.l{left:14px;transform:rotate(-12deg)} .arm.r{right:14px;transform:rotate(12deg)}
.leg{position:absolute;top:192px;width:48px;height:150px;background:#1a1a1a;border:2px solid #000;border-radius:12px;z-index:1}
.leg.l{left:36px} .leg.r{right:36px}
.shoe{position:absolute;bottom:-10px;width:58px;height:22px;background:#000;border-radius:8px;border:2px solid #ffcc00}
.shoe.l{left:-6px} .shoe.r{right:-6px}
.gun{position:absolute;top:110px;right:-32px;width:78px;height:14px;background:linear-gradient(90deg,#ffaa00,#ff4400);border-radius:4px;border:2px solid #000;transform:rotate(-12deg);z-index:4}
.btnStart{padding:16px;background:linear-gradient(90deg,#ffcc00,#ff8800);border:none;border-radius:14px;font-weight:900;color:#000;font-size:18px;width:100%;box-shadow:0 0 25px #ffcc00;cursor:pointer;letter-spacing:1px}
.card{background:rgba(255,255,255,0.08);border:1.5px solid rgba(255,255,255,0.15);border-radius:12px;padding:8px;margin:5px;cursor:pointer;text-align:center}
.card.sel{border-color:#ffcc00;background:rgba(255,204,0,0.2);box-shadow:0 0 12px rgba(255,204,0,0.4)}
#top{position:absolute;top:0;left:0;right:0;height:48px;display:flex;justify-content:space-between;padding:6px 10px;color:#fff;z-index:5;background:linear-gradient(180deg,#000,transparent)}
.joy{position:absolute;bottom:12px;width:124px;height:124px;background:radial-gradient(rgba(255,255,255,0.15),transparent 70%);border-radius:50%;border:2px solid rgba(255,255,255,0.3);z-index:5}
#jM{left:10px} #jA{right:100px;width:92px;height:92px;bottom:16px}
.stick{position:absolute;width:52px;height:52px;background:radial-gradient(#fff,#aaa);border-radius:50%;left:36px;top:36px;box-shadow:0 3px 8px #000}
#sA{width:40px;height:40px;left:26px;top:26px;background:radial-gradient(#ff6666,#900)}
.bF{position:absolute;z-index:5;border:none;font-weight:900;color:#fff}
#fire{bottom:104px;right:8px;width:90px;height:90px;background:radial-gradient(#ff5555,#900);border-radius:50%;border:3px solid #fff;font-size:16px}
#glooB{bottom:8px;right:8px;width:80px;height:46px;background:linear-gradient(#00eaff,#0066ff);border-radius:10px;border:2.5px solid #fff;font-size:10px}
#skRow{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:5}
.sk{width:58px;height:58px;border-radius:14px;border:2.5px solid #fff;background:radial-gradient(#222,#000);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;position:relative}
</style></head><body>
<div id="wrap">
<canvas id="cv"></canvas>
<div id="lobby">
<div id="lLobby">
<div style="display:flex;justify-content:space-between"><div><b style="color:#ffcc00;font-size:20px;letter-spacing:2px">FREE FIRE</b><b style="color:#fff;font-size:20px"> MAX</b><div style="font-size:9px;opacity:0.6">LV.58 ACE • BERMUDA</div></div><div style="text-align:right;font-size:11px">💎 1,200<br><span style="color:#ffcc00">🪙 45,200</span></div></div>
<div class="human" id="hum">
<div class="head"><div class="face"><div class="eye l"></div><div class="eye r"></div></div></div>
<div class="arm l"></div><div class="arm r"></div>
<div class="torso"></div>
<div class="leg l"><div class="shoe l"></div></div>
<div class="leg r"><div class="shoe r"></div></div>
<div class="gun"></div>
</div>
<div style="display:flex;gap:8px"><button class="btnStart" id="playBtn">▶ START</button></div>
<div style="display:flex;gap:6px;font-size:9px"><span style="background:rgba(0,0,0,0.6);padding:6px 10px;border-radius:8px">VAULT</span><span style="background:rgba(0,0,0,0.6);padding:6px 10px;border-radius:8px">WEAPON</span><span style="background:rgba(0,0,0,0.6);padding:6px 10px;border-radius:8px">STORE</span><span style="background:rgba(0,0,0,0.6);padding:6px 10px;border-radius:8px">LUCK ROYALE</span></div>
</div>
<div id="rLobby">
<div style="font-size:10px;color:#ffcc00;margin-bottom:6px">CHARACTER - HUMAN STYLE</div>
<div id="cGrid" style="display:grid;grid-template-columns:1fr 1fr;gap:6px"></div>
<div style="font-size:10px;color:#ffcc00;margin:10px 0 6px">TEAM <span style="font-size:8px;background:#00ff88;color:#000;padding:2px 6px;border-radius:6px">+ Invite</span></div>
<div style="background:rgba(255,255,255,0.06);border-radius:10px;padding:8px;font-size:9px;line-height:12px">NO MORE DOTS!<br>• Human head + cap + face<br>• Jacket + arms + legs + shoes<br>• Real gun model<br>• Lobby like FF Max</div>
</div>
</div>
<div id="top" style="display:none"><div style="display:flex;gap:8px"><div style="background:rgba(0,0,0,0.7);border-radius:10px;padding:4px 10px;text-align:center"><div style="font-size:8px;opacity:0.6">ALIVE</div><div id="alive" style="font-size:16px;font-weight:900">13</div></div><div style="background:rgba(0,0,0,0.7);border-radius:10px;padding:4px 10px"><div id="gName" style="font-size:11px;color:#ffcc00">FIST</div><div id="am" style="font-size:9px">∞</div></div></div><div style="background:rgba(0,0,0,0.7);border-radius:10px;padding:4px 10px"><div style="width:100px;height:12px;background:#222;border-radius:6px;border:1.5px solid #fff;overflow:hidden"><div id="hpF" style="height:100%;background:linear-gradient(90deg,#0f8,#0ff);width:100%"></div></div><div style="font-size:8px;margin-top:2px">VEST <span id="vT">0</span></div></div></div>
<div class="joy" id="jM" style="display:none"><div class="stick" id="sM"></div></div>
<div class="joy" id="jA" style="display:none"><div class="stick" id="sA"></div></div>
<button class="bF" id="fire" style="display:none">FIRE</button>
<button class="bF" id="glooB" style="display:none">GLOO<br><span id="gC">4</span></button>
<div id="skRow" style="display:none"><div class="sk" id="skB"><div style="font-size:20px">⚡</div><div style="font-size:6px">SKILL</div></div><div class="sk" id="medB"><div style="font-size:18px">💊</div><div style="font-size:6px">MED</div></div></div>
</div>
<script>
const cv=document.getElementById('cv'), ctx=cv.getContext('2d');
function rs(){cv.width=cv.clientWidth*2; cv.height=cv.clientHeight*2; ctx.setTransform(2,0,0,2,0,0)} setTimeout(rs,100); addEventListener('resize',rs);
const W=()=>cv.clientWidth, H=()=>cv.clientHeight;
const chars=[{id:'alok',c:'#00ff99',n:'ALOK'},{id:'chrono',c:'#00aaff',n:'CHRONO'},{id:'kelly',c:'#ffaa00',n:'KELLY'},{id:'wukong',c:'#88ff44',n:'WUKONG'},{id:'hayato',c:'#ff4444',n:'HAYATO'},{id:'moco',c:'#ff88cc',n:'MOCO'}];
let sel='alok';
const cg=document.getElementById('cGrid');
chars.forEach(ch=>{let d=document.createElement('div'); d.className='card'+(ch.id==sel?' sel':''); d.innerHTML=`<div style="width:36px;height:36px;background:${ch.c};border-radius:50%;margin:0 auto;border:2px solid #000"></div><b style="font-size:10px;color:${ch.c}">${ch.n}</b>`; d.onclick=()=>{sel=ch.id; document.querySelectorAll('#cGrid .card').forEach(x=>x.classList.remove('sel')); d.classList.add('sel'); document.querySelector('.torso').style.background=ch.c;}; cg.appendChild(d);});
let game=false, player, bullets=[], enemies=[], builds=[], loots=[], gWalls=[], parts=[], cam={x:1000,y:1000}, shake=0, jM={x:0,y:0}, jA={x:0,y:0}, gCount=4;
let guns={fist:{n:'FIST',dmg:20,rate:350,col:'#fff',a:0}, mp40:{n:'MP40',dmg:22,rate:85,col:'#ffaa00',a:40}, m1887:{n:'M1887',dmg:100,rate:580,col:'#ff4444',a:8}, awm:{n:'AWM',dmg:90,rate:1200,col:'#00ffff',a:5}, ak:{n:'AK',dmg:38,rate:140,col:'#ffaa00',a:30}};
function reset(){player={x:1000,y:1000,ang:0,hp:100,mx:100,gun:guns.fist,am:0,spd:1}; bullets=[]; enemies=[]; builds=[]; loots=[]; gWalls=[]; parts=[]; for(let i=0;i<22;i++) builds.push({x:Math.random()*2400,y:Math.random()*2400,w:80+Math.random()*100,h:80+Math.random()*100}); builds.push({x:900,y:900,w:220,h:220}); let ts=['mp40','m1887','awm','ak','med','gloo']; for(let i=0;i<34;i++){let t=ts[Math.floor(Math.random()*ts.length)]; loots.push({x:Math.random()*2400,y:Math.random()*2400,t,tk:false}) } for(let i=0;i<10;i++) enemies.push({x:Math.random()*2400,y:Math.random()*2400,hp:100,ang:0,g:Object.keys(guns)[1+Math.floor(Math.random()*4)],cd:0}); gCount=4; document.getElementById('gC').innerText=gCount;}
function setJoy(jID,sID,o){const j=document.getElementById(jID), s=document.getElementById(sID); let ac=false; const mv=e=>{if(!ac) return; let r=j.getBoundingClientRect(), t=e.touches?e.touches[0]:e, cx=r.left+r.width/2, cy=r.top+r.height/2, dx=t.clientX-cx, dy=t.clientY-cy, d=Math.hypot(dx,dy), m=r.width/2-14; if(d>m){dx=dx/d*m; dy=dy/d*m;} s.style.left=(r.width/2-s.offsetWidth/2+dx)+'px'; s.style.top=(r.height/2-s.offsetHeight/2+dy)+'px'; o.x=dx/m; o.y=dy/m;}; const end=()=>{ac=false; s.style.left='36px'; s.style.top='36px'; if(sID=='sA'){s.style.left='26px'; s.style.top='26px'} o.x=0; o.y=0}; j.addEventListener('touchstart',e=>{ac=true; mv(e)}); j.addEventListener('touchmove',mv); j.addEventListener('touchend',end); }
setJoy('jM','sM',jM); setJoy('jA','sA',jA);
document.getElementById('playBtn').onclick=()=>{document.getElementById('lobby').style.display='none'; document.getElementById('top').style.display='flex'; document.getElementById('jM').style.display='block'; document.getElementById('jA').style.display='block'; document.getElementById('fire').style.display='block'; document.getElementById('glooB').style.display='block'; document.getElementById('skRow').style.display='flex'; reset(); game=true;};
function shoot(){if(!game) return; if(Date.now()-(shoot.l||0) < player.gun.rate) return; shoot.l=Date.now(); if(player.gun!=guns.fist && player.am<=0) return; if(player.gun!=guns.fist) player.am--; let pel=player.gun.n=='M1887'?5:1; for(let p=0;p<pel;p++){let a=player.ang+(Math.random()-0.5)*0.12; bullets.push({x:player.x+Math.cos(player.ang)*38,y:player.y+Math.sin(player.ang)*38,vx:Math.cos(a)*22,vy:Math.sin(a)*22,ow:'p',dmg:player.gun.dmg/(pel>1?pel:1),lf:78});} shake=player.gun.n=='AWM'?14:6;}
document.getElementById('fire').addEventListener('touchstart',e=>{e.preventDefault(); shoot()}); document.getElementById('glooB').onclick=()=>{if(gCount<=0) return; gCount--; document.getElementById('gC').innerText=gCount; let gx=player.x+Math.cos(player.ang)*88, gy=player.y+Math.sin(player.ang)*88; gWalls.push({x:gx-38,y:gy-38,w:76,h:76,hp:500});};
function drawHuman(x,y,ang,col,isPlayer){ctx.save(); ctx.translate(x,y); ctx.rotate(ang);
ctx.fillStyle='rgba(0,0,0,0.4)'; ctx.beginPath(); ctx.ellipse(0,22,18,8,0,0,Math.PI*2); ctx.fill();
ctx.fillStyle=col; ctx.beginPath(); ctx.roundRect(-16,-16,32,28,8); ctx.fill(); ctx.strokeStyle='#000'; ctx.lineWidth=2; ctx.stroke();
ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(14,0,12,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#000'; ctx.lineWidth=1.5; ctx.stroke();
ctx.fillStyle='#000'; ctx.beginPath(); ctx.arc(18,-4,3,0,Math.PI*2); ctx.fill();
ctx.fillStyle='#111'; ctx.beginPath(); ctx.arc(14,0,13,0,Math.PI*2); ctx.fill(); ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(14,0,9,0,Math.PI*2); ctx.fill();
ctx.fillStyle='#111'; ctx.fillRect(20,-14,8,28);
ctx.fillStyle='#222'; ctx.fillRect(-14,12,10,18); ctx.fillRect(4,12,10,18);
ctx.fillStyle='#ffcc00'; ctx.fillRect(-18,28,12,6); ctx.fillRect(2,28,12,6);
if(isPlayer){ctx.fillStyle=player.gun.col; ctx.fillRect(22,-5,36,8); ctx.fillStyle='#000'; ctx.fillRect(54,-3,14,6);}
ctx.restore();}
function loop(){
if(!game){requestAnimationFrame(loop); return}
let sp=6*player.spd, nx=player.x+jM.x*sp, ny=player.y+jM.y*sp; let blk=false; [...builds,...gWalls].forEach(b=>{if(nx>b.x && nx<b.x+b.w && player.y>b.y && player.y<b.y+b.h) blk=true; if(player.x>b.x && player.x<b.x+b.w && ny>b.y && ny<b.y+b.h) blk=true;}); if(!blk){player.x=nx; player.y=ny;}
if(Math.hypot(jA.x,jA.y)>0.28) player.ang=Math.atan2(jA.y,jA.x);
cam.x+=(player.x-cam.x)*0.13; cam.y+=(player.y-cam.y)*0.13;
let safe=1000-Date.now()/1400; safe=Math.max(170,safe); if(Math.hypot(player.x-1200,player.y-1200)>safe) player.hp-=0.45;
loots.forEach(l=>{if(!l.tk && Math.hypot(player.x-l.x,player.y-l.y)<48){if(l.t=='med') player.hp=Math.min(player.mx,player.hp+70); else if(l.t=='gloo'){gCount=Math.min(6,gCount+1); document.getElementById('gC').innerText=gCount;} else {player.gun=guns[l.t]; player.am=player.gun.a;} l.tk=true;}});
bullets.forEach(b=>{b.x+=b.vx; b.y+=b.vy; b.lf--; let hit=false; [...builds,...gWalls].forEach(w=>{if(b.x>w.x && b.x<w.x+w.w && b.y>w.y && b.y<w.y+w.h){hit=true; b.lf=0;}}); if(!hit && b.ow=='p'){enemies.forEach((en,i)=>{if(Math.hypot(b.x-en.x,b.y-en.y)<28){en.hp-=b.dmg; b.lf=0; if(en.hp<=0) enemies.splice(i,1);}});} else if(b.ow!='p' && Math.hypot(b.x-player.x,b.y-player.y)<30){player.hp-=b.dmg; b.lf=0; shake=12; if(player.hp<=0){alert('ELIMINATED'); location.reload();}}});
bullets=bullets.filter(b=>b.lf>0); gWalls=gWalls.filter(w=>w.hp>0);
enemies.forEach(en=>{if(en.cd>0) en.cd--; let d=Math.hypot(en.x-player.x,en.y-player.y); if(d<600){en.ang=Math.atan2(player.y-en.y,player.x-en.x); if(d>140){let tx=en.x+Math.cos(en.ang)*1.6, ty=en.y+Math.sin(en.ang)*1.6; en.x=tx; en.y=ty;} if(en.cd==0 && d<400){let gd=guns[en.g]; bullets.push({x:en.x+Math.cos(en.ang)*32,y:en.y+Math.sin(en.ang)*32,vx:Math.cos(en.ang)*16,vy:Math.sin(en.ang)*16,ow:'e',dmg:gd.dmg*0.5,lf:70}); en.cd=gd.rate/16;}}});
ctx.save(); if(shake>0){ctx.translate((Math.random()-0.5)*shake,(Math.random()-0.5)*shake); shake*=0.88;} ctx.translate(W()/2-cam.x, H()/2-cam.y);
ctx.fillStyle='#0f1e0f'; ctx.fillRect(cam.x-1300,cam.y-1000,2600,2000);
ctx.beginPath(); ctx.arc(1200,1200,safe,0,Math.PI*2); ctx.strokeStyle='#00ffcc'; ctx.lineWidth=3; ctx.setLineDash([26,14]); ctx.stroke(); ctx.setLineDash([]);
builds.forEach(b=>{ctx.fillStyle='rgba(0,0,0,0.4)'; ctx.fillRect(b.x+6,b.y+6,b.w,b.h); ctx.fillStyle='#2a2a2a'; ctx.fillRect(b.x,b.y,b.w,b.h); ctx.strokeStyle='#000'; ctx.lineWidth=2; ctx.strokeRect(b.x,b.y,b.w,b.h); ctx.fillStyle='rgba(120,200,255,0.2)'; for(let wx=b.x+10;wx<b.x+b.w-12;wx+=20) for(let wy=b.y+12;wy<b.y+b.h-12;wy+=18) ctx.fillRect(wx,wy,10,8);});
loots.forEach(l=>{if(l.tk) return; let c=guns[l.t]?guns[l.t].col:l.t=='med'?'#ff44ff':'#00eaff'; ctx.shadowColor=c; ctx.shadowBlur=14; ctx.fillStyle=c; ctx.beginPath(); ctx.roundRect(l.x-10,l.y-10,20,20,5); ctx.fill(); ctx.shadowBlur=0;});
gWalls.forEach(w=>{ctx.fillStyle='rgba(0,230,255,0.9)'; ctx.fillRect(w.x,w.y,w.w,w.h); ctx.strokeStyle='#fff'; ctx.lineWidth=2; ctx.strokeRect(w.x,w.y,w.w,w.h);});
enemies.forEach(en=>{let col=chars.find(c=>c.id==en.g)?.c||'#ff4444'; drawHuman(en.x,en.y,en.ang,col,false); ctx.fillStyle='#000'; ctx.fillRect(en.x-22,en.y-38,44,6); ctx.fillStyle='#0f0'; ctx.fillRect(en.x-22,en.y-38,en.hp*0.44,6);});
drawHuman(player.x,player.y,player.ang, chars.find(c=>c.id==sel)?.c||'#00ff99', true);
bullets.forEach(b=>{ctx.strokeStyle=b.ow=='p'?'#ff0':'#f55'; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(b.x-b.vx*2,b.y-b.vy*2); ctx.lineTo(b.x,b.y); ctx.stroke();});
ctx.restore();
document.getElementById('alive').innerText=enemies.length+1; document.getElementById('gName').innerText=player.gun.n; document.getElementById('am').innerText=player.gun==guns.fist?'∞':player.am; document.getElementById('hpF').style.width=(player.hp/player.mx*100)+'%';
if(enemies.length==0 && game){game=false; setTimeout(()=>{alert('BOOYAH! HUMAN CHAMPION!'); location.reload()},400);}
requestAnimationFrame(loop);
} loop();
</script></body></html>
""", height=820)
