from time import sleep
from functions.newGame import new_game

def intro_game():
    airport_art = '''
          .--.                                          .--.
       .-(    ).                 __|__              .-(    ).
      (___.__)__)        --o--o--(_)--o--o--       (___.__)__)

                                                        |
                                                     [=====]
                                                     |[] []|
       ______________________________________        I_____I
      | L E N T O K E N T T Ä               |         | |
      | [] [] [] [] [] [] [] [] [] [] [] [] |         | |
      |______________________________________|_________| |____

      ============================================================
         ----    ----    ----    ----    ----    ----    ----
      ============================================================
    '''

    print(airport_art)
    print("Uhhh... Päätä jomottaa kuin joku löisi sitä vasaralla.")
    sleep(3)
    print("Avaat silmäsi. Makaat kovalla penkillä keskellä lentokenttää!")
    sleep(3)
    print("Missä minä olen? Kädessäsi on viinapullo.")
    sleep(3)
    print("Kello on 7.32, ja portti sulkeutuu 7.45!")
    sleep(3)
    print("Nyt pitää mennä, on kiire!")

    new_game()