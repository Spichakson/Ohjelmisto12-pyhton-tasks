import models
import funktiot



home_loc = models.Room("Koti", "Oma vuokraasunto")
    

#jobs_available = (models.Job("myyjä"), models.Job("sairaanhoitaja"), models.Job("koodari"), models.Job("kuljettaja"), 
#models.Job("siivoja"), models.Job("kokki"), models.Job("kielenopettaja"), models.Job("puutarhuri"))



# Program start and main menu
print("=== KOTKAN MOST WANTED ===")
name = input('\nMikä sinun nimi on?: ')
age = int(input('Kuinka ikäinen olet?: '))
if age < 12:
    print('Olet liian nuori!')
    quit()

money = 100
location = 
player1 = models.Player(name, money, home_loc)

funktiot.main_menu(player1)

# Game prosses
funktiot.new_game()


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
        funktiot.commands_list()
    if command == 'aloita':
        tie = input("Ensin sinun täytyy valita: menetkö töihin tai kelaan?(työ/kela/takaisin): \n ")
        if tie == 'työ':
            funktiot.job_search()
        
        

    

