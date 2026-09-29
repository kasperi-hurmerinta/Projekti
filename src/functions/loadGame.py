from database.database_connection import database_connect as connection
from main.player import Player
from functions.gameLoop import game

def load_game():
    screen_name = input("Anna pelaajanimesi: ")

    connect = connection()
    cursor = connect.cursor()

    check_sql = "SELECT id, pisteet, location, route FROM game WHERE screen_name = %s"
    cursor.execute(check_sql, (screen_name,))
    result = cursor.fetchone()

    if not result:
        print(f"Virhe: nimeä {screen_name} ei löytynyt!")

        cursor.close()
        connect.close()
        return

    player_id, pisteet, location, route = result

    Player.current_player = Player(screen_name, player_id, pisteet, location)
    Player.current_player.route = route

    cursor.close()
    connect.close()

    game()
