# Modelo del bucle del Hito 1 (Hugo, Economía, 11-11). Todo en enteros, como pide el lockstep (D-N206).
# Pregunta: sin la línea, ¿el pelotón se queda seco a mitad del caserío? Con la línea, ¿termina?
# Uso: python3 -I modelo_hito1.py [k_milesimas] [semillas]
import random, sys, statistics

P = {
    "zombis_caserio": 100,          # D-N207
    "k_mil": 5000,                  # cartuchos por zombi abatido x1000 (SIN VERIFICAR: lo mide Nacho en NightSim con el pelotón con munición)
    "soldados": 8,
    "cartuchos_soldado": 30,        # 1 cargador; propuesta = 0,5 x zombis x k / soldados, redondeado al cargador
    "caja": 120,                    # cartuchos por caja (4 cargadores)
    "b_inicial_cajas": 1,           # munición de partida en B
    "a_inicial_cajas": 20,          # munición de partida en A (no hay producción en el Hito 1)
    "plazas_tren": 6,               # 2 vagones x 3 plazas; una plaza = 1 caja de munición o 1 palé de material
    "linea_cajas_viaje": 4,         # orden por defecto de la línea A -> B
    "via_ab_m": 1250,               # Álvaro 11-11: 1234 m en recta + entradas (posiciones_hito1.csv)
    "b_caserio_m": 200,             # Álvaro, terreno v2: 213 m de B al centro; se usa 200
    "tren_mm_s": 11111,             # 40 km/h
    "paso_mm_s": 1400,              # soldado andando
    "carga_s_plaza": 15,            # carga o descarga, por plaza
    "fuego_mil_s": 250,             # cartuchos por segundo y soldado en combate x1000 (15 por minuto)
    "t_linea_creada_s": 120,        # el jugador traza la vía y crea la línea en ~2 min
    "palés_caserio": 4,             # material de vía que deja el caserío limpio
}

def disparos_hasta_abatir(rng, k_mil):
    # cada disparo abate con probabilidad 1/k (geométrica, media k)
    n = 1
    while rng.randrange(k_mil) >= 1000: n += 1
    return n

def combate(rng, cartuchos, quedan, k_mil):
    """Devuelve (abatidos, cartuchos que sobran). Se dispara hasta vaciar o hasta que no quede ninguno."""
    ab = 0
    falta = 0  # disparos que lleva el zombi actual
    while quedan > 0 and cartuchos > 0:
        if falta == 0: falta = disparos_hasta_abatir(rng, k_mil)
        cartuchos -= 1; falta -= 1
        if falta == 0: ab += 1; quedan -= 1
    return ab, cartuchos

def partida(semilla, con_linea, P=P):
    rng = random.Random(semilla)
    Z, k = P["zombis_caserio"], P["k_mil"]
    dot = P["soldados"] * P["cartuchos_soldado"]
    b = P["b_inicial_cajas"] * P["caja"]
    t = 0
    andar = P["b_caserio_m"] * 1000 // P["paso_mm_s"]
    cadencia = P["soldados"] * P["fuego_mil_s"]  # x1000 cartuchos/s del pelotón
    # llegada del primer tren a B (cartuchos disponibles en B desde ese segundo)
    viaje = P["via_ab_m"] * 1000 // P["tren_mm_s"]
    n = P["linea_cajas_viaje"]
    t_tren = P["t_linea_creada_s"] + n * P["carga_s_plaza"] + viaje + n * P["carga_s_plaza"]
    ciclo = 2 * viaje + 2 * n * P["carga_s_plaza"] + 2 * (P["plazas_tren"] - n) * P["carga_s_plaza"]
    quedan = Z; abatidos = 0; secos = []; idas = 0
    t += andar  # el pelotón sale de B hacia el caserío al empezar
    while quedan > 0 and idas < 6:
        idas += 1
        ab, sobra = combate(rng, dot, quedan, k)
        t += (dot - sobra) * 1000 // cadencia
        quedan -= ab; abatidos += ab
        if quedan == 0: break
        secos.append(abatidos)
        t += andar  # vuelve a B a rearmarse
        if con_linea:
            while t >= t_tren and P["a_inicial_cajas"] * P["caja"] > 0:
                b += n * P["caja"]; t_tren += ciclo
        if b <= 0: break
        dot = min(b, P["soldados"] * P["cartuchos_soldado"]); b -= dot
        t += andar
    return {"limpio": quedan == 0, "abatidos": abatidos, "primer_seco": secos[0] if secos else Z, "t_fin_s": t}

def resumen(con_linea, semillas, P=P):
    rs = [partida(s, con_linea, P) for s in range(semillas)]
    ab = sorted(r["abatidos"] for r in rs); ps = sorted(r["primer_seco"] for r in rs)
    q = lambda v, f: v[int(f * (len(v) - 1))]
    tf = sorted(r["t_fin_s"] for r in rs if r["limpio"])
    return {"limpio_%": round(100 * sum(r["limpio"] for r in rs) / semillas, 1),
            "primer_seco_p10/p50/p90": (q(ps, .1), q(ps, .5), q(ps, .9)),
            "abatidos_p10/p50/p90": (q(ab, .1), q(ab, .5), q(ab, .9)),
            "t_fin_p50_min": round(statistics.median(tf) / 60, 1) if tf else None}

if __name__ == "__main__":
    if len(sys.argv) > 1: P["k_mil"] = int(sys.argv[1])
    sem = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    print("k =", P["k_mil"] / 1000, "cartuchos por zombi;", sem, "semillas")
    print("sin línea:", resumen(False, sem))
    print("con línea:", resumen(True, sem))
