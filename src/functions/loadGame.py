from database.database_connection import database_connect as connection
from main.player import Player

def load_game():
    screen_name = input("Anna pelaaja nimesi: ")
    connect = connection()
    check_sql = f"SELECT screen_name FROM game WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(check_sql)
    result = cursor.fetchone()
    cursor.close()
    connect.close()

    if not result:
        print(f"virhe: nimi {screen_name} on virheellinen!")
        return

    Player.current_player = Player(screen_name, cursor.lastrowid)

    print(f"Testi: {screen_name}")