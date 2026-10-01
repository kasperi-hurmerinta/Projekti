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

    while True:
        print(plane_art)
        print("1.Uusi peli")
        print("2.Jatka peliä")
        print("3.Ohjeet")
        print("4.Lopeta")

        selection = input("Valitse toiminto: ")

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
                return
            case _:
                print("Virheellinen valinta! Valitse luku 1-4 väliltä.")