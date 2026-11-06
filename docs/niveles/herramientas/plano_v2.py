# Boceto de Sagunto sobre una zona de 512 x 256 m (nivel 2 de §9). Álvaro, 7-nov.
from PIL import Image, ImageDraw, ImageFont
S=2.4; X0,X1,Z0,Z1=-40,552,-20,276
W,H=int((X1-X0)*S),int((Z1-Z0)*S)+80
im=Image.new("RGB",(W,H),"#1c1812"); d=ImageDraw.Draw(im)
F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",13); FB=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",15)
def P(x,z): return ((x-X0)*S,(Z1-z)*S)
def R(x0,z0,x1,z1,fill=None,outline=None,w=1): d.rectangle([P(x0,z1),P(x1,z0)],fill=fill,outline=outline,width=w)
def T(x,z,s,c="#1c1812"): d.text(P(x,z),s,fill=c,font=F)
TY=128
R(X0,Z0,X1,Z1,fill="#6b5c40"); R(0,0,512,256,fill="#b0a060",outline="#d4d0cc",w=2); T(4,254,"Zona 512 × 256 m")
R(0,0,512,50,fill="#a86c50"); T(6,20,"HUERTA (alquerías sueltas)")
for x in range(20,512,48): R(x,0,x+1.5,40,fill="#6c7874")
R(0,39,512,41,fill="#6c7874"); T(300,36,"acequia madre (agua)")
for (ax,az) in ((60,20),(250,12),(420,25)): R(ax-4,az-3.5,ax+4,az+3.5,fill="#d4d0cc",outline="#1c1812"); 
R(X0,50,X1,60,fill="#6c7874"); T(330,58,"Carretera vieja 10 m · atasco →","#d4d0cc")
R(130,0,140,256,fill="#6c7874"); T(141,250,"Calle de la Estación 10 m")
R(X0,TY-2,X1,TY+2,fill="#48403c"); d.line([P(X0,TY),P(X1,TY)],fill="#94948c",width=2)
d.line([P(X0,TY-5),P(120,TY-5)],fill="#605c48",width=2); T(-38,TY-8,"vía 2 muerta","#d4d0cc")
R(146,84,176,188,fill="#d8c8a0"); R(176,84,330,96,fill="#d8c8a0"); R(316,84,330,188,fill="#d8c8a0"); R(146,176,330,188,fill="#d8c8a0"); T(148,92,"glacis 30 m")
R(90,70,101,91,fill="#a86c50",outline="#1c1812"); T(70,96,"almacén de naranjas\n(tejado de pruebas)")
R(176,96,316,176,fill="#c8b490",outline="#88885c",w=6); T(240,99,"FUERTE 140 × 80 m")
d.line([P(176,TY-3),P(176,TY+3)],fill="#7c3c18",width=7); d.line([P(316,TY-3),P(316,TY+3)],fill="#7c3c18",width=7)
d.line([P(236,96),P(244,96)],fill="#7c3c18",width=7); T(226,93,"puerta vehículos 8 m","#1c1812")
R(186,127,250,129,fill="#50541c"); T(186,124,"tren 64 m")
R(184,130,254,134,fill="#605c48"); T(186,137,"andén 70 m")
R(196,160,220,174,fill="#b4a080",outline="#1c1812"); T(197,172,"viajeros")
R(268,102,290,112,fill="#94948c",outline="#1c1812"); T(268,110,"almacén")
R(182,100,262,120,outline="#283440",w=2); T(184,118,"parque de vehículos 80 × 20")
R(262,134,306,172,fill="#d8c8a0",outline="#283440",w=2); T(276,158,"H"); T(264,170,"patio de armas\nhelipuerto 44 × 38")
# pueblo
for i in range(24):
  x=168+i*7
  if 228<=x<264: continue
  R(x,188,x+6,198,fill="#a86c50",outline="#1c1812")
  R(x,207,x+6,217,fill="#a86c50",outline="#1c1812")
  R(x,226,x+6,236,fill="#a86c50",outline="#1c1812")
R(140,198,336,207,fill="#6c7874"); R(140,217,336,226,fill="#6c7874")
R(228,188,264,236,fill="#c8b490",outline="#1c1812"); R(240,236,252,250,fill="#b4a080",outline="#1c1812"); T(230,214,"PLAZA\n36 × 48"); T(253,248,"iglesia")
R(346,140,360,154,fill="#b4a080",outline="#1c1812"); T(362,152,"bloque")
R(380,150,512,256,fill="#a86c50"); T(400,200,"HUERTA ESTE")
for r in range(2):
  for i in range(30): x=170+i*5.5; z=243+r*5; d.ellipse([P(x-1.2,z+1.2),P(x+1.2,z-1.2)],fill="#506030")
A="#e08c30"
def arrow(pts):
  d.line([P(*p) for p in pts],fill=A,width=3); x,z=pts[-1]; d.ellipse([P(x-2,z+2),P(x+2,z-2)],fill=A)
arrow([(-35,TY+4),(60,TY+4),(172,TY+4)]); T(-36,TY+12,"1 · vía (176 m de carrera)",A)
arrow([(-35,55),(100,55),(200,92)]); T(-36,64,"2 · carretera",A)
arrow([(-35,210),(120,212),(168,203),(228,203)]); T(-36,220,"3 · pueblo",A)
d.text((8,H-70),"Sagunto · boceto v2 sobre una zona de 512 × 256 m (nivel 2 de §9) · Álvaro, 7-nov · naranja: recorridos de la horda",fill="#d4d0cc",font=FB)
d.text((8,H-44),"Vía en Z = 128. Remates fuera de la zona: paso superior al oeste (X < 0) y puente del Palancia al este (X > 512). Castillo y sierra detrás del pueblo, fuera de cámara.",fill="#d4d0cc",font=F)
im.save("/mnt/project-files/docs/niveles/sagunto_plano_v2_boceto.png"); print(im.size)
