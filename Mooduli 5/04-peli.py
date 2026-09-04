import random
numero = int(random.randint(1, 10))

while True:
    arvo = int(input('Arvo numero(1-10): '))
    if arvo == numero:
        print('Oikein!')
        break
    elif arvo < numero:
        print('Liian pieni arvaus')
    elif arvo > numero:
        print('Liian suuri arvaus')
    
