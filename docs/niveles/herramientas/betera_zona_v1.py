# Genera betera_obstaculos_v1.csv y betera_zona_v1.json (Álvaro, 9-nov). python3 -I betera_zona_v1.py <carpeta docs/niveles>
import csv, json, math, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else '.'
F = (0.0, -4.0, 256.0, 124.0)   # encuadre MVP
# medidas de los FBX de Teo (LOD1, caja envolvente; largo en X local, frente en +Z con yaw 0)
DIM = {'SM_Hangar': (64.0, 25.9, 12.2), 'SM_TorreControl': (5.9, 5.9, 15.0), 'SM_TorretaVigia': (4.64, 4.6, 6.7),
       'SM_Caseta': (6.1, 3.2, 2.7), 'SM_CisternaFlexible': (11.4, 5.9, 1.4), 'SM_Vallas': (10.4, 0.34, 1.1),
       'SM_TorreLuz': (3.1, 3.7, 8.7), 'camion': (2.45, 8.0, 3.3), 'remolque': (2.3, 3.6, 1.45), 'SM_Carrete': (2.04, 1.76, 1.4)}
filas = []
def caja(id_, tipo, x, z, prefab, yaw, vision, paso, fuente, nota=''):
    L, W, H = DIM[prefab]
    if round(yaw) % 180 == 90: L, W = W, L
    filas.append([id_, tipo, 'caja', int(round((x - L/2)*1000)), int(round((z - W/2)*1000)), int(round((x + L/2)*1000)), int(round((z + W/2)*1000)), 0, int(H*1000), vision, paso, fuente, nota])
def seg(id_, tipo, x0, z0, x1, z1, h, fuente, nota=''):
    filas.append([id_, tipo, 'seg', int(x0*1000), int(z0*1000), int(x1*1000), int(z1*1000), 500, h, 'si', 'si', fuente, nota])
caja('hangar_h1', 'edificio', 90, 40, 'SM_Hangar', 0, 'si', 'si', 'betera_instancias_v1.csv', 'el FBX mide 64 x 25,9 m (el plano decía 40 x 25)')
caja('hangar_h2', 'edificio', 160, 40, 'SM_Hangar', 0, 'si', 'si', 'betera_instancias_v1.csv', 'el FBX mide 64 x 25,9 m')
caja('torre_control', 'edificio', 224, 4, 'SM_TorreControl', 0, 'si', 'si', 'betera_instancias_v1.csv')
caja('torreta_no', 'edificio', 4, 121, 'SM_TorretaVigia', 0, 'si', 'si', 'betera_instancias_v1.csv', 'torreta de vigía, 6,7 m')
caja('torreta_ne', 'edificio', 252, 121, 'SM_TorretaVigia', 0, 'si', 'si', 'betera_instancias_v1.csv', 'torreta de vigía, 6,7 m')
caja('caseta_1', 'mueble', 125, 30, 'SM_Caseta', 90, 'si', 'si', 'betera-nivel.md §11', 'movida de (116; 30), que caía dentro del hangar H1')
caja('caseta_2', 'mueble', 198, 30, 'SM_Caseta', 0, 'si', 'si', 'betera-nivel.md §11', 'movida de (186; 30), que caía dentro del hangar H2')
caja('cisterna_farp', 'mueble', 53, 104, 'SM_CisternaFlexible', 180, 'no', 'si', 'betera-nivel.md §10.1', '1,4 m: no tapa la vista')
caja('carrete_farp', 'mueble', 46.5, 99, 'SM_Carrete', 0, 'no', 'si', 'betera-nivel.md §10.1')
caja('camion_rearme', 'vehiculo', 152, 100, 'camion', 0, 'si', 'si', 'betera-nivel.md §9', 'camión cisterna, yaw 180')
caja('remolque_rearme', 'vehiculo', 152, 106.5, 'remolque', 0, 'no', 'si', 'betera-nivel.md §9')
for i, (x, z) in enumerate([(21, 121), (41, 121), (118, 121), (138, 121), (216, 121), (236, 121)]):
    caja('vallas_%d' % i, 'mueble', x, z, 'SM_Vallas', 0, 'no', 'si', 'betera_instancias_v1.csv', 'vallas de obra, 1,1 m')
# reducto: dentro del encuadre solo entra el muro norte (Z 124), cortado por las 3 puertas de vehículos de 8 m
gates = [31, 128, 226]
xs = [F[0]] + sum([[g - 4, g + 4] for g in gates], []) + [F[2]]
for i in range(0, len(xs), 2):
    seg('reducto_norte_%d' % (i // 2), 'muro_hesco', xs[i], 124, xs[i + 1], 124, 2100, 'betera_instancias_v1.csv', 'HESCO; sigue fuera del encuadre')
for g in gates:
    seg('puerta_norte_%d' % g, 'puerta', g - 4, 124, g + 4, 124, 2100, 'betera_instancias_v1.csv', 'puerta de vehículos (D-N111), cerrada de noche')
cols = ['id', 'tipo', 'forma', 'x0_mm', 'z0_mm', 'x1_mm', 'z1_mm', 'medio_grosor_mm', 'altura_mm', 'tapa_vision', 'tapa_paso', 'fuente', 'nota']
with open(os.path.join(D, 'betera_obstaculos_v1.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter=';'); w.writerow(cols); w.writerows(filas)
# comprobación: ninguna caja se pisa con otra ni con los claros
cajas = [r for r in filas if r[2] == 'caja']
claros = {'P1': (128, 104, 30), 'P2': (31, 104, 25), 'P3': (226, 104, 25)}
def solapa(a, b): return a[3] < b[5] and b[3] < a[5] and a[4] < b[6] and b[4] < a[6]
for i in range(len(cajas)):
    for j in range(i + 1, len(cajas)):
        if solapa(cajas[i], cajas[j]): print('SOLAPE', cajas[i][0], cajas[j][0])
    for k, (cx, cz, l) in claros.items():
        c = [k, '', '', (cx - l/2)*1000, (cz - l/2)*1000, (cx + l/2)*1000, (cz + l/2)*1000]
        if solapa(cajas[i], c): print('EN CLARO', cajas[i][0], k)
print(len(filas), 'filas')
