
class Player:
    def __init__(self, name, money, starting_room):
        self.name = name
        self.money = money
        self.location = starting_room
        self.inventory = [ ]
        self.morale = 50
        self.day = 1

        self.has_eaten = False

    def player_info(self):
        print("\n-- PLAYER PROFILE --")
        print(f"\nNimi: {self.name}")
        print(f"Sijainti: {self.location}")
        print(f"Raha: {self.money}")
        print(f"Moraali: {self.morale}")

    def inventory_info(self):
        for i in self.inventory: print(i)
    
    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def move(self, direction: str):
        direction = direction.lower().strip()
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            self.morale -= 5
            print("\n")
            print(f'=' * 30)
            print(f"\nMatka väsyttää! Moraali -5")
            print(f"Olet nyt paikassa: {self.location.name}")
        else:
            print("\n")
            print(f'=' * 30)
            print("\nSiihen suuntaan ei voi mennä")
            

    def collect_item(self, item_name: str):
        item_name = item_name.lower().strip()
        for item in self.location.items:
            if item.name.lower() == item_name:
                self.inventory.append(item)
                self.location.remove_item(item)
                print("\n")
                print(f'=' * 30)
                print(f"\nOtit esineen: {item.name}")
                return
        print("\n")
        print(f'=' * 30)   
        print("\nTämä esinettä ei ole täällä!")    

    def restore_moral(self, amount: int):
        self.morale += amount
        if self.morale > 100:
            self.morale = 100
        print("\n")
        print(f'=' * 30)
        print(f"\nMoraalisi nousi! Nykyinen moraali: {self.morale}/100")

    def sleep(self):
        print("\n")
        print(f'=' * 30)
        print("\n---Sinä nukut---")
        print("---Nälkä tulee taas---")
        self.day += 1
        self.has_eaten = False

    def eat(self):
        if self.has_eaten:
            print("\n")
            print(f'=' * 30)
            print("\nOlet jo syönyt tänään!")
            return

        print("\n")
        print(f'=' * 30)
        print("---Sinä syöt/juot---")
        self.has_eaten = True
        self.restore_moral(10)
        print(f"Moraali + 10")

    def work(self):
        is_card = any(item.name == "kulkukortti" for item in self.inventory)
        if is_card:
            self.money += 200
            self.morale -= 15
            print("\n")
            print(f'=' * 30)
            print("\nTyöskentelet hyvin! Ansaisit 200€ (Moraali -15)")
        else:
            print("\n")
            print(f'=' * 30)
            print("\nSinulta puuttuu kulkukorttia! Ei voi saada töitä!")

    def buy_ticket(self):
        if self.money >= 500:
            self.money -= 500
            print("\n")
            print(f'=' * 30)
            print("\nOstot lipun pois Kotkasta!")
            return True
        else:
            print("\n")
            print(f'=' * 30)
            print(f"Lippu maksaa 500€. Sinulla on vain {self.money}€")
            return False

    def use_item(self, item_name):
        item_name = item_name
        for item in self.inventory:
            if item.name == item_name:
                if item.item_type == "food":
                    if self.has_eaten:
                        print("\n")
                        print(f'=' * 30)
                        print("\nOlet jo syönyt tänään!")
                        return
                    
                    self.restore_moral(10)
                    self.inventory.remove(item)
                    print("\n")
                    print(f'=' * 30)
                    print(f"Käytit esineen {item.name}")
                    return
                else:
                    print("\n")
                    print(f'=' * 30)
                    print(f"\n Esinettä {item.name} ei voi käyttää tästä!")
                    return
        print("\nSinulla ei ole tällaista esinettä repussa!")

class Item:
    def __init__(self, name, weight, item_type: str):
        self.name = name
        self.weight = weight
        self.item_type = item_type
        

    def __str__(self):
        return f"{self.name}, {self.weight}"

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



        

