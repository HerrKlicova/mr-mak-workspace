"""Genera los archivos de trabajos de los bloques del lote v1.3 (excepto iconos y VFX).
Uso: python gen_bloques.py <bloque> > trabajos_<bloque>.jsonl     bloques: mapa retratos decals eventos ui
"""
import json
import sys

ESTILO = ("pixel art, gritty post-apocalyptic military, muted desaturated palette, rust, olive drab, "
          "concrete grey, dried blood red, high contrast silhouettes, no text")

MAPA = {  # emblema plano visto desde arriba (no isométrico)
    "estacion": "railway station building with a platform and two tracks",
    "pueblo": "small village, a cluster of houses around a church",
    "ciudad": "dense city blocks with a tall tower",
    "puerto": "harbor with a quay, a crane and a cargo ship",
    "aerodromo": "airfield with a crossed runway and a hangar",
    "taller": "railway workshop shed with a turntable",
    "puente": "railway bridge over a river",
    "paso_fronterizo": "border checkpoint with a barrier gate and a booth",
    "nido": "hive nest, a pulsing mass of dark red flesh and tendrils over ruins",
    "refineria": "oil refinery with round tanks and a chimney",
    "almacen": "warehouse depot with stacked crates",
    "granja": "farm with a barn and fields",
    "fuerte": "small star-shaped fort with walls",
    "tren_marcador": "train marker, a locomotive and wagons in a line",
    "vagon_marcador": "single freight wagon marker",
    "obras_via": "railway works site with a crane and cones",
    "horda_baja": "scattered few small dark red dots, low horde density marker",
    "horda_media": "medium cluster of dark red dots, medium horde density marker",
    "horda_alta": "dense swirling mass of dark red dots, high horde density marker",
    "via_cortada": "railway track broken by a red cross, cut line marker",
}
MAPA_ESTILO = "flat emblem seen straight from above, top-down map symbol, no perspective, not isometric, centered, "

MANDOS = [
    "grizzled old general with a white mustache and a peaked cap",
    "stern woman colonel with short grey hair and a scar over the eyebrow",
    "young captain with a cleft chin and a bandaged ear",
    "heavyset sergeant major with a thick black beard and a helmet",
    "calm woman commander with a long braid and a field cap",
    "tired major with round glasses and a stubble",
    "tall lieutenant with a shaved head and an eyepatch",
    "middle aged woman captain with a headscarf and a radio headset",
    "veteran commissioner with a battered beret and deep wrinkles",
    "young woman lieutenant with freckles and a helmet with goggles",
    "burly colonel with a gray crew cut and a missing front tooth",
    "elderly woman general with a stern face and a worn peaked cap",
]
ESPECIALISTAS = [
    "locomotive engineer driver with a cap and soot on the face", "woman railway mechanic with welding goggles",
    "combat medic with a red cross armband", "woman field doctor with a surgical mask pulled down",
    "sniper with a ghillie hood and a long rifle strap", "woman scout with a bandana and binoculars",
    "demolitions expert with a bandolier and ear protection", "radio operator with a big headset",
    "track layer worker with a hard hat and a pickaxe", "woman telegraph signalman with a lantern",
    "armorer with a leather apron and soot", "woman cook with a bandana and a ladle",
    "stoker with a sweat towel around the neck", "woman engineer with a blueprint tube and glasses",
    "scavenger with a gas mask on the forehead", "woman drone pilot with a visor",
    "trooper with a machine gun belt over the shoulder", "woman flamethrower trooper with a scarred cheek",
    "mechanic with a monkey wrench and oil stains", "woman surveyor with a theodolite case",
    "young messenger boy with a satchel and a flat cap", "old railwayman with a pipe and a conductor cap",
    "woman guard with a baton and a riot helmet", "interpreter with a notebook and tired eyes",
]

DECALS = {
    "sangre_charco": "dried blood puddle on concrete", "sangre_salpicadura": "blood splatter spray",
    "sangre_arrastre": "blood drag marks on the ground", "sangre_huellas": "bloody boot prints trail",
    "sangre_mancha": "old dark blood stain", "sangre_rociada": "arterial blood spray fan",
    "grieta_hormigon": "crack in a concrete slab", "grieta_asfalto": "cracked asphalt with weeds",
    "baldosas_rotas": "shattered floor tiles", "riel_roto": "broken railway track piece on gravel",
    "escombros_hormigon": "pile of broken concrete rubble", "escombros_ladrillo": "scattered red brick rubble",
    "escombros_madera": "splintered wooden planks and debris", "escombros_metal": "twisted scrap metal pieces",
    "aceite_mancha": "black oil stain with a rainbow sheen", "aceite_charco": "puddle of engine oil",
    "aceite_goteo": "oil drips trail", "quemado_suelo": "scorched burnt ground mark",
    "quemado_explosion": "blast crater scorch mark", "quemado_hoguera": "burnt campfire ashes ring",
    "senal_flecha": "rusty metal arrow sign lying on the ground, no text",
    "senal_peligro": "warning triangle sign with a skull symbol, no text",
    "senal_cruz": "red cross painted on the ground", "senal_marca_x": "painted X mark on the ground",
}

