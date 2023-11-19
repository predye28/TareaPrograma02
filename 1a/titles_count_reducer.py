#!/usr/bin/env python3

import sys

current_title = None
title_count = 0

for line in sys.stdin:
    title = line.strip()
    
    if current_title and current_title != title:
        print(f"{current_title}\t{title_count}")
        title_count = 0

    current_title = title
    title_count += 1

if current_title:
    print(f"{current_title}\t{title_count}")
