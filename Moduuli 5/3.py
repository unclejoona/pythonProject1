import math

luku = int(input("Syötä luku: "))
alkuluku = True
numerot = math.floor(math.sqrt(luku))
for i in range(2,numerot+1):
    if luku % i == 0:
        print("luku ei ole alkuluku")
        alkuluku = False
        break
if alkuluku is True:
    print("Luku on alkuluku")