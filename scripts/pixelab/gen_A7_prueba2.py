"""Prueba de 4 texturas de A7 con el prefijo D-N50/Iris (sin rust, red, orange ni negaciones). Uso: python gen_A7_prueba2.py > trabajos_A7_prueba2.jsonl"""
import json
PREFIJO = ("flat seamless tileable pixel art texture, repeating pattern, front view, even lighting, muted earth tones, olive green, "
           "concrete grey, dusty beige, weathered surface")
TEX = {"chapa_ondulada": ("corrugated metal sheet", 7401), "hormigon": ("concrete", 7501), "balasto": ("railway ballast gravel", 7601), "teja_arabe": ("arab clay roof tiles", 7701)}
for n, (d, seed) in TEX.items():
    print(json.dumps({"bloque": "A7b_texturas", "nombre": n, "variante": "v1", "tool": "create_image_pixen", "coste": 1, "seed": seed, "sin_paleta": True,
                      "args": {"description": "%s, %s" % (PREFIJO, d), "width": 32, "height": 32, "no_background": False, "seed": seed}}, ensure_ascii=False))
