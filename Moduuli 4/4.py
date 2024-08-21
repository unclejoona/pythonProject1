import random

numero = random.randint(1,10)

while True:
    luku = int(input("Heitä arvaus:"))
    if luku == numero:
        print("Oikein!")
        break
    elif luku > numero:
        print("Pienempi")
    else:
        print("Suurempi")