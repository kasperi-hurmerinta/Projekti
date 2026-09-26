def instructions_game():
    print("""
    
Tavoite:
Kerää vähintään 150 pistettä yhteensä.

Pelin kulku:
Valitse oikea lento pelin alussa.
Suorita tehtäviä ja kerää pisteitä lentokentiltä.
Saavu määränpäähän.

Huom:
Väärä lento alussa = häviö.
Alle 150 pistettä = häviö.
""")
    player_ready = input("Oletko lukenut ohjeet?: Y/N ")
    if player_ready.lower() == "y":
        print("Hienoa! Palataan päävalikkoon.")
        from functions.mainScreen import main_screen
        main_screen()
    else:
        print("Lue ohjeet huolellisesti ennen kuin jatkat.")
        instructions_game()
    #Ohjeitten jälkeen voisi kutsua uudestaan main_screen() funktiota kun hän sitä haluaa. Eli kysytään inputilla haluaako hän palata päävalikkoon. Jotain tyyliin "Oletko lukenut ohjeet?: Y/N" - Daniel