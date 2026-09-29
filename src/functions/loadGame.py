from database.database_connection import database_connect as connection
from main.player import Player

def load_game():
    screen_name = input("Anna pelaajanimesi: ")

    connect = connection()
    cursor = connect.cursor()

    sql = """
    SELECT id, screen_name, pisteet
    FROM game
    WHERE screen_name = %s
    """

    cursor.execute(sql, (screen_name,))
    result = cursor.fetchone()

    if not result:
        print(f"Virhe: nimeä {screen_name} ei löytynyt!")

        cursor.close()
        connect.close()
        return

    player_id = result[0]
    pisteet = result[2]

    Player.current_player = Player(screen_name, player_id)


    Player.current_player.score = pisteet

    cursor.close()
    connect.close()

    print(f"Peli ladattu.")
