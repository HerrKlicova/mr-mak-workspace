from PIL import Image, ImageDraw, ImageFont
S=4; X0,X1,Z0,Z1=-40,296,-30,160
W,H=(X1-X0)*S,(Z1-Z0)*S+90
im=Image.new("RGB",(W,H),"#1c1812"); d=ImageDraw.Draw(im)
try:
  F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",14); FB=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",16)
except: F=FB=ImageFont.load_default()
def P(x,z): return ((x-X0)*S, (Z1-z)*S)
def R(x0,z0,x1,z1,fill=None,outline=None,w=1):
  a=P(x0,z1); b=P(x1,z0); d.rectangle([a,b],fill=fill,outline=outline,width=w)
def L(x0,z0,x1,z1,c,w=2): d.line([P(x0,z0),P(x1,z1)],fill=c,width=w)
def T(x,z,s,c="#d4d0cc",f=None): d.text(P(x,z),s,fill=c,font=f or F)
# faldón y zona
R(X0,Z0,X1,Z1,fill="#6b5c40")
R(0,0,256,128,fill="#b0a060",outline="#d4d0cc",w=2)
T(2,127,"Zona simulada 256 × 128 m","#1c1812")
T(-38,-4,"Faldón decorativo (P3), sin simulación","#d4d0cc")
# huerta
for z in range(4,40,6):
  for x in range(70,250,5):
    if not (z>=18 and z<=28): d.ellipse([P(x-1,z+1),P(x+1,z-1)],fill="#506030")
for row in range(2):
  for i in range(14):
    x=80+i*5+(2.5 if row else 0); z=121+row*4; d.ellipse([P(x-1.5,z+1.5),P(x+1.5,z-1.5)],fill="#506030")
# carretera vieja y calle
R(-40,20,296,26,fill="#383430"); T(150,32,"Carretera vieja (P6) · atasco hacia el este →","#1c1812")
R(56,0,62,128,fill="#48403c"); T(63,118,"Calle de la Estación","#1c1812")
for x in range(100,200,9): R(x,21,x+4,24,fill="#283440")
# tejado pruebas = almacén de naranjas
R(40,30,51,51,fill="#a86c50",outline="#1c1812"); T(28,55,"Almacén de naranjas\n(tejado de pruebas)","#1c1812")
# vía actual y propuesta
R(X0,62.5,X1,66.5,fill="#48403c")
L(X0,64.5,X1,64.5,"#94948c",3)

L(-40,59,40,59,"#605c48",2); T(-38,57,"vía 2 muerta","#d4d0cc")
for i in range(4): R(-10+i*11,55,-1+i*11,58,fill="#7c3c18")
T(-30,52,"mercancías descarrilado","#d4d0cc")
# paso superior y puente
R(18,52,26,78,fill="#94948c",outline="#1c1812",w=2); T(4,82,"Paso superior\n(remate oeste)","#1c1812")
R(222,40,250,90,fill="#506878"); R(222,62,250,67,fill="#605c48",outline="#1c1812"); T(214,96,"Puente del Palancia\n(remate este)","#1c1812")
# paso a nivel
R(56,61,62,68,outline="#f0dc9c",w=2)
# fuerte
R(70,44,156,85,outline="#88885c",w=8)
L(70,62,70,67,"#7c3c18",8); L(156,62,156,67,"#7c3c18",8)
T(118,48,"Fuerte 86 × 41 m","#1c1812")
T(157,58,"Puerta este\n(nueva, P4)","#1c1812")
R(78,66.7,138,70.7,fill="#605c48"); R(96.5,75,115.5,84,fill="#b4a080",outline="#1c1812")
T(98,82,"Viajeros","#1c1812")
R(127,50,143,58,fill="#94948c",outline="#1c1812"); T(128,57,"Almacén","#1c1812")
# tren
R(73.5,63.5,154,65.5,fill="#50541c",outline="#1c1812")
# casas
for i in range(5): R(84+i*9,93.5,92+i*9,100.5,fill="#a86c50",outline="#1c1812")
for i in range(4): R(88+i*9,105.5,96+i*9,112.5,fill="#a86c50",outline="#1c1812")
R(76,90,84,97,outline="#605c48",w=2); T(66,89,"solar","#1c1812")
# bloque actual y nuevo
R(167,63,177,77,outline="#c83c30",w=3); T(180,76,"← Bloque hoy:\n   encima de la vía","#c83c30")
R(169,76,179,88,fill="#b4a080",outline="#1c1812",w=2); T(180,86,"Bloque nuevo (P2)","#1c1812")
L(10,66,100,66,"#c83c30",5); T(105,70,"","#c83c30")
d.rectangle([P(160,140),P(250,131)],fill="#1c1812"); T(162,139.5,"Rojo grueso: raíles de hoy (X 10–100)","#c83c30")
# horda
A="#e08c30"
def arrow(pts):
  d.line([P(*p) for p in pts],fill=A,width=4); x,z=pts[-1]; d.ellipse([P(x-1.5,z+1.5),P(x+1.5,z-1.5)],fill=A)
arrow([(-35,61),(20,61),(66,61)]); T(-36,70,"1 · por la vía","#e08c30")
arrow([(-35,23),(40,23),(80,40)]); T(-36,30,"2 · carretera","#e08c30")
arrow([(-35,100),(40,104),(80,92),(100,88)]); T(-36,108,"3 · pueblo","#e08c30")
arrow([(290,61),(236,61),(160,61)]); T(258,70,"más tarde:\npor el puente","#e08c30")
T(80,148,"↑ Norte: pueblo y cerro del castillo","#d4d0cc"); T(80,-22,"↓ Sur: huerta, Puerto de Sagunto y el mar","#d4d0cc")
T(-38,150,"← Valencia","#d4d0cc"); T(250,150,"Castellón / Teruel →","#d4d0cc")
d.text((10,H-80),"Sagunto · plano del nivel v1 (Álvaro, 6-nov) · 1 cuadro = 4 px/m · naranja: recorridos de la horda · rojo: lo que está mal hoy",fill="#d4d0cc",font=FB)
d.text((10,H-50),"Ejes del código: +X este, +Z norte. Vía en Z = 64,5. Orientación de ficción: el oeste va a Valencia y el este a Castellón (la línea real va SSO–NNE).",fill="#d4d0cc",font=F)
im.save("/mnt/project-files/docs/niveles/sagunto_plano_v1.png"); print(im.size)
