#Kirjoita ohjelma,
# joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
import mysql.connector
import geopy
from geopy.distance import geodesic


yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="joona",
    password="500-Series",
    autocommit=True
)

def kahden_lentokoneaseman_etaisyys():
    asema1 = str(input("Anna ensimmäisen aseman ICAO-koodi: "))
    asema2 = str(input("Anna toisen aseman ICAO-koodi: "))
    sql = f"select longitude_deg,latitude_deg from airport where ident='{asema1}' "
    sql2 = f"select longitude_deg,latitude_deg from airport where ident='{asema2}' "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchone()
    kursori.execute(sql2)
    tulos2 = kursori.fetchone()
    print((tulos1[0],tulos1[1]),(tulos2[0],tulos2[1]))
    print(geodesic((tulos1[0],tulos1[1]),(tulos2[0],tulos2[1])).km)
kahden_lentokoneaseman_etaisyys()