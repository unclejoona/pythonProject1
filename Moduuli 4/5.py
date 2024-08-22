kayttajatunnus = str(input("Anna käyttäjätunnus:"))
salasana = str(input("Anna salasana:"))
i = 0
while kayttajatunnus != "python" or salasana != "rules":
    if i == 5:
        print("Pääsy evätty")
        break
    else:
        i += 1
    kayttajatunnus = str(input("Yritys " + str(i) + ". Anna käyttäjätunnus:"))
    salasana = str(input("Anna salasana:"))

else:
    print("Tervetuloa")
