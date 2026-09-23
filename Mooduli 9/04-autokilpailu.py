import random


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

autot = []


for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)



kilpailu = True

while kilpailu:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu = False

print (
    f"{'Rekisteritunnus': <15} | {'Huippunopeus':<15}      | {'Nopeus':<10}      | {'Matka':<10}"
)
for auto in autot:
    print(f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<15} km/h | {auto.tamanhetkinen_nopeus:<10} km/h | {auto.kuljettu_matka:<10} km ")







