from database.database_connection import database_connect as connection
from main.player import Player
from functions.gameLoop import game_loop

def new_game():
    connect = connection()
    cursor = connect.cursor()

    while True:
        screen_name = input("Anna pelaajanimesi: ")

        check_sql = f"SELECT screen_name FROM game WHERE screen_name = '{screen_name}'"
        cursor.execute(check_sql)
        result = cursor.fetchone()

        if result:
            print(f"Virhe: nimi {screen_name} on jo varattu.")
            print("Valitse toinen nimi.\n")
        else:
            break

    insert_sql = f"INSERT INTO game (screen_name) VALUES ('{screen_name}')"
    cursor.execute(insert_sql)
    connect.commit()

    player_id = cursor.lastrowid

    cursor.close()
    connect.close()

    Player.current_player = Player(screen_name, player_id)

    game_loop()
    # Tahan funktio joka kutsutaan etta peli voidaan aloittaa. - Daniel