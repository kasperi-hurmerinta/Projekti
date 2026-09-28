from database.database_connection import database_connect as connection
from main.player import Player
from functions.flightRoutes import *
import random
from time import sleep
from functions.randomEvents import *

def random_destination():
    avain = random.choice(list(flightroutes.keys()))
    valittu_reitti = flightroutes[avain]

    ensimmainen_lentokentta = flightroutes[avain][1]
    toinen_lentokentta = flightroutes[avain][2]
    kolmas_lentokentta = flightroutes[avain][3]

    maaranpaa = flightroutes[avain][4]

    print(avain, valittu_reitti)
    print(ensimmainen_lentokentta, toinen_lentokentta, kolmas_lentokentta)

    return avain, valittu_reitti, ensimmainen_lentokentta, toinen_lentokentta, kolmas_lentokentta, maaranpaa

## en jaksa testata toimiiko mikään vittu - Kasperi

def question_randomizer():
    pelaajan_nimi = Player.current_player.screen_name
    kierroksen_kysymykset = random.sample(tehtavat_kolme_max, min(3, len(tehtavat_kolme_max)))
    
    for kysymys in kierroksen_kysymykset:
        print(kysymys["kysymys"])
        for vaihtoehto in kysymys["kysymykset"]:
            print(vaihtoehto)
        
        vastaus = input("Vastauksesi: ")
        
        if vastaus == str(kysymys["oikea_vastaus"] + 1):
            print(f"Oikein! Sait {kysymys['pisteet']} pistettä!")
            Player.current_player.addScore(kysymys["pisteet"])
        else:
            print("Väärin! Et saanut pisteitä.")

def game_loop():
    pelaajan_nimi = Player.current_player.screen_name
    
    route, valittu_lista, e_kentta, t_kentta, k_kentta, m_paa = random_destination()
    Player.current_player.setRoute(route)

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
    ║ FI 847     ║ {t_kentta}           ║ 07:45    ║  4       ║ PORTILLA   ║
    ╚════════════╩══════════════════════╩══════════╩══════════╩════════════╝
    """


    print(lentotaulu)

    lentotaulu_kysymys = input("Anna portin numero: ")

    if lentotaulu_kysymys == "4":
        print("Oikein! Ehdit portille ja pääset koneeseen.")
    else:
        print("Väärä portti. Myöhästyit lennolta.")
        return

    print("Lentokone käynnistää moottorit...")
    sleep(1.5)
    print("Lentokone rullaa kiitotielle ja nousee ilmaan!")

    ensimmainen_pysakki = e_kentta
    print(f"Laskeudut lentoasemalle: {ensimmainen_pysakki}")
    Player.current_player.setLocation(ensimmainen_pysakki)

    question_randomizer()

    toinen_pysakki = t_kentta
    print(f"Laskeudut lentoasemalle: {toinen_pysakki}")
    Player.current_player.setLocation(toinen_pysakki)

    question_randomizer()

    kolmas_pysakki = k_kentta
    print(f"Laskeudut lentoasemalle: {kolmas_pysakki}")
    Player.current_player.setLocation(kolmas_pysakki)

    question_randomizer()

## en tiiä oli vähän tylsää niin korjasin vähän tota looppia ei viel kyl tallenna mitään tietokantaan eikä mihinkään
## lisäksi pysäkit nyt antaa sen lentokentän identin eikä lentokentän nimeä