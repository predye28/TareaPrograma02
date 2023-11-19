#!/usr/bin/env python3

import sys
import csv


def map_function(row):
    page_title = row[0]
    reference_link = row[5]

    print(f"{page_title}\t{1 if reference_link else 0}")


csv_reader = csv.reader(sys.stdin)

for row in csv_reader:
    if row[0] == "Page_Title":
        continue

    if len(row) >= 6:
        map_function(row)
