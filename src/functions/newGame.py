from database.database_connection import database_connect as connection
from functions.loadGame import load_game
from main.player import Player # Tämä tekee muuttujista globaallisia, eli tämän avulla pelaajan nimi voidaan tallentaa ja käyttää myöhemmin pelin aikana. - Daniel

def new_game():
    connect = connection()
    screen_name = input("Anna pelaaja nimesi: ")
    check_sql = f"SELECT screen_name FROM game WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(check_sql)
    result = cursor.fetchone()

    if result:
        print(f"Virhe: nimi {screen_name} on jo varattu")
        return

    insert_sql = f"INSERT INTO game (screen_name) VALUES ('{screen_name}')"
    cursor.execute(insert_sql)
    connect.commit()
    cursor.close()
    connect.close()
    Player.current_player = Player.Player(screen_name, cursor.lastrowid)
    # Tahan funktio joka kutsutaan etta peli voidaan aloittaa. - Daniel