# Muestra de estados del muro (Álvaro, 8-nov; D-N163 §1). Alzado lateral, 1 m = 14 px. Solo dirección para Teo: no es el modelo.
import random
from PIL import Image, ImageDraw, ImageFont
K=14; CW,CH=170,92; LX=150; TOP=40
Fp="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; Fb="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F=ImageFont.truetype(Fp,11); FB=ImageFont.truetype(Fb,13); FT=ImageFont.truetype(Fb,16)
SACO="#605c48"; SACOS="#48403c"; REL="#b4a080"; HES="#70784c"; HESS="#50541c"; MAL="#b8b8b8"; SUELO="#c4ac84"; OSC="#1c1812"; CHAPA="#94948c"; MAD="#a86c50"; CAM="#303424"; SACOM="#847c34"
ESTADOS=["Sano ≥ 70 %","Dañado 30–70 %","Muy dañado 1–30 %","Brecha 0 (no bloquea)"]
bloques=[("SACOS TERREROS · tramo de 8 m = 2 módulos de Teo (1,2 m de alto)",["v0 hiladas rectas","v1 en talud","v2 irregular, aspilleras","v3 con tablón","v4 con red"]),
         ("HESCO · módulo de 10 m, 2,1 m de alto (D-N59)",["v0 malla limpia","v1 geotextil a la vista","v2 doble escalonado","v3 remate de sacos","v4 red de camuflaje"]),
         ("PUERTA DE VEHÍCULOS · 8 m, dos hojas de 4 m (D-N111)",["v0 tubo y chapa","v1 chapa ondulada","v2 tablones y flejes","v3 malla con espino","v4 blindada con pórtico"])]
