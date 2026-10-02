import models

def main_menu(player):
    while True:
        print("=== MAIN MENU ===")
        print("\n 1 - Pelaa" "\n 2 - Profile" "\n 3 - Lopeta ")
        action = int(input("\n Valita toiminta(1-3): "))
        if action == 1:
            return
        elif action == 2:
            player.player_info()
        elif action == 3:
            print("\n == GAME OVER ==")
            quit()

def run_game(player):
    while True:
        print(f'='*30)
        print(f"Sijainti {player.location}")
        print(f"{player.location.info}")

        print(f"1 - Liiku")
        print(f"2 - Ota esine")
        print(f"3 - Avaa repu")
        print(f"4 - Lopeta")

        choice = int(input("\nValinta: "))

        if choice == 1:
            print("Mahdolliset suunnat: ")
            direction = input("Laita sunta: ")
            player.move(direction)
        elif choice == 2:

            print(f"Tässä sijainnissa on esineet: {models.Room.items}") # en vielä päättänyt
            item = input("\nMikä esine haluat ottaa?: ")
            player.add_to_inventory(item)









    
def commands_list(): 
    commands = ['pelaaja', 'muoka nimi', 'lopeta', 'aloita', 'valita paikat', ]
    print('Kommennot: ')
    for i in commands:
        print(i)



def kela_money():
    kela = input('Tervetuloa Kelaan! Miten voisimme auttaa?(raha/takaisin): \n' \
    '')
    if kela == "raha":
        if money >= 50:
            print("Me emme voi antaa sinulle tukea, kun sinulla on niin paljon rahaa!")
        
    return


def new_game():
    print('\n Moi ja tervetuloa Kotkaan! Tässä sinä yrität tehdä mahdototonta - hakea töitä!')
    pass

