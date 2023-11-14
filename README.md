# TareaPrograma02
Bases de datos II

Este proyecto es realizado en una maquina virtual en ubuntu.

Ingresar los siguientes comandos para actualizar y instalar lo necesario para correr el proyecto:

#Actualizar el sistema:
sudo apt update
sudo apt upgrade

#Instalar Pyhton3 y pip
sudo apt install python3
sudo apt install python3-pip

#Instalar herramientas necesarias para el WebCrawler y la parte de hadoop
sudo apt install wget
sudo apt install curl
pip3 install beautifulsoup4
pip3 install nltk  #Para el stemming
python3 -m nltk.downloader punkt
pip install mrjob

#Instalar MariaDB
sudo apt install mariadb-server mariadb-client

#Instalacion de hadoop
https://www.youtube.com/watch?v=Slbi-uzPtnw

#Inicio del servidor en hadoop
ssh localhost 
chmod 0600 ~/.ssh/authorized_keys 
hadoop-3.3.6/bin/hdfs namenode -format
export PDSH_RCMD_TYPE=ssh
start-all.sh

#Ingresar un archivo
hdfs dfs -copyFromLocal /home/predye/Documentos/TareaII/wikipedia_data.json /predye

#verificar que este un archivo:
hdfs dfs -ls /predye
