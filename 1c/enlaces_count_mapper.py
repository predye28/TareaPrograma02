#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0]  # Convertir la línea CSV en una lista
    if len(row) >= 7 and row[0].lower() != "page_title":  # Ignorar la fila de encabezado y las filas mal formateadas
        page_title = row[0]
        references = row[5].split("|")  # Suponemos que las referencias están en la columna 5

        for reference in references:
            if reference:  # Asegurarse de que la referencia no esté vacía
                url, description = reference.split(",", 1) if "," in reference else (reference, "")
                print(f"{page_title}\t{url}\t{description}")
