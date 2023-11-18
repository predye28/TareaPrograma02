#!/usr/bin/env python3

import sys

current_key = None
reference_counts = {}

for line in sys.stdin:
    key, reference, count = line.strip().split("\t")
    count = int(count)

    if current_key == key:
        reference_counts[reference] = reference_counts.get(reference, 0) + count
    else:
        if current_key:
            for ref, ref_count in reference_counts.items():
                print(f"{current_key}\t{ref}\t{ref_count}")
        current_key = key
        reference_counts = {reference: count}

# Imprimir el resultado para la última clave
if current_key:
    for ref, ref_count in reference_counts.items():
        print(f"{current_key}\t{ref}\t{ref_count}")
