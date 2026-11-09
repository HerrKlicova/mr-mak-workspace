import math, numpy as np
from modelo import *
def dirsol(e, a):
    e, a = math.radians(e), math.radians(a); return np.array([math.cos(e)*math.sin(a), math.sin(e), math.cos(e)*math.cos(a)])
V = {"E": dict(sol=dirsol(45,180), sol_col='fff0d8', sol_i=1.3, cielo='c8bca4', suelo='a89878', amb_i=1.0, L=64),
     "N": dict(sol=dirsol(40,220), sol_col='b8c4e0', sol_i=1.0, cielo='283440', suelo='303424', amb_i=0.35, L=25)}
def luz(v, n):
    n = np.asarray(n, float); n = n/np.linalg.norm(n)
    amb = v['amb_i']*(s2l(h2s(v['cielo']))*(0.5+0.5*n[1]) + s2l(h2s(v['suelo']))*(0.5-0.5*n[1]))
    return s2l(h2s(v['sol_col']))*v['sol_i']*max(0, n@v['sol']) + amb
def expo(v):
    c = s2l(h2s('b4a080'))*luz(v, (0,1,0)); Y = c@np.array([0.2126,0.7152,0.0722]); return (((v['L']+16)/116)**3)/Y
def pantalla(alb, var, n, mix=0.65):
    v = V[var]; c = s2l(h2s(alb))*luz(v, n)*expo(v); o, k = quant(c, mix); return o, PAL[k], c
def hexs(o): return ''.join('%02x' % int(round(x*255)) for x in l2s(o))
