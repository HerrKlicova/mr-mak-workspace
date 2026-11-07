# Plano v1.2 de Sagunto (Álvaro, 7-nov): nivel 1 de la escala (E1-E6) + frentes de la D-N113 dentro de la zona.
# Fondo: el mapa de zonas v1.2 (zonas.py). Encima, lo construido (build 5188f83) y lo nuevo de la v1.2.
import numpy as np
from PIL import Image, ImageDraw, ImageFont
S=4; X0,X1,Z0,Z1=-30,262,-8,140
zon=np.array(Image.open("/mnt/project-files/docs/niveles/sagunto_zonas_1m.png"))
col={0:"#b4a080",1:"#c8b490",2:"#d8c8a0",3:"#48403c",4:"#6c7874",5:"#a86c50",6:"#c4ac84",7:"#94948c",8:"#605c48",9:"#506878",10:"#88885c",11:"#605c48"}
# recorte: fila 0 del PNG = Z 480, columna 0 = X -250
sub=zon[480-Z1:480-Z0, X0+250:X1+250]
rgb=np.zeros(sub.shape+(3,),np.uint8)
for k,c in col.items(): rgb[sub==k]=[int(c[i:i+2],16) for i in (1,3,5)]
base=Image.fromarray(rgb).resize(((X1-X0)*S,(Z1-Z0)*S),Image.NEAREST)
LEG=250
im=Image.new("RGB",(base.width,base.height+LEG),"#1c1812"); im.paste(base,(0,0)); d=ImageDraw.Draw(im)
Fp="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; Fb="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F=ImageFont.truetype(Fp,13); FS=ImageFont.truetype(Fp,11); FB=ImageFont.truetype(Fb,15); FT=ImageFont.truetype(Fb,18)
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
# zona simulada
R(0,0,256,128,outline="#d4d0cc",w=2); T(1,139,"Zona simulada 0–256 × 0–128 m (marco claro)","#d4d0cc",FS,"#1c1812")
# vías
L([(X0,64.5),(X1,64.5)],"#94948c",3); L([(X0,59.5),(50,59.5),(64,64.5)],"#94948c",2)
for x,y in((35,0),(20,8),(5,-12)): rot(x,59.5,14,3,y,"#605c48")
T(2,56,"tolvas (C2)","#1c1812",FS)
for x in range(-240,262,50): d.ellipse([P(x-0.8,61.7),P(x+0.8,60.1)],fill="#283440")
# línea central de la carretera (E1) y del carril abierto
for x in range(X0,X1,6): L([(x,23),(x+3,23)],"#b8b8b8",1)
# atasco: v1.2 carril norte abierto de X 64 a 200, apretado al este de 200
import random; random.seed(7); ax=70
while ax<250:
    ax+=random.uniform(5,12) if ax<200 else random.uniform(4.5,6.5)
    if ax>=250: break
    if ax<200: z=random.choice([19.5,20.5,21.5,16.2,15.5]); yaw=random.uniform(-25,25)+random.choice([0,0,60])
    else: z=random.choice([20,21,24.5,25.5,26]); yaw=random.uniform(-25,25)
    rot(ax,z,4.2,1.8,yaw,random.choice(["#283440","#605c48","#94948c"]))
