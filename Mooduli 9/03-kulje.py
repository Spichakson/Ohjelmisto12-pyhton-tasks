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


    def kulje(self, tuntimaara):
        self.kuljettu_matka += tuntimaara * self.tamanhetkinen_nopeus
        


auto1 = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus {auto1.rekisteritunnus} huippunopeus {auto1.huippunopeus}")

auto1.kiihdyta(50)
auto1.kulje(0.5)
print(f"Tamanhetkinen nopeus {auto1.tamanhetkinen_nopeus}")
print(f"Auton kuljettu matka on {auto1.kuljettu_matka} km")
auto1.kiihdyta(80)
print(f"Tamanhetkinen nopeus {auto1.tamanhetkinen_nopeus}")
auto1.kulje(1.5)
print(f"Auton kuljettu matka on {auto1.kuljettu_matka} km")

