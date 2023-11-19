#!/usr/bin/env python3

import sys

current_title = None
total_references_with_links = 0

for line in sys.stdin:
    line = line.strip()

    title, has_link = line.split("\t")

    has_link = int(has_link)

    if current_title and current_title != title:
        print(f"{current_title}\t{total_references_with_links}")
        total_references_with_links = 0

    total_references_with_links += has_link

    current_title = title

if current_title:
    print(f"{current_title}\t{total_references_with_links}")
