## from database_connection import database_connect

import mysql.connector

def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Metropolia!",
        database="flight_game"
    )
