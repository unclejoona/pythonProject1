#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.
setti = {}
while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi in setti:
        print("Aiemmin syötetty nimi")
        setti[nimi] = setti[nimi]+1
        print(setti[nimi])
    else:
        setti[nimi] = 1
        print("Uusi nimi")

sortedsetti = dict(sorted(setti.items()))

for nimi in sortedsetti :
    print(nimi, sortedsetti[nimi])