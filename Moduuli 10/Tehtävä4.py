import random
from prettytable import PrettyTable

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
        self.matka += self.nopeus * tunti

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot_lkm):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = []

        for i in range(autot_lkm):
            arvohuippunopeus = random.randint(100, 200)
            auto = Auto(f"ABC-{i+1}", arvohuippunopeus)
            self.autot.append(auto)

    def tunti_kuluu(self):
        for auto in self.autot:
            arvonopeus = random.randint(-10, 15)
            auto.kiihdytä(arvonopeus)
            auto.kulje(1)

    def tulosta_tilanne(self):
        taulukko = PrettyTable()
        taulukko.field_names = ["Rekisteritunnus", "Huippunopeus (km/h)", "Kuljettu matka (km)"]
        
        self.autot.sort(key=lambda a: a.matka, reverse=True)
        for auto in self.autot:
            taulukko.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.matka])
        
        print(taulukko)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False

    def aja_kilpailu(self):
        tunnit = 0
        while not self.kilpailu_ohi():
            self.tunti_kuluu()
            tunnit += 1
            if tunnit % 10 == 0:
                print(f"\nTilanne {tunnit} tunnin jälkeen:")
                self.tulosta_tilanne()
        
        print("\nKilpailu päättyi!")
        self.tulosta_tilanne()

# Pääohjelma
if __name__ == "__main__":
    kilpailu = Kilpailu("Suuri romuralli", 8000, 10)
    kilpailu.aja_kilpailu()
