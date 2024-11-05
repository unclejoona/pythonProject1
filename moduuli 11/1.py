#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.


class julkaisu():
    def __init__(self,nimi):
        self.nimi = nimi

class kirja(julkaisu):
    def __init__(self,nimi,kirjailija,sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
    def tulosta(self):
        print(self.nimi,"(Kirjailija",self.kirjailija,",", self.sivumaara, "sivua)")

class lehti(julkaisu):
    def __init__(self,nimi,toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja
    def tulosta(self):
        print(self.nimi,"(Päätoimittaja",self.toimittaja+")")

kirja = kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = lehti("Aku Ankka", "Aki Hyyppä")
kirja.tulosta()
lehti.tulosta()



