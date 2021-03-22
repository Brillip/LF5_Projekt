"""
    Programm zum Auslesen der CPU- und RAM-
    Auslastung und Export in das CSV-Datenformat.

    Autor:  Marvin Bänsch, Marc Busse, Philip Decker, Emin Jafarov, Yusuf Kocak
    Datum:  08.03.2021
"""

# Module importieren
import time
import csv
import psutil
import mysql.connector
import stats
from datetime import datetime


# Schleife laufen lassen bis das Programm geschlossen wird
while 1:
  
    # Verbindung zur Datenbank herstellen
    mydb = mysql.connector.connect(   
    host="localhost",
    user="root",
    password="",
    database="monitoring"
    )
    # Variablen mit Metriken definieren
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(1)
    ram = psutil.virtual_memory().percent

    # Erstellung eines Cursors
    mc = mydb.cursor()

    # Speichern der SQL-Query als Variable
    # %s = Platzhalter
    sql = "INSERT INTO pi1 (Zeit,CPU,RAM) VALUES (%s,%s,%s)"
    # Speichern der Metriken als Liste in einer Variable
    val = (time,cpu,ram)
    # Ausführen der Query
    mc.execute(sql, val)
    # Pushen der Daten auf die Datenbank
    mydb.commit()
    # Benutzeroberfläche
    print ("#################################################################################")
    print ("############################## Hardware Monitoring ##############################")
    print ("#################################################################################")
    print ("#################################################################################")
    print ("############################ Wählen sie eine Option #############################")
    print ("#################################################################################")
    print ("########################### 1 = Statistiken anzeigen ############################")
    print ("########################### 0 = Programm beenden     ############################")
    print ("#################################################################################")

    # Benutzerinput speichern
    eingabe = int(input("Wählen sie eine der Optionen aus "))

    # Anzeigen von Statistiken
    if eingabe == 1:
        stats.show()

    if eingabe == 0:
        break

exit()

#wat is dat denn kokosmilk
