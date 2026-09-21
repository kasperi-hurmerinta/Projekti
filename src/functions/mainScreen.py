from functions.introGame import intro_game
from functions.loadGame import load_game
from functions.instructionsGame import instructions_game

def main_screen():
    plane_art = '''
            ______
            _( _~-)___
    =  = ==(____AA____D     Finn in air
                /_____/___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |)_
                `~-.__        ___..----..                  )
                      `---~~)___________(------------`````
                      =  ===(_________D
    '''
    # Tässä oli ennen while True, ja ennen match case tehtiin jokaisen if lauseen jälkeen break, eli kutsuttiin funktio ja suljettiin tää while breakillä... Miksi?
    print(plane_art)
    print("1.Uusi peli")
    print("2.Jatka peliä")
    print("3.Ohjeet")
    print("4.Lopeta")

    selection = input("Valitse toiminto: ")

    # Käytetään match-case -rakennetta valinnan käsittelyyn sillä if lauseet vievät liikaa tilaa ja tekevät koodista vaikealukuista. Match-case on myös helpompi laajentaa tulevaisuudessa. Ite oot AI
    match selection:
        case "1":
            print("Aloitetaan uusi peli!")
            intro_game()
        case "2":
            print("Valitse peli!")
            load_game()
        case "3":
            instructions_game()
        case "4":
            print("Kiitos pelaamisesta. Näkemiin!")
        case _:
            print("Virheellinen valinta! Valitse luku 1-4 väliltä.")