from main.player import Player
from functions.flightRoutes import flightroutes
from functions.randomEvents import EVENTS
import random
from time import sleep

def game_loop():
    route = random.choice(list(flightroutes.keys()))
    Player.current_player.setRoute(route)
    game()

def game():
    player = Player.current_player
    route_list = flightroutes.get(player.getRoute())

    if route_list is None:
        print("Tallennetulla pelillä ei ole reittiä. Aloita uusi peli.")
        return

    if player.getLocation() not in route_list[1:]:
        if not departure_gate(route_list[1]):
            return
        print(f"Laskeudut lentoasemalle: {route_list[1]}")
        player.setLocation(route_list[1])

    while True:
        location = player.getLocation()
        index = route_list.index(location)
        print(f"Olet kohteessa {location} ({index}/{len(route_list) - 1}).")

        if not question_randomizer():
            return

        if index == len(route_list) - 1:
            end_game(player)
            return

        next_location = route_list[index + 1]
        print(f"Lennetään seuraavaksi kohteeseen {next_location}...")
        player.setLocation(next_location)


def departure_gate(kohde):
    lentotaulu = f"""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                 HELSINKI-VANTAAN LENTOLÄHTÖTAULU                     ║
    ║                         KELLO 07:32                                  ║
    ╠════════════╦══════════════════════╦══════════╦══════════╦════════════╣
    ║ LENTO      ║ KOHDE                ║ LÄHTÖ    ║ PORTTI   ║ TILA       ║
    ╠════════════╬══════════════════════╬══════════╬══════════╬════════════╣
    ║ AY 104     ║ Tukholma             ║ 07:38    ║ 12       ║ LÄHTENYT   ║
    ║ FR 219     ║ Lontoo               ║ 08:05    ║ 18       ║ ODOTTAA    ║
    ║ AY 532     ║ Oulu                 ║ 08:21    ║  6       ║ ODOTTAA    ║
    ║ FI 847     ║ {kohde:<20} ║ 07:45    ║  4       ║ PORTILLA   ║
    ╚════════════╩══════════════════════╩══════════╩══════════╩════════════╝
    """
    
    print(lentotaulu)

    if input("Anna portin numero: ") != "4":
        print("Väärä portti. Myöhästyit lennolta.")
        return False

    print("Oikein! Ehdit portille ja pääset koneeseen.")
    print("Lentokone käynnistää moottorit...")
    sleep(1.5)
    print("Lentokone rullaa kiitotielle ja nousee ilmaan!")
    return True


def question_randomizer():
    kierroksen_kysymykset = random.sample(list(EVENTS.values()), 3)

    for kysymys in kierroksen_kysymykset:
        print(kysymys["kysymys"])
        for vaihtoehto in kysymys["kysymykset"]:
            print(vaihtoehto)
        print("\n0. Palaa päävalikkoon")

        vastaus = input("Vastauksesi: ")

        if vastaus == "0":
            print("Peli tallennettu.")
            return False

        elif vastaus == str(kysymys["oikea_vastaus"] + 1):
            print(f"Oikein! Sait {kysymys['pisteet']} pistettä!")
            Player.current_player.addScore(kysymys["pisteet"])
            sleep(3)
        else:
            print("Väärin! Et saanut pisteitä.")

    return True


def end_game(player):
    print("Onneksi olkoon, reitti suoritettu!")

    putka_art = """
    
    _________________________
     |  |  |  |  |  |  |  | |
     |  |  |  |  |  |  |  | |
     |  |  |  |  |  |  |  | |
     |  |  |  |  |  |  |  | |
     |  |  |  |  |  |  |  | |
     |__|__|__|__|__|__|__|_|
     |                      |
     |   .-------------.    |
     |   |    PUTKA    |    |
     |   |             |    |
     |   |_____________|    |
     |______________________|
    
    """

    if player.getScore() >= 150:
        print("Selvisit kaikista kolmesta lentokentästä. Olet aivan poikki.")
        sleep(1.5)
        print("Et jaksa enää lähteä lennolle. Menet lentokentän hotelliin.")
        sleep(1.5)
        print("Pääset huoneeseen ja kaadut sänkyyn.")
        sleep(1.5)
        print("Aamulla heräät. Pää ei enää jomota. Vihdoin saat nukkua rauhassa. Olet voittanut pelin!")
        sleep(3)
    else:
        print("Et saanut tarpeeksi pisteitä.")
        sleep(1.5)
        print("Järjestyksenvalvojat odottavat sinua määränpäässä. He ottavat sinut kiinni.")
        sleep(1.5)
        print("He vievät sinut putkaan. Hävisit pelin! #GG")
        print(putka_art)
        sleep(3)

    print(f"Lopulliset pisteesi: {player.getScore()}")
