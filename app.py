import streamlit as st, streamlit.components.v1 as comps
st.set_page_config(page_title="FF EXACT", layout="wide")
st.markdown("<style>header{visibility:hidden}#MainMenu{visibility:hidden}footer{visibility:hidden}.block-container{padding:0!important;margin:0!important;max-width:100vw!important}</style>", unsafe_allow_html=True)
comps.html("""
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
<style>
*{margin:0;padding:0;box-sizing:border-box;touch-action:none;user-select:none}
html,body{width:100vw;height:100vh;background:#000;overflow:hidden}
#wrap{position:fixed;inset:0;width:100vw;height:100vh;background:linear-gradient(180deg,#4a4a4a 0%,#7a6a5a 40%,#3a2f2a 100%)}
@media(orientation:portrait){#wrap{width:100vh;height:100vw;transform:rotate(90deg) translate(0,-100vw);transform-origin:top left}}
#bg{position:absolute;inset:0;background:radial-gradient(ellipse at 70% 15%,rgba(120,100,80,0.9),rgba(40,35,30,1) 100%);z-index:1}
#char{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:190px;height:420px;z-index:5}
.head{position:absolute;top:0;left:50%;transform:translateX(-50%);width:62px;height:62px;background:#ffdebb;border-radius:50%;border:3.5px solid #000}
.cap{position:absolute;top:-14px;left:-12px;width:86px;height:28px;background:#111;border-radius:16px 16px 6px 6px;border:3px solid #000}
.jacket{position:absolute;top:58px;left:50%;transform:translateX(-50%);width:108px;height:110px;background:linear-gradient(#6a9ad0,#3a5a80);border-radius:16px;border:3.5px solid #000}
.hood{position:absolute;top:62px;left:50%;transform:translateX(-50%);width:52px;height:66px;background:linear-gradient(#d22,#700);border-radius:10px;border:3px solid #000;z-index:2}
.pants{position:absolute;top:164px;left:50%;transform:translateX(-50%);width:96px;height:136px;background:linear-gradient(#8a7350,#4a3f2f);border:3.5px solid #000;border-radius:0 0 14px 14px}
.shoe{position:absolute;bottom:0;width:58px;height:24px;background:#fff;border:3.5px solid #000;border-radius:10px}.shoe.l{left:2px}.shoe.r{right:2px}
.pet{position:absolute;bottom:12px;right:-48px;width:46px;height:40px;background:#e8a85a;border-radius:50%;border:3px solid #000}
.top{position:absolute;top:0;left:0;right:0;height:46px;background:rgba(0,0,0,0.85);display:flex;justify-content:space-between;align-items:center;padding:0 12px;color:#fff;z-index:20;border-bottom:3px solid #ffcc00}
.bottom{position:absolute;bottom:0;left:0;right:0;height:60px;background:rgba(0,0,0,0.88);display:flex;gap:7px;padding:8px 10px;align-items:center;z-index:20;border-top:3px solid #ffcc00}
.bS{background:rgba(255,255,255,0.14);color:#fff;border-radius:12px;padding:9px 6px;font-size:10px;flex:1;text-align:center;font-weight:700}
.bStart{background:linear-gradient(90deg,#ffcc00,#ff8800);color:#000;border:none;border-radius:14px;padding:13px 18px;font-weight:900;font-size:18px;flex:1.9;box-shadow:0 0 20px #ffcc00}
.left{position:absolute;top:58px;left:10px;z-index:20;display:flex;flex-direction:column;gap:10px;width:126px}
.mB{background:rgba(0,0,0,0.72);border-left:5px solid #ffcc00;color:#fff;padding:11px;border-radius:10px;font-size:11px;font-weight:800}
.right{position:absolute;top:58px;right:10px;z-index:20;width:132px}
.tB{background:rgba(0,0,0,0.8);border:2px solid #ffcc00;border-radius:12px;padding:10px;margin-bottom:10px;color:#fff;font-size:9.5px}
#fs{position:absolute;top:10px;right:10px;z-index:99;background:#ffcc00;color:#000;border:none;padding:8px 14px;border-radius:20px;font-weight:900;font-size:11px}
#game{position:absolute;inset:0;background:#0a1a0e;z-index:100;display:none}
canvas{width:100%;height:100%;display:block}
.joy{position:absolute;bottom:24px;width:130px;height:130px;background:rgba(255,255,255,0.13);border-radius:50%;border:3.5px solid rgba(255,255,255,0.5);z-index:200}
#jM{left:16px}#jA{right:108px;width:100px;height:100px;bottom:28px}
.stick{position:absolute;width:60px;height:60px;background:#fff;border-radius:50%;left:35px;top:35px;border:2.5px solid #000}
#sA{width:44px;height:44px;left:28px;top:28px;background:#f55;border:2px solid #fff}
.btn{position:absolute;z-index:200;border:3px solid #fff;color:#fff;font-weight:900;border-radius:18px}
#fire{bottom:118px;right:16px;width:92px;height:92px;background:radial-gradient(#ff8a8a,#900);border-radius:50%;font-size:16px}
#gloo{bottom:18px;right:16px;width:86px;height:48px;background:linear-gradient(#00eaff,#0044ff);border-radius:12px;font-size:11px}
</style></head><body>
<div id="wrap"><div id="bg"></div>
<button id="fs">⛶ FULLSCREEN</button>
<div id="char"><div class="head"><div class="cap"></div></div><div class="jacket"><div class="hood"></div></div><div class="pants"><div class="shoe l"></div><div class="shoe r"></div></div><div class="pet"></div></div>
<div class="top"><div>LV.58 ★ ACE 💎 5,203</div><div style="color:#ffcc00;font-weight:900">FREE FIRE x NARUTO</div></div>
<div class="left"><div class="mB">🛒 STORE</div><div class="mB" style="border-color:#0f8">🍀 LUCK ROYALE</div><div class="mB" style="border-color:#f44">📅 EVENTS</div></div>
<div class="right"><div class="tB"><b style="color:#ff8800">🦂 TEAMCODE</b><br><span style="font-size:14px;color:#ff8800;font-weight:900">Scorpion</span></div><div class="tB" style="border-color:#0f8"><b>CS RANKED</b><br><span style="color:#0f0">● ONLINE</span></div></div>
<div class="bottom"><div class="bS">📦 VAULT</div><div class="bS">🔫 WEAPON</div><div class="bS">🎯 PRESET</div><div class="bS">🧪 LAB</div><button class="bStart" id="start">▶ START</button></div>
<div id="game"><canvas id="cv"></canvas><div class="joy" id="jM"><div class="stick" id="sM"></div></div><div class="joy" id="jA"><div class="stick" id="sA"></div></div><button class="btn" id="fire">FIRE</button><button class="btn" id="gloo">GLOO</button><div style="position:absolute;top:10px;left:10px;background:rgba(0,0,0,0.8);padding:8px 12px;border-radius:10px;color:#fff;z-index:201">ALIVE <span id="alive">9</span></div></div>
</div>
<script>
document.getElementById('fs').onclick=()=>{document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();document.getElementById('fs').style.display='none';};
const cv=document.getElementById('cv'),ctx=cv.getContext('2d');function rs(){cv.width=innerWidth;cv.height=innerHeight}rs();addEventListener('resize',rs);
let game=false,pl={x:1000,y:1000,ang:0},bul=[],ene=[],bui=[],cam={x:1000,y:1000},jM={x:0,y:0},jA={x:0,y:0};
function reset(){pl.x=1000;pl.y=1000;bul=[];ene=[];bui=[];for(let i=0;i<18;i++)bui.push({x:Math.random()*2600,y:Math.random()*2600,w:110,h:110});for(let i=0;i<9;i++)ene.push({x:Math.random()*2600,y:Math.random()*2600,hp:100,ang:0});}
function setJoy(jId,sId,o){const j=document.getElementById(jId),s=document.getElementById(sId);let a=false;const mv=e=>{if(!a)return;e.preventDefault();let r=j.getBoundingClientRect(),t=e.touches[0],cx=r.left+r.width/2,cy=r.top+r.height/2,dx=t.clientX-cx,dy=t.clientY-cy;if(innerHeight>innerWidth){let tmp=dx;dx=dy;dy=-tmp}let d=Math.hypot(dx,dy),m=r.width/2-12;if(d>m){dx=dx/d*m;dy=dy/d*m}s.style.left=(r.width/2-s.offsetWidth/2+dx)+'px';s.style.top=(r.height/2-s.offsetHeight/2+dy)+'px';o.x=dx/m;o.y=dy/m};const end=()=>{a=false;s.style.left='35px';s.style.top='35px';if(sId=='sA'){s.style.left='28px';s.style.top='28px'}o.x=0;o.y=0};j.addEventListener('touchstart',e=>{a=true;mv(e)},{passive:false});j.addEventListener('touchmove',mv,{passive:false});j.addEventListener('touchend',end);}
setJoy('jM','sM',jM);setJoy('jA','sA',jA);
function startG(){document.querySelector('.left').style.display='none';document.querySelector('.right').style.display='none';document.querySelector('.top').style.display='none';document.querySelector('.bottom').style.display='none';document.getElementById('char').style.display='none';document.getElementById('bg').style.display='none';document.getElementById('game').style.display='block';reset();game=true;}
document.getElementById('start').addEventListener('click',startG);document.getElementById('start').addEventListener('touchstart',e=>{e.preventDefault();startG();},{passive:false});
function shoot(){bul.push({x:pl.x+Math.cos(pl.ang)*44,y:pl.y+Math.sin(pl.ang)*44,vx:Math.cos(pl.ang)*26,vy:Math.sin(pl.ang)*26,lf:95});}
document.getElementById('fire').addEventListener('touchstart',e=>{e.preventDefault();shoot();},{passive:false});document.getElementById('fire').addEventListener('click',shoot);
document.getElementById('gloo').addEventListener('touchstart',e=>{e.preventDefault();let gx=pl.x+Math.cos(pl.ang)*110,gy=pl.y+Math.sin(pl.ang)*110;bui.push({x:gx-44,y:gy-44,w:88,h:88,tmp:true});setTimeout(()=>{bui=bui.filter(b=>!b.tmp)},6000);},{passive:false});
function drawH(x,y,ang,col){ctx.save();ctx.translate(x,y);ctx.rotate(ang);ctx.fillStyle=col;ctx.beginPath();ctx.roundRect(-16,-18,32,36,9);ctx.fill();ctx.strokeStyle='#000';ctx.lineWidth=2.8;ctx.stroke();ctx.fillStyle='#ffdbac';ctx.beginPath();ctx.arc(15,0,12,0,6.28);ctx.fill();ctx.fillStyle='#111';ctx.fillRect(22,-6,34,9);ctx.restore();}
function loop(){if(!game){requestAnimationFrame(loop);return}let sp=6.5,nx=pl.x+jM.x*sp,ny=pl.y+jM.y*sp;pl.x=nx;pl.y=ny;if(Math.hypot(jA.x,jA.y)>0.22)pl.ang=Math.atan2(jA.y,jA.x);cam.x+=(pl.x-cam.x)*0.14;cam.y+=(pl.y-cam.y)*0.14;bul.forEach(b=>{b.x+=b.vx;b.y+=b.vy;b.lf--;ene.forEach((en,i)=>{if(Math.hypot(b.x-en.x,b.y-en.y)<32){en.hp-=38;b.lf=0;if(en.hp<=0)ene.splice(i,1);}});});bul=bul.filter(b=>b.lf>0);ene.forEach(en=>{let d=Math.hypot(en.x-pl.x,en.y-pl.y);if(d<620){en.ang=Math.atan2(pl.y-en.y,pl.x-en.x);en.x+=Math.cos(en.ang)*1.7;en.y+=Math.sin(en.ang)*1.7;}});ctx.save();ctx.translate(innerWidth/2-cam.x,innerHeight/2-cam.y);ctx.fillStyle='#1b2f1b';ctx.fillRect(cam.x-1400,cam.y-1000,2800,2000);bui.forEach(b=>{ctx.fillStyle=b.tmp?'#0ff':'#3c3c3c';ctx.fillRect(b.x,b.y,b.w,b.h);ctx.strokeRect(b.x,b.y,b.w,b.h);});ene.forEach(en=>{drawH(en.x,en.y,en.ang,'#e03a3a');});drawH(pl.x,pl.y,pl.ang,'#6b8ec0');bul.forEach(b=>{ctx.fillStyle='#ff0';ctx.beginPath();ctx.arc(b.x,b.y,5.5,0,6.28);ctx.fill();});ctx.restore();document.getElementById('alive').innerText=ene.length+1;if(ene.length==0){alert('BOOYAH!');location.reload();}requestAnimationFrame(loop);}loop();
</script></body></html>
""", height=2200)
