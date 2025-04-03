import random
from prettytable import PrettyTable


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
            
    def kulje(self, tunti):
        self.matka += self.nopeus * tunti
    
class Kilpailu():
    def __init__(self, nimi, pituus_km, autot_määrä):
        self.nimi = nimi
        self.pituus_km = pituus_km
        
        self.autolista = []
        for i in range(autot_määrä):
            arvonopeus = random.randint(100, 200)
            auto = Auto(f"ABC-{i + 1}", arvonopeus)
            self.autolista.append(auto)
        
    def tunti_kuluu(self):
        for auto in self.autolista:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdyta(kiihdytys)
            auto.kulje(1)
        
    
    def tulosta_tilanne(self):
        taulukko = PrettyTable()
        taulukko.field_names = ["Rekisteritunnus", "Huippunopeus (km/h)", "Kuljettu matka (km)"]
        self.autolista.sort(key = lambda a: a.matka, reverse=True)
             
        for auto in self.autolista:
            taulukko.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.matka])
            taulukko.add_divider

        print(f"TULOKSET KILPAILULLE: {self.nimi.upper()}")
        print(taulukko)
        print("\nKILPAILUN TOP 3:\n")
        
        i = 0
        
        for auto in self.autolista[0:3]:
            print(f"{i + 1}. {auto.rekisteritunnus}\n")
            i += 1
    
    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka >= self.pituus_km:
                return True
        return False

    def aja_kilpailu(self):
        tunnit = 0
        while not self.kilpailu_ohi():
            self.tunti_kuluu()
            tunnit += 1
            if tunnit % 10 == 0:
                self.tulosta_tilanne()
        print("===============================================================")
        print("Kilpailu päättyi \n")
        self.tulosta_tilanne()


  
kilpailu = Kilpailu("Suuri romuralli", 8000, 10)
kilpailu.aja_kilpailu()

