import json
import requests


import requests


API_KEY = #"YourApiKeyHere"



kaupunki = input("\nSyötä kaupunki josta haluat säätietoja: ").strip().title()


url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Säätila kaupungissa: {kaupunki}\n   {data['weather'][0]['description']}")
        print(f"Lämpötila: {data ['main']['temp']} C")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")   
except NameError:
    print(f"\nKirjoittamaasi kaupunkia {kaupunki} ei löytynyt.")

