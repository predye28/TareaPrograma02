#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en palabras
    words = line.strip().split("\t")

    # Ignorar líneas vacías o con menos de dos columnas
    if len(words) < 2:
        continue

    # Tomar el título de la página y emitir una pareja (clave, valor) para contar cada título
    title = words[0]
    print(f"{title}\t1")
