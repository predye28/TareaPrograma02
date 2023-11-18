#!/usr/bin/env python3

import sys

current_title = None
total_references_with_links = 0

# Procesar la entrada de la secuencia estándar
for line in sys.stdin:
    # Eliminar espacios en blanco
    line = line.strip()

    # Obtener el título y el indicador de enlace de la línea
    title, has_link = line.split("\t")

    # Convertir el indicador de enlace de cadena a entero
    has_link = int(has_link)

    # Si cambia el título, imprimir el recuento actual y reiniciar para el nuevo título
    if current_title and current_title != title:
        print(f"{current_title}\t{total_references_with_links}")
        total_references_with_links = 0

    # Actualizar el contador de referencias con enlaces
    total_references_with_links += has_link

    # Actualizar el título actual
    current_title = title

# Imprimir el último título
if current_title:
    print(f"{current_title}\t{total_references_with_links}")
