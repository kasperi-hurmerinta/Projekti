from database.database_connection import database_connect as connection
import player

def load_game():
    connect = connection()
    check_sql = f"SELECT screen_name FROM game WHERE screen_name = '{player.current_player.screen_name}'"
    cursor = connect.cursor()
    cursor.execute(check_sql)
    result = cursor.fetchone()
    cursor.close()
    connect.close()

    if not result:
        print(f"virhe: nimi {player.current_player.screen_name} on virheellinen!")
        return
    
    print(f"Testi: {player.current_player.screen_name}")