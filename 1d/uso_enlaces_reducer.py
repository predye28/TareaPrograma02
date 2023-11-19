#!/usr/bin/env python3

import sys

current_key = None
description_counts = {}

for line in sys.stdin:
    fields = line.strip().split("\t")

    if len(fields) >= 2:
        key, description = fields[:2]
        count = int(fields[2]) if len(fields) == 3 else 1

        if current_key == key:
            if description:  
                description_counts[description] = description_counts.get(description, 0) + count
        else:
            if current_key is not None:
                for desc, desc_count in description_counts.items():
                    print(f"{current_key}\t{desc}\t{desc_count}")
            current_key = key
            description_counts = {description: count if description else 0}

if current_key is not None:
    for desc, desc_count in description_counts.items():
        if desc: 
            print(f"{current_key}\t{desc}\t{desc_count}")
