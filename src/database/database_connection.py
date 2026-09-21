## from database.database_connection import database_connect - käyttäkää tätä kun kutsutte sitä saatanan tietokantaa

import mysql.connector

def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Metropolia!",
        database="flight_game"
    )

# Käyttäisin itseasiassa dotenv kirjastoa, mutta koska tämä on koulu projekti niin pidetään tämä yksinkertaisena.