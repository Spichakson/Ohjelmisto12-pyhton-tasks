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
    
    

jobs_available = ["myyjä", "sairaanhoitaja", "koodari", "kuljettaja", "siivoja", "kokki", "kielenopettaja", "puutarhuri"]
jobs_chosen = []

commands = ['käyttäjä', 'muoka nimi', 'lopeta', 'valita paikat']



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
    elif command == 'käyttäjä':
        print(f'Nimi: {name}')
        print(f'Ikä: {age}')
    elif command == 'muoka nimi':
        name = input('Anna uusi nimi: ')
    elif command == 'kommentolista':
        commands_list()
    elif command == 'aloita':
        job_search()
    elif command == 'valita paikat':
        job_choose()

    

