from luz import *
def Lv(c): return float(Lstar_lin(np.asarray(c)))
def scr(alb, var, n, k=1.0):
    v=V[var]; return s2l(h2s(alb))*luz(v,n)*expo(v)*k
K=1.285
R = {}
for var in 'EN':
    kk = K if var=='N' else 1.0
    lw = Lv(scr('88885c',var,(-1,0,0), kk if var=='N' else 1)); ls = Lv(scr('88885c',var,(0,0,-1)))
    R[var]=dict(lat_w=lw, lat_s=ls)
    for alb in PAL:
        c = scr(alb,var,(0,1,0),kk); o,ent = quant(c)
        R[var][alb]=dict(L=Lv(c), ent=PAL[ent], entL=Lv(s2l(h2s(PAL[ent]))), Lq=Lv(o))
if __name__=='__main__':
    print('lateral', {v:(round(R[v]['lat_w'],1), round(R[v]['lat_s'],1)) for v in 'EN'})
    for alb in PAL:
        e,n = R['E'][alb], R['N'][alb]
        print('%s alb %5.1f | dia %5.1f (dO %+5.1f dS %+5.1f) | noche %5.1f (dO %+5.1f) entrada %s %4.1f  q %4.1f' % (alb, Lv(s2l(h2s(alb))), e['L'], e['L']-R['E']['lat_w'], e['L']-R['E']['lat_s'], n['L'], n['L']-16.6, n['ent'], n['entL'], n['Lq']))
