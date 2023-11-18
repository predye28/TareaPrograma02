#!/usr/bin/env python3

import sys

current_key = None
description_counts = {}

for line in sys.stdin:
    key, description, count = line.strip().split("\t")
    count = int(count)

    if current_key == key:
        if description:  # Verificar si la descripción no está vacía
            description_counts[description] = description_counts.get(description, 0) + count
    else:
        if current_key is not None:
            for desc, desc_count in description_counts.items():
                print(f"{current_key}\t{desc}\t{desc_count}")
        current_key = key
        description_counts = {description: count if description else 0}

# Imprimir el resultado para la última clave
if current_key is not None:
    for desc, desc_count in description_counts.items():
        if desc:  # Verificar si la descripción no está vacía
            print(f"{current_key}\t{desc}\t{desc_count}")
