#!/usr/bin/env python3

import sys

current_page_title = None
image_with_alt_count = 0

for line in sys.stdin:
    page_title, count = line.strip().split("\t")
    count = int(count)

    # Si la clave actual es diferente de la anterior, imprimir resultado y reiniciar el conteo
    if current_page_title and current_page_title != page_title:
        print(f"{current_page_title}\t{image_with_alt_count}")
        image_with_alt_count = 0

    # Actualizar la clave y el conteo
    current_page_title = page_title
    image_with_alt_count += count

# Imprimir el resultado para la última clave
if current_page_title:
    print(f"{current_page_title}\t{image_with_alt_count}")
