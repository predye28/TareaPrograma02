#!/usr/bin/env python

import sys

current_title = None
title_count = 0

for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en palabras
    title, count = line.strip().split("\t")

    # Convertir el conteo a un entero
    count = int(count)

    # Si la clave actual es diferente de la anterior, imprimir resultado y reiniciar el conteo
    if current_title and current_title != title:
        print(f"{current_title}\t{title_count}")
        title_count = 0

    # Actualizar la clave y el conteo
    current_title = title
    title_count += count

# Imprimir el resultado para la última clave
if current_title:
    print(f"{current_title}\t{title_count}")
