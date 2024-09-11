#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)
def add(kirjasto):
    koodi = str(input("Mikä on lentoaseman ICAO-koodi: "))
    nimi = str(input("Mikä on lentoaseman nimi: "))
    kirjasto[str(koodi)] = str(nimi)
    return kirjasto

def search(kirjasto):
    koodi = str(input("Mikä on lentoaseman ICAO-koodi?: "))
    lentoasema = kirjasto[koodi]
    print(lentoasema)

kirjasto = {}
options = {"add": add, "search": search}
while True:
    komento = str(input("Syötä komento (add/search/lopeta): "))
    if(komento == "lopeta"):
        print("Kiitos")
        break
    options[komento](kirjasto)
