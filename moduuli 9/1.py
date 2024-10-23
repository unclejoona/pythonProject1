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


auto = Auto("ABC-1", randint(100,200))
print(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka)

auto2 = Auto("ABC-2",randint(100,200))
print(auto2.rekisteritunnus, auto2.huippunopeus, auto2.nopeus, auto2.matka)

while auto.matka < 10000 and auto2.matka < 10000:
    auto.kiihdytä(randint(-10,15))
    auto2.kiihdytä(randint(-10,15))
    auto.kulje(1)
    auto2.kulje(1)
    print("auto1:", auto.nopeus,auto.matka)
    print("auto2:", auto2.nopeus,auto2.matka)
print("rekisteritunnus: ",auto.rekisteritunnus,"Huippunopeus:",auto.huippunopeus,"Nopeus:",auto.nopeus,"Matka:",auto.matka)
print("rekisteritunnus: ",auto2.rekisteritunnus,"Huippunopeus:",auto2.huippunopeus,"Nopeus:",auto2.nopeus,"Matka:",auto2.matka)

print((auto.rekisteritunnus if auto.matka >= 10000 else auto2.rekisteritunnus), "voitti!")