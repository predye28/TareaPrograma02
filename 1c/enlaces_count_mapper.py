#!/usr/bin/env python3

import sys
import csv

# Definir la función de mapeo
def map_function(row):
    page_title = row[0]
    reference_link = row[5]

    # Emitir el título de la página y un valor indicando si la referencia tiene enlace
    print(f"{page_title}\t{1 if reference_link else 0}")

# Entrada de la secuencia de entrada estándar
csv_reader = csv.reader(sys.stdin)

# Iterar sobre las filas del archivo CSV
for row in csv_reader:
    # Ignorar la primera línea (encabezados)
    if row[0] == "Page_Title":
        continue

    # Asegurarse de que la fila tenga al menos 6 campos (índice 5 existe)
    if len(row) >= 6:
        map_function(row)
