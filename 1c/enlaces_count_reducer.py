#!/usr/bin/env python3

import sys

current_reference = None
reference_count = 0
active_count = 0

for line in sys.stdin:
    # Dividir la línea en elementos
    elements = line.strip().split("\t")

    # Verificar que haya al menos dos elementos
    if len(elements) >= 2:
        page_title, url, description = elements[0], elements[1], elements[2] if len(elements) == 3 else ""

        # Comprobar si estamos tratando con la misma referencia
        if current_reference == url:
            reference_count += 1

            # Verificar si la descripción indica que el enlace está activo
            if description.lower() == "activo":
                active_count += 1

        else:
            # Imprimir resultados para la referencia anterior
            if current_reference:
                print(f"{current_reference}\t{reference_count}\t{active_count}")

            # Reiniciar variables para la nueva referencia
            current_reference = url
            reference_count = 1
            active_count = 1 if description.lower() == "activo" else 0

# Imprimir el resultado para la última referencia
if current_reference:
    print(f"{current_reference}\t{reference_count}\t{active_count}")
