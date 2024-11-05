#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
# sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

class Auto():
    def __init__(self,rekisteritunnus, huippunopeus, nopeus=0,matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def kiihdyta(self, nopeudenmuutos):
        temp = self.nopeus+nopeudenmuutos
        if(temp <= self.huippunopeus and temp>=0):
            self.nopeus += nopeudenmuutos
        elif temp > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus=0
    def kulje(self,tuntimaara):
        self.matka += self.nopeus * tuntimaara

class Sahkoauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.kapasiteetti = akkukapasiteetti
class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,bensatankki):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bensa = bensatankki

Sauto = Sahkoauto("ABC-15",180,52.5)
Mauto = Polttomoottoriauto("ACD-123",165,32.3)
Sauto.kiihdyta(20)
Mauto.kiihdyta(30)
for i in range(3):

    Sauto.kulje(1)
    Mauto.kulje(1)
    print(f"""
                        Matka   Nopeus
    Sähköauto           {Sauto.matka}       {Sauto.nopeus}
    Polttomoottoriauto  {Mauto.matka}       {Mauto.nopeus}""")
