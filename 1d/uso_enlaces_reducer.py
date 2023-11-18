#!/usr/bin/env python3

import sys

current_reference = None
reference_count = 0

for line in sys.stdin:
    reference, count = line.strip().split("\t")
    count = int(count)

    # Si la clave actual es diferente de la anterior, imprimir resultado y reiniciar el conteo
    if current_reference and current_reference != reference:
        print(f"{current_reference}\t{reference_count}")
        reference_count = 0

    # Actualizar la clave y el conteo
    current_reference = reference
    reference_count += count

# Imprimir el resultado para la última clave
if current_reference:
    print(f"{current_reference}\t{reference_count}")
