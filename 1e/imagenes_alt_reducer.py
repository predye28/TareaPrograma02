#!/usr/bin/env python3

import sys

current_page_title = None
image_with_alt_count = 0

for line in sys.stdin:

    parts = line.strip().split("\t")


    if len(parts) < 2:
        continue  

    page_title, count = parts[0], int(parts[1])

    if current_page_title and current_page_title != page_title:
        print(f"{current_page_title}\t{image_with_alt_count}")
        image_with_alt_count = 0

    current_page_title = page_title
    image_with_alt_count += count

if current_page_title:
    print(f"{current_page_title}\t{image_with_alt_count}")

