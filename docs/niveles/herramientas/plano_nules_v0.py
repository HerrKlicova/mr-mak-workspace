# Plano v0 de Nules (Álvaro, 7-nov): emplazamiento fundable (D-N18, D-N49). Coordenadas locales de la zona 256 × 128 m, vía en Z 64,5.
import numpy as np, random
from PIL import Image, ImageDraw, ImageFont
S=4; X0,X1,Z0,Z1=-6,262,-6,134
W=(X1-X0)*S; H=(Z1-Z0)*S; LEG=230
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
random.seed(11)
R(X0,Z0,X1,Z1,fill="#a89470")
# naranjal en hileras (víveres), con calles de riego
def naranjal(x0,z0,x1,z1):
    for x in np.arange(x0,x1,5):
        for z in np.arange(z0,z1,5):
            if random.random()<0.9: d.ellipse([P(x-1.6,z+1.6),P(x+1.6,z-1.6)],fill="#605c48")
naranjal(4,26,70,52); naranjal(186,26,252,52); naranjal(4,2,250,11)
# pueblo al norte (fotos N1_6: bloques y casas pegados a la estación) con el kit de Sagunto
for i,x in enumerate(range(4,250,14)):
    if abs(x-80)<10: continue
    if i%3==0: R(x,106,x+12,124,fill="#b4a080",outline="#1c1812")
    else: R(x,108,x+12,118,fill="#a86c50",outline="#1c1812")
R(X0,90,X1,100,fill="#94948c"); T(150,94,"calle de la Estación (borde del pueblo)","#1c1812",FS,"#94948c")
for x in range(10,250,30): d.ellipse([P(x-1.5,87.5),P(x+1.5,84.5)],fill="#605c48")
# canal de hormigón con muros, caseta de compuertas, cañar y palmeras (fotos N3)
R(X0,14,X1,21,fill="#506878"); L([(X0,13.6),(X1,13.6)],"#94948c",2); L([(X0,21.4),(X1,21.4)],"#94948c",2)
R(196,12,204,23,fill="#94948c",outline="#1c1812"); T(205,24,"caseta de compuertas","#1c1812",FS,"#c4ac84")
T(150,17,"canal de riego de hormigón (7 m)","#d4d0cc",FS,"#1c1812")
# vía, andén, edificio de viajeros abandonado
R(X0,62,X1,67,fill="#48403c"); L([(X0,64.5),(X1,64.5)],"#94948c",3)
for x in range(0,257,40): d.ellipse([P(x-0.8,70.3),P(x+0.8,68.7)],fill="#283440")
R(100,67.5,160,71.5,fill="#94948c",outline="#1c1812"); T(101,73,"andén 60 m","#1c1812",FS,"#94948c")
R(121,74,139,82,fill="#d4d0cc",outline="#1c1812"); R(115,72,135,74,fill="#88885c"); T(122,81,"Viajeros\n2 plantas","#1c1812",FS)
# cruce de caminos: camino de la Vilavella (N) y avenida de la Estación (S), paso a nivel en X 80
R(76,Z0,84,Z1,fill="#94948c"); T(86,126,"avenida → centro de Nules (N)","#1c1812",FS,"#94948c"); T(86,8,"camino de la huerta (S), puente sobre el canal","#1c1812",FS,"#94948c")
R(75,60,85,69,outline="#d4d0cc",w=2); T(56,56,"paso a nivel\n(sin barreras)","#1c1812",FS,"#d4d0cc")
R(84,28,160,34,fill="#c8b490"); T(100,26,"ramal de la cooperativa","#1c1812",FS,"#c8b490")
# cooperativa citrícola (almacén de naranjas con muelle)
R(140,34,176,52,fill="#a86c50",outline="#1c1812"); R(140,52,176,55,fill="#94948c"); T(142,48,"Cooperativa: almacén\ndel kit, frontón ondulado","#1c1812",FS)
# trazado sugerido de 150 m de HESCO (44 × 31 m) a ≤ 60 m del andén, con dos puertas de vía y una de vehículos
R(108,56,152,87,outline="#70784c",w=6)
L([(108,62),(108,67)],"#7c3c18",7); L([(152,62),(152,67)],"#7c3c18",7); L([(126,56),(134,56)],"#f0dc9c",6)
T(153,90,"trazado sugerido: 150 m de HESCO\n(44 × 31 m), puertas de vía O/E\ny de vehículos al sur","#1c1812",FS,"#70784c")

# tren al fundar
R(96,62.6,166,66.4,fill="#50541c",outline="#1c1812"); T(98,61,"tren de fundación: 30 u y 12 personas","#d4d0cc",FS)
# sitios
def sitio(x,z,n,txt,dx,dz):
    d.ellipse([P(x-3.2,z+3.2),P(x+3.2,z-3.2)],outline="#d4d0cc",width=3); T(x-2.4,z+2.2,n,"#d4d0cc",FB); T(x+dx,z+dz,txt,"#d4d0cc",F,"#1c1812")
sitio(130,78,"N1","N1 Estación (130; 78)",-14,14); sitio(158,44,"N2","N2 Cooperativa (158; 44)",4,-2); sitio(80,64.5,"N3","N3 Paso a nivel (80; 64,5)",-62,-8)
def flecha(x0,z0,x1,z1,lab):
    L([(x0,z0),(x1,z1)],"#982420",4); a=np.arctan2(z1-z0,x1-x0)
    for s in (2.6,-2.6): L([(x1,z1),(x1-4*np.cos(a+s*0.3),z1-4*np.sin(a+s*0.3))],"#982420",4)
    T(x0+1,z0+3,lab,"#d4d0cc",FB,"#1c1812")
flecha(-4,64.5,40,64.5,"Na"); flecha(260,64.5,215,64.5,"Nb"); flecha(40,131,40,102,"Nd"); flecha(230,131,230,102,"Nd"); flecha(140,-4,140,26,"Nc")
R(0,0,256,128,outline="#d4d0cc",w=2)
T(-4,133,"Nules v0 · planta 4 px/m · zona local 256 × 128 m · solo papel","#d4d0cc",FS,"#1c1812")
ly=H+10
items=[("#605c48","naranjal al sur (víveres); casas y bloques del pueblo al norte"),("#506878","canal de hormigón y compuertas: el agua (fotos N3)"),("#94948c","caminos asfaltados y andén"),("#c8b490","ramal de tierra a la cooperativa"),("#70784c","trazado sugerido de HESCO (no se construye solo)"),("#f0dc9c","puerta de vehículos del trazado"),("#7c3c18","puertas de vía del trazado"),("#982420","entradas de la horda Na–Nd (solo en el plano)")]
for i,(c,t) in enumerate(items):
    x=20+(i%2)*W//2; y=ly+(i//2)*26
    d.rectangle([x,y,x+18,y+16],fill=c,outline="#d4d0cc"); d.text((x+26,y),t,fill="#d4d0cc",font=F)
d.text((20,ly+112),"Álvaro (Niveles) · Nules v0.1 · ajustado con las fotos N1–N3 de Paula · disposición SIN VERIFICAR",fill="#d4d0cc",font=FB)
d.text((20,ly+138),"Llano, agua y cruce de caminos: las tres razones del §9b del GDD para que un emplazamiento sea fundable, dibujadas en el sitio.",fill="#d4d0cc",font=F)
im.save("/mnt/project-files/docs/niveles/nules_plano_v0.png"); print(im.size)
