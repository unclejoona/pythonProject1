import random


N = int(input("Anna pisteiden kokonaismäärä: "))
n = 0
indeksi = 0.0

while indeksi < N:
    indeksi += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(str(indeksi), end='\r')
    if x**2 + y**2 <= 1:
        n += 1

print( 4*n/N )
