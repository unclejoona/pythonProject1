#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def parilliset(lista = []):
    for indeksi,luku in enumerate(lista):
        if luku % 2 != 0:
            lista.pop(indeksi)
    return lista

lista = [2,3,4,5,6,7,8]
print(parilliset(lista))