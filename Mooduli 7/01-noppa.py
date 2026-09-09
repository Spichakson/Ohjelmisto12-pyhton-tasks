import random

def throw_dice():
    return random.randint(1, 6)
     

dice = 0
while dice != 6:
    dice = throw_dice()
    print(f"Dice thrown: {dice}")
   

    