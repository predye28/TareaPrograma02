#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0]
    if len(row) >= 6 and row[0].lower() != "page_title":
        page_title = row[0]
        references = row[5].split("|")
        
        for reference in references:
            if reference:
                print(f"{page_title}\t{reference}\t1")
