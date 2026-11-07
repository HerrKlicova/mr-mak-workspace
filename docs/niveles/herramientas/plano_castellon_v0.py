# Plano v0 de Castellón (Álvaro, 7-nov): ciudad de la demo con la refinería (combustible 60/día). Coordenadas locales 256 × 128 m.
# Reutiliza el kit de Sagunto con otra combinación; solo dos piezas nuevas (vagón cisterna y depósito flexible).
import numpy as np, random
from PIL import Image, ImageDraw, ImageFont
S=4; X0,X1,Z0,Z1=-6,262,-6,134
W=(X1-X0)*S; H=(Z1-Z0)*S; LEG=250
im=Image.new("RGB",(W,H+LEG),"#1c1812"); d=ImageDraw.Draw(im)
Fp="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; Fb="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F=ImageFont.truetype(Fp,13); FS=ImageFont.truetype(Fp,11); FB=ImageFont.truetype(Fb,15)
def P(x,z): return ((x-X0)*S,(Z1-z)*S)
def R(x0,z0,x1,z1,fill=None,outline=None,w=1): d.rectangle([P(x0,z1),P(x1,z0)],fill=fill,outline=outline,width=w)
def L(pts,c,w=2): d.line([P(*p) for p in pts],fill=c,width=w)
def T(x,z,s,c="#1c1812",f=None,bg=None):
    f=f or F; p=P(x,z)
    if bg: bb=d.multiline_textbbox(p,s,font=f); d.rectangle([bb[0]-2,bb[1]-1,bb[2]+2,bb[3]+1],fill=bg)
    d.multiline_text(p,s,fill=c,font=f)
def rot(cx,cz,w,h,yaw,fill,outline="#1c1812"):
    a=np.radians(yaw); ux=(np.cos(a),-np.sin(a)); uz=(np.sin(a),np.cos(a))
    pts=[(cx+sx*w/2*ux[0]+sz*h/2*uz[0], cz+sx*w/2*ux[1]+sz*h/2*uz[1]) for sx,sz in((-1,-1),(1,-1),(1,1),(-1,1))]
    d.polygon([P(*p) for p in pts],fill=fill,outline=outline)
random.seed(21)
R(X0,Z0,X1,Z1,fill="#b4a080")
# ciudad al norte: bloques de pisos (kit Sagunto, v1-v5 por semilla) y plaza de la estación
R(X0,92,X1,104,fill="#94948c"); T(166,96,"plaza y avenida de la Estación (coches abandonados)","#1c1812",FS,"#94948c")
for i,x in enumerate(range(46,250,17)):
    R(x,108,x+13,124,fill="#b4a080",outline="#1c1812"); T(x+1,122,f"B{1+i%5}","#1c1812",FS)
for x in range(52,250,9):
    if random.random()<0.6: rot(x+random.uniform(-2,2),random.choice([94.5,101.5]),4.2,1.8,random.uniform(-30,30),random.choice(["#283440","#605c48","#94948c"]))
# ronda: paso superior (kit Sagunto) cruzando todo el haz de vías en X 34-42
R(34,Z0,42,Z1,fill="#6c7874"); R(33,36,43,76,outline="#1c1812",w=2); T(-4,84,"ronda sobre las vías\n(paso superior ×2 vanos)","#1c1812",FS,"#6c7874")
# vías: dos generales (Z 57,5 y 66,5), andén central y lateral, haz de mercancías Z 44/48/52 y ramal del Grau
R(X0,55,X1,69,fill="#48403c")
for z in (57.5,66.5): L([(X0,z),(X1,z)],"#94948c",3)
R(70,60,190,64,fill="#94948c",outline="#1c1812"); T(72,58.7,"andén central 120 m","#1c1812",FS,"#94948c")
R(70,69,190,73,fill="#94948c",outline="#1c1812")
for x in range(72,190,24): R(x,69.2,x+20,72.8,fill="#88885c")     # marquesinas (kit, ×5)
R(46,40,230,54,fill="#605c48")
for z in (44,48,52): L([(46,z),(230,z)],"#94948c",2)
L([(46,52),(30,57.5)],"#94948c",2); L([(230,44),(X1,44)],"#94948c",3); T(232,40,"ramal del Grau\n→ refinería","#1c1812",FS,"#94948c")
for x in range(0,257,40): d.ellipse([P(x-0.8,70.3),P(x+0.8,68.7)],fill="#283440"); d.ellipse([P(x-0.8,55.3),P(x+0.8,53.7)],fill="#283440")
# edificio de viajeros: dos edificios del kit en espejo unidos por un cuerpo central
R(98,75,116,84,fill="#b4a080",outline="#1c1812"); R(144,75,162,84,fill="#b4a080",outline="#1c1812"); R(116,75,144,88,fill="#a86c50",outline="#1c1812")
T(117,86,"Viajeros: 2 del kit\nen espejo + cuerpo central","#1c1812",FS)
# cargadero de cisternas y depósito de combustible (nuevo: vagón cisterna y depósito flexible)
for x in range(150,212,12): rot(x+6,44,11,2.8,0,"#283440")
T(92,37.8,"cargadero de cisternas →","#1c1812",FS,"#c4ac84")
R(148,34,214,37,fill="#94948c")
for z in (14,22,30):
    L([(146,z),(214,z)],"#94948c",2)
    for x in range(150,212,12): rot(x+6,z,11,2.8,0,"#283440")
