from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route("/alkuluku/<luku>")

def alkuluku(luku):

    alku = True
    
    if alku:    
        try:
            luku = int(luku)
            for i in range(2, luku):
                if luku % i == 0:
                    alku = False
                    break
            
               
            vastaus = {
                "Number" : luku,
                "isPrime" : alku
            }
        
        except ValueError:
            tilakoodi = 400
            vastaus = {
                "status" : tilakoodi,
                "vastaus" : f"Virheellinen syöte: {luku}"
            }
            
        jsonvast = json.dumps(vastaus, ensure_ascii=False) # Varmistetaan että tulostetaan ääkköset
        return Response(response = jsonvast, mimetype="application/json; charset=utf-8")

    
@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus, ensure_ascii=False)
    return Response(response=jsonvast, status=404, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)