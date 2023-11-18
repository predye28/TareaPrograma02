#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0]
    if len(row) >= 6 and row[0].lower() != "page_title":
        page_title = row[0]
        description = row[6]  # Ajusta el índice según la posición correcta de la descripción
        # Emitir la descripción completa como una sola entrada
        print(f"{page_title}\t{description}\t1")
