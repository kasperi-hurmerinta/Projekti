from database.database_connection import database_connect as connection
current_player = None
connect = connection()

class Player:
    def __init__(self, screen_name, id, pisteet=0, location="EFHK"):
        self.screen_name = screen_name
        self.id = id
        self.score = pisteet
        self.location = location
        self.route = None
    
    def addScore(self, score):
        cursor = connect.cursor()
        self.score += score
        update_sql = f"UPDATE game SET pisteet = {self.score} WHERE id = {self.id}"
        cursor.execute(update_sql)
        connect.commit()
        cursor.close()
        connect.close()

    def setLocation(self, location):
        cursor = connect.cursor()
        self.location = location
        update_sql = f"UPDATE game SET location = '{location}' WHERE id = {self.id}"
        cursor.execute(update_sql)
        connect.commit()
        cursor.close()
        connect.close()
        
    def setScore(self):
        cursor = connect.cursor()
        pull_score_sql = f"SELECT pisteet FROM game WHERE id = {self.id}"
        cursor.execute(pull_score_sql)
        result = cursor.fetchone()
        cursor.close()
        connect.close()
        self.score = result[0] if result else 0
        
    def setRoute(self, route):
        cursor = connect.cursor()
        update_sql = f"UPDATE game SET route = '{route}' WHERE id = {self.id}"
        cursor.execute(update_sql)
        connect.commit()
        cursor.close()
        connect.close()
        self.route = route        
    
    def getScore(self):
        return self.score
    
    def getLocation(self):
        return self.location

## Eikö tähän olioon kannata myös tallentaa pisteet sekä sijainti niin ei tarvitse tehdä funktiota esim. (tarkista_pisteet) ? - Kasperi