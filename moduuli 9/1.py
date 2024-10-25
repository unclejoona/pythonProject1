from random import randint
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
