import mysql.connector
#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='joona',
         password='500-Series',
         autocommit=True
         )

def hae_lentokontta_icao_koodilla(icao):
    sql = f"select name,municipality from airport where ident=%s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql,(icao,))
    tulos = cursor.fetchone()
    print(tulos['name'], tulos['municipality'])
icao = str(input("Syötä ICAO-koodi: "))
hae_lentokontta_icao_koodilla(icao)