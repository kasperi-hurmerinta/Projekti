from database.database_connection import database_connect as connection
connect = connection()

class Player:
    current_player = None

    def __init__(self, screen_name, id, pisteet=0, location="EFHK"):
        self.screen_name = screen_name
        self.id = id
        self.score = pisteet
        self.location = location
        self.route = None
    
    def addScore(self, score):
        cursor = connect.cursor()
        self.score += score
        update_sql = "UPDATE game SET pisteet = %s WHERE id = %s"
        cursor.execute(update_sql, (self.score, self.id))
        connect.commit()
        cursor.close()

    def setLocation(self, location):
        cursor = connect.cursor()
        self.location = location
        update_sql = "UPDATE game SET location = %s WHERE id = %s"
        cursor.execute(update_sql, (location, self.id))
        connect.commit()
        cursor.close()
        
    def setScore(self):
        cursor = connect.cursor()
        pull_score_sql = "SELECT pisteet FROM game WHERE id = %s"
        cursor.execute(pull_score_sql, (self.id,))
        result = cursor.fetchone()
        cursor.close()
        self.score = result[0] if result else 0
        
    def setRoute(self, route):
        cursor = connect.cursor()
        update_sql = "UPDATE game SET route = %s WHERE id = %s"
        cursor.execute(update_sql, (route, self.id))
        connect.commit()
        cursor.close()
        self.route = route        
    
    def getScore(self):
        return self.score
    
    def getLocation(self):
        return self.location
    
    def getRoute(self):
        return self.route