W=LX+4*CW+20; H=2000
im=Image.new("RGB",(W,H),"#1c1812"); d=ImageDraw.Draw(im)
d.text((10,10),"Muestra · estados del muro (D-N163 §1) · alzado, 1 m = 14 px · sin rojo en el modelo",fill="#d4d0cc",font=FT)
def R(x0,y0,x1,y1,c,o=OSC): d.rectangle([x0,y0,x1,y1],fill=c,outline=o)
def cell(ox,oy,mat,v,e,rnd):
    gy=oy+CH-14; d.rectangle([ox,oy,ox+CW-6,oy+CH-4],fill="#3c3428"); d.rectangle([ox,gy,ox+CW-6,oy+CH-4],fill=SUELO)
    x0=ox+10; L=(8 if mat==0 else 10 if mat==1 else 8)*K*1.0; L=min(L,CW-26)
    if mat==0:   # sacos: hiladas de 0,6 × 0,3 m
        filas=4; hl=0.3*K; sl=0.6*K
        if v==1: filas=5                                   # talud: base más ancha y una hilada más
        if v==2: filas=6                                   # parapeto irregular: de 0,9 a 1,8 m
        alt={0:filas,1:filas,2:2,3:0}[e]
        perfil=[4,4,6,6,6,6,4,3,3,5,6,6,6,6,4]             # v2: altura irregular por columna
        for f in range(alt):
            if v==1: off=f*0.5*K+(sl/2 if f%2 else 0); fin=L-f*0.5*K   # 0,5 m de retranqueo por hilada a cada lado
            else:    off=(sl/2 if f%2 else 0); fin=L
            n=int((fin-off)//sl)
            for i in range(n):
                if v==2 and f>=perfil[i%len(perfil)]: continue
                if v==2 and f==3 and i in (4,11) and e==0: continue        # huecos de tirador (aspilleras)
                if e==1 and f==alt-1 and 3<=i<=5: continue          # muesca en la fila de arriba
                if e==2 and rnd.random()<0.25: continue
                c=SACO if not (v==2 and rnd.random()<0.35) else SACOM
                R(x0+off+i*sl,gy-(f+1)*hl,x0+off+(i+1)*sl-1,gy-f*hl-1,c)
        if v==2 and e==0:
            for i in (4,11): R(x0+i*sl,gy-4*hl,x0+(i+1)*sl-1,gy-3*hl-1,"#000000",REL)
        if v==3 and e<2: R(x0,gy-filas*hl-3,x0+L,gy-filas*hl,MAD)
        if v==4 and e<2:
            for i in range(0,int(L),6): d.line([x0+i,gy-filas*hl,x0+i+4,gy-filas*hl+8],fill=CAM)
        if e>=1:
            for i in range(e*3):
                cx=x0+rnd.uniform(0,L); d.ellipse([cx-5,gy-3,cx+5,gy+3],fill=REL)
        if e==3:
            for i in range(14):
                cx=x0+rnd.uniform(0,L-8); R(cx,gy-rnd.uniform(2,8),cx+8,gy-1,SACOS)
    elif mat==1:  # HESCO: celdas de 1 m, 2,1 m
        h=2.1*K; cw=1.0*K; n=int(L//cw)
        for i in range(n):
            hh=h
            if v==2: hh=h if i%2==0 else 1.3*K
            if e==1 and i in (4,5): hh=h*0.75
            if e==2: hh=h*(0.45+0.1*rnd.random())
            if e==3: hh=rnd.uniform(0.15,0.35)*K
            x=x0+i*cw
            R(x,gy-hh,x+cw-1,gy,HES if e<3 else HESS)
            if e<3:
                for yy in range(int(gy-hh)+3,int(gy),4): d.line([x+1,yy,x+cw-2,yy],fill=MAL)
            if v==1 and e<3: R(x+2,gy-hh+2,x+cw-3,gy-hh+5,REL,None)
        if v==3 and e<2:
            for i in range(n): R(x0+i*cw+1,gy-h-0.3*K,x0+(i+1)*cw-1,gy-h,SACO)
        if v==4 and e<2:
            for i in range(0,int(L),5): d.line([x0+i,gy-h,x0+i+3,gy-h*0.5],fill=CAM)
        if e>=1:
            for i in range(2+e*3): d.polygon([(x0+4*K+rnd.uniform(-20,40),gy),(x0+4.5*K+rnd.uniform(-20,40),gy-rnd.uniform(4,10)),(x0+5*K+rnd.uniform(-20,40),gy)],fill=REL)
        if e==3:
            for i in range(6): d.line([x0+rnd.uniform(0,L),gy-rnd.uniform(0,6),x0+rnd.uniform(0,L),gy-rnd.uniform(0,6)],fill=MAL,width=1)
    else:         # puerta: dos hojas de 4 m, 2,1 m, postes
        h=2.1*K; hw=4*K*0.95
        R(x0-3,gy-h-6,x0,gy,CHAPA); R(x0+2*hw,gy-h-6,x0+2*hw+3,gy,CHAPA)
        if v==4: R(x0-3,gy-h-12,x0+2*hw+3,gy-h-7,CHAPA)
        col=[CHAPA,CHAPA,MAD,MAL,"#6c7874"][v]
        for k in range(2):
            hx=x0+k*hw
            if e==0 or (e==1):
                sag=(6 if (e==1 and k==1) else 0)
                d.polygon([(hx+1,gy-h),(hx+hw-1,gy-h+sag),(hx+hw-1,gy),(hx+1,gy)],fill=col,outline=OSC)
                if v==1:
                    for xx in range(int(hx)+3,int(hx+hw),4): d.line([xx,gy-h+2,xx,gy-1],fill="#6c7874")
                if v==2:
                    for yy in (gy-h*0.75,gy-h*0.3): d.line([hx+2,yy,hx+hw-2,yy],fill=OSC,width=2)
                if v==3:
                    for xx in range(int(hx)+2,int(hx+hw),5): d.line([xx,gy-h,xx+5,gy],fill="#6c7874")
                    d.line([hx,gy-h-3,hx+hw,gy-h-3],fill=OSC)
                if e==1 and k==0: R(hx+hw*0.4,gy-h*0.6,hx+hw*0.6,gy-h*0.35,"#3c3428")   # chapa arrancada
            elif e==2:
                if k==0: d.polygon([(hx+1,gy-h*0.5),(hx+hw-1,gy-h*0.45),(hx+hw-1,gy),(hx+1,gy)],fill=col,outline=OSC)
                else: d.polygon([(hx+hw-4,gy-h),(hx+hw-1,gy-h),(hx+hw*0.3,gy),(hx+hw*0.3-4,gy)],fill=col,outline=OSC)  # colgando de una bisagra
            else:
                d.polygon([(hx+4,gy-2),(hx+hw-4,gy-5),(hx+hw-2,gy),(hx+2,gy)],fill=col,outline=OSC)
        if e==3:
            for i in range(6):
                cx=x0+rnd.uniform(0,2*hw); d.ellipse([cx-4,gy-2,cx+4,gy+2],fill=REL)
y=TOP
for mi,(tit,vars_) in enumerate(bloques):
    d.text((10,y+6),tit,fill="#f0dc9c",font=FB); y+=28
    for ei,e in enumerate(ESTADOS): d.text((LX+ei*CW+4,y-2),e,fill="#d4d0cc",font=F)
    y+=14
    for vi,vn in enumerate(vars_):
        d.text((10,y+CH//2-8),vn,fill="#d4d0cc",font=F)
        for ei in range(4): cell(LX+ei*CW,y,mi,vi,ei,random.Random(mi*100+vi*10+ei))
        y+=CH
    y+=4
d.text((10,y+8),"Álvaro (Niveles) · dirección para Teo, no modelo · la capa de obras va aparte",fill="#d4d0cc",font=FB)
im=im.crop((0,0,W,y+44)); im.save("/mnt/project-files/docs/niveles/muestras/muestra_estados_muro.png"); print(im.size)
