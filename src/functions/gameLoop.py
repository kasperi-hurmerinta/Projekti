from database.database_connection import database_connect as connection
from main.player import Player
from flightRoutes import *
import random
pelaajan_nimi = Player.current_player.screen_name

def tarkista_pisteet():
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

    ensimmainen_pysakki = arvo_kohteet[1]
    toinen_pysakki = arvo_kohteet[2]
    kolmas_pysakki = arvo_kohteet[1]

    ensimmainen_lentokentta = "Helsinki-Vantaa Lentokenttä"

    while True:
        flight_panel()

        lentotaulu_kysymys = input("Anna portin numero: ")

        if lentotaulu_kysymys != 4:
            print("bläh bläh bläh")
            break




    if tarkista_pisteet():
        print("bläh bläh bläh")
