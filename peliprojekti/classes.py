import functions


class Player:
    def __init__(self, name, money, starting_room):
        self.name = name
        self.money = money
        self.location = starting_room
        self.inventory = [ ]

        self.morale = 50

    def player_info(self):
        print("\n-- PLAYER PROFILE --")
        print(f"\nNimi: {self.name}")
        print(f"Sijainti: {self.location}")
        print(f"Raha: {self.money}")
        print(f"Moraali: {self.morale}")

    def inventory_info(self):
        for i in self.inventory: print(i)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def move(self, direction: str):
        direction = direction.lower().strip()
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            print(f"\nOlet nyt paikassa: {self.location.name}")
            return True
        else:
            print("\nSiihen suuntaan ei voi mennä")
            return False

    def collect_item(self, item_name: str):
        item_name = item_name.lower().strip()
        for item in self.location.items:
            if item.name.lower() == item_name:
                self.inventory.append(item)
                self.location.remove_item(item)
                print(f"\nOtit esineen: {item.name}")
                return
        print("\nTämä esinettä ei ole täällä!")    

    def restore_moral(self, amount: int):
        self.morale += amount
        if self.morale > 100:
            self.morale = 100
        print(f"\nMoraalisi nousi! Nykyinen moraali: {self.morale}/100")

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.weight}"

    

class Job:
    def __init__(self, title, work_hours, salary, distance):
        self.title = title
        self.work_hours = work_hours
        self.salary = salary
        self.distance = distance

    def show_info(self):
        print(f" Työpaikka: {self.title}, {self.work_hours} h, palkka {self.salary}")

class Room:
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.items = []
        self.exits = {}
        self.actions = []

    def __str__(self):
        return f"{self.name}, {self.info}"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)



        

