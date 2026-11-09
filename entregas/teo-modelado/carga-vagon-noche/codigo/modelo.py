import numpy as np, itertools
PAL = "000000 340000 1c200c 181c30 4c1008 442c0c 303424 283440 642030 7c181c 543820 48403c 404460 982420 7c3c18 6c4038 50541c 60546c 605c48 8c5048 845c28 70784c 6c7874 847c34 a86c50 88885c 94948c e08c30 b4a080 b8b8b8 d4d0cc f0dc9c".split()
def h2s(h): return np.array([int(h[i:i+2],16)/255 for i in (0,2,4)])
def s2l(c): c=np.asarray(c,float); return np.where(c<=0.04045, c/12.92, ((c+0.055)/1.055)**2.4)
def l2s(c): c=np.clip(np.asarray(c,float),0,1); return np.where(c<=0.0031308, c*12.92, 1.055*c**(1/2.4)-0.055)
def Lstar_lin(c):
    Y = 0.2126*c[...,0]+0.7152*c[...,1]+0.0722*c[...,2]
    return np.where(Y>216/24389, 116*np.cbrt(Y)-16, Y*24389/27)
PL = np.array([s2l(h2s(h)) for h in PAL])
def quant(c, mix=0.65):
    d = ((PL - c)**2).sum(1); k = int(d.argmin()); return (1-mix)*c + mix*PL[k], k
def L(h): return float(Lstar_lin(s2l(h2s(h))))