rot(258,23,8,2.5,78,"#94948c")
# corte K1 y K2, balizas
def corte(x,z,yaw): rot(x,z,8.8,3,yaw,"#b8b8b8","#1c1812")
corte(201.5,23,90); T(203,31,"K1 corte","#1c1812",FS,"#b8b8b8")
corte(59,86,0); T(65,87,"K2 corte","#1c1812",FS,"#b8b8b8")
bal=[(x,28.8) for x in (70,86,110,126,142,158,174,186)]+[(94.2,36),(103.8,36),(53.2,40),(64.8,40),(53.2,52),(64.8,52)]   # §10.3: 14 balizas
for x,z in bal: d.ellipse([P(x-1,z+1),P(x+1,z-1)],fill="#f0dc9c",outline="#1c1812")
# fuerte
R(70,44,156,85,outline="#88885c",w=8)
L([(70,62),(70,67)],"#7c3c18",8); L([(156,62),(156,67)],"#7c3c18",8)
L([(95,45),(103,45)],"#70784c",9); T(92,41.5,"E4 puerta de vehículos 8 m","#1c1812",FS,"#c4ac84")
R(78,66.7,138,70.7,fill="#605c48"); R(96.5,75,115.5,84,fill="#b4a080",outline="#1c1812"); T(98,82,"Viajeros","#1c1812")
R(127,50,143,58,fill="#94948c",outline="#1c1812"); T(128,57,"Almacén","#1c1812",FS)
R(73.5,63.5,154,65.5,fill="#50541c",outline="#1c1812")
R(72,46,124,60,outline="#f0dc9c",w=2); T(73,59.2,"E5 parque de vehículos","#1c1812",FS)
for x,n,l in((99,"Dragón",8),(88,"VAMTAC",4.9),(80,"VAMTAC",4.9)): rot(x,53,3 if n=="Dragón" else 2.2,l,0,"#50541c")
# almacén de naranjas, caseta, barricada, bus
R(40,30,51,51,fill="#a86c50",outline="#1c1812"); T(29,28,"Almacén de naranjas","#1c1812",FS)
R(49.7,71.3,52.3,73.9,fill="#94948c",outline="#1c1812")
rot(59,92,11,2.6,74,"#94948c"); T(64,95,"autobús y barricada","#1c1812",FS)
for i in range(5): rot(53+i*2.3,88.5+(i%2)*1.6,1.8,1.2,i*31,"#605c48")
# casas (C7 + E3)
for i in range(12):
    if i not in(4,8): R(72+i*6,98,78+i*6,108,fill="#a86c50",outline="#1c1812")
    if i!=3: R(72+i*6,117,78+i*6,127,fill="#a86c50",outline="#1c1812")
T(152,114,"E3 calle del pueblo 9 m","#1c1812",FS)
R(169,75,179,89,fill="#b4a080",outline="#1c1812"); T(180,86,"Bloque","#1c1812",FS)
# helipuerto, NH90, rearme, puesto F3
R(165.2,28.8,195.6,59.2,fill="#6c7874",outline="#1c1812",w=2)
d.ellipse([P(172,52),P(188,36)],outline="#d4d0cc",width=3); T(177.5,47.5,"H","#d4d0cc",FT)
rot(180,44,19.6,3,0,"#50541c"); d.ellipse([P(171.85,52.15),P(188.15,35.85)],outline="#50541c",width=1)
R(159,31,164,41,fill="#847c34",outline="#1c1812"); T(150,30,"rearme","#1c1812",FS,"#c4ac84")
L([(186,38),(222,2)],"#d4d0cc",1); T(206,10,"aproximación\ny salida (SE)","#1c1812",FS,"#d4d0cc")
def puesto(cx,cz,yaw,label):
    rot(cx+(1.05*np.sin(np.radians(yaw))),cz+(1.05*np.cos(np.radians(yaw))),14.3,16.4,yaw,"#70784c")
    a=np.radians(yaw); ex,ez=cx+9.2*np.sin(a),cz+9.2*np.cos(a); d.ellipse([P(ex-1.2,ez+1.2),P(ex+1.2,ez-1.2)],fill="#f0dc9c")
    T(cx-6,cz+2,label,"#d4d0cc",FS)
puesto(43,82,90,"puesto\nF2"); puesto(207,51,270,"puesto\nF3")
# frentes
def frente(x,z,n,txt,dx=3,dz=6):
    d.ellipse([P(x-3.2,z+3.2),P(x+3.2,z-3.2)],outline="#d4d0cc",width=3); T(x-2,z+2.2,n,"#d4d0cc",FB)
    T(x+dx,z+dz,txt,"#d4d0cc",F,"#1c1812")
