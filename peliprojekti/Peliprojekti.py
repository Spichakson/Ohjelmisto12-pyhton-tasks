def main_menu():
    print("=== MAIN MENU ===")
    print("\n 1 - Pelaa" "\n 2 - Profile" "\n 3 - Lopeta ")
    action = int(input("\n Valita toiminta(1-3): "))
    if action == 1:
        return
    elif action == 2:
        print(f"Nimi: {name}")
        main_menu()
    elif action == 3:
        print("\n == GAME OVER ==")
        quit()
    




def commands_list():
    print('Kommennot: ')
    for i in commands:
        print(i)

def job_search():
    print("Työpaikat saatavilla: ")
    for title in jobs_available:
        print(title)

def job_choose():
    print("Nyt sinä voit valita vain 4 työpaikkaa")
    title = input('Lisää työpaikka: ')
    jobs_chosen.append(title)
    while True:
        if len(jobs_chosen) >= 4:
            print('Ei saa enemman!')
            break
        elif title == '':
            break
        else:
            title = input('Lisää työpaikka: ')
            jobs_chosen.append(title)

def kela_money():
    kela = input('Tervetuloa Kelaan! Miten voisimme auttaa?(raha/takaisin): \n' \
    '')
    if kela == "raha":
        if money >= 100:
            print("Me emme voi antaa sinulle tukea, kun sinulla on niin paljon rahaa!")
        
    return

def new_game():
    print('\n Moi ja tervetuloa Kotkaan! Tässä sinä yrität tehdä mahdototonta - hakea töitä!')
    pass







class Player:
    def __init__(self, name, money, location):
        self.name = name
        self.money = money
        self.location = location

    def player_info(self):
        print(f"Nimi: {self.name}")
        print(f"Raha: {self.money}")
        print(f"Sijainti: {self.location}")



class Job:
    def __init__(self, title, work_hours, salary):
        self.title = title
        self.work_hours = work_hours
        self.salary = salary

    def show_info(self):
        print(f" {self.title} {self.work_hours} h, palkka {self.salary}")













    
    

jobs_available = ("myyjä", "sairaanhoitaja", "koodari", "kuljettaja", 
"siivoja", "kokki", "kielenopettaja", "puutarhuri")
commands = ['pelaaja', 'muoka nimi', 'lopeta', 'aloita', 'valita paikat', ]





# Program start and main menu
print("=== KOTKAN MOST WANTED ===")
name = input('\nMikä sinun nimi on?: ')
age = int(input('Kuinka ikäinen olet?: '))
if age < 12:
    print('Olet liian nuori!')
    quit()

money = 100
location = "Koti"
main_menu()

player1 = Player(name, money, location)

# Game prosses
new_game()


while True:
    print('\n Käytä kommentolista')
    command = input('Anna kommento: ')
    if command == 'lopeta':
        print('Lopetettu!')
        break
    if command == 'pelaaja':
        player1.player_info()
    if command == 'muoka nimi':
        player1.name = input('Anna uusi nimi: ')
    if command == 'kommentolista':
        commands_list()
    if command == 'aloita':
        tie = input("Ensin sinun täytyy valita: menetkö töihin tai kelaan?(työ/kela/takaisin): \n ")
        if tie == 'työ':
            job_search()
        
        
    if command == 'valita paikat':
        job_choose()

    

