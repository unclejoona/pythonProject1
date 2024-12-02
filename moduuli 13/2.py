#oteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
from flask import Flask,request
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='joona',
         password='500-Series',
         autocommit=True
         )
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    sql = f"select ident,name,municipality from airport where ident=%s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql,(icao,))
    tulos = cursor.fetchone()
    print(tulos['name'], tulos['municipality'])
    return { 'ICAO':tulos['ident'], 'name': tulos['name'], 'municipality':tulos['municipality']}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port='3000')
