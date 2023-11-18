#!/usr/bin/env python3

import sys

current_key = None
current_word = None
current_count = 0

for line in sys.stdin:
    key, word, count = line.strip().split("\t")
    count = int(count)

    if current_key == key and current_word == word:
        current_count += count
    else:
        if current_key and current_word:
            print(f"{current_key}\t{current_word}\t{current_count}")
        current_key = key
        current_word = word
        current_count = count

# Imprimir el resultado para la última clave
if current_key and current_word:
    print(f"{current_key}\t{current_word}\t{current_count}")
