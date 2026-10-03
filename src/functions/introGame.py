from time import sleep

from functions.gameLoop import game_loop
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
    sleep(1.5)
    print("Avaat silmäsi. Makaat kovalla penkillä keskellä lentokenttää!")
    sleep(1.5)
    print("Missä minä olen? Kädessäsi on viinapullo.")
    sleep(1.5)
    print("Minulla on kiire, pitää äkkiä päästä lennolle! Portti sulkeutuu 12 minuutin päästä.")
    sleep(1.5)
    print("Nyt pitää mennä!")

    # Kun mä testailin tätä projektii pikkasen, niin toi sleep(3) on vähä liian pitkä. Kanttii varmaan pistää sleep(1.5), ainakin kokeiluun, kattokaa ite, ei mul o välii - Daniel

    new_game()