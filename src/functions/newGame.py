from database.database_connection import database_connect as connection
from main.player import Player
from functions.gameLoop import game_loop

def new_game():
    connect = connection()
    cursor = connect.cursor()

    while True:
        screen_name = input("Anna pelaajanimesi: ")
        
        if not screen_name:
            print("Virhe: pelaajanimi ei voi olla tyhjä.")
            continue

        check_sql = "SELECT screen_name FROM game WHERE screen_name = %s"
        cursor.execute(check_sql, (screen_name,))
        result = cursor.fetchone()

        if result:
            print(f"Virhe: nimi {screen_name} on jo varattu.")
            print("Valitse toinen nimi.\n")
        else:
            break

    insert_sql = "INSERT INTO game (screen_name) VALUES (%s)"
    cursor.execute(insert_sql, (screen_name,))
    connect.commit()

    player_id = cursor.lastrowid

    cursor.close()
    connect.close()

    Player.current_player = Player(screen_name, player_id)

    print("Kuulet kuulutuksen: lentosi lähtee pian. Valitse oikea lento lentotaulusta. Kello on 7.32, ja kone nousee ilmaan jo 12 minuutin kuluttua!")

    game_loop()