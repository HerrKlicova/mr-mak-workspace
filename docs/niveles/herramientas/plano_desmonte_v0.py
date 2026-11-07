# Plano v0 del desmonte (Álvaro, 7-nov). Zona de emboscada de 256 × 128 m (D-N38), vía en Z 64.
# Arriba: planta. Abajo: sección transversal por X 130. Solo papel: nada de esto está en el código.
import numpy as np
from PIL import Image, ImageDraw, ImageFont
S=4; X0,X1,Z0,Z1=-6,262,-6,134
W=(X1-X0)*S; H=(Z1-Z0)*S; SEC=330; LEG=200
im=Image.new("RGB",(W,H+SEC+LEG),"#1c1812"); d=ImageDraw.Draw(im)
Fp="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; Fb="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F=ImageFont.truetype(Fp,13); FS=ImageFont.truetype(Fp,11); FB=ImageFont.truetype(Fb,15); FT=ImageFont.truetype(Fb,18)
def P(x,z): return ((x-X0)*S,(Z1-z)*S)
def R(x0,z0,x1,z1,fill=None,outline=None,w=1): d.rectangle([P(x0,z1),P(x1,z0)],fill=fill,outline=outline,width=w)
def L(pts,c,w=2): d.line([P(*p) for p in pts],fill=c,width=w)
def T(x,z,s,c="#1c1812",f=None,bg=None):
    f=f or F; p=P(x,z)
    if bg: bb=d.multiline_textbbox(p,s,font=f); d.rectangle([bb[0]-2,bb[1]-1,bb[2]+2,bb[3]+1],fill=bg)
    d.multiline_text(p,s,fill=c,font=f)
# Profundidad de la trinchera a lo largo de X: emboquilles en rampa (X 60-80 y 180-200), 7 m en medio.
def prof(x): return 0 if x<=60 or x>=200 else 7*min(1,(x-60)/20,(200-x)/20)
# Bordes: fondo Z 58-70 (12 m). Sur en roca a 45° (1:1), norte en tierra a 35° (1:1,43).
def bsur(x): return 58-prof(x)*1.0
def bnor(x): return 70+prof(x)*1.428
# Suelo: loma (olivar/almendro abandonado al norte, matorral al sur)
R(X0,Z0,X1,Z1,fill="#b4a080")
R(X0,Z0,X1,50,fill="#a89470")           # matorral sur (coscoja, romero, lentisco)
for zb in (96,110): L([(40,zb),(230,zb)],"#88885c",3)   # bancales de piedra seca (0,8 m)
import random; random.seed(3)
for i in range(140):                     # olivos y almendros abandonados (norte), en hileras rotas
    x=random.uniform(30,250); z=random.choice([90,94,100,104,114,118,124]) + random.uniform(-1,1)
    if abs(x-120)<6: continue
    d.ellipse([P(x-1.4,z+1.4),P(x+1.4,z-1.4)],fill="#605c48")
for i in range(110):                     # matorral (sur)
    x=random.uniform(20,250); z=random.uniform(2,48)
    if abs(x-120)<6 or z>bsur(x)-2: continue
    d.ellipse([P(x-0.9,z+0.9),P(x+0.9,z-0.9)],fill="#70784c")
# Rambla y terraplén al oeste (X 0-60)
d.polygon([P(18,Z0),P(30,Z0),P(34,Z1),P(22,Z1)],fill="#94948c")
T(1,128,"Rambla seca\n(5 m de hondo)","#1c1812",FS,"#94948c")
R(0,60,60,69,fill="#c4ac84"); T(36,76,"terraplén 3 m","#1c1812",FS,"#c4ac84")
R(20,59,36,70,outline="#1c1812",w=2); T(18,56,"pontón 12 m","#1c1812",FS,"#c4ac84")
# Trinchera: taludes y fondo
xs=np.arange(60,201,1)
d.polygon([P(x,bsur(x)) for x in xs]+[P(x,58) for x in xs[::-1]],fill="#6c7874")   # roca sur
d.polygon([P(x,70) for x in xs]+[P(x,bnor(x)) for x in xs[::-1]],fill="#a86c50")    # tierra norte
R(60,58,200,70,fill="#605c48"); R(X0,62,X1,67,fill="#48403c")   # fondo y balasto
L([(X0,64.5),(X1,64.5)],"#94948c",3)
for x in range(60,201,3): L([(x,58.2),(x+1.5,58.2)],"#283440",1); L([(x,69.8),(x+1.5,69.8)],"#283440",1)  # cunetas
# malla de triple torsión en la roca sur (rayado)
for x in range(82,180,4): L([(x,57.5),(x+3,51.5)],"#b8b8b8",1)
# cuneta de coronación (norte) y vallado de ADIF en los dos bordes
L([(x,bnor(x)+1.5) for x in xs],"#283440",2)
L([(x,bnor(x)+3) for x in xs],"#d4d0cc",1); L([(x,bsur(x)-1.5) for x in xs],"#d4d0cc",1)
# Camino de servicio de ADIF (norte) y camino del Mas con su paso superior
R(62,86,200,90,fill="#c8b490"); T(64,93,"camino de servicio (tierra, 4 m)","#1c1812",FS,"#c8b490")
R(117,Z0,123,Z1,fill="#c8b490")
R(116.5,48,123.5,83,fill="#94948c",outline="#1c1812",w=2); T(125,82,"P paso superior\nvano 35 m, pretil 1,1 m","#1c1812",FS,"#94948c")
T(101,128,"camino del Mas","#1c1812",FS,"#c8b490")
# Tren, tapón, derrumbe y puesto de obra
R(70,62.4,170,66.6,fill="#50541c",outline="#1c1812"); T(72,61,"tren (≈100 m, SIN VERIFICAR)","#d4d0cc",FS)
R(162,62,170,67,fill="#70784c",outline="#1c1812")
R(175,61,185,68,fill="#1c200c"); T(171,57,"tapón","#d4d0cc",FS,"#1c1812")
for (x,z,r) in ((178,57,1.6),(182,59,1.2),(186,58,2),(189,60,1.4),(184,61,1)):
    d.ellipse([P(x-r,z+r),P(x+r,z-r)],fill="#94948c",outline="#1c1812")
