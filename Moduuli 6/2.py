#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
def noppa(maksimiluku = int):
    return random.randint(1,maksimiluku)

def kuutone(maksimiluku = int):
    while True:
        luku = noppa(maksimiluku)
        print(luku)
        if luku == maksimiluku:
            break

kuutone(20)