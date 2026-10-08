import modules
import json






def run_game():
    # start and thigs' set
    # locations
    home_loc = modules.Room("Koti", "Oma vuokraasunto")
    store = modules.Room("Kauppa", "\nIhan normaali kauppa, " \
    "josta voi ostaa ruokaa ja muuta ")
    job_loc = modules.Room("Työ", "Tässä työskentelet ja saat rahaa")

    #items
    job_card = modules.Item("kulkukortti", 0.1, item_type="key")
    apple = modules.Item("omena", 0.2, item_type="food")
    coffee = modules.Item("kahvi", 0.3, item_type="food")
    home_loc.add_item(job_card)
    home_loc.add_item(apple)
    store.add_item(coffee)
    job_loc.add_item(coffee)



    # actions
    home_loc.actions = ["syödä", "nukkua"]
    job_loc.actions = ["työskenellä", "pidä kahvitauko"]
    store.actions = ["osta lentolippu"]

    # directions
    store.exits = {"koti": home_loc}
    home_loc.exits = {"työ": job_loc, "kauppa": store}
    job_loc.exits = {"koti": home_loc}
    
    
   # entrance, age check and player creation
    
    #name = input('\nMikä sinun nimi on?: ')
    #age = int(input('Kuinka ikäinen olet?: '))
    name = "Artem"
    age = 26
    if age < 12:
        print('Olet liian nuori!')
        quit()

    money = 100
    player1 = modules.Player(name, money, home_loc)
    
    rooms_dict = {home_loc.name: home_loc, store.name: store, job_loc.name: job_loc}
    items_dict = {job_card.name: job_card, apple.name: apple, coffee.name: coffee}

    return player1, rooms_dict, items_dict


    # main menu
def main_menu(rooms_dict: dict, items_dict: dict, default_player: modules.Player):
    show_intro_and_instructions()

    while True:
        print("\n=== PÄÄVALIKKO ===")
        print("\n 1 - Uusi peli" "\n 2 - Lataa peli" "\n 3 - Profile" "\n 4 - Lopeta ")
        action = input("\n Valita toiminta(1-4): ")
        if action == "1":
            return run_game()
        elif action == "2":
            player = load_game(rooms_dict, items_dict)
            return player
        elif action == "3":
            player.player_info()
        elif action == "4":
            print("\n == GAME OVER ==")
            quit()
    # main game loop
def game_loop(player):

    commands = ["Liiku", "Ota esine", "Avaa reppu", "Toiminta",
                "Pelaajan tiedot", "Talenna peli", "Lopeta"]

    while True:
        # conditions of lose
        if player.day > 3:
            print("\n")
            print(f'=' * 30)
            print("\nAika loppui! NO MORE WAY FROM KOTKA")
            print("\n== GAME OVER ==")
            break
        elif player.morale <20:
            print("\n")
            print(f'=' * 30)
            print("\nMoraali on liian pientä!")
            print("\n== GAME OVER ==")
            break

        # constant info
        print("\n")
        print(f'=' * 30)
        print(f"Päivä {player.day}")
        print(f"Nykyinen sijainti: \n{player.location.name}, {player.location.info } ")
        print(f"\nTässä sijainnissä toiminnat: ")
        for i in player.location.actions: print(i)

        # gameplay starts from here
        print("\n== Komennot ==")
        command_num = 1
        for command in commands:
            print(f"{command_num} - {command} | ", end="")
            command_num += 1

        choice = (input("\nValitse toiminta: "))
        # move between locations
        if choice == "1":
            print("Mahdolliset suunnat:", ", ".join(player.location.exits.keys()))
            direction = input("Laita suunta: ")
            player.move(direction)
        # check items and pick up
        elif choice == "2":
            print(f"Tässä sijainnissa on esineet: ")
            for i in player.location.items: print(i)
            item = input("\nMikä esine haluat ottaa?: ")
            player.collect_item(item)
        # check the inventory
        elif choice == "3":
            print("== REPPU ==")
            if not player.inventory:
                print("\nReppu on tyhjä")
            else:
                for i in player.inventory: print(i)
        # commint an action 
        elif choice == "4":
            action_num = 1
            for i in player.location.actions: 
                print(f"{action_num} - {i}")
                action_num += 1
            do_action = input("Mitä toimintaa haluat tehdä?: ")
            if do_action == "syödä":
                player.eat()
            if do_action == "nukkua":
                player.sleep()
            if do_action == "työskenellä":
                player.work()
            if do_action == "pidä kahvitauko":
                player.collect_item("kahvi")
                player.eat(25)
            if do_action == "osta lippu":
                win = player.buy_ticket()
                if win:
                    print("\n")
                    print(f'=' * 30)
                    print("\n VOITTTAJA! Pääsit pois Kotkasta!")
                    break
        elif choice == "5":
            player.player_info()

        elif choice == "6":
            save_game(player)
        elif choice == "7":
            print("== GAME OVER ==")
            break

# txt file reading
def load_text_file(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Tiedostoa {filename} ei löytynyt!]"

def show_intro_and_instructions():
    print("=== KOTKAN MOST WANTED ===")
    print(load_text_file("intro.txt"))
    print("\n" + load_text_file("instructions.txt"))
    print("-" * 30)


# game save in savegame.json
def save_game(player: modules.Player):
    # only important data saved
    save_data = {
        "name": player.name,
        "money": player.money,
        "morale": player.morale,
        "day": player.day,
        "has_eaten": player.has_eaten,
        "location_name": player.location.name,
        "inventory": [item.name for item in player.inventory] 
    }
    
    with open("savegame.json", "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=4)
    print("\n[Peli tallennettu onnistuneesti!]")


# game loading
def load_game(rooms_dict: dict, all_items_dict: dict) -> modules.Player:
    try:
        with open("savegame.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # location lodaing
        location = rooms_dict.get(data["location_name"], list(rooms_dict.values())[0])
        
        # player object loading
        player = modules.Player(data["name"], data["money"], location)
        player.morale = data["morale"]
        player.day = data["day"]
        player.has_eaten = data["has_eaten"]
        
        # inventory loading
        for item_name in data["inventory"]:
            if item_name in all_items_dict:
                player.inventory.append(all_items_dict[item_name])
                
        print(f"\n[Peli ladattu! Tervetuloa takaisin, {player.name}!]")
        return player
    except FileNotFoundError:
        print("\nTallennustiedostoa ei löytynyt!")
        return None


if __name__ == "__main__":
    # base structure for loading
    temp_player, rooms_dict, items_dict = run_game()
    
    # srtat menu and the main game loop
    active_player = main_menu(rooms_dict, items_dict)
    if active_player:
        game_loop(active_player)