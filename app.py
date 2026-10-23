import streamlit as st, streamlit.components.v1 as comps
st.set_page_config(page_title="NEON STRIKE x NARUTO LOBBY", layout="wide")
comps.html("""
<!DOCTYPE html><html><head>
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;font-family:Arial}
body{background:#000;overflow:hidden}
#wrap{position:fixed;inset:0;background:linear-gradient(180deg,#87ceeb 0%,#a8d8ea 40%,#6fb76f 100%)}
#konohaBg{position:absolute;inset:0;background:radial-gradient(ellipse at 70% 10%,rgba(255,255,255,0.8),transparent 30%), linear-gradient(180deg,#6ec6ff 0%,#c2e8ff 35%,#7ab86f 35%,#5a8a4a 100%);z-index:1}
.hokageRock{position:absolute;top:8%;right:5%;width:55%;height:28%;background:linear-gradient(145deg,#8b7355,#5d4e37);border-radius:20px 20px 4px 4px;clip-path:polygon(0 30%,20% 0,80% 0,100% 20%,100% 100%,0 100%);opacity:0.9}
.village{position:absolute;bottom:18%;left:0;right:0;height:22%;background:linear-gradient(90deg,#d4a574 0%,#8b6f47 20%,#c19a6b 40%,#8b6f47 60%,#d4a574 100%);opacity:0.7}
#lobby{position:absolute;inset:0;z-index:10;display:flex;flex-direction:column}
.topBar{height:48px;background:rgba(0,0,0,0.75);display:flex;justify-content:space-between;align-items:center;padding:0 10px;color:#fff;border-bottom:2px solid #ffcc00}
.charArea{flex:1;display:flex;align-items:center;justify-content:center;position:relative}
.human{width:150px;height:340px;position:relative;filter:drop-shadow(0 10px 20px rgba(0,0,0,0.5))}
.head{position:absolute;top:0;left:50%;transform:translateX(-50%);width:46px;height:46px;background:#e8b896;border-radius:50%;border:2px solid #000;z-index:4}
.cap{position:absolute;top:-8px;left:-6px;width:58px;height:18px;background:#1a1a1a;border-radius:10px 10px 2px 2px;border:2px solid #000}
.jacket{position:absolute;top:44px;left:50%;transform:translateX(-50%);width:86px;height:88px;background:linear-gradient(180deg,#6b8cae,#4a6a8a);border-radius:12px;border:2.5px solid #000;z-index:3}
.hoodie{position:absolute;top:48px;left:50%;transform:translateX(-50%);width:38px;height:52px;background:#cc2222;border-radius:6px;z-index:4;border:1px solid #000}
.pants{position:absolute;top:128px;left:50%;transform:translateX(-50%);width:76px;height:108px;background:linear-gradient(180deg,#8b7355,#6b5a42);border:2.5px solid #000;border-radius:0 0 10px 10px;z-index:2}
.shoe{position:absolute;bottom:0;width:48px;height:18px;background:#fff;border:2.5px solid #000;border-radius:6px}
.shoe.l{left:2px} .shoe.r{right:2px}
.pet{position:absolute;bottom:8px;right:-28px;width:32px;height:28px;background:#e8a95a;border-radius:50% 50% 30% 30%;border:2px solid #000;z-index:5}
.pet:after{content:'🐶';position:absolute;top:-6px;left:2px;font-size:20px}
.narutoSymbol{position:absolute;bottom:22%;left:50%;transform:translateX(-50%);width:120px;height:120px;border:4px solid rgba(255,0,0,0.3);border-radius:50%;z-index:2}
.bottomBar{height:52px;background:rgba(0,0,0,0.85);display:flex;gap:6px;padding:6px;align-items:center;border-top:2px solid #ffcc00}
.bBtn{background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.2);color:#fff;border-radius:8px;padding:6px 10px;font-size:9px;flex:1;text-align:center}
.startBtn{background:linear-gradient(90deg,#ffcc00,#ff8800);color:#000;border:none;border-radius:10px;padding:10px 18px;font-weight:900;font-size:14px;flex:1.6;box-shadow:0 0 15px #ffcc00}
#sidePanel{position:absolute;top:58px;right:8px;width:82px;z-index:12}
.teamCard{background:rgba(0,0,0,0.75);border:1px solid #ffcc00;border-radius:8px;padding:6px;margin-bottom:6px;color:#fff;font-size:8px}
#gameUI{position:absolute;inset:0;background:#0a1a0a;z-index:20;display:none}
canvas{width:100%;height:100%;display:block}
.joy{position:absolute;bottom:18px;width:122px;height:122px;background:rgba(255,255,255,0.12);border-radius:50%;border:3px solid rgba(255,255,255,0.4);z-index:30}
#jM{left:14px} #jA{right:98px;width:94px;height:94px;bottom:22px}
.stick{position:absolute;width:56px;height:56px;background:#fff;border-radius:50%;left:33px;top:33px}
#sA{width:42px;height:42px;left:26px;top:26px;background:#ff4444}
.btn{position:absolute;z-index:30;border:2.5px solid #fff;color:#fff;font-weight:900}
#fire{bottom:110px;right:12px;width:88px;height:88px;background:radial-gradient(#ff5555,#900);border-radius:50%;font-size:15px}
#gloo{bottom:12px;right:12px;width:78px;height:44px;background:linear-gradient(#00eaff,#0055ff);border-radius:10px;font-size:10px}
</style></head><body>
<div id="wrap">
<div id="konohaBg"><div class="hokageRock"></div><div class="village"></div></div>
<div id="lobby">
<div class="topBar"><div style="display:flex;gap:8px;align-items:center"><div style="background:#111;padding:4px 8px;border-radius:6px;font-size:9px">LV.58 ACE</div><div style="font-size:10px">💎 5,621 💰 3</div></div><div style="font-size:12px;color:#ffcc00">FREE FIRE x NARUTO</div></div>
<div style="position:absolute;top:54px;left:8px;z-index:11;display:flex;flex-direction:column;gap:6px"><div style="background:rgba(0,0,0,0.7);color:#fff;padding:6px 10px;border-radius:8px;font-size:10px;border-left:3px solid #ffcc00">STORE</div><div style="background:rgba(0,0,0,0.7);color:#fff;padding:6px 10px;border-radius:8px;font-size:10px;border-left:3px solid #00ff88">LUCK ROYALE</div><div style="background:rgba(0,0,0,0.7);color:#fff;padding:6px 10px;border-radius:8px;font-size:10px;border-left:3px solid #ff4444">EVENTS</div></div>
<div id="sidePanel"><div class="teamCard"><b>TEAMCODE</b><br>Scorpion<br>+ Invite</div><div class="teamCard">CS RANKED<br><span style="color:#0f0">● ONLINE</span></div></div>
<div class="charArea">
<div class="narutoSymbol"></div>
<div class="human"><div class="head"><div class="cap"></div></div><div class="jacket"><div class="hoodie"></div></div><div class="pants"><div class="shoe l"></div><div class="shoe r"></div></div><div class="pet"></div></div>
</div>
<div class="bottomBar"><div class="bBtn">VAULT</div><div class="bBtn">WEAPON</div><div class="bBtn">PRESET</div><div class="bBtn">LAB</div><button class="startBtn" id="startBtn">▶ START</button></div>
</div>
<div id="gameUI">
<canvas id="cv"></canvas>
<div class="joy" id="jM"><div class="stick" id="sM"></div></div>
<div class="joy" id="jA"><div class="stick" id="sA"></div></div>
<button class="btn" id="fire">FIRE</button>
<button class="btn" id="gloo">GLOO</button>
<div style="position:absolute;top:8px;left:8px;background:rgba(0,0,0,0.7);padding:6px 10px;border-radius:8px;color:#fff;z-index:31"><div style="font-size:8px">ALIVE</div><div id="alive" style="font-size:16px">10</div></div>
</div>
</div>
<script>
const cv=document.getElementById('cv'), ctx=cv.getContext('2d');
function rs(){cv.width=innerWidth; cv.height=innerHeight} rs(); addEventListener('resize',rs);
let game=false, player={x:1000,y:1000,ang:0,hp:100}, bullets=[], enemies=[], builds=[], cam={x:1000,y:1000}, jM={x:0,y:0}, jA={x:0,y:0};
function reset(){player.x=1000; player.y=1000; player.hp=100; bullets=[]; enemies=[]; builds=[]; for(let i=0;i<18;i++) builds.push({x:Math.random()*2400,y:Math.random()*2400,w:100,h:100}); for(let i=0;i<9;i++) enemies.push({x:Math.random()*2400,y:Math.random()*2400,hp:100,ang:0});}
function setJoy(jId,sId,o){const j=document.getElementById(jId), s=document.getElementById(sId); let a=false; const mv=e=>{if(!a) return; let r=j.getBoundingClientRect(), t=e.touches?e.touches[0]:e, cx=r.left+r.width/2, cy=r.top+r.height/2, dx=t.clientX-cx, dy=t.clientY-cy, d=Math.hypot(dx,dy), m=r.width/2-12; if(d>m){dx=dx/d*m; dy=dy/d*m;} s.style.left=(r.width/2-s.offsetWidth/2+dx)+'px'; s.style.top=(r.height/2-s.offsetHeight/2+dy)+'px'; o.x=dx/m; o.y=dy/m;}; const end=()=>{a=false; s.style.left='33px'; s.style.top='33px'; if(sId=='sA'){s.style.left='26px'; s.style.top='26px'} o.x=0; o.y=0}; j.addEventListener('touchstart',e=>{a=true; mv(e)}); j.addEventListener('touchmove',mv); j.addEventListener('touchend',end); }
setJoy('jM','sM',jM); setJoy('jA','sA',jA);
document.getElementById('startBtn').onclick=()=>{document.getElementById('lobby').style.display='none'; document.getElementById('konohaBg').style.display='none'; document.getElementById('gameUI').style.display='block'; reset(); game=true;};
function shoot(){if(!game) return; bullets.push({x:player.x+Math.cos(player.ang)*36,y:player.y+Math.sin(player.ang)*36,vx:Math.cos(player.ang)*22,vy:Math.sin(player.ang)*22,lf:80});}
document.getElementById('fire').addEventListener('touchstart',e=>{e.preventDefault(); shoot()});
document.getElementById('gloo').onclick=()=>{let gx=player.x+Math.cos(player.ang)*90, gy=player.y+Math.sin(player.ang)*90; builds.push({x:gx-36,y:gy-36,w:72,h:72}); setTimeout(()=>{builds.pop()},4000);};
function drawHuman(x,y,ang,col){ctx.save(); ctx.translate(x,y); ctx.rotate(ang); ctx.fillStyle=col; ctx.beginPath(); ctx.roundRect(-14,-16,28,30,8); ctx.fill(); ctx.fillStyle='#e8b896'; ctx.beginPath(); ctx.arc(14,0,10,0,6.28); ctx.fill(); ctx.fillStyle='#222'; ctx.fillRect(18,-5,28,7); ctx.restore();}
function loop(){
if(!game){requestAnimationFrame(loop); return}
let sp=5.5, nx=player.x+jM.x*sp, ny=player.y+jM.y*sp; player.x=nx; player.y=ny;
if(Math.hypot(jA.x,jA.y)>0.25) player.ang=Math.atan2(jA.y,jA.x);
cam.x+=(player.x-cam.x)*0.12; cam.y+=(player.y-cam.y)*0.12;
bullets.forEach(b=>{b.x+=b.vx; b.y+=b.vy; b.lf--; enemies.forEach((en,i)=>{if(Math.hypot(b.x-en.x,b.y-en.y)<26){en.hp-=35; b.lf=0; if(en.hp<=0) enemies.splice(i,1);}});});
bullets=bullets.filter(b=>b.lf>0);
enemies.forEach(en=>{let d=Math.hypot(en.x-player.x,en.y-player.y); if(d<500){en.ang=Math.atan2(player.y-en.y,player.x-en.x); en.x+=Math.cos(en.ang)*1.4; en.y+=Math.sin(en.ang)*1.4;}});
ctx.save(); ctx.translate(innerWidth/2-cam.x, innerHeight/2-cam.y);
ctx.fillStyle='#1a2e1a'; ctx.fillRect(cam.x-1200,cam.y-900,2400,1800);
builds.forEach(b=>{ctx.fillStyle='#3a3a3a'; ctx.fillRect(b.x,b.y,b.w,b.h); ctx.strokeStyle='#000'; ctx.strokeRect(b.x,b.y,b.w,b.h);});
enemies.forEach(en=>{drawHuman(en.x,en.y,en.ang,'#ff4444')});
drawHuman(player.x,player.y,player.ang,'#6b8cae');
bullets.forEach(b=>{ctx.fillStyle='#ff0'; ctx.beginPath(); ctx.arc(b.x,b.y,4,0,6.28); ctx.fill();});
ctx.restore();
document.getElementById('alive').innerText=enemies.length+1;
if(enemies.length==0){alert('BOOYAH! NARUTO COLLAB WIN!'); location.reload();}
requestAnimationFrame(loop);
} loop();
</script></body></html>
""", height=800)