EVENTOS = [
    "armored train stopped in a railway cutting at dusk with zombie silhouettes on the embankment",
    "besieged railway station at night with sandbag defenders and floodlights",
    "blown-up railway bridge over a river with a train wagon hanging",
    "huge horde crossing a barren plain toward a distant train",
    "convoy of wagons arriving at a fortified station at dawn",
    "night track repair works with workers and a crane, guarded by soldiers",
    "hospital train wagon interior with wounded soldiers and a medic",
    "hive nest inside a ruined city plaza, pulsing flesh and tendrils",
    "helicopter evacuating survivors from a roof, zombies below",
    "ambush at a tunnel mouth, zombies pouring out in the dark",
    "snowy winter landscape with a dormant horde frozen along the tracks",
    "dead city skyline with a locomotive silhouette and smoke",
    "burning oil refinery at night with fire towers",
    "rescue of survivors from a barricaded village by a work train",
    "decoy train luring a horde away with lights and loudspeakers",
    "heavy railway artillery wagon firing at night",
    "dawn after a siege, tired soldiers among the debris",
    "thunderstorm over a bridge with a train crossing",
    "locomotive graveyard with rusted engines and tall grass",
    "survivors camping around a fire beside a stopped train",
]

UI = [  # (nombre, elementos)
    ("panel_boton", ["panel", "button"]),
    ("ventana_pestana", ["window", "tab"]),
    ("barra_icono", ["toolbar", "icon_button"]),
    ("salud_avatar", ["health_bar", "avatar"]),
]
UI_DESC = ("military command interface in pixel art, riveted dark steel frame with rust and scratches, "
           "olive drab and concrete grey, a small dried blood red accent, completely blank with no text, no letters, no labels")


def job(bloque, nombre, var, tool, args, coste=1, sin_paleta=False):
    j = {"bloque": bloque, "nombre": nombre, "variante": var, "tool": tool, "coste": coste, "seed": args.get("seed"),
         "args": args}
    if sin_paleta:
        j["sin_paleta"] = True
    return j


def main(b):
    out = []
    if b == "mapa":
        for nombre, d in MAPA.items():
            for i, v in enumerate("abcd", 1):
                out.append(job("mapa", nombre, v, "create_image_pixen", {
                    "description": MAPA_ESTILO + d + ", " + ESTILO, "width": 32, "height": 32, "no_background": True,
                    "outline": "single color black outline", "view": "high top-down", "seed": i}))
    elif b == "retratos":
        for tipo, lista in (("mando", MANDOS), ("especialista", ESPECIALISTAS)):
            for n, d in enumerate(lista, 1):
                for i, v in enumerate("ab", 1):
                    out.append(job("retratos", "%s%02d" % (tipo, n), v, "create_image_pixen", {
                        "description": "bust portrait of a %s, %s" % (d, ESTILO), "width": 64, "height": 64,
                        "no_background": True, "outline": "single color black outline", "seed": 10 * n + i}))
    elif b == "decals":
        for nombre, d in DECALS.items():
            for i, v in enumerate("ab", 1):
                out.append(job("decals", nombre, v, "create_image_pixen", {
                    "description": "%s, top-down ground decal, flat on the ground, %s" % (d, ESTILO), "width": 64,
                    "height": 64, "no_background": True, "view": "high top-down", "seed": i}))
    elif b == "eventos":
        for n, d in enumerate(EVENTOS, 1):
            for i, v in enumerate("ab", 1):
                out.append(job("eventos", "escena%02d" % n, v, "create_image_pixen", {
                    "description": "%s, event illustration, %s" % (d, ESTILO), "width": 512, "height": 288,
                    "no_background": False, "seed": 100 + 10 * n + i}))
    elif b == "ui":
        for nombre, elems in UI:
            for i, v in enumerate("abc", 1):
                out.append(job("ui", nombre, v, "create_ui_asset", {
                    "description": UI_DESC, "elements": elems, "width": 256, "height": 256,
                    "name": "vm_%s_%s" % (nombre, v), "seed": i}, coste=10))
    else:
        raise SystemExit("bloque desconocido")
    for j in out:
        print(json.dumps(j, ensure_ascii=False))
    print("%s: %d trabajos, %d generaciones" % (b, len(out), sum(j["coste"] for j in out)), file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
