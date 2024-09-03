#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def pizza(halkaisija,euro):
    pintaala = math.pi * ((halkaisija)/200)**2
    return euro/pintaala

pizzahalk = int(input("Syötä pizzan halkaisija: "))
euro = int(input("Syötä pizzan hinta: "))
eka = pizza(pizzahalk,euro)
pizzahalk = int(input("Syötä toisen pizzan halkaisija: "))
euro = int(input("Syötä toisen pizzan hinta: "))
toka = pizza(pizzahalk,euro)

if(eka > toka):
    print("toka on halvempi kuin eka: " + str(toka) + " euroa per neliömetri")
else:
    print("Eka on halvempi kuin toka: " + str(eka) + " euroa per neliömetri")