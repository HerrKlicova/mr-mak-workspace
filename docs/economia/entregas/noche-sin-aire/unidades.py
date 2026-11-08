#!/usr/bin/env python3
"""Estadísticas jugables de pelotones, vehículo de tierra y helicóptero (Hugo, 6-nov noche).
Fuente de verdad de las unidades: ARMAS, PELOTONES y VEHICULOS de este archivo. Genera ../csv/balance_unidades.csv (clave;valor;escala;nota,
todo entero) y ../csv/referencia_unidades.csv (bajas/s y bajas/u esperadas), y comprueba el asedio de 10.000 contra la economía (400 zombis/u).
Las referencias reales (Paula, docs/arte/referencias/catalogo.md) solo orientan el papel de cada arma: los números son de JUEGO.
Convenciones de la zona (balance_combate.csv): 30 ticks/s, 1 u de munición = 2.000 disparos equivalentes, zombi común de un impacto,
soldado de 100 de vida, 2 de daño por tick y zombi en contacto."""
import os, math, csv

TICKS = 30
DISP_POR_U = 2000
Z_POR_U_ECONOMIA = 400       # sim_economia.py: lo que cuesta un zombi en el modelo de red

# arma: cadencia en ticks, alcance, alcance mínimo, acierto (bocajarro, pendiente por m, mínimo) en ‰,
# coste en disparos equivalentes, radio de área (mm, 0 = tiro directo), letalidad en el radio (‰), tope de bajas por impacto,
# perforación (zombis extra detrás, al 50 %), despliegue (ticks parado antes de poder disparar), vuelo del proyectil (ticks).
ARMAS = {
 "fusil":               dict(clase="ligera",   cad=15,  alc=60,  amin=0,  ab=210, pend=3, amin_p=30,  coste=1,  radio=0,    letal=0,   tope=1,  perf=0, despl=0,  vuelo=0,   ref="HK G36E (Paula: 750 disp./min de cadencia máxima)", nota="sin cambios, validado en P7: 2 disparos/s es tiro apuntado, no la cadencia cíclica"),
 "ametralladora_ligera":dict(clase="ligera",   cad=2,   alc=70,  amin=0,  ab=126, pend=2, amin_p=18,  coste=1,  radio=0,    letal=0,   tope=1,  perf=0, despl=0,  vuelo=0,   ref="HK MG4E en marcha (Paula: alza hasta 1.000 m)", nota="sin cambios: el 60 % del fusil, como hoy"),
 "ametralladora_emplazada":dict(clase="ligera",cad=2,   alc=80,  amin=0,  ab=300, pend=3, amin_p=40,  coste=2,  radio=0,    letal=0,   tope=1,  perf=1, despl=60, vuelo=0,   ref="HK MG4E sobre bípode, unos 1.000 m (Paula); la MG5 de 7,62 como mejora", nota="ametralladores: 2 s para emplazarse, cono de 60 grados, perfora 1 en masa; quieta, no dispara en marcha"),
 "lanzagranadas":       dict(clase="especial", cad=180, alc=140, amin=15, ab=0,   pend=0, amin_p=0,   coste=40, radio=4000, letal=500, tope=25, perf=0, despl=0,  vuelo=20,  ref="HK AG36 de 40 mm, monotiro, hasta 350 m (Paula)", nota="D-N137 (7-nov): radio 2,5 -> 4 m y tope 10 -> 25 (40 mm HE: letal ~5 m); tiro parabólico; solo si hay >= 6 zombis en el radio, si no el granadero usa su fusil"),
 "fusil_precision":     dict(clase="ligera",   cad=60,  alc=160, amin=0,  ab=950, pend=1, amin_p=600, coste=3,  radio=0,    letal=0,   tope=1,  perf=1, despl=0,  vuelo=0,   ref="HK G28 semiautomático, 600 m precisos (Paula); la mejora es fusil_antimaterial", nota="prioridad: el zombi más cercano al muro o el especial; muy eficiente por u y de poco caudal"),
 "fusil_antimaterial":  dict(clase="ligera",   cad=90,  alc=200, amin=0,  ab=950, pend=1, amin_p=650, coste=6,  radio=0,    letal=0,   tope=1,  perf=2, despl=60, vuelo=0,   ref="Barrett M95SP 12,7 mm, cerrojo, 1.800 m, cargador de 5 (Paula)", nota="D-N81: MEJORA de los tiradores, fuera de la noche; más lenta que el G28 (cerrojo), más alcance y perfora 2; bípode: 2 s de despliegue"),
 "carga_zapador":       dict(clase="especial", cad=900, alc=10,  amin=0,  ab=0,   pend=0, amin_p=0,   coste=200,radio=4000, letal=800, tope=40, perf=0, despl=90, vuelo=150, ref="carga explosiva (Paula: sin dato)", nota="se coloca a <= 10 m y estalla a los 5 s; una cada 30 s por zapador con carga"),
 "canon_30":            dict(clase="pesada",   cad=10,  alc=220, amin=0,  ab=500, pend=1, amin_p=200, coste=15, radio=2500, letal=500, tope=10, perf=0, despl=0,  vuelo=0,   ref="Mk44S de 30 mm del VCR Dragón (Paula: 200 disp./min, 3.000 m)", nota="D-N137 (7-nov): radio 1,5 -> 2,5 m y tope 4 -> 10; explosivo: impacto directo más metralla en 2,5 m; apunta y dispara solo"),
 "ametralladora_pesada":dict(clase="ligera",   cad=3,   alc=100, amin=0,  ab=300, pend=2, amin_p=40,  coste=3,  radio=0,    letal=0,   tope=1,  perf=1, despl=0,  vuelo=0,   ref="Browning M2HB 12,7 mm (Paula: sin verificar)", nota="para el nido de ametralladora de la estación (pieza fija)"),
 "ametralladora_puerta":dict(clase="ligera",   cad=3,   alc=120, amin=0,  ab=180, pend=1, amin_p=30,  coste=1,  radio=0,    letal=0,   tope=1,  perf=0, despl=0,  vuelo=0,   ref="FN MAG 58 de 7,62 mm, 2 por aparato, 650-1.000 disp./min (Paula); montaje sin verificar", nota="cada una dispara solo hacia su lado (sector de 180 grados); desde plataforma en vuelo acierta menos; alcance inclinado desde 30 m"),
 "canon_30_heli":       dict(clase="pesada",   cad=5,   alc=200, amin=0,  ab=450, pend=1, amin_p=200, coste=15, radio=2500, letal=500, tope=10, perf=0, despl=0,  vuelo=0,   ref="cañón de 30 mm del Tigre (Paula A3)", nota="alternativa al NH90"),
 "c90":                 dict(clase="especial", cad=300, alc=120, amin=10, ab=0,   pend=0, amin_p=0,   coste=2000,radio=5000, letal=500, tope=40, perf=0, despl=0,  vuelo=15,  ref="Instalaza C90-CR-AM de 90 mm, desechable, unos 200-350 m eficaces (dotación real sin verificar)", nota="D-N137 (Lucía, 7-nov): SOLO por orden del jugador, nunca automático; un solo uso, 2 por pelotón de fusileros (1 por escuadra), se reponen del almacén en la recarga; coste 1 u por tiro (2.000 disparos equivalentes) para que gastarlo sea una decisión"),
 "cohetes_70":          dict(clase="especial", cad=600, alc=220, amin=30, ab=0,   pend=0, amin_p=0,   coste=200,radio=7000, letal=600, tope=60, perf=0, despl=0,  vuelo=30,  ref="cohetes de 70 mm del Tigre (Paula A3)", nota="salva cada 20 s; solo 2 salvas por salida"),
}


