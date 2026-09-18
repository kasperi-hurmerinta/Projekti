def main_screen():

    lentokone_art = """
            ______
            _\ _~-\___
    =  = ==(____AA____D     Finn in air
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
"""
    while True:
        print(lentokone_art)
        print("1.Uusi peli")
        print("2.Jatka peliä")
        print("3.Ohjeet")
        print("4.Lopeta")

        valinta = input("Valitse toiminto: ")
        if valinta == "1":
            print("Aloitetaan uusi peli!")
            New_game()
            break

        elif valinta == "2":
            print("Valitse peli!")
            load_game()
            break

        elif valinta == "3":
            instructions_game()
            break

        elif valinta == "4":
            print("Kiitos pelaamisesta. Näkemiin!")
            break

        else:
            print("Virheellinen valinta! Valitse luku 1-4 väliltä.")

