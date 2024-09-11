#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="joona",
    password="500-Series",
    autocommit=True
)
def hae_lentokone_tyypit(maakoodi):
    sql = f"select type, count(type) as 'lukumäärä' from airport where iso_country = '{maakoodi}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0][0],str(tulos[0][1]))
    print(tulos[1][0],str(tulos[1][1]))
    print(tulos[2][0],str(tulos[2][1]))
    print(tulos[3][0],str(tulos[3][1]))
    print(tulos[4][0],str(tulos[4][1]))

koodi = str(input("syötä maakoodi: "))

hae_lentokone_tyypit(koodi)