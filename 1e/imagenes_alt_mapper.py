#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0]  # Convertir la línea CSV en una lista
    if len(row) >= 6 and row[0].lower() != "page_title":  # Ignorar la fila de encabezado y las filas mal formateadas
        page_title = row[0]
        alt_text = row[4]  # Obtener el texto alternativo de la imagen
        if alt_text:
            print(f"{page_title}\t1")
