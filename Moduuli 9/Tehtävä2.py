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
        

auto = Auto("ABC-123", 142)
#print(f"""Rekisteritunnus: {auto.rekisteritunnus}\nHuippunopeus: {auto.huippunopeus}
#Tämänhetkinen nopeus: {auto.nopeus} km/h\nKuljettu matka: {auto.matka} km/h""")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton tämänhetkinen nopeus on: {auto.nopeus} km/h")
auto.kiihdytä(-200)
print(f"Auton uusi nopeus on: {auto.nopeus} km/h")