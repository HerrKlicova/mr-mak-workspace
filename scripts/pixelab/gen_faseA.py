"""Trabajos de la fase A de Pixelab (docs/arte/encargo-fase-a.md, aprobada por Eugenio el 6-nov).
Uso:  python gen_faseA.py A1 > trabajos_A1.jsonl     (bloques A1 a A7; A8 es una prueba aparte)
Herramienta: create_image_pixen (1 generación por imagen). Nunca create_ui_asset ni create_image_pro.
Semilla fija por familia (base) + variante (1..8), y 8 variantes que cambian solo la semilla.
"""
import json
import sys

PREFIJO = ("pixel art, muted desaturated palette, rust, olive drab, concrete grey, high contrast silhouettes, clean flat shapes, "
           "transparent background")      # D-N48 (Iris): nada de negaciones («no skull» dibuja calaveras) y sin «dried blood red» ni «gritty»
PREFIJO_UNIDADES = PREFIJO
SUF_ICONO = "single centered game icon, bold readable silhouette, 1px dark outline, flat, no gradient"
SUF_MAPA = "old military staff map symbol, railway map symbology, flat, top-down"

A1 = {"municion": "ammunition crate with bullets", "combustible": "fuel jerrycan",
      "materiales": "stack of steel beams and planks", "viveres": "food ration box and water canteen",
      "poblacion": "group of three civilian survivors silhouettes"}
A2 = {"ataque": "warning sign with zombie hand, attack alert", "via_cortada": "broken railway track, cut line alert",
      "tren_detenido": "stopped locomotive with stop symbol", "sin_municion": "empty ammunition crate with red cross mark",
      "sin_combustible": "empty jerrycan with red cross mark", "asedio": "fortified wall surrounded by horde, siege alert"}
A3 = {"aguantar": "raised fist shield, hold position order", "seguir": "arrow along railway, proceed order",
      "retirarse": "arrow turning back, retreat order", "desplegar": "soldiers stepping off train car, deploy order",
      "embarcar": "soldiers boarding train car, embark order", "escoltar": "shield beside locomotive, escort order"}
A4 = {"segura": "safe, calm", "amenazada": "threatened, warning", "asediada": "under siege, enemies around", "perdida": "lost, ruined"}
A5 = {"movimiento": "moving", "parado": "stopped", "bajo_ataque": "under attack", "obras": "work train with crane"}
A6 = {"fusileros": "rifle infantry squad", "ametralladora": "heavy machine gun team",
      "blindado_8x8": "8x8 armored personnel carrier", "tren_blindado": "armored combat train",
      "artilleria_ferroviaria": "railway artillery wagon with howitzer turret"}
A7 = {"ladrillo": "brick wall", "ladrillo_grietas": "cracked brick wall", "chapa_oxidada": "rusty metal sheet",
      "chapa_ondulada": "corrugated metal sheet", "hormigon": "concrete", "hormigon_manchado": "stained concrete",
      "balasto": "railway ballast gravel", "traviesas": "railway sleepers on ballast", "teja_arabe": "arab clay roof tiles",
      "tierra_seca": "dry cracked earth", "hierba_seca": "dry grass", "asfalto_roto": "broken asphalt",
      "madera_vagon": "wooden wagon planks", "pintura_oliva": "chipped olive drab military paint",
      "sacos_terreros": "sandbags", "hesco": "HESCO gabion wall", "gravilla": "fine gravel", "barro": "mud",
      "nieve_sucia": "dirty snow", "oxido_remaches": "rust with rivets"}


def trabajo(bloque, nombre, var, desc, w, h, seed, fondo):
    return {"bloque": bloque, "nombre": nombre, "variante": var, "tool": "create_image_pixen", "coste": 1, "seed": seed,
            "sin_paleta": True,
            "args": {"description": desc, "width": w, "height": h, "no_background": fondo,
                     "outline": "single color black outline" if fondo else None, "seed": seed}}


def main():
    b = sys.argv[1]
    base = {"A1": 1000, "A2": 2000, "A3": 3000, "A4": 4000, "A5": 5000, "A6": 6000, "A7": 7000}[b]
    out = []
    if b in ("A1", "A2", "A3"):
        tabla = {"A1": A1, "A2": A2, "A3": A3}[b]
        for i, (n, d) in enumerate(tabla.items()):
            for size in (16, 32):
                for v in range(1, 9):
                    out.append(trabajo(b + "_" + {"A1": "cargas", "A2": "alertas", "A3": "ordenes"}[b], "%s_%d" % (n, size), "v%d" % v,
                                       "%s, %s, %s" % (PREFIJO, d, SUF_ICONO), size, size, base + i * 100 + size + v, True))
    elif b == "A4":
        for i, (n, d) in enumerate(A4.items()):
            for v in range(1, 9):
                out.append(trabajo("A4_estaciones", n, "v%d" % v,
                                   "%s, railway station symbol, circle with platform mark, %s, grayscale shades only, %s" % (PREFIJO, d, SUF_MAPA), 32, 32, base + i * 100 + v, True))
    elif b == "A5":
        for i, (n, d) in enumerate(A5.items()):
            for v in range(1, 9):
                out.append(trabajo("A5_trenes", n, "v%d" % v,
                                   "%s, armored train map marker, %s, grayscale shades only, %s" % (PREFIJO, d, SUF_MAPA), 32, 32, base + i * 100 + v, True))
    elif b == "A6":
        for i, (n, d) in enumerate(A6.items()):
            for v in range(1, 9):
                out.append(trabajo("A6_unidades", n, "v%d" % v, "%s, %s, %s" % (PREFIJO_UNIDADES, d, SUF_ICONO), 32, 32, base + i * 100 + v, True))
    elif b == "A7":
        for i, (n, d) in enumerate(A7.items()):
            for v in range(1, 4):
                out.append(trabajo("A7_texturas", n, "v%d" % v,
                                   "pixel art, muted desaturated palette, rust, olive drab, concrete grey, "
                                   "seamless tileable texture, %s, flat top-down surface" % d, 32, 32, base + i * 100 + v, False))
    for j in out:
        j["args"] = {k: v for k, v in j["args"].items() if v is not None}
        print(json.dumps(j, ensure_ascii=False))


main()
