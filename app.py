import streamlit as st, streamlit.components.v1 as comps
st.set_page_config(page_title="FF NARUTO MATURE - SIDEWAYS LOCKED", layout="wide")
comps.html("""
<!DOCTYPE html><html><head>
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no,maximum-scale=1">
<meta name="apple-mobile-web-app-capable" content="yes">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;user-select:none;-webkit-user-select:none;font-family:'Segoe UI',Arial}
html,body{width:100%;height:100%;background:#000;overflow:hidden;overscroll-behavior:none}
#gameWrap{position:fixed;inset:0;width:100vw;height:100vh;background:linear-gradient(180deg,#6fb7ff 0%,#a8d8ff 22%,#7aae6a 22%,#4a6b3a 100%);overflow:hidden}
/* AUTO SIDEWAYS - Even in portrait, force landscape */
@media (orientation:portrait){
 #gameWrap{
  width:100vh; height:100vw;
  transform:rotate(90deg) translate(0,-100vw);
  transform-origin:top left;
 }
}
#bgMount{position:absolute;top:0;right:0;width:60%;height:34%;background:linear-gradient(145deg,#8b7355,#4a3f2f);clip-path:polygon(5% 25%,25% 0,85% 0,100% 18%,100% 100%,0 100%);opacity:0.85;z-index:1}
#bgMount:after{content:'火影';position:absolute;top:22%;left:18%;font-size:28px;color:rgba(0,0,0,0.15);font-weight:900}
#topBar{position:absolute;top:0;left:0;right:0;height:46px;background:linear-gradient(90deg,rgba(0,0,0,0.9),rgba(20,20,20,0.85));display:flex;justify-content:space-between;align-items:center;padding:0 12px;color:#fff;z-index:50;border-bottom:2.5px solid #ffcc00;backdrop-filter:blur(4px)}
#lobby{position:absolute;inset:0;top:46px;bottom:58px;display:flex;z-index:10}
#leftCol{width:122px;padding:10px;display:flex;flex-direction:column;gap:10px}
.mBtn{background:linear-gradient(90deg,rgba(0,0,0,0.7),rgba(30,30,30,0.6));border-left:5px solid #ffcc00;color:#fff;padding:10px 12px;border-radius:10px;font-size:11px;font-weight:800;letter-spacing:0.5px;box-shadow:0 3px 8px rgba(0,0,0,0.4)}
.mBtn.g{border-left-color:#00ff88} .mBtn.r{border-left-color:#ff4444}
#centerCol{flex:1;display:flex;align-items:center;justify-content:center;position:relative}
.human{width:170px;height:380px;position:relative;filter:drop-shadow(0 14px 20px rgba(0,0,0,0.6))}
.head{position:absolute;top:0;left:50%;transform:translateX(-50%);width:58px;height:58px;background:radial-gradient(circle at 32% 30%,#ffdebb 0%,#d4a07a 55%,#a0704a 100%);border-radius:50%;border:3.2px solid #000;z-index:6}
.cap{position:absolute;top:-12px;left:-10px;width:78px;height:26px;background:linear-gradient(180deg,#222,#000);border-radius:16px 16px 6px 6px;border:2.5px solid #000;z-index:7}
.capBrim{position:absolute;top:16px;left:2px;width:74px;height:12px;background:#111;border-radius:0 0 12px 12px;border:2px solid #000}
.eyes{position:absolute;top:24px;left:50%;transform:translateX(-50%);width:36px;display:flex;justify-content:space-between}
.eye{width:8px;height:8px;background:#000;border-radius:50%;box-shadow:0 0 0 1px #fff}
.jacket{position:absolute;top:54px;left:50%;transform:translateX(-50%);width:102px;height:104px;background:linear-gradient(180deg,#7faed6 0%,#5a7ea6 50%,#3d5a7a 100%);border-radius:16px;border:3.2px solid #000;z-index:4;box-shadow:inset 0 4px 10px rgba(0,0,0,0.25)}
.jacketLine{position:absolute;left:50%;top:0;bottom:0;width:3px;background:#000;transform:translateX(-50%)}
.pocket{position:absolute;top:22px;width:16px;height:14px;background:rgba(0,0,0,0.15);border:1px solid #000;border-radius:3px}
.pocket.l{left:10px} .pocket.r{right:10px}
.hood{position:absolute;top:58px;left:50%;transform:translateX(-50%);width:48px;height:62px;background:linear-gradient(180deg,#e02020,#7a0000);border-radius:10px;border:2.5px solid #000;z-index:5}
.pants{position:absolute;top:154px;left:50%;transform:translateX(-50%);width:90px;height:128px;background:linear-gradient(180deg,#9c8468,#6b5a42 70%,#4a3f2f);border:3.2px solid #000;border-radius:0 0 14px 14px;z-index:3}
.shoe{position:absolute;bottom:0;width:56px;height:22px;background:linear-gradient(180deg,#ffffff,#c8c8c8);border:3.2px solid #000;border-radius:9px;box-shadow:inset 0 -4px 6px rgba(0,0,0,0.2)}
.shoe.l{left:0} .shoe.r{right:0}
.shoe:after{content:'';position:absolute;top:6px;left:6px;right:6px;height:2px;background:#000;opacity:0.2}
.pet{position:absolute;bottom:10px;right:-42px;width:42px;height:36px;background:linear-gradient(180deg,#f5c070,#c98a3a);border-radius:55% 55% 45% 45%;border:3px solid #000;z-index:10;animation:petBob 1.4s ease-in-out infinite}
.pet:before{content:'▲';position:absolute;top:-10px;left:4px;font-size:10px;color:#000}
.pet:after{content:'';position:absolute;top:8px;left:8px;width:6px;height:6px;background:#000;border-radius:50%}
@keyframes petBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
.narutoRing{position:absolute;bottom:24%;left:50%;transform:translateX(-50%);width:150px;height:150px;border:5px solid rgba(255,0,0,0.18);border-radius:50%;z-index:1}
#rightCol{width:130px;padding:10px}
.tBox{background:linear-gradient(180deg,rgba(0,0,0,0.82),rgba(10,10,10,0.7));border:1.8px solid #ffcc00;border-radius:12px;padding:9px;margin-bottom:10px;color:#fff;font-size:9.5px;line-height:1.4;box-shadow:0 4px 10px rgba(0,0,0,0.5)}
#bottomBar{position:absolute;bottom:0;left:0;right:0;height:58px;background:linear-gradient(180deg,rgba(10,10,10,0.9),rgba(0,0,0,0.95));display:flex;gap:7px;padding:8px 10px;align-items:center;border-top:2.5px solid #ffcc00;z-index:60}
.bSm{background:linear-gradient(180deg,rgba(255,255,255,0.15),rgba(255,255,255,0.06));border:1.5px solid rgba(255,255,255,0.18);color:#fff;border-radius:12px;padding:9px 6px;font-size:10px;flex:1;text-align:center;font-weight:700;backdrop-filter:blur(4px)}
.bStart{background:linear-gradient(90deg,#ffcc00 0%,#ff9900 100%);color:#000;border:none;border-radius:14px;padding:13px 18px;font-weight:900;font-size:17px;flex:1.9;box-shadow:0 0 22px rgba(255,204,0,0.6),inset 0 -3px 0 rgba(0,0,0,0.3);letter-spacing:0.5px}
.bDownload{background:linear-gradient(90deg,#00e5ff,#0066ff);color:#fff;border:none;border-radius:12px;padding:8px 10px;font-size:9px;font-weight:800;margin-left:4px}
#gameUI{position:absolute;inset:0;background:#0a1a0e;z-index:100;display:none}
canvas{width:100%;height:100%;display:block}
.joy{position:absolute;bottom:24px;width:136px;height:136px;background:rgba(255,255,255,0.10);border-radius:50%;border:3.5px solid rgba(255,255,255,0.45);z-index:200;backdrop-filter:blur(2px)}
#jM{left:20px} #jA{right:116px;width:104px;height:104px;bottom:28px}
.stick{position:absolute;width:62px;height:62px;background:radial-gradient(circle at 30% 30%,#fff,#888);border-radius:50%;left:37px;top:37px;box-shadow:0 6px 14px #000, inset 0 2px 4px #fff;border:2.5px solid #000}
#sA{width:46px;height:46px;left:29px;top:29px;background:radial-gradient(circle at 30% 30%,#ff7a7a,#900);border:2.5px solid #fff}
.btn{position:absolute;z-index:200;border:3px solid #fff;color:#fff;font-weight:900;border-radius:20px;box-shadow:0 6px 16px rgba(0,0,0,0.6)}
#fire{bottom:122px;right:18px;width:96px;height:96px;background:radial-gradient(circle at 32% 28%,#ff8a8a,#cc0000);border-radius:50%;font-size:18px;letter-spacing:1px}
#gloo{bottom:18px;right:18px;width:88px;height:50px;background:linear-gradient(180deg,#00eaff,#0044ff);border-radius:14px;font-size:11px}
</style></head><body>
<div id="gameWrap">
<div id="bgMount"></div>
<div id="topBar"><div style="display:flex;align-items:center;gap:10px"><span style="background:#111;padding:5px 10px;border-radius:8px;font-size:11px;border:1px solid #333">LV.58 ACE</span><span style="font-size:12px">💎 5,621 🪙 3</span></div><div style="display:flex;align-items:center;gap:8px"><span style="color:#ffcc00;font-weight:900;font-size:13px;letter-spacing:0.5px">FREE FIRE x NARUTO</span><button class="bDownload" id="dlBtn">⬇ DOWNLOAD</button></div></div>
<div id="lobby">
<div id="leftCol"><div class="mBtn">STORE</div><div class="mBtn g">LUCK ROYALE</div><div class="mBtn r">EVENTS</div><div class="mBtn" style="border-left-color:#8a5cff;font-size:9px">★ NIGHTMARE<br>TEMPLE</div></div>
<div id="centerCol"><div class="narutoRing"></div><div class="human"><div class="head"><div class="cap"></div><div class="capBrim"></div><div class="eyes"><div class="eye"></div><div class="eye"></div></div></div><div class="jacket"><div class="jacketLine"></div><div class="pocket l"></div><div class="pocket r"></div><div class="hood"></div></div><div class="pants"><div class="shoe l"></div><div class="shoe r"></div></div><div class="pet"></div></div></div>
<div id="rightCol"><div class="tBox"><b style="color:#ffcc00">TEAMCODE</b><br>Scorpion<br><span style="opacity:0.7">+ Invite Team</span></div><div class="tBox" style="border-color:#00ff88"><b>CS RANKED</b><br><span style="color:#00ff88">● ONLINE</span><br><span style="opacity:0.6">Bermuda</span></div><div class="tBox" style="border-color:#555;font-size:8px">⚙️ VAULT<br>🔫 WEAPON<br>🎭 PRESET<br>🧪 LAB</div></div>
</div>
<div id="bottomBar"><div class="bSm">VAULT</div><div class="bSm">WEAPON</div><div class="bSm">PRESET</div><div class="bSm">LAB</div><button class="bStart" id="startBtn">▶ START</button></div>
<div id="gameUI">
<canvas id="cv"></canvas>
<div class="joy" id="jM"><div class="stick" id="sM"></div></div>
<div class="joy" id="jA"><div class="stick" id="sA"></div></div>
<button class="btn" id="fire">FIRE</button>
<button class="btn" id="gloo">GLOO WALL</button>
<div style="position:absolute;top:12px;left:12px;background:rgba(0,0,0,0.78);padding:8px 14px;border-radius:12px;color:#fff;z-index:201;border:1px solid rgba(255,255,255,0.15)"><div style="font-size:8px;opacity:0.7;letter-spacing:1px">ALIVE</div><div id="alive" style="font-size:20px;font-weight:900">9</div></div>
<div style="position:absolute;top:12px;right:12px;background:rgba(0,0,0,0.78);padding:6px 12px;border-radius:20px;color:#fff;z-index:201;font-size:10px;border:1px solid #ffcc00">NARUTO MAP • Konoha</div>
</div>
</div>
<script>
// DOWNLOADABLE - Save game offline
document.getElementById('dlBtn').onclick=()=>{
 let html=document.documentElement.outerHTML;
 let blob=new Blob([html],{type:'text/html'});
 let a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='NeonStrike-Naruto-Mature-Sideways.html'; a.click();
 alert('Downloaded! Open file anytime offline. Add to Home Screen for app-like feel.');
};
const cv=document.getElementById('cv'), ctx=cv.getContext('2d');
function rs(){cv.width=innerWidth; cv.height=innerHeight} rs(); addEventListener('resize',rs);
let game=false, player={x:1000,y:1000,ang:0,hp:100}, bullets=[], enemies=[], builds=[], cam={x:1000,y:1000}, jM={x:0,y:0}, jA={x:0,y:0};
function reset(){player.x=1000; player.y=1000; bullets=[]; enemies=[]; builds=[]; for(let i=0;i<20;i++) builds.push({x:Math.random()*2600,y:Math.random()*2600,w:110+Math.random()*40,h:110+Math.random()*40}); for(let i=0;i<9;i++) enemies.push({x:Math.random()*2600,y:Math.random()*2600,hp:100,ang:Math.random()*6});}
function getTouch(e, jRect){
 let t=e.touches[0];
 let isPortrait=innerHeight>innerWidth;
 let cx, cy;
 if(isPortrait){
  // Correct for auto-rotate 90deg
  cx=t.clientY;
  cy=innerWidth - t.clientX;
  let rW=100*(innerHeight/100); // approximated
 } else {
  cx=t.clientX; cy=t.clientY;
 }
 return {x:cx, y:cy};
}
function setJoy(jId,sId,o){
 const j=document.getElementById(jId), s=document.getElementById(sId);
 let a=false;
 const mv=e=>{
  if(!a) return; e.preventDefault();
  let r=j.getBoundingClientRect();
  let pt=getTouch(e,r);
  let cx=r.left+r.width/2, cy=r.top+r.height/2;
  let dx=pt.x-cx, dy=pt.y-cy;
  // If portrait rotated, swap axes for joystick logic
  if(innerHeight>innerWidth){ let tmp=dx; dx=dy; dy=-tmp; }
  let d=Math.hypot(dx,dy), m=r.width/2-12;
  if(d>m){dx=dx/d*m; dy=dy/d*m;}
  s.style.left=(r.width/2-s.offsetWidth/2+dx)+'px';
  s.style.top=(r.height/2-s.offsetHeight/2+dy)+'px';
  o.x=dx/m; o.y=dy/m;
 };
 const end=()=>{a=false; s.style.left='37px'; s.style.top='37px'; if(sId=='sA'){s.style.left='29px'; s.style.top='29px'} o.x=0; o.y=0;};
 j.addEventListener('touchstart',e=>{a=true; mv(e)},{passive:false});
 j.addEventListener('touchmove',mv,{passive:false});
 j.addEventListener('touchend',end); j.addEventListener('touchcancel',end);
}
setJoy('jM','sM',jM); setJoy('jA','sA',jA);
function startGame(){
 document.getElementById('lobby').style.display='none';
 document.getElementById('bottomBar').style.display='none';
 document.getElementById('leftCol').style.display='none';
 document.getElementById('rightCol').style.display='none';
 document.getElementById('topBar').style.display='none';
 document.getElementById('gameUI').style.display='block';
 reset(); game=true;
}
document.getElementById('startBtn').addEventListener('click',startGame);
document.getElementById('startBtn').addEventListener('touchstart',e=>{e.preventDefault(); startGame();},{passive:false});
function shoot(){if(!game) return; bullets.push({x:player.x+Math.cos(player.ang)*44,y:player.y+Math.sin(player.ang)*44,vx:Math.cos(player.ang)*26,vy:Math.sin(player.ang)*26,lf:95});}
document.getElementById('fire').addEventListener('touchstart',e=>{e.preventDefault(); shoot();},{passive:false});
document.getElementById('fire').addEventListener('click',shoot);
document.getElementById('gloo').addEventListener('touchstart',e=>{e.preventDefault(); let gx=player.x+Math.cos(player.ang)*110, gy=player.y+Math.sin(player.ang)*110; builds.push({x:gx-44,y:gy-44,w:88,h:88,tmp:true}); setTimeout(()=>{builds=builds.filter(b=>!b.tmp)},6000);},{passive:false});
function drawHuman(x,y,ang,col,scale=1){ctx.save(); ctx.translate(x,y); ctx.rotate(ang); ctx.scale(scale,scale);
 ctx.fillStyle='rgba(0,0,0,0.35)'; ctx.beginPath(); ctx.ellipse(0,28,22,9,0,0,6.28); ctx.fill();
 ctx.fillStyle=col; ctx.beginPath(); ctx.roundRect(-16,-18,32,36,9); ctx.fill(); ctx.strokeStyle='#000'; ctx.lineWidth=2.8; ctx.stroke();
 ctx.fillStyle='#ffdbac'; ctx.beginPath(); ctx.arc(15,0,12,0,6.28); ctx.fill(); ctx.strokeStyle='#000'; ctx.lineWidth=1.8; ctx.stroke();
 ctx.fillStyle='#111'; ctx.fillRect(22,-6,34,9); ctx.fillRect(52,-4,16,6);
 ctx.fillStyle='#222'; ctx.fillRect(-16,18,14,24); ctx.fillRect(2,18,14,24);
 ctx.fillStyle='#fff'; ctx.fillRect(-18,40,16,9); ctx.fillRect(0,40,16,9); ctx.strokeStyle='#000'; ctx.lineWidth=1.5; ctx.strokeRect(-18,40,16,9); ctx.strokeRect(0,40,16,9);
 ctx.restore();}
function loop(){
 if(!game){requestAnimationFrame(loop); return}
 let sp=6.5, nx=player.x+jM.x*sp, ny=player.y+jM.y*sp; player.x=nx; player.y=ny;
 if(Math.hypot(jA.x,jA.y)>0.22) player.ang=Math.atan2(jA.y,jA.x);
 cam.x+=(player.x-cam.x)*0.14; cam.y+=(player.y-cam.y)*0.14;
 bullets.forEach(b=>{b.x+=b.vx; b.y+=b.vy; b.lf--; enemies.forEach((en,i)=>{if(Math.hypot(b.x-en.x,b.y-en.y)<32){en.hp-=38; b.lf=0; if(en.hp<=0) enemies.splice(i,1);}});});
 bullets=bullets.filter(b=>b.lf>0);
 enemies.forEach(en=>{let d=Math.hypot(en.x-player.x,en.y-player.y); if(d<620){en.ang=Math.atan2(player.y-en.y,player.x-en.x); en.x+=Math.cos(en.ang)*1.7; en.y+=Math.sin(en.ang)*1.7;}});
 ctx.save(); ctx.translate(innerWidth/2-cam.x, innerHeight/2-cam.y);
 ctx.fillStyle='#1b2f1b'; ctx.fillRect(cam.x-1400,cam.y-1000,2800,2000);
 ctx.fillStyle='rgba(255,255,255,0.04)'; for(let i=0;i<2800;i+=80){ctx.fillRect(cam.x-1400+i,cam.y-1000,1,2000)} for(let j=0;j<2000;j+=80){ctx.fillRect(cam.x-1400,cam.y-1000+j,2800,1)}
 builds.forEach(b=>{ctx.fillStyle=b.tmp?'rgba(0,220,255,0.92)':'#3c3c3c'; ctx.fillRect(b.x,b.y,b.w,b.h); ctx.strokeStyle=b.tmp?'#fff':'#000'; ctx.lineWidth=b.tmp?2.5:2; ctx.strokeRect(b.x,b.y,b.w,b.h); if(b.tmp){ctx.fillStyle='rgba(255,255,255,0.5)'; ctx.fillRect(b.x+8,b.y+8,b.w-16,6)}});
 enemies.forEach(en=>{drawHuman(en.x,en.y,en.ang,'#e03a3a',1.05)});
 drawHuman(player.x,player.y,player.ang,'#6b8ec0',1.15);
 bullets.forEach(b=>{ctx.fillStyle='#ffef00'; ctx.shadowColor='#ffef00'; ctx.shadowBlur=10; ctx.beginPath(); ctx.arc(b.x,b.y,5.5,0,6.28); ctx.fill(); ctx.shadowBlur=0;});
 ctx.restore();
 document.getElementById('alive').innerText=enemies.length+1;
 if(enemies.length==0){alert('BOOYAH! NARUTO VICTORY!'); location.reload();}
 requestAnimationFrame(loop);
} loop();
</script></body></html>
""", height=900)
