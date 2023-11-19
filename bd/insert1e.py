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

        title, count = line.strip().split("\t")
    except ValueError:
        print(f"Error al desempaquetar la línea: {line.strip()}")
        continue
    
    try:

        cursor.execute("INSERT INTO resultados1e (title, count) VALUES (?, ?)", (title, int(count)))
        conn.commit()
    except mariadb.Error as e:
        print(f"Error al insertar en la base de datos: {e}")

cursor.close()
conn.close()