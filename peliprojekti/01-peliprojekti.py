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
    command = input('Anna kommento: ')
    if command == 'lopeta':
        print('Lopettu!')
        break
    

