#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def listasumma (lista = []):
    summa = 0
    for luku in lista:
        summa = summa + luku
    return summa

lista = [1,2,3,4,5,6,7,8]
print(listasumma(lista))