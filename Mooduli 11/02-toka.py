import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if self.current_speed + speed_change <= 0:
            self.current_speed = 0
        elif self.current_speed + speed_change >= self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_change

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed



class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, max_speed)


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_capacity):
        self.tank_capacity = tank_capacity
        super().__init__(registration_number, max_speed)

e1 = ElectricCar("ABC-15", 180, 52.5)
g1 = GasolineCar("ACD-123", 165, 32.3)

print(f"Electric car registration number {e1.registration_number}, max speed {e1.max_speed}, battery capacity{e1.battery_capacity} kWh ")
print(f"Gasoline car registration number {g1.registration_number}, max speed {g1.max_speed}, battery capacity{g1.tank_capacity} l ")



e1.accelerate(random.randint(70, 180))
print(f"Electric car current speed is {e1.current_speed} km/h")
e1.drive(3)
print(f"Electric car is driving for 3 hours")
print(f"Electric car travelled {e1.travelled_distance} km ")

g1.accelerate(random.randint(70, 165))
print(f"Gasoline car current speed is {g1.current_speed} km/h")
g1.drive(3)
print(f"Gasoline car is driving for 3 hours")
print(f"Gasoline car travelled {g1.travelled_distance} km ")