# pelotón: personas, armas (arma: cuántas), personas sin arma (servidores), velocidad (mm/s), dotación de munición (‰ de u),
# materiales del equipo (u, solo al crearlo), tiempo de formación (h), etapa.
PELOTONES = {
 "fusileros":     dict(pers=8, armas={"fusil": 4, "ametralladora_ligera": 2, "lanzagranadas": 2}, c90=2, servidores=0, vel=2500, dot=1500, mat=0, form=6,  etapa=1, prioridad="P0",
                       papel="todoterreno: 2 escuadras de 4 (jefe, ametrallador MG4E, granadero con AG36 y fusilero); guarnición, escolta y línea"),
 "ametralladores":dict(pers=4, armas={"ametralladora_emplazada": 2}, servidores=2, vel=2200, dot=2000, mat=2, form=8,  etapa=1, prioridad="P0",
                       papel="emplazados, cono de fuego sostenido devastador contra masas; quietos y vulnerables por los flancos"),
 "granaderos":    dict(pers=6, armas={"lanzagranadas": 6}, servidores=0, vel=2300, dot=2000, mat=3, form=8,  etapa=1, prioridad="P1",
                       papel="área con tiro parabólico (mínimo 15 m): rompen la pila contra el muro; con la horda suelta tiran de fusil"),
 "tiradores":     dict(pers=2, armas={"fusil_precision": 1, "fusil": 1}, servidores=0, vel=2500, dot=300,  mat=1, form=12, etapa=1, prioridad="P1",
                       papel="tirador y observador: alcance largo, especiales y grandes primero; casi no gastan"),
 "zapadores":     dict(pers=6, armas={"fusil": 6, "carga_zapador": 2}, servidores=0, vel=2300, dot=1500, mat=2, form=10, etapa=1, prioridad="P2",
                       papel="construyen y reparan obras al doble de velocidad (obra x2) y ponen cargas; 2 de los 6 llevan carga"),
}


VEHICULOS = {
 "dragon": dict(vida=4000, armadura=990, vel_mm_s=12000, vel_horda_mm_s=4000, acel_mm_s2=3000, giro_cdeg_s=4500, bloqueo_pila=3,
                plazas=8, armas={"canon_30": 1, "ametralladora_ligera": 1}, municion_bordo=2000, comb_marcha_e4_s=200, comb_ralenti_e4_s=60, deposito_u=8, repostar_s_por_u=2, coste_mat=60, coste_comb=15,
                taller_dias=2, reparar_u_por_1000_vida=5, etapa=1, atropello_vel_min_mm_s=3000, atropello_permil=500,
                ref="VCR 8x8 Dragón (Paula V1: 8 x 3 x 2,34 m, 30 t, torre de 30 mm)",
                nota="la horda casi no lo araña (armadura 99 %); lo que lo mata es quedarse encajado: con pila >= 3 delante se para, como el tren",
                vel_carretera_kmh=80, vel_via_kmh=30),
 # D-N101 (Hugo, 7-nov): VAMTAC y Pizarro del PR #24. Velocidad y aceleración en zona = Vehiculos.cs de Nacho. Vida contra 2 de daño por tick y zombi; armadura en ‰.
 "vamtac": dict(vida=2000, armadura=950, vel_mm_s=19000, vel_horda_mm_s=3000, acel_mm_s2=3800, giro_cdeg_s=5000, bloqueo_pila=2,
                plazas=4, armas={"ametralladora_pesada": 1}, municion_bordo=3000, comb_marcha_e4_s=90, comb_ralenti_e4_s=25, deposito_u=4, repostar_s_por_u=2, coste_mat=20, coste_comb=5,
                taller_dias=1, reparar_u_por_1000_vida=4, etapa=1, atropello_vel_min_mm_s=3000, atropello_permil=300,
                ref="URO VAMTAC ST5 con M2 de 12,7 mm (4,9 x 2,2 m, 7 t)",
                nota="rápido y barato: enlace, reconocimiento y reabastecer; con 24 zombis pegados cae en unos 28 s; con pila >= 2 delante se para",
                vel_carretera_kmh=90, vel_via_kmh=25),
 "pizarro": dict(vida=5000, armadura=993, vel_mm_s=14000, vel_horda_mm_s=5000, acel_mm_s2=2500, giro_cdeg_s=4000, bloqueo_pila=6,
                plazas=8, armas={"canon_30": 1, "ametralladora_ligera": 1}, municion_bordo=2500, comb_marcha_e4_s=250, comb_ralenti_e4_s=80, deposito_u=8, repostar_s_por_u=2, coste_mat=80, coste_comb=20,
                taller_dias=3, reparar_u_por_1000_vida=6, etapa=2, atropello_vel_min_mm_s=2000, atropello_permil=700,
                ref="VCI Pizarro (ASCOD) de orugas con Mauser de 30 mm (6,8 x 3,2 m, 28 t)",
                nota="ariete de orugas: atraviesa la pila (se para con >= 6) y aguanta unos 6 min con 33 zombis pegados; lento y caro de combustible: de lejos, mejor en el tren",
                vel_carretera_kmh=50, vel_via_kmh=35),
}
HELIS = {
 "nh90": dict(vida=3000, armadura=900, vel_max_mm_s=45000, acel_mm_s2=5000, fren_mm_s2=7000, guinada_cdeg_s=6000, subida_mm_s=6000, bajada_mm_s=4000,
              altura_crucero_mm=30000, altura_contacto_mm=3000, inclinacion_max_cdeg=1500, plazas=12, armas={"ametralladora_puerta": 2},
              municion_bordo=3000, comb_vuelo_e4_s=270, comb_suelo_e4_s=90, deposito_u=6, repostar_s_por_u=2, huella_salida=1500, etapa=2,
              ref="NH90 de las FAMET (Paula A2)", nota="RECOMENDADO para el MVP: lleva un pelotón lejos de la vía y lo apoya. Solo se le puede tocar por debajo de 3 m"),
 "tigre": dict(vida=2500, armadura=900, vel_max_mm_s=50000, acel_mm_s2=6000, fren_mm_s2=8000, guinada_cdeg_s=7000, subida_mm_s=7000, bajada_mm_s=5000,
              altura_crucero_mm=30000, altura_contacto_mm=3000, inclinacion_max_cdeg=1800, plazas=0, armas={"canon_30_heli": 1, "cohetes_70": 1},
              municion_bordo=3000, comb_vuelo_e4_s=270, comb_suelo_e4_s=90, deposito_u=6, repostar_s_por_u=2, huella_salida=1500, etapa=3,
              ref="EC665 Tigre HAD-E de las FAMET (Paula A3)", nota="alternativa de ataque: espectacular, pero no transporta"),
}

# ---------- modelo de rendimiento
def p_acierto(a, d):
    return max(a["amin_p"], a["ab"] - a["pend"] * d) / 1000

