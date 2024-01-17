# config.py>

import mysql.connector

# Connexion à la base de données : -------------------------------------------------------------------------------------------------

def connect_to_sql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pydo"
    )
    mycursor = mydb.cursor()
    return mycursor
