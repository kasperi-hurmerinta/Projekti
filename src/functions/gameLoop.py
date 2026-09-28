from database.database_connection import database_connect as connection
from main.player import Player
from flightRoutes import *
import random
from time import sleep

pelaajan_nimi = Player.current_player.screen_name

def check_points():
    connect = connection()
    check_sql = f"SELECT pisteet FROM game WHERE screen_name = '{pelaajan_nimi}'"
    cursor = connect.cursor()
    cursor.execute(check_sql)
    result = cursor.fetchone()

    if result is not None and result[0] >= 150:
        return True

    cursor.close()
    connect.close()

    return False

def update_location(Player, new_location):
    Player.location = new_location

    connect = connection()
    cursor = connect.cursor()

    cursor.execute("UPDATE game SET location = %s WHERE id = %s", (new_location, Player.id))
    connect.commit()
    cursor.close()
    connect.close()

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

def game_loop():
    arvo_kohteet = random_destination()

    def flight_panel():
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
    ║ FI 847     ║ {arvo_kohteet}       ║ 07:45    ║  4       ║ PORTILLA   ║
    ╚════════════╩══════════════════════╩══════════╩══════════╩════════════╝
    """
        return lentotaulu

    ensimmainen_lentokentta = "EFHK"

    while True:
        print(flight_panel())

        lentotaulu_kysymys = input("Anna portin numero: ")

        if lentotaulu_kysymys == "4":
            print("Oikein! Ehdit portille ja pääset koneeseen.")
        else:
            print("Väärä portti. Myöhästyit lennolta.")
            break

    print("Lentokone käynnistää moottorit...")
    sleep(1.5)
    print("Lentokone rullaa kiitotielle ja nousee ilmaan!")

    ensimmainen_pysakki = arvo_kohteet[1]
    print(f"Laskeudut lentoasemalle: {ensimmainen_pysakki}")
    update_location(pelaajan_nimi, f"{ensimmainen_pysakki}")

    toinen_pysakki = arvo_kohteet[2]
    print(f"Laskeudut lentoasemalle: {toinen_pysakki}")
    update_location(pelaajan_nimi, f"{toinen_pysakki}")

    kolmas_pysakki = arvo_kohteet[3]
    print(f"Laskeudut lentoasemalle: {kolmas_pysakki}")
    update_location(pelaajan_nimi, f"{kolmas_pysakki}")


    if tarkista_pisteet():
        print("bläh bläh bläh")

## en tiiä oli vähän tylsää niin korjasin vähän tota looppia ei viel kyl tallenna mitään tietokantaan eikä mihinkään
## lisäksi pysäkit nyt antaa sen lentokentän identin eikä lentokentän nimeä