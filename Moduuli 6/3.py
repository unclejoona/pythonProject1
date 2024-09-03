#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

    #Yksi gallona on 3,785 litraa.

def litra_muuntaja(Gallona):
    litra = 3.785
    return Gallona * litra


luku = int(input("Anna gallonamäärä:"))

while luku >= 0:
    print(litra_muuntaja(luku))
    luku = int(input("Anna gallonamäärä:"))
    