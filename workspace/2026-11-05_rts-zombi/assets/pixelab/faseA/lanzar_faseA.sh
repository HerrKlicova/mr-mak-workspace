#!/bin/bash
# fase A de Pixelab, A2 a A7 y A1b, bloque a bloque (reanudable: lote.py no vuelve a pagar lo hecho)
cd /c/Dev/mr-mak-workspace/scripts/pixelab || exit 1
D=/c/Dev/mr-mak-workspace/workspace/2026-11-05_rts-zombi/assets/pixelab/faseA
for b in A2_32 A3_32 A4 A5 A6 A7 A1b; do
  echo "== $b $(date +%T)"
  python lote.py $D/trabajos_$b.jsonl --hilos 4 > $D/salida_$b.txt 2>&1
  tail -2 $D/salida_$b.txt
done
echo "FIN $(date +%T)"
