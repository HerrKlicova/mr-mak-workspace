# Plano v0 del puente del Palancia (Álvaro, 7-nov). Plantilla del desmonte adaptada a un puente BAJO sobre rambla ancha.
# Coordenadas del MUNDO (mundo persistente, D-N96): la zona va de X 240 a 496 y de Z 0 a 128, justo al este de Sagunto (0-256).
import numpy as np, random
from PIL import Image, ImageDraw, ImageFont
S=4; X0,X1,Z0,Z1=234,500,-6,134
W=(X1-X0)*S; H=(Z1-Z0)*S; SEC=300; LEG=200
im=Image.new("RGB",(W,H+SEC+LEG),"#1c1812"); d=ImageDraw.Draw(im)
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
random.seed(5)
R(X0,Z0,X1,Z1,fill="#b4a080")                       # faldón oeste (Sagunto)
R(345,Z0,X1,Z1,fill="#a89470")                      # huerta este
for i in range(120):                                # naranjos al este, en hileras
    x=random.choice(range(362,496,6)); z=random.choice(range(80,128,6))
    d.ellipse([P(x-1.5,z+1.5),P(x+1.5,z-1.5)],fill="#605c48")
for i in range(60):
    x=random.choice(range(362,496,6)); z=random.choice(range(4,16,6))
    d.ellipse([P(x-1.5,z+1.5),P(x+1.5,z-1.5)],fill="#605c48")
# cauce: X 265,6-340,8, lecho a -4,5 m, escollera en las orillas
R(265.6,Z0,340.8,Z1,fill="#94948c")
R(262,Z0,265.6,Z1,fill="#6c7874"); R(340.8,Z0,344.4,Z1,fill="#6c7874")
for i in range(140):
    x=random.uniform(268,338); z=random.uniform(Z0,Z1)
    d.ellipse([P(x-0.8,z+0.8),P(x+0.8,z-0.8)],fill=random.choice(["#88885c","#70784c"]))
for (x,z) in ((268,100),(267,40),(338,110),(337,30)):  # cañas solo al pie de las orillas
    R(x-2,z-6,x+2,z+6,fill="#88885c")
R(268,Z0,272,Z1,fill="#c8b490"); T(273,124,"senda del cauce\n(a pie)","#1c1812",FS,"#c8b490")
# vía y viaducto ferroviario (Teo v3): estribos 262-265,6 y 340,8-344,4; pilas cada 15 m
L([(X0,64.5),(X1,64.5)],"#94948c",3); R(X0,62,X1,67,fill="#48403c"); L([(X0,64.5),(X1,64.5)],"#94948c",3)
R(262,60,344.4,69,outline="#1c1812",w=2)
for x in (280.6,295.6,310.6,325.6): R(x-1,60.5,x+1,68.5,fill="#6c7874",outline="#1c1812")
T(282,74,"viaducto ferroviario (Teo v3): 5 vanos de 15 m, carril a +4,5 m sobre el lecho","#1c1812",FS,"#94948c")
for x in range(262,346,20): d.ellipse([P(x-0.8,70.3),P(x+0.8,68.7)],fill="#283440")   # postes de catenaria
# carretera vieja y su tablero paralelo (Z 23), atasco y camión cruzado
R(X0,18,X1,28,fill="#94948c"); R(262,17,344.4,29,outline="#1c1812",w=2)
for x in range(X0,X1,6): L([(x,23),(x+3,23)],"#b8b8b8",1)
rot(258,23,8,2.5,78,"#94948c"); T(240,34,"camión cruzado (X 258)","#1c1812",FS,"#b8b8b8")
ax=262
while ax<344:
    ax+=random.uniform(4.5,6.5); z=random.choice([20,21,25,26]); rot(ax,z,4.2,1.8,random.uniform(-20,20),random.choice(["#283440","#605c48","#94948c"]))
