import numpy as np, json, sys
from PIL import Image, ImageDraw
Q='/home/claude/mr-mak-workspace/docs/capturas/qa24/'
OUT='/tmp/claude-0/-home-user/2818eb2c-097b-5b7d-b51d-5e861bbbc311/scratchpad/var/'
def dec(u): return np.where(u<=.04045,u/12.92,((u+.055)/1.055)**2.4)
def enc(l): l=np.clip(l,0,1); return np.where(l<=.0031308,l*12.92,1.055*l**(1/2.4)-.055)
def load(f): return np.array(Image.open(Q+f).convert('RGB')).astype(float)/255
act,luna,amb=load('actual_captura_20261107_095057.png'),load('luna_captura_20261107_095651.png'),load('ambiente_captura_20261107_095952.png')
# 1) deshacer la codificación sRGB de más -> sRGB verdadero; 2) a lineal
T=lambda x: dec(x)            # sRGB verdadero
Lin=lambda x: dec(dec(x))     # lineal
hud=(np.abs(luna-amb).sum(2)==0)
A,Lu,Am=Lin(act),Lin(luna),Lin(amb)
W=np.array([.2126,.7152,.0722])
def luma(c): return (c*W).sum(2,keepdims=True)
# deshacer la gradación actual: exposición +0,35 y saturación -15
Au=A/2**0.35; y=luma(Au); Au=y+(Au-y)/0.85
moon0=np.array([.42,.48,.62])*.45; amb0=np.array([.012,.016,.026])
F=np.clip(Au-moon0*Lu-(amb0/0.1)*Am,0,None)      # focos, emisivos, trazadoras y fogonazos
alb=Am/0.1                                       # albedo aproximado (el ambiente es plano)
PAL=["000000","340000","1c200c","181c30","4c1008","442c0c","303424","283440","642030","7c181c","543820","48403c","404460","982420","7c3c18","6c4038","50541c","60546c","605c48","8c5048","845c28","70784c","6c7874","847c34","a86c50","88885c","94948c","e08c30","b4a080","b8b8b8","d4d0cc","f0dc9c"]
P=np.array([[int(h[i:i+2],16) for i in (0,2,4)] for h in PAL])/255
def quant(lin,mix,espacio):
    if mix==0: return lin
    if espacio=='lineal':
        c=lin; p=dec(P)
    else:
        c=enc(lin); p=P
    d=((c[:,:,None,:]-p[None,None,:,:])**2).sum(3); r=p[d.argmin(2)]
    out=c+(r-c)*mix
    return out if espacio=='lineal' else dec(out)
def render(moon,ambc,filt,sat,exp,mix,esp):
    c=np.array(moon)*Lu+(np.array(ambc)/0.1)*Am+F
    c=quant(c,mix,esp)
    c=c*np.array(filt)*2**exp
    y=luma(c); c=y+(c-y)*(1+sat/100)
    s=enc(c)
    s[hud]=T(act)[hud]           # el HUD con su valor correcto
    return s
def lab(s):
    l=dec(s); Y=(l*W).sum(2); f=np.where(Y>.008856,np.cbrt(Y),7.787*Y+16/116); L=116*f-16
    X=(l@np.array([.4124,.3576,.1805]))/.95047; Z=(l@np.array([.0193,.1192,.9505]))/1.08883
    fx=np.where(X>.008856,np.cbrt(X),7.787*X+16/116); fz=np.where(Z>.008856,np.cbrt(Z),7.787*Z+16/116)
    return L,500*(fx-f),200*(f-fz)
