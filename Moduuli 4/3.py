lista = []

while(True):
    syote = input("Syötä numero:")
    if syote == "":
        break
    syote = int(syote)
    lista.append(syote)
lista.sort()
print("Suurin:" + str(lista[-1]) + "\nPienin:" + str(lista[0]))