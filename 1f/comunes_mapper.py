#!/usr/bin/env python3

import sys
import csv
import re

def get_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

for line in sys.stdin:
    row = list(csv.reader([line]))[0]
    if len(row) >= 6 and row[0].lower() != "page_title":
        page_title = row[0]
        subtitle_text = row[2]
        words = get_words(subtitle_text)

        for word in words:
            print(f"{page_title}\t{word}\t1")
