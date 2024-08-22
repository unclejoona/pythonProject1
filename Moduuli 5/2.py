
lista = []
luku = input("Syötä luku: ")
while luku:
    lista.append(int(luku))
    luku = input("Syötä luku: ")

else:
    lista.sort(reverse=True)
    for i in lista[0:5]:
        print(i)