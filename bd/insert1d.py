#!/usr/bin/env python3

import sys
import mariadb


try:
    conn = mariadb.connect(
        user="predye",
        password="password",
        host="localhost",
        port=3306,
        database="dbresultados"
    )
    cursor = conn.cursor()
except mariadb.Error as e:
    print(f"Error al conectar a MariaDB: {e}")
    sys.exit(1)

for line in sys.stdin:
    try:
        title, references, count = line.strip().split("\t")
    except ValueError:
        print(f"Error al desempaquetar la línea: {line.strip()}")
        continue

    max_title_length = 250  
    max_references_length = 250  
    if len(title) > max_title_length:
        title = title[:max_title_length]
    if len(references) > max_references_length:
        references = references[:max_references_length]

    try:
        cursor.execute("INSERT INTO resultados1d (title, referencias, count) VALUES (?, ?, ?)", (title, references, int(count)))
        conn.commit()
    except mariadb.Error as e:
        print(f"Error al insertar en la base de datos: {e}")

cursor.close()
conn.close()

