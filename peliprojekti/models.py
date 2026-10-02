class Player:
    def __init__(self, name, money, location):
        self.name = name
        self.money = money
        self.location = location
        self.inventory = [ ]

    def player_info(self):
        print("\n-- PLAYER PROFILE --")
        print(f"\nNimi: {self.name}")
        print(f"Raha: {self.money}")
        print(f"Sijainti: {self.location}")

    def inventory_info(self):
        print(self.inventory)

    def add_to_inventory(self, item):
        self.inventory.add(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def move(self, direction):
        self.direction = direction
        print(f"Sinä menet {self.location}:sta {self.direction}:iin")
        self.location = self.direction
        



class Room:
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.items = []
        self.destinations = []

    def __str__(self):
        return f"{self.name}, {self.info}"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.weight} kg"


class Job:
    def __init__(self, title, work_hours, salary, distance):
        self.title = title
        self.work_hours = work_hours
        self.salary = salary
        self.distance = distance

    def show_info(self):
        print(f" Työpaikka: {self.title}, {self.work_hours} h, palkka {self.salary}")