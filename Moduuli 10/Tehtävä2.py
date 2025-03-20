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
            print(f"Talossa ei ole kerrosta numero {kerros}")
            return

        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, talon_alin_kerros, talon_ylin_kerros, hissien_lkm):
        self.talon_ylin_kerros = talon_ylin_kerros
        self.talon_alin_kerros = talon_alin_kerros
        self.hissit = []
        
        for i in range(hissien_lkm):
            hissi = Hissi(talon_alin_kerros, talon_ylin_kerros)
            self.hissit.append(hissi)
            
            
    def aja_hissillä(self, hissi_nro, kerros):
        if hissi_nro < 1 or hissi_nro > len(self.hissit):
            print(f"Hissiä numero {hissi_nro} ei löytynyt!")
            return
        
        hissi = self.hissit[hissi_nro -1]
        print(f"Valitsit hissin numero {hissi_nro}.")
        print(f"Valitsit kerroksen {kerros}")
        hissi.siirry_kerrokseen(kerros)
        
        
talo = Talo(1, 18, 2)

talo.aja_hissillä(2, 18)
talo.aja_hissillä(2, 1)
        
        











