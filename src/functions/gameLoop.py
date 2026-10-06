from main.player import Player
from functions.flightRoutes import flightroutes
from functions.randomEvents import EVENTS
import random
from time import sleep
from database.database_connection import database_connect as connection

def game_loop():
    route = random.choice(list(flightroutes.keys()))
    Player.current_player.setRoute(route)
    game()

def icaokoodi_lentokentaksi(icao):

    connect = connection()
    cursor = connect.cursor()

    check_sql = "SELECT name FROM airport WHERE ident = %s"
    cursor.execute(check_sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connect.close()

    return result[0]

def icaokoodi_maaksi(icao):
    connect = connection()
    cursor = connect.cursor()

    check_sql = "SELECT country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE airport.ident = %s"
    cursor.execute(check_sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connect.close()

    return result[0]

def game():
    player = Player.current_player
    route_list = flightroutes.get(player.getRoute())

    if route_list is None:
        print("Tallennetulla pelillä ei ole reittiä. Aloita uusi peli.")
        return

    if player.getLocation() not in route_list[1:]:
        if not departure_gate(route_list[1]):
            return

        player.setLocation(route_list[1])
        lentokentan_nimi = icaokoodi_lentokentaksi(player.getLocation())
        print(f"Laskeudut lentoasemalle: {lentokentan_nimi}\n")
        sleep(3)

    while True:
        location = player.getLocation()
        index = route_list.index(location)
        lentokentan_nimi = icaokoodi_lentokentaksi(player.getLocation())
        print(f"Olet kohteessa {lentokentan_nimi} ({index}/{len(route_list) - 1}).")

        if not question_randomizer():
            return

        if index == len(route_list) - 1:
            end_game(player)
            return

        next_location = route_list[index + 1]
        seuraava_lentokentan_nimi = icaokoodi_lentokentaksi(next_location)
        print(f"Lennetään seuraavaksi kohteeseen {seuraava_lentokentan_nimi}...\n")
        player.setLocation(next_location)
        sleep(3)


def departure_gate(kohde):
    satunnainen_numero = random.randint(1,10)

    lentotaulu = f"""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                 HELSINKI-VANTAAN LENTOLÄHTÖTAULU                     ║
    ║                         KELLO 07:32                                  ║
    ╠════════════╦══════════════════════╦══════════╦══════════╦════════════╣
    ║ LENTO      ║ KOHDE                ║ LÄHTÖ    ║ PORTTI   ║ TILA       ║
    ╠════════════╬══════════════════════╬══════════╬══════════╬════════════╣
    ║ AY 104     ║ Stockholm            ║ 07:38    ║ 12       ║ LÄHTENYT   ║
    ║ FR 219     ║ London               ║ 08:05    ║ 18       ║ ODOTTAA    ║
    ║ AY 532     ║ Oulu                 ║ 08:21    ║ 6        ║ ODOTTAA    ║
    ║ {'FI 847':<11}║ {icaokoodi_maaksi(kohde):<21}║ {'07:45':<9}║ {satunnainen_numero:<9}║ {'PORTILLA':<11}║
    ╚════════════╩══════════════════════╩══════════╩══════════╩════════════╝
    """

    lentokone = f"""
                 __|__
          --o--o--(_)--o--o--
    """

    sleep(1.5)
    print(lentotaulu)

    if input("Anna portin numero: ") != str(satunnainen_numero):
        print("Väärä portti. Myöhästyit lennolta.")
        peli_valmis_poista_tiedot()
        return False

    print("Oikein! Ehdit portille ja pääset koneeseen.")
    print("Lentokone käynnistää moottorit...")
    sleep(1.5)
    print("Lentokone rullaa kiitotielle ja nousee ilmaan!")
    print(lentokone)
    sleep(1.5)
    print("Seuraavaksi pääset suorittamaan tehtäviä eri lentokentillä.")
    print("Jokaisesta tehtävästä saat 22 pistettä. Kerää vähintään 150 pistettä, niin voitat pelin ennen viimeistä lentokenttää! \n")
    sleep(5)
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
            print(f"Oikein! Sait {kysymys['pisteet']} pistettä! \n")
            Player.current_player.addScore(kysymys["pisteet"])
            sleep(1.5)
        else:
            print("Väärin! Et saanut pisteitä. \n")
            sleep(1.5)

    return True

def peli_valmis_poista_tiedot():
    player = Player.current_player.screen_name

    connect = connection()
    cursor = connect.cursor()

    check_sql = "DELETE FROM game WHERE screen_name = %s"
    cursor.execute(check_sql, (player,))
    connect.commit()

    cursor.close()
    connect.close()

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
        peli_valmis_poista_tiedot()
    else:
        print("Et saanut tarpeeksi pisteitä.")
        sleep(1.5)
        print("Järjestyksenvalvojat odottavat sinua määränpäässä. He ottavat sinut kiinni.")
        sleep(1.5)
        print("He vievät sinut putkaan. Hävisit pelin! #GG")
        print(putka_art)
        sleep(3)
        peli_valmis_poista_tiedot()

    print(f"Lopulliset pisteesi: {player.getScore()}. Päävalikko avautuu (5) sekunnin päästä.")
    sleep(5)


