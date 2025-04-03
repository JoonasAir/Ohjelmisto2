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
        
    def tulosta_tiedot(self):
        print(f"Auto {self.rekisteritunnus}:\nHuippunopeus: {self.huippunopeus}")
    
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
     
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"    -Auto toimii sähkömoottorilla\n")
        
           
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankinkoko):
        self.tankinkoko = tankinkoko
        super().__init__(rekisteritunnus, huippunopeus)
        
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"    -Auto toimii polttomoottorilla\n")
        
        
sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(150)
polttomoottoriauto.kiihdytä(80)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"\nSähköauto ({sähköauto.rekisteritunnus}) on kulkenut {sähköauto.matka}km.")
print(f"Polttomoottoriauto ({polttomoottoriauto.rekisteritunnus}) on kulkenut {polttomoottoriauto.matka}km.\n")

sähköauto.tulosta_tiedot()
polttomoottoriauto.tulosta_tiedot()