# Borrador de la noche de Nules (Hugo (3), 8-nov). Mismo esquema que noche_sagunto.json, el único que lee FromJson (Nacho).
# SIN MEDIR: es el punto de partida para que Nacho lo mida en NightSim con la geometría de Nules.
import json, os
RELOJ_X = 103
DIFICULTAD = {"facil": 853, "normal": 1000, "dificil": 1086}       # las mismas palancas que Sagunto sin aire
BASE = 2400                                                        # normal; ver LEEME §2
LLEGADA_S = 180
ENTRADAS = {"O1": {"nombre": "Na", "lado": "O", "desde": "vía desde Almenara (oeste)"},
            "O2": {"nombre": "Nb", "lado": "E", "desde": "vía desde Castellón (este, infestada); la que más presiona"},
            "O3": {"nombre": "Nc", "lado": "N", "desde": "pueblo, por las calles; corta distancia y sin línea de visión, choca con el edificio"},
            "O4": {"nombre": "Nd", "lado": "S", "desde": "calle del polígono desde el paso inferior (este), contra la puerta de vehículos"}}
REPARTO = {"O1": 250, "O2": 400, "O3": 200, "O4": 150}            # ‰
def oleadas(permil):
    tot = int(round(BASE * permil / 1000 / 10) * 10)
    por = {k: tot * r // 1000 for k, r in REPARTO.items()}; por["O2"] += tot - sum(por.values())
    return [{"n": 1, "hora": "22:00", "minuto_juego": 0, "llegada_s_reales": LLEGADA_S, "total": tot, "por_entrada": por}]
doc = {"_nota": "Hugo (3), 8-nov: la noche de Nules, BORRADOR SIN MEDIR. Mismo esquema que noche_sagunto.json. Generado por docs/economia/entregas/nules-noche/generar_nules.py; geometría en docs/niveles/estaciones/nules.json (Álvaro). No hay asedio la 1.ª noche (D-N, 8-nov 15:40): esta noche es del día 2 en adelante.",
       "reloj_x": RELOJ_X, "hora_inicio": "22:00", "hora_fin": "06:00", "duracion_s_reales": 8 * 3600 // RELOJ_X,
       "victoria": "acabar con la horda con el edificio de viajeros en pie (D-N164: el amanecer no da la victoria)",
       "derrota": "la horda destruye el edificio de viajeros (el tren puede no estar: si está, su pérdida también es derrota)",
       "entradas": ENTRADAS, "dificultad_por_defecto": "normal", "escala_oleadas_permil": DIFICULTAD,
       "recursos_iniciales": {"municion_u": 20, "materiales_u": 20, "combustible_u": 0,
                              "nota": "CASO DE REFERENCIA: el objetivo «Lleva munición a Nules» tras la 1.ª noche se cumple al descargar 20 u o más (Lucía, 8-nov); materiales 20 u, supuesto mío. La reserva de Nules empieza con 0 u de munición (existencias_red.json); el almacén toma min(tope 47/30/40, reserva). Recinto de partida 124,3 u ya construido (82,3 de muro + 42 de puertas, Iker)."},
       "fuerza": {"pelotones": ["fusileros", "ametralladores"], "vehiculos": [], "helicopteros": [],
                  "_nota": "guarnición = 12 personas (sim_economia.py, guarnicion 12): fusileros (8) + ametralladores (4). Caso B: + 1 pelotón de fusileros que lleve el jugador en ese tren."},
       "oleadas": {d: oleadas(v) for d, v in DIFICULTAD.items()}}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nules.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
print({d: v[0]["total"] for d, v in doc["oleadas"].items()}, doc["oleadas"]["normal"][0]["por_entrada"])
