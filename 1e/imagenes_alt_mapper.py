#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0] 
    if len(row) >= 6 and row[0].lower() != "page_title":  
        page_title = row[0]
        alt_text = row[4]  
        if alt_text:
            print(f"{page_title}\t1")
