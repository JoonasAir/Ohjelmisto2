import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"

answer = input("\nDo you want to hear Chuck Norris Joke? (Y)(N)").upper()

vastaus = requests.get(pyyntö).json()
while answer != "N":
    if answer == "Y": 
        vastaus = requests.get(pyyntö).json()
        print(vastaus["value"])
        answer = input("\nDo you want to hear more Chuck Norris jokes? (Y)(N): ").upper()

print("Good bye..")
