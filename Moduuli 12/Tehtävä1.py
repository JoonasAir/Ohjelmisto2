import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"

answer = input("\nWrote (Y) if you want to hear Chuck Norris joke: ").upper()
vastaus = requests.get(pyyntö).json()

try:
    request = requests.get(pyyntö)
    if request.status_code==200:
        if answer == "Y":
            vastaus = requests.get(pyyntö).json()
            print(f"\n{vastaus['value']}")
        else:
            print("Good bye..")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")            