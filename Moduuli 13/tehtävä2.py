from flask import Flask, request, Response
import mysql.connector
import json

app = Flask(__name__)
@app.route("/kenttä/<ICAO>")

def get_airports(ICAO):
    
    try:
        sql = f"SELECT name, municipality FROM airport WHERE ident='{ICAO}';"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if tulos:
            name, municipality = tulos[0]
            vastaus = {
                "ICAO" : ICAO,
                "NAME" : name,
                "Municipality" : municipality
                }
        else:
            vastaus = {
                "Status": 404,
                "Virhe" : f"Lentoasemaa koodilla {ICAO} ei löytynyt."
            }
    except Exception as e:
            tilakoodi = 500
            vastaus = {
                "status" : tilakoodi,
                "vastaus" : f"Sisäinen palvelinvirhe",
                "kuvaus" : str(e)
            }
            
    jsonvast = json.dumps(vastaus, ensure_ascii=False) 
    return Response(response = jsonvast, mimetype="application/json; charset=utf-8")

    
@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus, ensure_ascii=False)
    return Response(response=jsonvast, status=404, mimetype="application/json")

yhteys = mysql.connector.connect(
         host='127.0.0.1', #"localhost" käy myös
         port= 3306,
         database='flight_game',
         user='',
         password='',
         charset="utf8mb4",
         collation="utf8mb4_unicode_ci",
         autocommit=True
         )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)