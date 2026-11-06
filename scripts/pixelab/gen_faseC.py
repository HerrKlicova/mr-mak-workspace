"""Fase C de Pixelab: retratos de la demo (docs/arte/encargo-fase-c.md, D-N50: prompts solo en positivo).
Uso:  python gen_faseC.py prueba > trabajos_C_prueba.jsonl      (4 imágenes: Reig y Mora, 2 variantes cada uno)
      python gen_faseC.py completa > trabajos_C.jsonl            (8 personajes: 8 normal + 4 herido + 4 agotado)
"""
import json
import sys

PREFIJO = ("pixel art portrait, head and shoulders bust of one person, muted desaturated palette, olive drab, concrete grey, "
           "high contrast, plain transparent background, face filling the image, three-quarter view looking slightly to one side, "
           "face brightly lit from upper left, plain olive uniform with simple shoulder straps")   # D-N56 (Lucía): sin rust; cara iluminada; uniforme liso
PERSONAJES = {  # nombre: (semilla base, descripción)
    "comandante_reig": (9100, "woman in her fifties, Valencian, dry and practical commander, short grey-streaked hair, weathered face, field cap, worn olive uniform, bone-coloured rank stripes, headset"),
    "teniente_bolea": (9200, "man in his thirties, Aragonese, stubborn lieutenant, square jaw, stubble, helmet pushed back, dusty olive jacket"),
    "sargento_ouali": (9300, "woman in her thirties, North African descent, infantry sergeant, hard calm gaze, tied-back dark hair, scar on cheek, combat helmet"),
    "chispas_ferrer": (9400, "man in his sixties, veteran train driver, grey moustache, oil-stained face, flat cap, goggles on forehead, work overalls"),
    "doctora_calvo": (9500, "woman in her forties, doctor, tired kind eyes, hair in a bun, surgical mask pulled down, stained white coat over olive jacket"),
    "pau_llorens": (9600, "man in his forties, railway track engineer, beard, hard hat, hi-vis vest worn grey, rolled-up plans under arm"),
    "nerea_ibarra": (9700, "young woman in her twenties, scout with drone controller, short messy hair, sharp alert expression, goggles, light jacket"),
    "julian_mora": (9800, "man in his fifties, radio and intelligence officer, thin, glasses, large headphones around neck, anxious focus, rumpled shirt"),
}
ESTADOS = {"normal": ("", 8), "herido": (", bandaged forehead, dirty cheek, pained expression", 4), "agotado": (", dark circles under the eyes, slumped shoulders, sweaty face, dull gaze", 4)}


def job(nombre, estado, v, seed, desc, extra):
    return {"bloque": "C_retratos2", "nombre": "%s_%s" % (nombre, estado), "variante": "v%d" % v, "tool": "create_image_pixen", "coste": 1,
            "seed": seed, "sin_paleta": True,
            "args": {"description": "%s, %s%s" % (PREFIJO, desc, extra), "width": 64, "height": 64, "no_background": True, "seed": seed}}


def main():
    modo = sys.argv[1]
    if modo == "prueba":
        for n in ("comandante_reig", "julian_mora"):
            base, d = PERSONAJES[n]
            for v in (1, 2):
                print(json.dumps(job(n, "normal", v, base + v, d, ""), ensure_ascii=False))
    else:
        for n, (base, d) in PERSONAJES.items():
            for est, (extra, k) in ESTADOS.items():
                off = {"normal": 0, "herido": 20, "agotado": 40}[est]
                for v in range(1, k + 1):
                    seed = base + 1 + (v - 1) if (est != "normal" and n in ("comandante_reig", "julian_mora")) else base + off + v   # parten de la semilla de su v1
                    print(json.dumps(job(n, est, v, seed, d, extra), ensure_ascii=False))


main()