def rendimiento(nombre, dens, d=25.0):
    """bajas por segundo y por u de UN arma contra una horda de densidad dens (zombis/m²) a la distancia media d."""
    a = ARMAS[nombre]
    disp_s = TICKS / a["cad"]
    if a["radio"]:
        en_radio = dens * math.pi * (a["radio"] / 1000) ** 2
        if nombre == "lanzagranadas" and en_radio < 6: return rendimiento("fusil", dens, d)   # regla del granadero
        bajas = min(a["tope"], en_radio * a["letal"] / 1000)
        if a["ab"]: bajas += p_acierto(a, d)              # impacto directo del cañón
    else:
        bajas = p_acierto(a, d) * (1 + (0.5 * a["perf"] if dens >= 1 else 0))
    return disp_s * bajas, DISP_POR_U / a["coste"] * bajas

def peloton(n, dens, d=25.0):
    p = PELOTONES[n]; bs = bu_num = u_s = 0
    for arma, k in p["armas"].items():
        r = rendimiento(arma, dens, d)
        bs += k * r[0]; u_s += k * r[0] / r[1]
    return bs, (bs / u_s if u_s else 0)

def filas():
    out = []
    add = lambda k, v, e, nota="": out.append((k, int(v), e, nota))
    add("unidades_version", 1, 1, "D-N72 (Hugo, 6-nov noche): primera tabla jugable; los números son de juego, no de manual")
    for n, a in ARMAS.items():
        add(f"arma_{n}_cadencia_ticks", a["cad"], 1, f"{a['ref']}; {a['nota']}")
        add(f"arma_{n}_clase_municion", {"ligera": 1, "pesada": 2, "especial": 3}[a["clase"]], 1, "1 ligera, 2 pesada, 3 especial: en el MVP las tres salen del MISMO stock de munición (la economía tiene una sola); la clase es para la Colmena (tipo de muerte) y para separarlas más adelante")
        add(f"arma_{n}_alcance_m", a["alc"], 1); add(f"arma_{n}_alcance_min_m", a["amin"], 1)
        add(f"arma_{n}_acierto_bocajarro_permil", a["ab"], 1000); add(f"arma_{n}_acierto_pendiente_permil_m", a["pend"], 1000)
        add(f"arma_{n}_acierto_minimo_permil", a["amin_p"], 1000); add(f"arma_{n}_coste_disparos", a["coste"], 1, "disparos equivalentes por disparo (1 u = 2.000)")
        add(f"arma_{n}_radio_mm", a["radio"], 1, "0 = tiro directo"); add(f"arma_{n}_letalidad_permil", a["letal"], 1000, "probabilidad de abatir a cada zombi dentro del radio")
        add(f"arma_{n}_tope_bajas", a["tope"], 1); add(f"arma_{n}_perforacion", a["perf"], 1, "zombis extra detrás del primero, al 50 %")
        add(f"arma_{n}_despliegue_ticks", a["despl"], 1, "parado este tiempo antes de disparar; no dispara en marcha si > 0")
        add(f"arma_{n}_vuelo_ticks", a["vuelo"], 1, "retardo hasta el impacto")
    for n, p in PELOTONES.items():
        add(f"peloton_{n}_personas", p["pers"], 1, p["papel"]); add(f"peloton_{n}_servidores", p["servidores"], 1, "personas sin arma propia (cargadores)")
        for arma, k in p["armas"].items(): add(f"peloton_{n}_arma_{arma}", k, 1)
        if p.get("c90"): add(f"peloton_{n}_c90_tiros", p["c90"], 1, "D-N137: C90 de un solo uso, solo por orden del jugador; se reponen del almacén en la recarga a 1 u cada uno (arma_c90_*)")
        add(f"peloton_{n}_velocidad_mm_s", p["vel"], 1, "el zombi común va de 1,2 a 2,0 m/s")
        add(f"peloton_{n}_dotacion_municion_permil_u", p["dot"], 1000, "munición que se lleva al desembarcar (sale del tren o de la estación)")
        add(f"peloton_{n}_materiales_u", p["mat"], 1, "equipo, una vez al formarlo"); add(f"peloton_{n}_formacion_h", p["form"], 1)
        add(f"peloton_{n}_etapa", p["etapa"], 1, f"prioridad de la noche {p['prioridad']}")
        add(f"peloton_{n}_soldado_vida", 4000, 1, "D-N107 (Hugo): 100 -> 2000 -> 4000 con el contacto de a210bd3 (2 por zombi y tick a 900 mm): un zombi solo tarda 67 s, seis tardan 11 s. Con 2000 el caso B de Sara daba 10 bajas")
    add("infanteria_campo_traves_permil", 700, 1000, "D-N119 (Hugo): a pie fuera de carretera y vía (huerta, descampado) al 70 % de la velocidad del pelotón; marcha de 5 km/h en camino frente a 3,5 por campo. Sustituye a Transporte.FootPenaltyPm")
    for n, v in VEHICULOS.items():
        for k in ("vida", "armadura", "vel_mm_s", "vel_horda_mm_s", "acel_mm_s2", "giro_cdeg_s", "bloqueo_pila", "plazas", "municion_bordo", "comb_marcha_e4_s", "comb_ralenti_e4_s", "deposito_u", "repostar_s_por_u", "coste_mat", "coste_comb", "taller_dias", "reparar_u_por_1000_vida", "etapa", "atropello_vel_min_mm_s", "atropello_permil", "vel_carretera_kmh", "vel_via_kmh"):
            esc = 10000 if k.startswith("comb_") else (1000 if k in ("armadura", "municion_bordo") else 1)
            nota = {"vida": v["ref"], "armadura": "‰ del daño de los zombis que se ignora", "vel_horda_mm_s": "a través de horda suelta (>= 0,5 zombis/m²)",
                    "bloqueo_pila": "pila delante a partir de la cual se para (= tapón del tren)", "municion_bordo": "‰ de u", "comb_marcha_e4_s": f"D-N76: E4 de u por segundo REAL en marcha ({str(round(v['comb_marcha_e4_s']*60/10000, 2)).replace('.', ',')} u/min), se cobra cada 30 ticks", "comb_ralenti_e4_s": f"D-N76: parado con el motor encendido ({str(round(v['comb_ralenti_e4_s']*60/10000, 2)).replace('.', ',')} u/min); apagado, 0", "deposito_u": "D-N76: sale lleno del almacén al empezar; a cero se queda inmóvil y sus armas siguen disparando", "repostar_s_por_u": "junto al depósito o al tren, del almacén de Sagunto; un zapador lleva un bidón de 2 u (20 s)",
                    "vel_mm_s": v["nota"], "atropello_permil": f"probabilidad de abatir a cada zombi que pisa yendo a >= {v['atropello_vel_min_mm_s']//1000} m/s (empuja y atropella)", "atropello_vel_min_mm_s": "por debajo solo empuja", "vel_carretera_kmh": "D-N96: en el mapa, km/h del reloj de juego por carretera habilitada", "vel_via_kmh": "D-N96: en el mapa, km/h de juego rodando por la caja de la vía (balasto); no van campo a través"}.get(k, "")
            add(f"vehiculo_{n}_{k}", v[k], esc, nota)
        for arma, k in v["armas"].items(): add(f"vehiculo_{n}_arma_{arma}", k, 1)
    for n, h in HELIS.items():
        for k in ("vida", "armadura", "vel_max_mm_s", "acel_mm_s2", "fren_mm_s2", "guinada_cdeg_s", "subida_mm_s", "bajada_mm_s", "altura_crucero_mm", "altura_contacto_mm",
                  "inclinacion_max_cdeg", "plazas", "municion_bordo", "comb_vuelo_e4_s", "comb_suelo_e4_s", "deposito_u", "repostar_s_por_u", "huella_salida", "etapa"):
            esc = 10000 if k.startswith("comb_") else (1000 if k in ("armadura", "municion_bordo", "huella_salida") else 1)
            nota = {"vida": h["ref"], "vel_max_mm_s": h["nota"], "altura_contacto_mm": "por debajo, los zombis pueden agarrarlo (posado o embarcando)",
                    "inclinacion_max_cdeg": "cabeceo a aceleración máxima (centésimas de grado)", "comb_vuelo_e4_s": "D-N76: E4 de u por segundo REAL en vuelo (1,62 u/min), se cobra cada 30 ticks", "comb_suelo_e4_s": "D-N76: posado con los rotores girando (0,54 u/min); apagado, 0", "deposito_u": "D-N76: sale lleno; a cero baja en autorrotación a 4 m/s donde esté, aviso al 20 %", "repostar_s_por_u": "solo posado en el helipuerto",
                    "huella_salida": "‰ de huella para la Colmena por salida (como una obra grande)", "municion_bordo": "‰ de u"}.get(k, "")
            add(f"heli_{n}_{k}", h[k], esc, nota)
        for arma, k in h["armas"].items(): add(f"heli_{n}_arma_{arma}", k, 1)
    add("heli_mvp_recomendado_nh90", 1, 1, "1 = NH90; Lucía decide")
    return out

