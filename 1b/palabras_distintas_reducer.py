#!/usr/bin/env python3

import sys

current_page = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    page, count = line.split("\t")

    if current_page == page:
        current_count += int(count)
    else:
        if current_page is not None:
            print(f"{current_page}\t{current_count}")
        current_page = page
        current_count = int(count)

if current_page is not None:
    print(f"{current_page}\t{current_count}")