R(144,6,216,33,outline="#88885c",w=4)
# naves de logística al suroeste (almacén de naranjas del kit, otra orientación)
for x in (68,92,116): R(x,6,x+20,22,fill="#a86c50",outline="#1c1812")
R(68,6,88,22,fill="#a86c50",outline="#f0dc9c",w=3); T(69,20,"cuartel","#1c1812",FS)
T(92,2.5,"naves (almacén de naranjas del kit, girado 90°)","#1c1812",FS,"#c4ac84")
R(42,26,144,32,fill="#c8b490")
L([(206,76),(206,88)],"#d4d0cc",3); d.ellipse([P(203,85),P(209,79)],outline="#d4d0cc",width=2); T(186,90.5,"radar (206; 82)","#1c1812",FS,"#d4d0cc")
# recinto: HESCO de 2,1 m alrededor de estación + cargadero; puertas de vía O/E y de vehículos
L([(64,4),(212,4),(222,14),(222,90),(64,90),(64,4)],"#70784c",6)
T(206,0.5,"chaflán (60 m)","#1c1812",FS,"#70784c")
for x in (64,222):
    L([(x,55.5),(x,59.5)],"#7c3c18",7); L([(x,64.5),(x,68.5)],"#7c3c18",7)
L([(222,42),(222,46)],"#7c3c18",7)
L([(64,25),(64,33)],"#f0dc9c",6); T(44,36,"puerta de\nvehículos","#1c1812",FS,"#f0dc9c")
T(66,86.5,"recinto HESCO","#1c1812",FS,"#70784c")
# puesto de frente en la cabeza del ramal y sitios
rot(238,26,14.3,16.4,0,"#70784c"); T(230,16,"puesto v2","#1c1812",FS,"#70784c")
def sitio(x,z,n,txt,dx,dz):
    d.ellipse([P(x-3.2,z+3.2),P(x+3.2,z-3.2)],outline="#d4d0cc",width=3); T(x-2.4,z+2.2,n,"#d4d0cc",FB); T(x+dx,z+dz,txt,"#d4d0cc",F,"#1c1812")
sitio(130,79,"C1","C1 Estación",8,14); sitio(178,22,"C2","C2 Depósito: cisternas en vías muertas con muro de tierra (300 u)",-70,-12); sitio(38,56,"C3","C3 Ronda",-40,-6); sitio(244,44,"C4","C4 Ramal",-60,8)
def flecha(x0,z0,x1,z1,lab):
    L([(x0,z0),(x1,z1)],"#982420",4); a=np.arctan2(z1-z0,x1-x0)
    for s in (2.6,-2.6): L([(x1,z1),(x1-4*np.cos(a+s*0.3),z1-4*np.sin(a+s*0.3))],"#982420",4)
    T(x0+1,z0+3,lab,"#d4d0cc",FB,"#1c1812")
flecha(-4,62,24,62,"Ca"); T(0,38,"◄ parada de asalto\n(−170; 57,5)","#d4d0cc",FS,"#1c1812"); T(214,76,"parada de asalto ►\n(430; 66,5) y (430; 44)","#d4d0cc",FS,"#1c1812"); flecha(260,66,232,66,"Cb"); flecha(150,131,150,107,"Cc"); flecha(90,131,90,107,"Cc"); flecha(260,30,250,30,"Cd")
R(0,0,256,128,outline="#d4d0cc",w=2)
T(-4,133,"Castellón v0 · planta 4 px/m · zona local 256 × 128 m · plano, no build","#d4d0cc",FS,"#1c1812")
T(-4,-2,"← Nules y Sagunto","#d4d0cc",FS,"#1c1812"); T(200,133,"Vinaròs (línea cerrada) →","#d4d0cc",FS,"#1c1812")
ly=H+10
items=[("#b4a080","kit de Sagunto: bloques B1–B5, viajeros ×2, marquesina ×5, paso superior, almacén"),("#283440","nuevo: vagón cisterna (5 variantes)"),("#94948c","vías muertas del depósito (kit)"),("#70784c","recinto HESCO y puesto v2 (kit)"),("#7c3c18","puertas de vía (8 u, D-N59)"),("#f0dc9c","puerta de vehículos (D-N111)"),("#d4d0cc","sitios C1–C4, radar y paradas del tren de asalto (D-N124)"),("#982420","entradas de la horda Ca–Cd (solo en el plano)")]
for i,(c,t) in enumerate(items):
    x=20+(i%2)*W//2; y=ly+(i//2)*26
    d.rectangle([x,y,x+18,y+16],fill=c,outline="#d4d0cc"); d.text((x+26,y),t,fill="#d4d0cc",font=FS)
d.text((20,ly+112),"Álvaro (Niveles) · Castellón v0 · disposición genérica de ciudad, SIN VERIFICAR con la estación real",fill="#d4d0cc",font=FB)
d.text((20,ly+138),"El combustible no se produce aquí: llega por el ramal del Grau desde la refinería y se guarda en el depósito C2.",fill="#d4d0cc",font=F)
d.text((20,ly+158),"C2 es el talón de Aquiles (economía §9): la Colmena va a por él el día 7. Por eso queda dentro del recinto, pero en su borde sur.",fill="#d4d0cc",font=F)
im.save("/mnt/project-files/docs/niveles/castellon_plano_v0.png"); print(im.size)