FUERZA = {"pelotones": list(PELOTONES), "vehiculos": ["dragon"], "helicopteros": [],  # D-N173: Sagunto sin NH90 (los NH90 están en Bétera)
          "_nota": "plantel de partida: 5 pelotones, 1 Dragón y 2 VAMTAC (los VAMTAC los pone AddDefaultVehicles en (88;53) y (80;53); están en vehiculos_tierra.json)"}

# Existencias (Hugo (3), 8-nov, docs/economia/escala-existencias.md). Una sola unidad: u. Reserva de la red (Stock de la estación) y almacén de la zona (tope).
EXISTENCIAS_RED = [
    # id, municion, combustible, materiales, viveres, personas, repone, nota
    ("sagunto", 150, 140, 100, 80, 80, True, "STOCK_INICIAL de sim_economia.py (equilibrado 14,2 %)"),
    ("nules", 0, 0, 0, 0, 0, True, "0 u de munición (Lucía); la guarnición lleva su dotación; víveres solo de su producción; recinto de partida 124,3 u ya construido"),
    ("betera", 50, 70, 0, 0, 0, False, "D-N173: base del aire; no se repone en el MVP; NH90: 1,8 u por rearme y unas 3 u de combustible por salida"),
    ("castellon", 0, 300, 0, 0, 0, True, "hereda el depósito de 300 u de combustible"),
]
TOPE_ZONA = {"municion_u": 47, "combustible_u": 30, "materiales_u": 40}  # Sagunto; las demás usan el mismo hasta tener uno propio

