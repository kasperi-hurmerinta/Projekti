from database.database_connection import database_connect as connection
from functions.loadGame import load_game
import player # Tämä tekee muuttujista globaallisia, eli tämän avulla pelaajan nimi voidaan tallentaa ja käyttää myöhemmin pelin aikana.

def new_game():
    connect = connection()
    player_name = input("Anna pelaaja nimesi: ")
    check_sql = f"SELECT screen_name FROM game WHERE screen_name = '{player_name}'"
    cursor = connect.cursor()
    cursor.execute(check_sql)
    result = cursor.fetchone()

    if result:
        print(f"Virhe: nimi {player_name} on jo varattu")
        return

    insert_sql = f"INSERT INTO game (screen_name) VALUES ('{player_name}')"
    cursor.execute(insert_sql)
    connect.commit()
    cursor.close()
    connect.close()
    player.current_player = player.Player(player_name, cursor.lastrowid)
    load_game()