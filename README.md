# TareaPrograma02
Bases de datos II

Este proyecto es realizado en una maquina virtual en ubuntu.

Ingresar los siguientes comandos para actualizar y instalar lo necesario para correr el proyecto:

## Actualizar el sistema:
- sudo apt update
- sudo apt upgrade

### Instalar Pyhton3 y pip
- sudo apt install python3
- sudo apt install python3-pip

### Instalar herramientas necesarias para el WebCrawler y la parte de hadoop
- sudo apt install wget
- sudo apt install curl
- pip3 install beautifulsoup4
- pip3 install nltk  #Para el stemming
- python3 -m nltk.downloader punkt
- pip install mrjob

### Instalar MariaDB
- sudo apt install mariadb-server mariadb-client

### Instalacion de hadoop
- https://www.youtube.com/watch?v=Slbi-uzPtnw
- https://codewitharjun.medium.com/install-hadoop-on-ubuntu-operating-system-6e0ca4ef9689


### Inicio del servidor en hadoop
- ssh localhost 
- chmod 0600 ~/.ssh/authorized_keys 
- hadoop-3.3.6/bin/hdfs namenode -format
- export PDSH_RCMD_TYPE=ssh
- start-all.sh

# Comandos en hadoop


### Crear carpeta en hdfs:
- hadoop fs -mkdir /ruta/en/hdfs

### Copiar el Archivo a HDFS:
- hadoop fs -copyFromLocal /ruta/local/al/archivo.csv /ruta/en/hdfs/

### Verificar que este un archivo:
- hadoop fs -ls /ruta/en/hdfs/

### Ejecutar el trabajo MapReduce en Hadoop:
- hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-files titles_count_mapper.py,titles_count_reducer.py -mapper titles_count_mapper.py -reducer titles_count_reducer.py \
-input /ruta/al/archivo.csv -output /ruta/de/salida

### Verificar el resultado:
- hadoop fs -cat /ruta/de/salida/output_titles_count/part-00000