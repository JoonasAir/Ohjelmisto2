class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        
        

auto = Auto("ABC-123", 142)
print(f"""Rekisteritunnus: {auto.rekisteritunnus}\nHuippunopeus: {auto.huippunopeus}
Tämänhetkinen nopeus: {auto.nopeus} km/h\nKuljettu matka: {auto.matka} km/h""")





