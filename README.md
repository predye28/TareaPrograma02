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

## Instalar herramientas
- sudo apt install wget
- sudo apt install curl
- pip3 install beautifulsoup4
- pip3 install nltk  #Para el stemming
- python3 -m nltk.downloader punkt
- pip install mrjob
- pip install mysql-connector-python
- sudo apt-get install libmariadb-dev-compat
- pip install mariadb
- sudo apt-get install php libapache2-mod-php php-mysql
- sudo apt-get install php-mysqli

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

## Comandos cada vez que reiniciamos la base de datos
### Crear tabla en la base de datos
- CREATE TABLE resultados1a (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250),
    count INT
);

### Crear tabla en la base de datos
- CREATE TABLE resultados1b (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250),
    count INT
);

### Crear tabla en la base de datos
- CREATE TABLE resultados1c (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250),
    count INT
);

### Crear tabla en la base de datos
- CREATE TABLE resultados1d (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250),
    referencias VARCHAR(255),
    count INT
);
### Crear tabla en la base de datos
- CREATE TABLE resultados1e (
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
- hadoop fs -copyFromLocal /home/predyye/Documentos/GitHub/TareaPrograma02/bueno.csv /archivo.csv

### Parar hadoop
- stop-all.sh

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


# Correr el archivo que sube la informacion a la base de datos con este resultado de hadoop 
- hadoop fs -cat /resultado1aNormal/part-00000 | python3 insert1a.py

### Todos los job a ejecutar en hadoop:


- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files titles_count_mapper.py,titles_count_reducer.py -mapper titles_count_mapper.py -reducer titles_count_reducer.py \
-input /archivo.csv/bueno.csv -output /resu1a

- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files palabras_distintas_mapper.py,palabras_distintas_reducer.py -mapper palabras_distintas_mapper.py -reducer palabras_distintas_reducer.py \
-input /archivo.csv/bueno.csv -output /resultado1b

- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files enlaces_count_mapper.py,enlaces_count_reducer.py -mapper enlaces_count_mapper.py -reducer enlaces_count_reducer.py \
-input /archivo.csv/bueno.csv -output /resultado1c


- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files uso_enlaces_mapper.py,uso_enlaces_reducer.py -mapper uso_enlaces_mapper.py -reducer uso_enlaces_reducer.py \
-input /archivo.csv/wikipedia_data.csv -output /resultado1d


- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files imagenes_alt_mapper.py,imagenes_alt_reducer.py -mapper imagenes_alt_mapper.py -reducer imagenes_alt_reducer.py \
-input /archivo.csv/wikipedia_data.csv -output /resultado1eFinal






# Comandos adiciones que utilizanos a lo largo del proyecto

## Dar permisos a los archivos
- chmod +x titles_count_mapper.py
- chmod +x titles_count_reducer.py

## Correr los archivos en local:
- cat bueno.csv | ./imagenes_alt_mapper.py | sort | ./imagenes_alt_reducer.py

# PHP

## INICIAR SERVIDOR:
- php -S localhost:8000