import numpy as np, json
from PIL import Image, ImageDraw, ImageFont
X0,X1,Z0,Z1=-250,506,-200,480
W,H=X1-X0,Z1-Z0
xs=np.arange(W)+X0+0.5; zs=Z1-np.arange(H)-0.5
X,Z=np.meshgrid(xs,zs)
ZON={0:"descampado",1:"recinto",2:"glacis",3:"via",4:"calle",5:"huerta",6:"descampado_pisado",7:"pueblo",8:"cauce",9:"acequia",10:"solar",11:"cerro_castillo"}
z=np.zeros((H,W),np.uint8)
def box(x0,x1,z0,z1): return (X>=x0)&(X<x1)&(Z>=z0)&(Z<z1)
# base: huerta sur, norte y este; descampado pisado al oeste (entrada de la horda)
z[Z<20]=5; z[Z>=125]=5; z[box(180,262,70,125)]=5
z[box(-250,40,26,125)]=6
# glacis: 30 m al oeste (X 40-70) y 12 m en N, S y E
z[box(40,70,32,98)]=2; z[box(40,168,86,98)]=2; z[box(40,168,32,44)]=2; z[box(156,168,32,98)]=2
# almacén de naranjas (no es glacis)
z[box(40,51,30,51)]=6
# recinto
z[box(70,156,44,85)]=1
# pueblo, calle del pueblo y solares
z[box(72,150,98,125)]=7
z[box(72,150,108,115)]=4
for gi in (4,8): z[box(75+gi*6-3,75+gi*6+3,98,108)]=10   # 5.ª y 9.ª casa de la hilera de delante
# calles y carreteras
z[box(X0,X1,20,26)]=4                 # carretera vieja
z[box(56,62,Z0,286)]=4                 # calle de la Estación (sube hasta el pie del cerro, x+z = 345)
z[box(-24,-16,-22,150)]=4             # carretera del paso superior (sobre los terraplenes)
# acequias (solo en la huerta sur; madre a Z 10, ramales N-S cada 40 m al sur de Z 10)
z[box(X0,X1,9,11)&(z==5)]=9
for x in range(-230,500,40): z[box(x,x+2,Z0,10)&(z==5)]=9
# vía 1, vía 2 y desvío (franja de 4 m)
z[box(X0,X1,62.5,66.5)]=3
z[box(X0,50,57.5,61.5)]=3
for x in range(50,64):
  zc=59.5+(x+0.5-50)/14*5; z[box(x,x+1,zc-2,zc+2)]=3
# cauce del Palancia (fuera de la zona simulada) — las carreteras y la vía lo cruzan por tableros, el cauce manda abajo
z[box(265.6,340.8,Z0,Z1)]=8
z[((X+Z)>=345)&((X+Z)<=458)&((X-Z)<=-40)&((X-Z)>=-480)&(z!=8)]=11   # cerro del castillo, fuera de cámara (adenda 5 de D-N68)
z[((X+Z)>=480)&((X-Z)<=200)&(z!=8)]=11   # sierra (pinar) detrás
Image.fromarray(z,"L").save("/mnt/project-files/docs/niveles/sagunto_zonas_1m.png")

# máscara sin vegetación (255 = prohibido) y máscara de altura (128 = máx 0,3 m)
m=np.zeros((H,W),np.uint8)
m[z==3]=255                                   # vía (los hierbajos entre traviesas fuera del recinto los decide el shader, no la dispersión)
m[box(X0,X1,61.5,67.5)&box(70,156,0,999)]=255 # vía dentro del recinto, sin excepción
m[box(52,76,54,73)]=255                       # paso a nivel, desvío y puerta oeste
m[box(150,162,58,71)]=255                     # puerta este
m[box(78,138,66,71)]=255                      # andén
m[box(96,116,74,85)]=255                      # edificio de viajeros
m[box(126,144,49,61)]=255                     # almacén y muelle
m[box(40,51,30,51)]=255                       # almacén de naranjas
m[box(169,179,76,88)]=255                     # bloque de pisos
m[box(72,150,98,108)&(z!=10)]=255; m[box(72,150,115,125)]=255   # casas (huellas)
m[box(-30,-10,-22,150)]=255                   # paso superior y terraplenes
m[box(68,72,44,85)|box(154,158,44,85)|box(70,156,42,46)|box(70,156,83,87)]=255  # muros (por si cambian, ver §8.3)
m[z==11]=255
mh=((z==2)&(m==0)).astype(np.uint8)*128
Image.fromarray(np.maximum(m,mh),"L").save("/mnt/project-files/docs/niveles/sagunto_sin_vegetacion_1m.png")

# vista previa en color, ×2
col={0:"#b4a080",1:"#c8b490",2:"#d8c8a0",3:"#48403c",4:"#6c7874",5:"#a86c50",6:"#c4ac84",7:"#94948c",8:"#605c48",9:"#506878",10:"#88885c",11:"#605c48"}
rgb=np.zeros((H,W,3),np.uint8)
for k,c in col.items(): rgb[z==k]=[int(c[i:i+2],16) for i in (1,3,5)]
rgb[m==255]=(rgb[m==255]*0.45).astype(np.uint8)
im=Image.fromarray(rgb).resize((W*2,H*2),Image.NEAREST)
d=ImageDraw.Draw(im)
def P(x,zz): return ((x-X0)*2,(Z1-zz)*2)
d.rectangle([P(0,128),P(256,0)],outline="#d4d0cc",width=3)
F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",18)
leg=Image.new("RGB",(W*2,170),"#1c1812"); dl=ImageDraw.Draw(leg)
for i,(k,n) in enumerate(ZON.items()):
  x=10+(i%6)*250; y=10+(i//6)*40
  dl.rectangle([x,y,x+26,y+26],fill=col[k]); dl.text((x+34,y+3),f"{k} {n}",fill="#d4d0cc",font=F)
dl.text((10,100+0),"Oscurecido: sin vegetación. Marco blanco: zona simulada (0-256 × 0-128 m). 1 px del PNG = 1 m; aquí ×2. Norte arriba.",fill="#d4d0cc",font=F)
dl.text((10,130),"Sagunto · mapa de zonas del suelo v1 (Álvaro, 6-nov) · faldón X −250..506, Z −200..480",fill="#d4d0cc",font=F)
out=Image.new("RGB",(W*2,H*2+170)); out.paste(im,(0,0)); out.paste(leg,(0,H*2)); out.save("/mnt/project-files/docs/niveles/sagunto_zonas_vista.png")
json.dump({"origen_px00":"esquina noroeste: X=-250, Z=480","px_m":1,"ancho":W,"alto":H,"X":[X0,X1],"Z":[Z0,Z1],
  "uv_unity":"u=(X+250)/756, v=(Z+200)/680 (Unity carga la fila 0 del PNG arriba, como v=1)","zonas":ZON,
  "color_zona_9_acequia":"agua #6c7874 con borde de 1 px en #94948c (D-N67, Lucía 6-nov 18:35); el cauce (8) sigue en #605c48","color_zona_11":"cerro del castillo y sierra: los cubre el modelo de fondo; sin capa C",
  "mascara":{"255":"sin vegetación","128":"glacis: nada de más de 0,3 m","0":"libre"}},
  open("/mnt/project-files/docs/niveles/sagunto_zonas.json","w"),ensure_ascii=False,indent=1)
u,c=np.unique(z[(X>=0)&(X<256)&(Z>=0)&(Z<128)],return_counts=True); print({ZON[a]:int(b) for a,b in zip(u,c)})
