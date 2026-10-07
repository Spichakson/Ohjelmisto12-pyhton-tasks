import classes
import objects

def run_game():
    # start and thigs' set
    

    
    
   
    print("=== KOTKAN MOST WANTED ===")
    #name = input('\nMikä sinun nimi on?: ')
    #age = int(input('Kuinka ikäinen olet?: '))
    name = "Artem"
    age = 26
    if age < 12:
        print('Olet liian nuori!')
        quit()

    money = 100
    player1 = classes.Player(name, money, objects.home_loc)
    return player1



def main_menu(player: classes.Player):
    while True:
        print("\n=== PÄÄVALIKKO ===")
        print("\n 1 - Pelaa" "\n 2 - Profile" "\n 3 - Lopeta ")
        action = int(input("\n Valita toiminta(1-3): "))
        if action == 1:
            return
        elif action == 2:
            player.player_info()
        elif action == 3:
            print("\n == GAME OVER ==")
            quit()

def game_loop(player):

    day = 1

    commands = ["Liiku", "Ota esine", "Avaa reppu", "Toiminta",
                "Pelaajan tiedot", "Lopeta"]

    while True:
        print("\n")
        print(f'=' * 30)
        print(f"Päivä {day}")
        print(f"Nykyinen sijainti: \n{player.location.name}, {player.location.info } ")
        print(f"\nTässä sijainnissä toiminnat: ")
        for i in player.location.actions: print(f"{i}")
        

        print("== Komennot ==")
        command_num = 1
        for command in commands:
            print(f"{command_num} - {command}")
            command_num += 1

        choice = (input("\nValitse toiminta: "))

        if choice == "1":
            print("Mahdolliset suunnat:", ", ".join(player.location.exits.keys()))
            direction = input("Laita suunta: ")
            player.move(direction)

        elif choice == "2":
            print(f"Tässä sijainnissa on esineet: ")
            for i in player.location.items: print(i)
            item = input("\nMikä esine haluat ottaa?: ")
            player.add_to_inventory(item)

        elif choice == "3":
            print("== REPPU ==")
            if not player.inventory:
                print("\nReppu on tyhjä")
            else:
                for i in player.location.items: print(i)

        elif choice == "4":
            action_num = 1
            for i in player.location.actions: 
                print(f"{action_num} - {i}")
                action_num += 1

            do_action = input("Mitä toimintaa haluat tehdä?: ")
            if do_action == "syödä":
                if player.location == objects.home_loc:
                    print("MMM DELICIOUS")
            
        


def new_game():
    print("\n Moi ja tervetuloa Kotkaan! Tässä sinä yrität tehdä mahdototonta - hakea töitä!")
    print("Tavoittesi on helppo ja haastava samaan aikaan! Sinun pitää lähteä Kotkasta MAHDOLLISIMMAN NOPEASI!")
    print("Sitä varten ehdottomasti tarvitset rahaa! Kokeile hankkia ne työstä tai jäät tähän IKUISESTI! ")















if __name__== "__main__":
    player = run_game()
    main_menu(player)