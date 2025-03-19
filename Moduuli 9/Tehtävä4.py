import random
from prettytable import PrettyTable

taulukko = PrettyTable()
taulukko.field_names = ["Rekisteritunnus", "Huippunopeus (km/h)", "Kuljettu matka (km)"]

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        
    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        
    def kulje(self, tunti):
        self.matka += tunti * self.nopeus
    
autolista = []
numero = 0

for i in range(10):
    arvohuippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{numero + 1}", arvohuippunopeus)
    autolista.append(auto)
    numero += 1

kilpailu = True

while kilpailu:
    for auto in autolista:
        arvonopeus = random.randint(-10, 15)
        auto.kiihdytä(arvonopeus)
        auto.kulje(1)
        
        if auto.matka >= 10000:
            kilpailu = False
            break

    
for auto in autolista:
    taulukko.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.matka])
    
print(taulukko)    
   
