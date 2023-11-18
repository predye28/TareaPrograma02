#!/usr/bin/env python3

import sys
import mariadb

# Configurar la conexión a la base de datos
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

# Procesar la entrada y realizar la inserción en la base de datos
for line in sys.stdin:
    try:
        # Intentar desempaquetar la línea
        title, count = line.strip().split("\t")
    except ValueError:
        # Si hay un error, imprimir la línea y continuar con la siguiente
        print(f"Error al desempaquetar la línea: {line.strip()}")
        continue
    
    try:
        # Insertar en la base de datos utilizando placeholders
        cursor.execute("INSERT INTO resultados1a (title, count) VALUES (?, ?)", (title, int(count)))
        conn.commit()
    except mariadb.Error as e:
        print(f"Error al insertar en la base de datos: {e}")

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
conn.close()


casa se 132
casa de 12
casa la 12