T(300,13,"tablero de la carretera: atasco cerrado","#1c1812",FS,"#94948c")
# tren, tapón y salida atrás
R(240,62.4,340,66.6,fill="#50541c",outline="#1c1812"); R(332,62,340,67,fill="#70784c",outline="#1c1812")
T(242,61,"tren (≈100 m, SIN VERIFICAR) hacia Castellón","#d4d0cc",FS)
R(345,61,355,68,fill="#1c200c"); T(346,58,"tapón","#d4d0cc",FS,"#1c1812")
R(240,60,262,69,outline="#f0dc9c",w=2); T(240,78,"salida atrás: hacia Sagunto","#1c1812",FS,"#f0dc9c")
# puesto en el estribo oeste
R(244,78,258.3,94.4,outline="#70784c",w=4); T(244,99,"puesto del estribo\nv2 HESCO, yaw 90","#1c1812",FS,"#70784c")
def flecha(x0,z0,x1,z1,lab):
    L([(x0,z0),(x1,z1)],"#982420",4); a=np.arctan2(z1-z0,x1-x0)
    for s in (2.6,-2.6): L([(x1,z1),(x1-4*np.cos(a+s*0.3),z1-4*np.sin(a+s*0.3))],"#982420",4)
    T(x0+1,z0+3,lab,"#d4d0cc",FB,"#1c1812")
flecha(498,64.5,358,64.5,"P1"); flecha(300,132,300,82,"P2"); flecha(318,-4,318,46,"P2")
flecha(330,23,330,52,"P3")
R(240,0,496,128,outline="#d4d0cc",w=2)
T(236,133,"Puente del Palancia v0 · planta 1 px = 0,25 m · zona X 240–496, Z 0–128 (mundo)","#d4d0cc",FS,"#1c1812")
# sección por X 303 (vertical ×2)
oy=H+40; ox=40; k=4
def Q(z,y): return (ox+z*k, oy+(10-y)*k*2)
d.text((10,H+8),"Sección por X 303 (vertical ×2): el cauce seco a −4,5 m; los dos tableros, a ras del faldón",fill="#d4d0cc",font=F)
d.polygon([Q(0,-4.5),Q(128,-4.5),Q(128,-7),Q(0,-7)],fill="#94948c",outline="#1c1812")
for z0,z1,lab in ((17,29,"carretera (atasco)"),(60,69,"vía (tren)")):
    d.rectangle([Q(z0,0.6),Q(z1,0)],fill="#6c7874",outline="#1c1812"); p=Q(z0,3.5); d.text(p,lab,fill="#d4d0cc",font=FS)
d.rectangle([Q(62.3,4.6),Q(66.7,0.6)],fill="#50541c",outline="#1c1812")
for z in (20,26,63,66): d.rectangle([Q(z-0.7,0),Q(z+0.7,-4.5)],fill="#6c7874")
d.text(Q(80,-1.5),"la horda cruza el lecho, se amontona en las pilas y sube por su pila (§5.7)",fill="#d4d0cc",font=FS)
for z in (0,23,64.5,128): p=Q(z,-7); d.text((p[0]-6,p[1]+4),f"Z {z}",fill="#d4d0cc",font=FS)
ly=H+SEC+10
items=[("#94948c","cauce seco: grava, hierba rala, matorral"),("#6c7874","escollera de las orillas, pilas"),("#88885c","cañas, solo al pie de las orillas"),("#c8b490","senda del cauce (solo a pie)"),("#70784c","puesto del estribo oeste (v2 HESCO)"),("#605c48","naranjos (este)"),("#f0dc9c","salida atrás hacia Sagunto"),("#982420","entradas de la horda P1–P3 (solo en el plano)")]
for i,(c,t) in enumerate(items):
    x=20+(i%2)*W//2; y=ly+(i//2)*26
    d.rectangle([x,y,x+18,y+16],fill=c,outline="#d4d0cc"); d.text((x+26,y),t,fill="#d4d0cc",font=F)
d.text((20,ly+110),"Álvaro (Niveles) · Palancia v0, solo papel · las medidas son cuentas · fotos F2 de Paula",fill="#d4d0cc",font=FB)
im.save("/mnt/project-files/docs/niveles/palancia_plano_v0.png"); print(im.size)
