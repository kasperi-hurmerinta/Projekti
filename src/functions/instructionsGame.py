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
        return
    else:
        print("Lue ohjeet huolellisesti ennen kuin jatkat.")
        instructions_game()