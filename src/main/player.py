from database.database_connection import database_connect as connection
current_player = None

class Player:
    def __init__(self, screen_name, id, pisteet=0, location="EFHK"):
        self.screen_name = screen_name
        self.id = id
        self.score = pisteet
        self.location = location
    
    def addScore(self, score):
        connect = connection()
        cursor = connect.cursor()
        self.score += score
        update_sql = f"UPDATE game SET pisteet = {self.score} WHERE id = {self.id}"
        cursor.execute(update_sql)
        connect.commit()
        cursor.close()
        connect.close()

    def setLocation(self, location):
        connect = connection()
        cursor = connect.cursor()
        self.location = location
        update_sql = f"UPDATE game SET location = '{location}' WHERE id = {self.id}"
        cursor.execute(update_sql)
        connect.commit()
        cursor.close()
        connect.close()
    
    def getScore(self):
        return self.score
    
    def getLocation(self):
        return self.location

## Eikö tähän olioon kannata myös tallentaa pisteet sekä sijainti niin ei tarvitse tehdä funktiota esim. (tarkista_pisteet) ? - Kasperi