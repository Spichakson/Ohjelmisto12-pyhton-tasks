def main_menu():
    print("=== MAIN MENU ===")
    print("\n 1 - uusi peli" "\n 2 - Profile" "3 - ")
    dia = input("\n Valita(1-3): ")



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









class Player:
    def __init__(self, name, age, money, location):
        self.name = name
        self.age = age
        self.money = money
        self.location = location


class Job:
    def __init__(self, name, work_hours, salary):
        self.name = name
        self.work_hours = work_hours
        self.salary = salary












    
    

jobs_available = ["myyjä", "sairaanhoitaja", "koodari", "kuljettaja", "siivoja", "kokki", "kielenopettaja", "puutarhuri"]
jobs_chosen = []

commands = ['käyttäjä', 'muoka nimi', 'lopeta', 'aloita', 'valita paikat', ]



print('Moi ja tervetuloa Kotkaan! Tässä sinä yrität tehdä mahdototonta - hakea töitä!')
name = input('Mikä sinun nimi on?: ')
age = int(input('Kuinka ikäinen olet?: '))
money = 100
if age < 12:
    print('Olet liian nuori!')
    quit()
elif age >= 12:
    print(f'Nimi: {name}')
    print(f'Ikä: {age}')
    print(f'Rahaa: {money}€')
while True:
    print('Käytä kommentolista')
    command = input('Anna kommento: ')
    if command == 'lopeta':
        print('Lopetettu!')
        break
    if command == 'käyttäjä':
        print(f'Nimi: {name}')
        print(f'Ikä: {age}')
    if command == 'muoka nimi':
        name = input('Anna uusi nimi: ')
    if command == 'kommentolista':
        commands_list()
    if command == 'aloita':
        tie = input("Ensin sinun täytyy valita: menetkö töihin tai kelaan?(työ/kela/takaisin): \n ")
        if tie == 'työ':
            job_search()
        
        
    if command == 'valita paikat':
        job_choose()

    

