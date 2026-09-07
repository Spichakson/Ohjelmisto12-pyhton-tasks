import random

result = 0

while True:
    throw = input('How many dices do you want to throw?: ')
    if throw != "":
        throw = int(throw)
        print(f"You have thrown {throw} dices")
        for dice in range(throw):
            dices = random.randint(1,6)
            result += dices
            print(f"Result: {dices}")
        print(f"Dices summ is {result}")
        result = 0
    else:
        print('Come back again!')
        quit()

