name = input('Mikä sinun nimi on?: ')
age = int(input('Kuinka ikäinen olet?: '))
if age < 12:
    print('Olet liian nuori!')
    quit()
elif age >= 12:
    print(f'Nimi: {name}')
    print(f'Ikä: {age}')
    print('Moi!')
while True:
    print('Käytä kommentolista')
    command = input('Anna kommento: ')
    if command == 'lopeta':
        print('Lopettu!')
        break
    elif command == 'käyttäjä':
        print(f'Nimi: {name}')
        print(f'Ikä: {age}')
    elif command == 'muoka nimi: ':
        name = input('Anna uusi nimi')
    elif command == 'kommentolista':
        print('Komennot: ')
        print(" 'käyttäjä' 'muoka nimi' 'lopeta' ")
        

    

