#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0]  # Convertir la línea CSV en una lista
    if len(row) >= 6 and row[0].lower() != "page_title":  # Ignorar la fila de encabezado y las filas mal formateadas
        page_title = row[0]
        references = row[5].split("|")  # Columna de referencias separadas por "|"
        
        # Emitir clave-valor para cada referencia encontrada en el texto
        for reference in references:
            if reference:
                print(f"{reference}\t1")
