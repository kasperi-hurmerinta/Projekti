current_player = None

class Player:
    def __init__(self, screen_name, id, score, location):
        self.screen_name = screen_name
        self.id = id
        self.score = score
        self.location = location

## Eikö tähän olioon kannata myös tallentaa pisteet sekä sijainti niin ei tarvitse tehdä funktiota esim. (tarkista_pisteet) ? - Kasperi