def json_existencias():
    est = []
    for i, m, c, ma, v, per, rep, nota in EXISTENCIAS_RED:
        est.append({"id": i, "reserva": {"municion_u": m, "combustible_u": c, "materiales_u": ma, "viveres_u": v}, "personas": per,
                    "tope_zona": dict(TOPE_ZONA), "se_repone": rep, "nota": nota})
    return {"_nota": "Existencias de partida de la red y topes del almacén de zona (Hugo (3), 8-nov; regla en docs/economia/escala-existencias.md). Generado por unidades.py; no editar a mano. Los id tienen que coincidir con los de RailNet.",
            "unidad": "u", "u_municion_zombis": 400,
            "reglas": {"llenado": ["inicio_partida", "inicio_ataque"],
                       "toma": "min(tope_zona, reserva) por recurso",
                       "fin_ataque": "lo que sobra en la zona vuelve a la reserva; lo gastado se pierde",
                       "durante_ataque": "no se repone de la reserva; la munición que llega en tren entra al almacén aunque pase del tope",
                       "entre_ataques": "el jugador puede reponer a mano desde la reserva hasta el tope",
                       "dotaciones": "la de los pelotones y vehículos (unas 10 u) va con ellos, no con el almacén"},
            "estaciones": est}

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    rows = filas()
    with open(os.path.join(base, "..", "csv", "balance_unidades.csv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("clave;valor;escala;nota\n")
        for k, v, e, n in rows: f.write(f"{k};{v};{e};{n.replace(';', ',')}\n")
    ref = []
    print("arma                  densa 2/m²: bajas/s  bajas/u | suelta 0,3/m²: bajas/s  bajas/u")
    for n in ARMAS:
        a2 = rendimiento(n, 2.0); a03 = rendimiento(n, 0.3)
        print(f"{n:22s} {a2[0]:8.2f} {a2[1]:8.0f}        | {a03[0]:8.2f} {a03[1]:8.0f}")
        ref.append((f"arma_{n}", round(a2[0]*1000), round(a2[1]), round(a03[0]*1000), round(a03[1])))
    print("\npelotón               densa: bajas/s  bajas/u | suelta: bajas/s  bajas/u")
    for n in PELOTONES:
        a2 = peloton(n, 2.0); a03 = peloton(n, 0.3)
        print(f"{n:22s} {a2[0]:8.2f} {a2[1]:8.0f}  | {a03[0]:8.2f} {a03[1]:8.0f}")
        ref.append((f"peloton_{n}", round(a2[0]*1000), round(a2[1]), round(a03[0]*1000), round(a03[1])))
    with open(os.path.join(base, "..", "csv", "referencia_unidades.csv"), "w", encoding="utf-8", newline="\n") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n")
        w.writerow(["unidad", "densa_bajas_mil_s", "densa_bajas_por_u", "suelta_bajas_mil_s", "suelta_bajas_por_u"]); w.writerows(ref)
    # ---------- asedio de referencia: 10.000 zombis contra la guarnición de Sagunto (unos 30 soldados, D-N27) y el Dragón
    print("\nAsedio de 10.000 contra Sagunto (horda densa al muro, 2/m², a 25 m):")
    for nombre, mezcla in [("solo fusileros (4)", {"fusileros": 4}), ("mixta: 2 fus + 1 ame + 1 gra", {"fusileros": 2, "ametralladores": 1, "granaderos": 1}),
                           ("mixta + Dragón", {"fusileros": 2, "ametralladores": 1, "granaderos": 1, "_dragon": 1}),
                           ("los 5 de la noche + Dragón", {"fusileros": 1, "ametralladores": 1, "granaderos": 1, "tiradores": 1, "zapadores": 1, "_dragon": 1}),
                           ("abuso: 4 granaderos + Dragón", {"granaderos": 4, "_dragon": 1})]:
        bs = u_s = sold = 0
        for n, k in mezcla.items():
            if n == "_dragon":
                for arma, c in VEHICULOS["dragon"]["armas"].items():
                    r = rendimiento(arma, 2.0); bs += k*c*r[0]; u_s += k*c*r[0]/r[1]
                continue
            r = peloton(n, 2.0); bs += k*r[0]; u_s += k*r[0]/r[1]; sold += k*PELOTONES[n]["pers"]
        t = 10000 / bs; u = 10000 * u_s / bs
        print(f"  {nombre:30s} {sold:2d} soldados  {bs:5.1f} bajas/s  {t/60:4.1f} min  {u:5.1f} u  ({10000/u:4.0f} zombis/u; economía {Z_POR_U_ECONOMIA})")
    print(f"\n{len(rows)} filas en balance_unidades.csv")

# ======================= LA NOCHE (plan-noche-7nov.md §1): 22:00–06:00 en ~17 min reales =======================
RELOJ_X = 103  # D-N161 (Lucía): CONSTANTE ÚNICA. 24 h de juego = 14 min reales (86400/840 = 102,9 -> 103). Se escribe en noche_sagunto.json (reloj_x) y de ahí la leen la build, NightSim y Transporte (Nacho). No escribir el factor a mano en ningún otro sitio.
NOCHE = dict(reloj_x=RELOJ_X, hora_inicio=22, hora_fin=6, municion_sagunto_u=47, materiales_u=40, combustible_u=30,  # D-N76: los 30 incluyen los depósitos llenos del Dragón (8) y del NH90 (6): en el almacén quedan 16
            escala_oleadas_permil=1000)
# D-N74: 850 por defecto (Lucía: Eugenio juega por primera vez y aprovechará el 50-60 % del fuego). Reservas de Sara: fácil 725 (-15 %), difícil 1000 (+18 %, el «difícil» de Lucía)
DIFICULTAD_NOCHE = {"facil": 853, "normal": 1000, "dificil": 1086}  # SIN AIRE (Hugo (3), 8-nov, D-N169 ampliada + D-N173/174/175): totales 4480/5250/5700 sobre la base 5250; NightSim 1000 semillas sin NH90 y sin rescate de Nules: fácil 100 %, normal 99,9 %, difícil 79,6 % (5800: 64,4 %). Antes, Noche58: D-N165/D-N169 (Hugo (3), 8-nov 13:30): difícil 1115 -> 985 (6400 sobre la base 6500; NightSim calibrado, k=0: 79,4 %; la build es ~11 % más dura en pila, así que se espera en torno al 65 %). Antes: D-N136 final (Hugo, 7-nov 15:15): difícil 1140 -> 1115 para que, con la base 8600, salga ~9590 (= H8410 a 1140, centro del 50-80 % del barrido de Sara con área). Antes: D-N103 (Hugo, 7-nov): 1000 -> 1120 (bot de Sara: 42-45 % de muro) -> 1090 (con 1120 quedaba 9-11 %) -> 1150 (D-N121, 05:10: compensa el muro de 1200000) -> 1140 (Mak: con 1150 el bot daba 13,5-18,3 %) -> 1280 (D-N127, 09:20: NightBot de Sara, mediana de muro 19,6 %, p10 14,8, p90 23,9)
# entradas del nivel (Álvaro/Mak): reparto ‰ por oleada; el puente entra en las dos últimas
ENTRADAS = {"O1": "vía", "O2": "carretera", "O3": "pueblo", "O4": "puente"}
REPARTO = [(500, 300, 200, 0)]  # D-N136c (Hugo, 7-nov 14:15): sin O4 (el puente está al ESTE, X 248-256; sus trepadores no tenían tropa a 30 m y tiraban el tren, Nacho 21ff07d). Mismo reparto que D-N135. Antes D-N136: [(300, 300, 200, 200)]. Antes, D-N135: [(500, 300, 200, 0)] * 4 # primer contacto: sin la O5 ni la O6 (antes + [(400, 300, 200, 100), (300, 300, 200, 200)])
# (hora de juego en minutos desde las 22:00, zombis, segundos REALES de llegada); todas desde el borde oeste
OLEADAS = [(0, 5250, 180)]  # SIN AIRE (Hugo (3), 8-nov): base 6500 -> 5250 con D-N174 (línea de visión + azotea) y D-N175 (horda a ≤25 m de la tropa), sin NH90 en Sagunto (D-N173). Antes: D-N165 (Hugo (3), 8-nov 13:30): base 8600 -> 6500 con la trepada calibrada contra la build (240 ‰/s, tope 55/s) y el muro por tramos: normal 5520 = 100 % (build -nightbot: victoria 04:10, 0 bajas); H7400 95,9 % al borde del precipicio (H8600 2,6 %). Antes: D-N136 FINAL (Hugo, 7-nov 15:15): base 4700 -> 8600 con el daño en área (D-N137) y sin O4; barrido de Sara sobre 9993dc0: normal 100 % y muro p50 87,2 %. Antes D-N136b (Hugo, 7-nov 14:00): la misma horda única, pero entra durante 180 s (con 75 s la pila pasaba de 1400 y trepaban al tren, Sara semillas 1-2). Contacto a los 60-90 s por la marcha; antes D-N136: 75 s. A escala: fácil 3400, normal 4000, difícil 5360. Ajuste con el barrido A-D de Sara (daño al muro ~ 0,021 x (H - 1790)^2 zombi·s). Antes, D-N135: [(20, 900, 30), (130, 1500, 45), (250, 2000, 60), (370, 3000, 70)]

def noche(eficiencia=0.7, escala=1.0):
    """Cola por segundo real: llegan zombis, la fuerza de la noche abate a su caudal efectivo; lo que sobra se apila contra el muro."""
    caudal = 0; u_s = 0
    for n in PELOTONES:
        r = peloton(n, 2.0); caudal += r[0]; u_s += r[0] / r[1]
    for arma, c in VEHICULOS["dragon"]["armas"].items():
        r = rendimiento(arma, 2.0); caudal += c * r[0]; u_s += c * r[0] / r[1]
    for arma, c in HELIS["nh90"]["armas"].items():
        r = rendimiento(arma, 0.3); caudal += c * r[0]; u_s += c * r[0] / r[1]
    z_por_u = caudal / u_s; caudal *= eficiencia
    dur = (24 - NOCHE["hora_inicio"] + NOCHE["hora_fin"]) * 3600 // NOCHE["reloj_x"]
    cola = pico = total = 0; picos = []
    for t in range(dur + 1):
        llega = 0
        for m, z, ds in OLEADAS:
            t0 = m * 60 // NOCHE["reloj_x"]
            if t0 <= t < t0 + ds: llega += z * escala / ds
        total += llega; cola = max(0.0, cola + llega - caudal); pico = max(pico, cola)
        for i, (m, z, ds) in enumerate(OLEADAS):
            if t == m * 60 // NOCHE["reloj_x"] + ds: picos.append(round(cola))
    disp = NOCHE["municion_sagunto_u"] + sum(p["dot"] for p in PELOTONES.values()) / 1000 + VEHICULOS["dragon"]["municion_bordo"] / 1000 + VEHICULOS["vamtac"]["municion_bordo"] / 1000 + HELIS["nh90"]["municion_bordo"] / 1000
    gasto = total / z_por_u / eficiencia ** 0.5        # el que pierde eficiencia también tira más
    return dict(dur_min=dur / 60, total=round(total), caudal=round(caudal, 1), pico=round(pico), picos=picos, gasto=round(gasto, 1), disp=round(disp, 1), z_por_u=round(z_por_u))

if __name__ == "__main__":
    print("\nLA NOCHE (oleadas desde el oeste; pico = zombis apilados contra el muro al acabar cada oleada):")
    for ef in (0.5, 0.7, 0.9):
        r = noche(ef)
        print(f"  eficiencia {ef:.0%}: {r['dur_min']:.1f} min reales, {r['total']} zombis, caudal {r['caudal']}/s, pila al acabar cada oleada {r['picos']}, "
              f"munición {r['gasto']} de {r['disp']} u")
    base = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base, "..", "csv", "balance_noche.csv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("clave;valor;escala;nota\n")
        f.write(f"noche_reloj_x;{NOCHE['reloj_x']};1;D-N161: reloj único, 1 s real = {NOCHE['reloj_x']} s de juego; de 22:00 a 06:00 son {8*3600//NOCHE['reloj_x']} s reales\n")
        f.write(f"noche_hora_inicio;{NOCHE['hora_inicio']};1;\nnoche_hora_fin;{NOCHE['hora_fin']};1;D-N164: se gana al acabar con la horda; el amanecer no da la victoria\n")
        f.write(f"noche_municion_sagunto_u;{NOCHE['municion_sagunto_u']};1;D-N128: 52 -> 47 porque la munición de a bordo de los vehículos sale del almacén (Dragón 2 u, VAMTAC 3 u y NH90 3 u, para unas 3 oleadas en fuego libre); el total de la noche no cambia. Además va la dotación de cada pelotón\n")
        f.write(f"noche_materiales_u;{NOCHE['materiales_u']};1;para sacos y nidos entre oleadas (el muro de partida de 120 u ya está, D-N63)\n")
        f.write(f"noche_escala_oleadas_permil;{NOCHE['escala_oleadas_permil']};1000;D-N74: PALANCA ÚNICA, 850 por defecto (primera partida de Eugenio), fácil {DIFICULTAD_NOCHE['facil']}, difícil {DIFICULTAD_NOCHE['dificil']} (D-N136 final; antes 1140)\n")
        f.write(f"noche_combustible_u;{NOCHE['combustible_u']};1;D-N76: total de la noche, con los depósitos llenos del Dragón (8) y del NH90 (6) incluidos: en el almacén quedan 16\n")
        f.write("noche_estacion_vida;60000;1;D-N99: el edificio de viajeros, con 100 zombis dentro cae en 30 s\n")
        f.write("noche_tren_vida;120000;1;D-N105 (Hugo): el tren blindado en el andén aguanta el doble que el edificio, con 100 zombis pegados cae en 60 s. Sin medir\n")
        f.write("noche_estacion_danio_zombi_s;20;1;por zombi pegado y segundo real\nnoche_tren_danio_zombi_s;20;1;por zombi pegado y segundo real\n")
        f.write("noche_contacto_mm;900;1;Nacho a210bd3, pendiente de la medición de Sara\nnoche_contacto_danio_tick;2;1;soldado de 100 de vida, pendiente de la medición de Sara\n")
        f.write(f"noche_oleadas;{len(OLEADAS)};1;D-N136: una sola horda desde el borde oeste, repartida a lo ancho; entra durante 180 s\n")
        for i, (m, z, ds) in enumerate(OLEADAS, 1):
            h = (22 * 60 + m) % (24 * 60)
            f.write(f"noche_oleada{i}_minuto;{m};1;minutos de juego desde las 22:00 ({h // 60:02d}:{h % 60:02d})\n")
            f.write(f"noche_oleada{i}_zombis;{z};1;\nnoche_oleada{i}_llegada_s;{ds};1;segundos REALES en los que entra la oleada\n")


# D-N128 (Hugo, 7-nov, 09:25; Mak, Eugenio): munición de a bordo para unas 3 oleadas en fuego libre (G = alto el fuego): Dragón 2 u, VAMTAC 1 -> 3 u, NH90 1 -> 3 u; sale del almacén (Sagunto 52 -> 47 u). La recarga no cambia
# ======================= D-N74: JSON de la noche para Marcos y tabla de munición para el HUD =======================
RECARGA_VEH_PERMIL = 600  # D-N135: recargas de los vehículos x0,6 (Sara, 1000 semillas: la normal da ★★ en el 84 % de las noches sin ★★★); recarga_u_mil = coste de una recarga COMPLETA (= ResupplyMilliU de NightVehicles)
def municion_hud():
    filas = []
    def fila(nombre, armas, dot_mil, recarga_s, donde, coste_recarga_permil=1000):
        u_s = sum(k * (TICKS / ARMAS[a]["cad"]) * ARMAS[a]["coste"] / DISP_POR_U for a, k in armas.items())
        disparos = {a: int(dot_mil / 1000 * DISP_POR_U / ARMAS[a]["coste"] * (k * TICKS / ARMAS[a]["cad"] * ARMAS[a]["coste"] / DISP_POR_U) / u_s) for a, k in armas.items()}
        filas.append(dict(unidad=nombre, dotacion_mil_u=dot_mil, fuego_continuo_s=int(dot_mil / 1000 / u_s), recarga_s=recarga_s, recarga_u_mil=dot_mil * coste_recarga_permil // 1000, donde=donde, disparos=disparos))
    for n, p in PELOTONES.items(): fila(n, p["armas"], p["dot"], 10, "junto al tren o al depósito de la estación")
    fila("dragon", VEHICULOS["dragon"]["armas"], VEHICULOS["dragon"]["municion_bordo"], 20, "junto al tren o al depósito", RECARGA_VEH_PERMIL)
    fila("vamtac", VEHICULOS["vamtac"]["armas"], VEHICULOS["vamtac"]["municion_bordo"], 20, "junto al tren o al depósito", RECARGA_VEH_PERMIL)
    fila("nh90", HELIS["nh90"]["armas"], HELIS["nh90"]["municion_bordo"], 30, "posado en el helipuerto (también repone 4 u de combustible)", RECARGA_VEH_PERMIL)
    return filas

def combustible():
    d, h = VEHICULOS["dragon"], HELIS["nh90"]; dur_min = (8 * 3600 // NOCHE["reloj_x"]) / 60
    g = lambda e4s, frac: e4s * 60 / 10000 * dur_min * frac
    siempre = g(d["comb_marcha_e4_s"], 1) + g(h["comb_vuelo_e4_s"], 1)
    racion = g(d["comb_marcha_e4_s"], 0.4) + g(d["comb_ralenti_e4_s"], 0.3) + h["comb_vuelo_e4_s"] * 60 / 10000 * 10 + h["comb_suelo_e4_s"] * 60 / 10000 * 2
    return {"_nota": "D-N76 (Hugo). Consumo en E4 de u (1 u = 10.000) por segundo REAL; se cobra cada 30 ticks. Los 30 u de la noche incluyen los depósitos llenos.",
            "total_noche_u": NOCHE["combustible_u"], "almacen_inicial_u": NOCHE["combustible_u"] - d["deposito_u"] - (h["deposito_u"] if "nh90" in FUERZA["helicopteros"] else 0),
            "dragon": {"deposito_u": d["deposito_u"], "marcha_e4_s": d["comb_marcha_e4_s"], "ralenti_e4_s": d["comb_ralenti_e4_s"], "apagado_e4_s": 0,
                       "repostar_s_por_u": d["repostar_s_por_u"], "repostar_donde": "junto al depósito de la estación o al tren, del almacén de Sagunto",
                       "bidon_zapador_u": 2, "bidon_zapador_s": 20,
                       "a_cero": "queda inmóvil; la torre y la coaxial siguen disparando con la batería; lo rescata un zapador con un bidón de 2 u (20 s) o se repone junto al tren",
                       "aviso_permil": 200},
            "nh90": {"deposito_u": h["deposito_u"], "vuelo_e4_s": h["comb_vuelo_e4_s"], "suelo_rotor_e4_s": h["comb_suelo_e4_s"], "apagado_e4_s": 0,
                     "repostar_s_por_u": h["repostar_s_por_u"], "repostar_donde": "solo posado en el helipuerto",
                     "a_cero": "baja en autorrotación a 4 m/s donde esté y queda posado; por debajo de 3 m la horda puede alcanzarlo",
                     "aviso_permil": 200},
            "comprobacion": {"siempre_en_marcha_u": round(siempre, 1), "racionado_u": round(racion, 1),
                             "racionado_es": "el Dragón en marcha el 40 % de la noche y al ralentí el 30 %; el NH90, 10 min de vuelo en 4 salidas y 2 min posado con los rotores girando"}}

def resultados():
    soldados = sum(p["pers"] for p in PELOTONES.values())
    return {"_nota": "D-N77 (Hugo). Pantalla al acabar la noche, con victoria o con derrota. Todo sale de contadores que ya existen (ZoneAmmo) o que añade D-N76 (combustible).",
            "soldados_iniciales": soldados,
            "estadisticas": [
              {"id": "abatidos", "texto": "Zombis abatidos", "formato": "{abatidos} de {llegados}",
               "calculo": "abatidos = suma de ZoneAmmo.Kills; llegados = zombis generados en la noche hasta el final (13.090 en normal si se llega a las 06:00)"},
              {"id": "bajas", "texto": "Bajas propias", "formato": "{bajas} de {soldados} soldados{vehiculos}",
               "calculo": "bajas = suma de ZoneAmmo.SoldiersLost; vehiculos = ' · Dragón perdido' y/o ' · NH90 perdido' si su vida llegó a 0"},
              {"id": "municion", "texto": "Munición gastada", "formato": "{gastada} u · {zpu} zombis por u",
               "calculo": "gastada = ZoneAmmo.ShotsFired / 2000 (una cifra decimal); zpu = Kills * 2000 / ShotsFired (entero; la referencia de la economía es 400)"},
              {"id": "municion_restante", "texto": "Munición restante", "formato": "{restante} u",
               "calculo": "restante = almacén de Sagunto + dotaciones de los pelotones vivos + munición a bordo del Dragón y del NH90, en u con una cifra decimal"},
              {"id": "combustible", "texto": "Combustible gastado", "formato": "{gastado} de {total} u",
               "calculo": "gastado = suma de lo cobrado por D-N76 (E4 / 10000); total = 30"},
              {"id": "hora", "texto": "Fin de la noche", "formato_victoria": "Amanecer, 06:00", "formato_derrota": "Cayó a las {hh:mm}, en la oleada {n}",
               "calculo": "hora del reloj de la noche en el tick en que se cumplió la derrota; n = última oleada que había empezado a entrar"}],
            "_nota_estrellas": "D-N149 (Lucía, 7-nov): sin estrellas; quitados resultados.nota y resultados.estrellas (D-N104). Los criterios de calibración son internos.",
            "textos": {"victoria": "Sagunto resiste", "derrota": "Sagunto ha caído", "boton_repetir": "Repetir la noche", "boton_menu": "Menú principal"}}

def json_noche(escala_mil):
    oleadas = []
    for i, ((m, z, ds), rep) in enumerate(zip(OLEADAS, REPARTO), 1):
        tot = int(round(z * escala_mil / 1000 / 10) * 10)
        por = {e: tot * r // 1000 for e, r in zip(ENTRADAS, rep)}
        por["O1"] += tot - sum(por.values())
        h = (22 * 60 + m) % (24 * 60)
        oleadas.append({"n": i, "hora": f"{h // 60:02d}:{h % 60:02d}", "minuto_juego": m, "llegada_s_reales": ds, "total": tot, "por_entrada": por})
    return oleadas

if __name__ == "__main__":
    import json
    base = os.path.dirname(os.path.abspath(__file__)); jd = os.path.join(base, "..", "json"); os.makedirs(jd, exist_ok=True)
    doc = {"_nota": "D-N74 (Hugo): la noche de Sagunto. Generado por docs/economia/unidades/unidades.py; no editar a mano. Las cifras de unidades están en csv/balance_unidades.csv.",
           "reloj_x": NOCHE["reloj_x"], "hora_inicio": "22:00", "hora_fin": "06:00", "duracion_s_reales": (8 * 3600) // NOCHE["reloj_x"],
           "victoria": "acabar con la horda con el edificio de viajeros y el tren en pie (D-N164: el amanecer ya no da la victoria)", "derrota": "la horda destruye el edificio de viajeros o la locomotora",
           "entradas": ENTRADAS, "dificultad_por_defecto": "normal", "escala_oleadas_permil": DIFICULTAD_NOCHE,
           "recursos_iniciales": {"municion_u": NOCHE["municion_sagunto_u"], "materiales_u": NOCHE["materiales_u"], "combustible_u": NOCHE["combustible_u"],
                                   "nota": "TOPES del almacén de zona de Sagunto; se llenan con min(tope, reserva) al empezar la partida y cada ataque (ver existencias_red.json). Aparte, los pelotones y vehículos llevan su dotación (unas 10 u en total). El muro de partida (D-N63) y el pretil de la azotea ya están construidos"},
           "fuerza": FUERZA,
           "oleadas": {d: json_noche(v) for d, v in DIFICULTAD_NOCHE.items()},
           "municion_hud": municion_hud(),
           "combustible": combustible(),
           "resultados": resultados()}
    with open(os.path.join(jd, "noche_sagunto.json"), "w", encoding="utf-8", newline="\n") as f: json.dump(doc, f, ensure_ascii=False, indent=2)
    with open(os.path.join(jd, "existencias_red.json"), "w", encoding="utf-8", newline="\n") as f: json.dump(json_existencias(), f, ensure_ascii=False, indent=2)
    with open(os.path.join(base, "..", "csv", "hud_municion.csv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("unidad;dotacion_permil_u;fuego_continuo_s;recarga_s;recarga_permil_u;donde\n")
        for r in municion_hud(): f.write(f"{r['unidad']};{r['dotacion_mil_u']};{r['fuego_continuo_s']};{r['recarga_s']};{r['recarga_u_mil']};{r['donde']}\n")
    print("\nMUNICIÓN (HUD):")
    for r in municion_hud(): print(f"  {r['unidad']:15s} dotación {r['dotacion_mil_u']/1000:4.1f} u, {r['fuego_continuo_s']:4d} s de fuego continuo, recarga {r['recarga_s']} s; {r['disparos']}")
    c = combustible(); print(f"\nCOMBUSTIBLE: siempre en marcha {c['comprobacion']['siempre_en_marcha_u']} u, racionado {c['comprobacion']['racionado_u']} u, hay {c['total_noche_u']} u")
    print("\nNOCHE por dificultad (eficiencia 50/60/70 %):")
    for d, v in DIFICULTAD_NOCHE.items():
        for ef in (0.5, 0.6, 0.7):
            r = noche(ef, v / 1000); print(f"  {d:8s} {ef:.0%}: pila final {r['picos'][-1]:5d}, munición {r['gasto']} de {r['disp']} u, {r['total']} zombis")

# ======================= D-N101 (Hugo, 7-nov): vehículos de tierra, coste, vida, velocidad y ETA =======================
# Puntos del nivel 1 de Álvaro (sagunto-nivel.md §9, E5/E6): x, z en m. Rutas por calles y por el recinto (D-N96: nada de campo a través).
PUNTOS = {"parque": (99, 53), "puerta_vehiculos": (99, 44), "tren": (114, 64.5), "estacion": (113, 78), "helipuerto": (180, 44), "paso_nivel": (59, 62)}
RUTAS_ZONA = {  # metros de recorrido por calle, medidos a mano sobre el plano (tramos rectos)
    "parque -> tren (andén)": 20, "parque -> estación (edificio)": 40, "parque -> helipuerto (puerta sur y carretera)": 95,
    "parque -> paso a nivel (puerta sur, carretera vieja y calle de la Estación)": 110, "estación -> tren (andén)": 15, "estación -> helipuerto": 120, "tren -> helipuerto": 115, "estación -> paso a nivel": 130}
# Puntos de la red: km por carretera y por vía desde Sagunto (sim_economia.NODOS; la carretera es un 10 % más larga que la vía, estimación)
RED = {"Castellón": 40, "Valencia": 30, "Segorbe": 35, "Teruel": 130}

def _eta_zona(d_m, v):
    vmax, a = v["vel_mm_s"] / 1000, v["acel_mm_s2"] / 1000; fren = 2 * a          # frenada: el doble que la aceleración (Vehiculos.cs: 8000/3800, 6000/2500)
    d_acc = vmax ** 2 / (2 * a) + vmax ** 2 / (2 * fren)
    t = (2 * d_m / (1 / a + 1 / fren)) ** 0.5 * (1 / a + 1 / fren) if d_m < d_acc else vmax / a + vmax / fren + (d_m - d_acc) / vmax
    return 2 + t                                                                        # 2 s de arrancar y dar la orden

def vehiculos_tierra():
    out = {"_nota": "D-N101 (Hugo). Vehículos de tierra para Marcos y Nacho. Fuente: VEHICULOS de unidades.py (también en balance_unidades.csv). "
                    "Vida contra 2 de daño por tick y zombi en contacto (el soldado tiene 4000 desde D-N107); armadura = ‰ que se ignora. "
                    "Combustible en E4 de u por segundo REAL (D-N76), también en el mapa. Coste de taller y reparación SIN MEDIR en sim_economia.",
           "reglas": {"vida_efectiva": "vida x 1000 / (1000 - armadura)", "si_Vehiculos_cs_no_tiene_armadura": "Hp = vida efectiva / 100 (VAMTAC 400, Dragón 4000, Pizarro 7143)",
                      "reloj_mapa": f"D-N161: 1 s real = {RELOJ_X} s de juego; ETA real = km / km_h x 3600 / reloj_x (el de noche_sagunto.json)",
                      "rutas": "D-N96: solo por carretera habilitada o por la caja de la vía; nunca campo a través"},
           "vehiculos": {}, "eta_zona_s_reales": {}, "eta_red": {}}
    for n, v in VEHICULOS.items():
        per = 2 * (8 if n == "dragon" else 4.9 if n == "vamtac" else 6.8) + 2 * (3 if n == "dragon" else 2.2 if n == "vamtac" else 3.2)
        pegados = round(per / 0.6); dps = pegados * 60 * (1000 - v["armadura"]) / 1000
        armas = {a: {"cantidad": k, "zombis_por_u_horda": round(rendimiento(a, 2.0)[1]), "zombis_por_u_sueltos": round(rendimiento(a, 0.3)[1])} for a, k in v["armas"].items()}
        out["vehiculos"][n] = {
            "ref": v["ref"], "papel": v["nota"], "vida": v["vida"], "armadura_permil": v["armadura"], "vida_efectiva": round(v["vida"] * 1000 / (1000 - v["armadura"])),
            "aguante_rodeado_s": round(v["vida"] / dps), "aguante_rodeado_nota": f"{pegados} zombis pegados alrededor",
            "bloqueo_pila": v["bloqueo_pila"], "plazas": v["plazas"], "armas": armas, "municion_bordo_permil_u": v["municion_bordo"], "recarga_s": 20,
            "combustible": {"deposito_u": v["deposito_u"], "marcha_e4_s": v["comb_marcha_e4_s"], "ralenti_e4_s": v["comb_ralenti_e4_s"], "repostar_s_por_u": v["repostar_s_por_u"],
                            "autonomia_marcha_s_reales": v["deposito_u"] * 10000 // v["comb_marcha_e4_s"]},
            "velocidad": {"zona_mm_s": v["vel_mm_s"], "zona_horda_mm_s": v["vel_horda_mm_s"], "acel_mm_s2": v["acel_mm_s2"], "carretera_kmh": v["vel_carretera_kmh"], "via_kmh": v["vel_via_kmh"]},
            "taller": {"materiales_u": v["coste_mat"], "combustible_u": v["coste_comb"], "dias": v["taller_dias"], "reparar_u_por_1000_vida": v["reparar_u_por_1000_vida"]}}
    for r, d in RUTAS_ZONA.items():
        out["eta_zona_s_reales"][r] = {"m": d, **{n: round(_eta_zona(d, v)) for n, v in VEHICULOS.items()}}
    for dest, km in RED.items():
        fila = {"km_via": km, "km_carretera": round(km * 1.1)}
        for n, v in VEHICULOS.items():
            for modo, kmr, vel in (("carretera", km * 1.1, v["vel_carretera_kmh"]), ("via", km, v["vel_via_kmh"])):
                s_real = kmr / vel * 3600 / 28
                fila[f"{n}_{modo}"] = {"juego_min": round(kmr / vel * 60), "real_s": round(s_real), "combustible_u": round(s_real * v["comb_marcha_e4_s"] / 10000, 1)}
        out["eta_red"][f"Sagunto -> {dest}"] = fila
    out["lectura"] = ["En la zona, de pedir a llegar pasan de 5 a 15 s reales: cualquier vehículo llega al tren o a la estación antes de que acabe de entrar una oleada.",
                      "En el mapa, la carretera es 2-3 veces más rápida que la vía; la vía queda para cuando la carretera está cortada.",
                      "El Pizarro no llega a Teruel con un depósito ni por carretera: de lejos se lleva en el tren (plataforma, regla pendiente de Lucía)."]
    return out

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "json", "vehiculos_tierra.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(vehiculos_tierra(), f, ensure_ascii=False, indent=2)
