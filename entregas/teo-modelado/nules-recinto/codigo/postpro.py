import json, csv, sys
f = sys.argv[1]; d = json.load(open(f))
for p in d['piezas']:
    p['material'] = 'Hesco' if 'Hesco' in p['malla'] else 'Sacos'
    if p['espejo']: p['malla'] = p['malla'].replace('Remate_', 'RemateEspejo_')
    carpeta = 'Defensas/muro' if p['malla'].startswith(('SM_MuroHesco','SM_MuroSacos')) else 'Defensas/' + p['material'].lower()
    p['ruta'] = carpeta + '/' + p['malla']
d['postes_catenaria_fuera'] = dict(bucle="PrototypeBootstrap.cs:1377 (cada 50 m, Z 60,9)", saltar_x=[60, 110], nota="Álvaro 9-nov: el de X 110 cae dentro del fuerte junto al tren y el de X 60 en la calle del paso a nivel; los de fuera se quedan")
json.dump(d, open(f,'w'), ensure_ascii=False, indent=1)
w = csv.writer(open(sys.argv[2],'w', newline=''), delimiter=';', lineterminator='\n')
w.writerow(['n','lado','ruta','x','z','yaw','largo_m','escala_x','espejo','nota'])
for i,p in enumerate(d['piezas']):
    w.writerow([i, p['lado'], p['ruta'], p['x'], p['z'], p['yaw'], p['largo'], p['escala_x'], 'si' if p['espejo'] else 'no', p.get('nota','')])
