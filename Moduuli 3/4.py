vuosi = int(input("Anna vuosiluku:"))
if(vuosi % 4 == 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi")