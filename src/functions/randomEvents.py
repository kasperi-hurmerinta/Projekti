import random

EVENTS = {
    "bensa": {
        "kysymys" : "Mitä polttoainetta lentokone käyttää?",
        "kysymykset" : ["(1.) Kerosiini", "(2.) Diesel", "(3.) 95E", "(4.) 98E"],
        "oikea_vastaus" : 0,
        "pisteet": 22,
        "tapahtuma_id": 1,
    },

    "palvelu_koira": {
        "kysymys": "Avustajakoira odottaa lähtöselvitystiskillä matkustajan kanssa. Mitä teet?",
        "kysymykset": ["(1.) Päästät koiran mukaan normaalisti, se on työkoira", "(2.) Kiellät koiran pääsyn kentälle", "(3.) Pyydät koiraa häkkiin", "(4.) Ohjaat matkustajan pois jonosta"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 2,
    },

    "turvatarkastus_kielletty_esine": {
        "kysymys": "Turvatarkastuksessa matkustajan käsimatkatavarasta löytyy saksia. Mitä teet?",
        "kysymykset": ["(1.) Tarkistat terän pituuden sääntöjen mukaan", "(2.) Päästät esineen läpi kysymättä", "(3.) Annat matkustajan pitää ne kädessään koneessa", "(4.) Kutsut poliisin heti paikalle"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 3,
    },

    "matkatavarat_kadonnut": {
        "kysymys": "Matkustajan matkalaukku ei löydy hihnalta laskeutumisen jälkeen. Mitä teet?",
        "kysymykset": ["(1.) Ohjaat matkustajan kadonneiden tavaroiden palvelupisteeseen", "(2.) Sanot, ettei sinulla ole aikaa", "(3.) Käsket etsiä itse koko kentältä", "(4.) Pyydät unohtamaan asian"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 4,
    },

    "lento_myohastyy": {
        "kysymys": "Lento on myöhässä sään vuoksi. Mitä ilmoitat matkustajille?",
        "kysymykset": ["(1.) Ajantasaisen tiedon uudesta lähtöajasta", "(2.) Et ilmoita mitään", "(3.) Väärän lähtöajan", "(4.) Että lento on peruttu vaikka ei ole"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 5,
    },

    "portille_myohassa": {
        "kysymys": "Matkustaja saapuu lähtöportille juuri ennen sen sulkeutumista. Mitä teet?",
        "kysymykset": ["(1.) Päästät matkustajan nopeasti läpi, jos aikaa vielä on", "(2.) Suljet portin heti näkemättä matkustajaa", "(3.) Käsket matkustajan odottaa seuraavaa lentoa ilman syytä", "(4.) Jätät portin auki loputtomiin"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 6,
    },

    "portti_vaihtuu": {
        "kysymys": "Lentosi lähtöportti on vaihtunut. Mitä teet?",
        "kysymykset": ["(1.) Tarkistat uuden portin ja lähdet sinne", "(2.) Jäät odottamaan vanhalle portille", "(3.) Menet lähimmälle portille", "(4.) Päätät lähteä kotiin"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 7,
    },

    "lompakko_lattialla": {
        "kysymys": "Löydät lompakon lentokentän lattialta. Mitä teet?",
        "kysymykset": ["(1.) Viet sen löytötavarapisteelle", "(2.) Laitat sen omaan taskuusi", "(3.) Jätät sen lattialle", "(4.) Annat sen ensimmäiselle vastaantulijalle"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 8,
    },

    "viimeinen_kutsu": {
        "kysymys": "Lentosi viimeinen kuulutus alkaa. Mitä teet?",
        "kysymykset": ["(1.) Menet heti oikealle lähtöportille", "(2.) Jäät vielä ostamaan eväitä", "(3.) Menet odottamaan väärälle portille", "(4.) Jäät selvittämään, mistä kuulutus tuli"],
        "oikea_vastaus": 0,
        "pisteet": 22,
        "tapahtuma_id": 9,
    },
}

## nyt saa yhteensä max jotain 200 pistettä.