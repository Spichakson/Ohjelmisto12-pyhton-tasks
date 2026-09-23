class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdyta(self, muutos):
        if self.tamanhetkinen_nopeus + muutos <= 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus += muutos

        self.kuljettu_matka = muutos


auto1 = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus {auto1.rekisteritunnus} huippunopeus {auto1.huippunopeus}")
auto1.kiihdyta(30)
print(f"Auton nopeus nyt on {auto1.tamanhetkinen_nopeus}")
auto1.kiihdyta(50)
print(f"Auton nopeus nyt on {auto1.tamanhetkinen_nopeus}")
auto1.kiihdyta(70)
print(f"Auton nopeus nyt on {auto1.tamanhetkinen_nopeus}")
auto1.kiihdyta(-200)
print(f"Auton nopeus nyt on {auto1.tamanhetkinen_nopeus}")


