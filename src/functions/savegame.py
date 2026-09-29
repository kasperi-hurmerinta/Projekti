from database.database_connection import database_connect as connection

def savegame(screen_name, pisteet, location):

    connect = connection()
    cursor = connect.cursor()

    sql = """
    UPDATE game
    SET pisteet = %s,
    location = %s
    WHERE screen_name = %s
    """

    cursor.execute(sql,(pisteet, location, screen_name))

    connect.commit()

    print("Peli tallennettu onnistuneesti.")

    cursor.close()
    connect.close()