T(186,53,"D derrumbe (solo con corte)","#1c1812",FS,"#94948c")
R(176,88,191,103,fill=None,outline="#70784c",w=4); T(176,108,"puesto de obra\nv2 HESCO, yaw 180","#1c1812",FS,"#70784c")
# Entradas de la horda
def flecha(x0,z0,x1,z1,lab):
    L([(x0,z0),(x1,z1)],"#982420",4); a=np.arctan2(z1-z0,x1-x0)
    for s in (2.6,-2.6): L([(x1,z1),(x1-4*np.cos(a+s*0.3),z1-4*np.sin(a+s*0.3))],"#982420",4)
    T(x0+1,z0+3,lab,"#d4d0cc",FB,"#1c1812")
flecha(150,131,150,92,"D1"); flecha(140,-3,140,40,"D2"); flecha(258,64.5,206,64.5,"D3")
flecha(120,131,120,100,"D4"); flecha(120,-3,120,30,"D4")
R(0,60,40,69,outline="#f0dc9c",w=2); T(1,74,"40 m libres","#1c1812",FS,"#f0dc9c")
R(0,0,256,128,outline="#d4d0cc",w=2)
T(1,133,"Desmonte v0 · planta 1 px = 0,25 m · zona 256 × 128 m (marco claro)","#d4d0cc",FS,"#1c1812")
# Sección por X 130 (escala vertical ×2)
oy=H+40; ox=40; k=4
def Q(z,y): return (ox+(z-0)*k, oy+ (14-y)*k*2)
d.text((10,H+8),"Sección por X 130 (vertical ×2). Fondo 12 m, 7 m de hondo; sur en roca a 45°, norte en tierra a 35°",fill="#d4d0cc",font=F)
prof7=7
pts=[(0,7),(51,7),(58,0),(70,0),(80,7),(128,7)]
d.polygon([Q(z,y) for z,y in pts]+[Q(128,-3),Q(0,-3)],fill="#b4a080",outline="#1c1812")
d.polygon([Q(51,7),Q(58,0),Q(58,-3),Q(51,-3)],fill="#6c7874")
d.polygon([Q(70,0),Q(80,7),Q(80,-3),Q(70,-3)],fill="#a86c50")
d.rectangle([Q(62,0.5),Q(67,0)],fill="#48403c"); d.rectangle([Q(62.3,4.3),Q(66.7,0.5)],fill="#50541c",outline="#1c1812")
d.rectangle([Q(48,8.2),Q(83,7.3)],fill="#94948c",outline="#1c1812")
for z,y,lab in ((10,7.4,"matorral (D2)"),(46,9.8,"borde roca, valla"),(58,12.6,"cuneta"),(76,12.6,"borde, valla, cuneta de coronación"),(86,9.8,"camino de servicio"),(100,7.4,"bancales, olivar (D1)")):
    p=Q(z,y); d.text((p[0],p[1]-14),lab,fill="#d4d0cc",font=FS)
for z in (0,51,58,70,80,128):
    p=Q(z,-3); d.text((p[0]-6,p[1]+4),f"Z {z}",fill="#d4d0cc",font=FS)
d.text((Q(40,16)[0],Q(40,16)[1]-26),"tablero del paso superior a +8 m (gálibo ≈ 7,5 m sobre carril, SIN VERIFICAR)",fill="#d4d0cc",font=FS)
# Leyenda
ly=H+SEC+10
items=[("#6c7874","talud sur en roca, malla de triple torsión"),("#a86c50","talud norte en tierra, surcos de erosión"),("#605c48","fondo, cunetas y balasto"),("#c8b490","caminos habilitados (camino del Mas, servicio)"),("#94948c","paso superior, pontón, derrumbe"),("#70784c","puesto de obra (v2 HESCO)"),("#d4d0cc","vallado de ADIF a los dos bordes"),("#982420","entradas de la horda D1–D4 (solo en el plano)")]
for i,(c,t) in enumerate(items):
    x=20+(i%2)*W//2; y=ly+(i//2)*26
    d.rectangle([x,y,x+18,y+16],fill=c,outline="#d4d0cc"); d.text((x+26,y),t,fill="#d4d0cc",font=F)
d.text((20,ly+110),"Álvaro (Niveles) · desmonte v0, solo papel · las medidas son cuentas, no medidas · SIN VERIFICAR hasta las fotos de Paula",fill="#d4d0cc",font=FB)
im.save("/mnt/project-files/docs/niveles/desmonte_plano_v0.png"); print(im.size)