world=~hud
Lalb,_,_=lab(enc(np.clip(alb,0,1)))
horda=world&(Lalb<16)&(Lalb>2)
lun_y=luma(Lu)[...,0]; sombra=world&(lun_y<np.percentile(lun_y[world],20))&~horda
suelo=world&~horda
V={
 'control':dict(moon=moon0,ambc=amb0,filt=(1,1,1),sat=-15,exp=.35,mix=.65,esp='lineal'),
 'v1':dict(moon=np.array([.45,.58,1.0])*.35,ambc=(.04,.05,.10),filt=(.80,.88,1),sat=-20,exp=0,mix=0,esp='srgb'),
 'v2':dict(moon=np.array([.45,.58,1.0])*.35,ambc=(.04,.05,.10),filt=(.80,.88,1),sat=-20,exp=0,mix=.2,esp='srgb'),
 'v3':dict(moon=np.array([.40,.55,1.0])*.45,ambc=(.03,.045,.10),filt=(.78,.86,1),sat=-10,exp=0,mix=0,esp='srgb'),
 'v4':dict(moon=np.array([.55,.62,.85])*.30,ambc=(.05,.055,.08),filt=(.75,.85,1),sat=-40,exp=0,mix=0,esp='srgb'),
 'v5':dict(moon=np.array([.45,.58,1.0])*.55,ambc=(.04,.05,.10),filt=(.80,.88,1),sat=-15,exp=0,mix=.2,esp='srgb'),
}
res={}
ims={}
for k,p in V.items():
    s=render(**p); ims[k]=s
    L,a,b=lab(s); C=np.hypot(a,b)
    Ls=L[suelo]; hist,_=np.histogram(Ls,bins=np.arange(0,101,5)); bandas=int((hist>0.03*Ls.size).sum())
    res[k]=dict(suelo_L_mediana=round(float(np.median(Ls)),1), suelo_bandas_5L=bandas,
        horda_L_mediana=round(float(np.median(L[horda])),1) if horda.sum()>50 else None, horda_px=int(horda.sum()),
        dL_horda_suelo=round(float(np.median(Ls)-np.median(L[horda])),1) if horda.sum()>50 else None,
        sombra_croma_mediana=round(float(np.median(C[sombra])),1), sombra_hue=round(float(np.degrees(np.arctan2(np.median(b[sombra]),np.median(a[sombra])))),0),
        mundo_croma_mediana=round(float(np.median(C[world])),1), suelo_b=round(float(np.median(b[suelo])),1), suelo_a=round(float(np.median(a[suelo])),1), color_propio_croma_p90=round(float(np.percentile(C[world],90)),1))
    Image.fromarray((s*255+.5).astype(np.uint8)).save(OUT+f'noche_{k}.png')
json.dump(res,open(OUT+'medidas.json','w'),indent=1,ensure_ascii=False)
print(json.dumps(res,indent=1,ensure_ascii=False))
# lámina 3x2
o=Image.new('RGB',(960*3+32,(540+28)*2+8),(24,28,48)); d=ImageDraw.Draw(o)
for i,k in enumerate(['control','v1','v2','v3','v4','v5']):
    x=8+(i%3)*(968); yy=8+(i//3)*(568)
    o.paste(Image.fromarray((ims[k]*255+.5).astype(np.uint8)),(x,yy+20))
    r=res[k]; d.text((x,yy+4),f"{k}: suelo L* {r['suelo_L_mediana']} ({r['suelo_bandas_5L']} valores) · horda L* {r['horda_L_mediana']} · sombra croma {r['sombra_croma_mediana']} · suelo a*/b* {r['suelo_a']}/{r['suelo_b']} · croma p90 {r['color_propio_croma_p90']}",fill=(212,208,204))
o.save(OUT+'lamina_noche_6.png')

if 'diag' in sys.argv:
    fy=luma(F)[...,0]; my=luma(moon0*Lu)[...,0]; ay=luma((amb0/0.1)*Am)[...,0]; uy=luma(Au)[...,0]
    for n,v in [('F',fy),('moon',my),('amb',ay),('act_ungraded',uy)]:
        print(n, np.percentile(v[world],[10,50,90]).round(4))
    Image.fromarray((enc(np.clip(F*4,0,1))*255).astype(np.uint8)).save(OUT+'F_x4.png')
