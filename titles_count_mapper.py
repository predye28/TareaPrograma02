#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.strip().split(",")
    if len(words) < 2 or not words[0] or not words[1]:
        continue
    page_title = words[0].strip('"')
    subtitle = words[1].strip('"')
    if page_title.lower() == "page_title":
        continue  # Ignorar la fila de encabezado
    print(f"{page_title}\t1")

