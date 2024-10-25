from random import randint
class Kilpailu():
    def __init__(self,nimi,pituus,autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(randint(-10,15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(vars(auto))
            #print("Rekisteri: ", auto.rekisteritunnus, "Nopeus: ", auto.nopeus, "Matka: ", auto.matka)
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

class Auto():
    def __init__(self,rekisteritunnus, huippunopeus, nopeus=0,matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def kiihdytä(self, nopeudenmuutos):
        temp = self.nopeus+nopeudenmuutos
        if(temp <= self.huippunopeus and temp>=0):
            self.nopeus += nopeudenmuutos
        elif temp > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus=0



    def kulje(self,tuntimäärä):
        self.matka += self.nopeus * tuntimäärä

autot = []
for i in range(10):
    rekisteri = "ABC-"+ str(i+1)
    autot.append(Auto(rekisteri, randint(100,200)))
voitto = False

while voitto == False:
    for auto in autot:
        auto.kiihdytä(randint(-10,15))
        auto.kulje(1)
        if(auto.matka >= 10000):
            voitto = True
for auto in autot:
    print("Rekisteri:",auto.rekisteritunnus, "Huippunopeus: ",auto.huippunopeus,"Nopeus:", auto.nopeus,"Matka:", auto.matka)


uudet_autot = []
for i in range(10):
    rekisteri = "ABC-"+ str(i+1)
    uudet_autot.append(Auto(rekisteri, randint(100,200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, uudet_autot)
print("TERVETULOA ", kilpailu.nimi+"in!")
tunti = 0
while kilpailu.kilpailu_ohi() == False:
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()
        print(tunti)

    kilpailu.tunti_kuluu()
print("Kilpailu ohi!, kului ", tunti, " tuntia")
kilpailu.tulosta_tilanne()