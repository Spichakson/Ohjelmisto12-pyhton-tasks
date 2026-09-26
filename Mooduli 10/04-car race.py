import random

class Race:

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars 
        

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(
        f"{'\nRegistration':<15} | {'Max Speed':<15} | {'Current Speed':<15} | {'Distance':<10}"
        )
        print("-" * 65)

        for car in self.cars:
            print(
            f"{car.registration_number:<15} | {car.max_speed:<10} km/h | {car.current_speed:<10} km/h | {car.travelled_distance:<10} km"
        )

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False




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



car_list = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    new_car = Car(registration_number, max_speed)
    car_list.append(new_car)

race1 = Race("Grand Demolotion Derby", 8000, car_list)

hour_passed = 0

while not race1.race_finished():
    race1.hour_passes()
    hour_passed += 1
    if hour_passed % 10 == 0:
        print(f"\n Hour {hour_passed}")
        race1.print_status()

print(f"\n Race finished in {hour_passed} hours")
race1.print_status()
        