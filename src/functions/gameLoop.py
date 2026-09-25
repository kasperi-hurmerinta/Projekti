from database.database_connection import database_connect as connection
from main.player import Player

def tarkista_pisteet():
    connect = connection()
    check_sql = f"SELECT screen_name FROM game WHERE screen_name = '{Player.current_player.screen_name}'"
    cursor = connect.cursor()
    cursor.execute(check_sql)
    result = cursor.fetchone()

    if result is not None and result[0] >= 150:
        return True

    cursor.close()
    connect.close()

    return False

def game_loop():



    if tarkista_pisteet():
        print("bläh bläh bläh")
