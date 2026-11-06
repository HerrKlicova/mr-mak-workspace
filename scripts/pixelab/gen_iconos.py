"""Genera el archivo de trabajos del bloque de iconos (lote v1.3). Uso: python gen_iconos.py > trabajos_iconos.jsonl"""
import json
import sys

ESTILO = ("pixel art game icon, centered, gritty post-apocalyptic military, muted desaturated palette, "
          "rust, olive drab, concrete grey, dried blood red, high contrast silhouette, no text")

# categoria -> {nombre: descripcion en ingles}
ICONOS = {
    "recursos": {
        "toneladas": "stack of cargo crates on a pallet, tonnes of supplies",
        "tren_servicio": "small steam locomotive seen from the side, train in service",
        "km_via": "short straight section of railway track with sleepers, safe track length",
        "rescatados": "rescued survivor wrapped in a blanket, person saved",
    },
    "ordenes": {
        "avanzar": "bold arrow pointing forward, advance order",
        "atacar": "crossed bayonet rifle and sword, attack order",
        "reparar": "wrench and hammer crossed, repair order",
        "construir": "hammer and a stack of planks, build order",
        "demoler": "sledgehammer smashing a brick wall, demolish order",
        "guarnecer": "soldier helmet on top of a bunker, garrison order",
        "patrullar": "two boot prints in a loop arrow, patrol order",
        "reabrir_linea": "railway track with a padlock opening, reopen line order",
        "trazar_linea": "railway track being drawn along a dotted line, lay new line",
        "senuelo": "decoy train wagon with a flashing lantern, decoy order",
        "detener_tren": "red stop hand over a train wheel, stop train order",
        "arrancar_tren": "train wheel with a green forward arrow, start train order",
        "enganchar_vagon": "two train couplers joined together, couple wagon order",
        "desenganchar_vagon": "two train couplers separating, uncouple wagon order",
        "evacuar": "people running toward an arrow pointing out, evacuate order",
        "rescatar": "life ring and a hand reaching out, rescue order",
        "abastecer": "supply crate with an arrow pointing down, resupply order",
        "apoyo_aereo": "fighter plane diving with a crosshair, air strike order",
        "artilleria": "heavy artillery gun barrel firing, artillery order",
        "cambiar_horario": "clock face with a circular arrow, change schedule order",
        "cambiar_ruta": "railway fork switch with a curved arrow, change route order",
        "mantener": "round shield with a bold cross, hold position order",
        "retirar": "bold arrow turning back, retreat order",
        "escoltar": "soldier walking beside a train wagon, escort order",
    },
    "estados": {
        "herido": "bandaged head with a blood stain, wounded status",
        "cansado": "drooping sweat drop over a tired face, exhausted status",
        "sin_municion": "empty rifle magazine with a red cross, out of ammunition",
        "sin_combustible": "empty fuel can with a red cross, out of fuel",
        "asediado": "ring of claws closing around a small fort, besieged status",
        "amenazado": "yellow warning triangle with a claw mark, threatened status",
        "segura": "green check mark over a small fort, secure zone status",
        "perdida": "broken black flag on a ruined fort, lost zone status",
        "en_llamas": "flame burning on a wooden crate, on fire status",
        "infectado": "green biohazard drop over a hand, infected status",
        "muerto": "grey skull with a helmet, dead status",
        "bloqueado": "railway track blocked by rubble, blocked status",
        "ruido": "sound waves coming out of a loudspeaker, noise status",
        "luz": "floodlight beam of light, light status",
        "letargo": "snowflake over a sleeping zombie head, dormant status",
        "alerta_baja": "small blue alert bell, low priority alert",
        "alerta_media": "orange alert bell with a spark, medium priority alert",
        "alerta_alta": "red flashing siren light, high priority alert",
    },
    "unidades": {
        "fusilero": "soldier with a rifle, rifleman",
        "arma_pesada": "soldier carrying a heavy machine gun, heavy weapons",
        "ingeniero": "soldier with a wrench and a toolbox, engineer",
        "francotirador": "soldier in a ghillie hood with a long rifle, sniper",
        "lanzallamas": "soldier with a flamethrower tank, flamethrower",
        "medico": "soldier with a medical bag and a red cross armband, medic",
        "obrero": "worker with a pickaxe and a hard hat, track worker",
        "comandante": "officer with a peaked cap and a binocular, commander",
        "locomotora": "armored steam locomotive seen from the side, locomotive",
        "tren_obras": "work train with a crane and tools, construction train",
        "vagon_transporte": "closed freight wagon, transport wagon",
        "vagon_artilleria": "flat wagon with a heavy gun, artillery wagon",
        "vagon_grua": "flat wagon with a crane arm, crane wagon",
        "vagon_obras": "flat wagon with rails and sleepers, track works wagon",
        "vagon_hospital": "wagon with a red cross on the side, hospital wagon",
        "vagon_antiaereo": "flat wagon with an anti-aircraft gun, anti-aircraft wagon",
        "plataforma_tiro": "flat wagon with sandbags and soldiers shooting, firing platform",
        "vagon_senuelo": "wagon with a lantern and loudspeaker, decoy wagon",
        "vehiculo_ligero": "small armored jeep, light vehicle",
        "blindado": "armored personnel carrier, armored vehicle",
        "excavadora": "bulldozer with a blade, bulldozer",
        "camion_grua": "truck with a crane arm, crane truck",
        "ataque_aereo": "bomb falling with a target circle, air strike",
        "helicoptero": "military helicopter seen from the side, helicopter",
        "dron": "small quadcopter drone, drone",
        "fuego_naval": "warship firing its main gun, naval gunfire",
    },
    "piezas": {
        "muro_sacos": "wall made of stacked sandbags, sandbag wall",
        "hesco": "wire mesh and canvas gabion barrier, HESCO barrier",
        "puerta": "reinforced steel gate, gate",
        "nido_ametralladora": "machine gun nest behind sandbags, machine gun nest",
        "foco": "military floodlight on a pole, floodlight",
        "deposito": "round fuel storage tank, tank depot",
        "anden_fortificado": "railway platform with sandbag walls, fortified platform",
        "muro_hormigon": "thick concrete wall segment, concrete wall",
        "torre": "wooden guard tower, watchtower",
        "mina": "round landmine with a spike, landmine",
        "alambrada": "coil of barbed wire, razor wire fence",
        "mortero": "mortar tube on a base plate, mortar",
        "antiaereo": "anti-aircraft gun on a mount, anti-aircraft",
        "generador": "diesel generator with a cable, power generator",
    },
    "cepas": {
        "comun": "grey-green zombie head, common zombie",
        "rapido": "lean zombie head with motion lines, fast zombie",
        "pesado": "bulky muscular zombie head, heavy zombie",
        "acorazado": "zombie head covered in metal plates, armored zombie",
        "ignifugo": "zombie head with charred blackened skin and ember eyes, fire resistant zombie",
        "trepador": "zombie hand with long claws gripping a ledge, climber zombie",
        "excavador": "zombie hands with huge shovel claws digging, digger zombie",
        "chillon": "screaming zombie head with sound waves, screamer zombie",
        "nocturno": "pale zombie head with glowing eyes and a moon, night zombie",
        "animal_infectado": "infected dog head with exposed teeth, infected animal",
    },
}


def main():
    n = 0
    for cat, items in ICONOS.items():
        for nombre, desc in items.items():
            for i, var in enumerate("abc", start=1):
                job = {
                    "bloque": "iconos", "nombre": "%s_%s" % (cat, nombre), "variante": var,
                    "tool": "create_image_pixen", "coste": 1, "seed": i,
                    "args": {"description": "%s, %s" % (desc, ESTILO), "width": 32, "height": 32,
                             "no_background": True, "outline": "single color black outline", "seed": i},
                }
                print(json.dumps(job, ensure_ascii=False))
                n += 1
    # órdenes en 16x16 (versión pequeña): 2 variantes
    for nombre, desc in ICONOS["ordenes"].items():
        for i, var in enumerate("ab", start=1):
            print(json.dumps({
                "bloque": "iconos", "nombre": "ordenes_%s_16" % nombre, "variante": var,
                "tool": "create_image_pixen", "coste": 1, "seed": i,
                "args": {"description": "%s, %s" % (desc, ESTILO), "width": 16, "height": 16,
                         "no_background": True, "outline": "single color black outline", "seed": i},
            }, ensure_ascii=False))
            n += 1
    print("total trabajos:", n, file=sys.stderr)


if __name__ == "__main__":
    main()
