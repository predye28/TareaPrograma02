#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    row = list(csv.reader([line]))[0]
    if len(row) >= 7 and row[0].lower() != "page_title":
        page_title = row[0]
        description = row[6]

        print(f"{page_title}\t{description}\t1")
