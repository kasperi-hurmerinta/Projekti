## from database.database_connection import database_connect - käyttäkää tätä kun kutsutte sitä saatanan tietokantaa

import mysql.connector

def database_connect():
    return mysql.connector.connect(
        host="192.168.1.7",
        user="python",
        password="Python",
        database="flight_game"
    )
