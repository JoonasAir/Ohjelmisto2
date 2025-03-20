""" Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. 
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. 
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi. """

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros  
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print("Kerrosta ei löytynyt.")
            return

        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, talon_ylin_kerros, talon_alin_kerros, hissien_lkm):
        self.talon_ylin_kerros = talon_ylin_kerros
        self.talon_alin_kerros = talon_alin_kerros
        self.hissien_lkm = hissien_lkm
        
        

    def aja_hissiä(self, hissi, kohde):
        self.hissi = hissilista[hissi - 1]
        
        pass



talo = Talo(1, 18, 2)

hissilista = []
for i in range(talo.hissien_lkm):
    hissi = f"Hissi {i + 1}"
    hissilista.append(hissi)


talo.aja_hissiä(2, 4)