frente(112,78,"F1","F1 Estación (112; 78)",-10,15)
frente(59,62,"F2","F2 Paso a nivel (59; 62)",-47,-6.5)
frente(180,44,"F3","F3 Helipuerto (180; 44)",-2,25)
T(-29,47,"F4 Tren: sitio móvil (en el dato, X −68 al llegar)","#d4d0cc",FS,"#1c1812")
# rutas del parque a los frentes (D-N96: solo por carreteras habilitadas y accesos)
L([(99,53),(99,23),(59,23),(59,62)],"#f0dc9c",3); T(66,33,"→ F2: 109 m · ≈ 19 s","#1c1812",FS,"#f0dc9c")
L([(99,53),(99,23),(180,23),(180,44)],"#f0dc9c",3); T(130,26.5,"→ F3: 132 m · ≈ 21 s","#1c1812",FS,"#f0dc9c")
# entradas de oleadas
for x0,z0,x1,z1,n in((0,56,8,73,"O1 50 %"),(0,14,8,31,"O2 30 %"),(0,92,8,124,"O3 20 %"),(248,56,256,73,"O4 0 %")):
    R(x0,z0,x1,z1,outline="#e08c30",w=3); T(x0+(-26 if x0==0 else -26),z1+4.5 if x0 else z0+(z1-z0)/2+2,n,"#e08c30",FB,"#1c1812")
T(110,139,"↑ Norte: pueblo y cerro","#d4d0cc",FS,"#1c1812"); T(110,-3,"↓ Sur: huerta y el mar","#d4d0cc",FS,"#1c1812")
T(-29,8,"← Valencia","#d4d0cc",FS,"#1c1812"); T(225,139,"Castellón →","#d4d0cc",FS,"#1c1812")
# leyenda
y=base.height+10
def lg(x,y,c,s,shape="r"):
    if shape=="r": d.rectangle([x,y,x+22,y+14],fill=c,outline="#1c1812")
    elif shape=="o": d.ellipse([x+6,y+2,x+16,y+12],fill=c)
    else: d.rectangle([x,y,x+22,y+14],outline=c,width=3)
    d.text((x+30,y-1),s,fill="#d4d0cc",font=F)
items=[("#6c7874","r","Asfalto: carretera vieja E1 y calle de la Estación E2, de 10 m"),("#c4ac84","r","Tierra pisada: camino de la puerta sur, puestos y rearme"),
       ("#f0dc9c","o","Baliza de ruta de Teo (carretera habilitada)"),("#b8b8b8","r","K1/K2: corte de carretera de Teo (no habilitada)"),
       ("#70784c","r","Puesto de frente v2 (HESCO), 14,3 × 16,4 m; punto crema = entrada"),("#f0dc9c","b","Ruta del parque a un frente, con su ETA (fórmula de la D-N120)"),
       ("#e08c30","b","Entradas de las oleadas (§9.5)"),("#d4d0cc","b","Frente de la D-N113 (sitio del dato)")]
for i,(c,sh,s) in enumerate(items): lg(10+(i%2)*580,y+(i//2)*24,c,s,sh)
d.text((10,y+104),"Sagunto · plano del nivel v1.2 (Álvaro, 7-nov) · 4 px/m, norte arriba · fondo: zonas v1.2 · encima: build 5188f83 + v1.2",fill="#d4d0cc",font=FB)
d.text((10,y+130),"Carril norte de la carretera abierto por el ejército de X 64 a 200 (los coches, al carril sur y a la cuneta); al este de 200, atasco cerrado y corte K1.",fill="#d4d0cc",font=F)
d.text((10,y+150),"Calle de la Estación habilitada hasta Z 86; al norte, autobús, barricada y corte K2. Las ETA son cuentas mías con la fórmula de Nacho, no medidas en el juego.",fill="#d4d0cc",font=F)
d.text((10,y+170),"Helipuerto v4 de Teo (30 × 30 m con balizas) sin anillo de HESCO: lo defiende el puesto F3. Aproximación y salida por el sureste, sobre la huerta.",fill="#d4d0cc",font=F)
d.text((10,y+190),"Colores de la paleta de 32; ningún rojo. El naranja de las oleadas es solo del plano, no del juego.",fill="#d4d0cc",font=F)
im.save("/mnt/project-files/docs/niveles/sagunto_plano_v1_2.png"); print(im.size)
