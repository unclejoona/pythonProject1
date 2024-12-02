from flask import Flask, request
import math

#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa:

app = Flask(__name__)
@app.route('/alkuluku/<numero>')
def alkuluku(numero):
    numero = int(numero)
    juuri = math.floor(math.sqrt(numero))
    isprime = True
    for i in range(2,juuri):
        if (numero % i == 0):
            isprime = False
    return {"Number": numero, "isPrime":isprime}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)