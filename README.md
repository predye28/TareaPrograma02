# TareaPrograma02
Bases de datos II

Este proyecto es realizado en una maquina virtual en ubuntu.

Ingresar los siguientes comandos para actualizar y instalar lo necesario para correr el proyecto:

## Actualizar el sistema:
- sudo apt update
- sudo apt upgrade

## Instalar Pyhton3 y pip
- sudo apt install python3
- sudo apt install python3-pip

### Instalar herramientas necesarias para el WebCrawler
- sudo apt install wget
- sudo apt install curl
- pip3 install beautifulsoup4
- pip3 install nltk  #Para el stemming
- python3 -m nltk.downloader punkt
- pip install mrjob
- pip install mysql-connector-python
- sudo apt-get install libmariadb-dev-compat
- pip install mariadb


# Mariadb

## Instalar MariaDB
- sudo apt install mariadb-server
- sudo mysql_secure_installation //configurarlo
- mysql --version //ver la version

## Comandos en Mariadb 

### Ejecutar MariaDB
- sudo mysql

### Crear usuario adicional
- GRANT ALL ON *.* TO 'predye'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

### Conectarme con un usuario
- mysql -u predye -p

### Crear base de datos
- create database dbresultados;

### Ver las bases de datos
- show databases;

### Ingresar a la base de datos
- USE dbresultados;

### Crear tabla en la base de datos
- CREATE TABLE resultados1a (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250),
    count INT
);



# hadoop


## Instalacion de hadoop
- https://www.youtube.com/watch?v=Slbi-uzPtnw
- https://codewitharjun.medium.com/install-hadoop-on-ubuntu-operating-system-6e0ca4ef9689


## Inicio del servidor en hadoop
- ssh localhost 
- chmod 0600 ~/.ssh/authorized_keys 
- hadoop-3.3.6/bin/hdfs namenode -format //FORMATEA TODOS LOS DATOS EXISTENTES
- export PDSH_RCMD_TYPE=ssh
- start-all.sh


## Comandos en hadoop

### Comandos para ingresar cada vez q reinicia hadoop
- hadoop fs -mkdir /archivo.csv
- hadoop fs -copyFromLocal /home/predye/Documentos/GitHub/TareaPrograma02/bueno.csv /archivo.csv

### Crear carpeta en hdfs:
- hadoop fs -mkdir /ruta/en/hdfs

### Copiar el Archivo a HDFS:
- hadoop fs -copyFromLocal /ruta/local/al/archivo.csv /ruta/en/hdfs/

### Verificar que este un archivo:
- hadoop fs -ls /ruta/en/hdfs/

### Ejecutar el job MapReduce en Hadoop:
- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files titles_count_mapper.py,titles_count_reducer.py -mapper titles_count_mapper.py -reducer titles_count_reducer.py \
-input /archivo.csv/bueno.csv -output /resultado1a

### Verificar el resultado:
- hadoop fs -cat /resultado1a/part-00000


# Correr los archivos en local:
- cat tu_archivo_prueba.csv | ./titles_count_mapper.py | sort | ./titles_count_reducer.py

# Correr el archivo que sube la informacion a la base de datos con este resultado de hadoop 
- hadoop fs -cat /resultado1aNormal/part-00000 | python3 insert_into_mariadb.py

# Dar permisos a los archivos
- chmod +x titles_count_mapper.py
- chmod +x titles_count_reducer.py