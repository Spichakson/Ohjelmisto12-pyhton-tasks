import random

def throw_dice(sides):
        return random.randint(1, sides)   

dice = 0
sides = int(input("How many sides the dice has?: "))
while dice != sides:
    dice = throw_dice(sides)
    print(f"Dice thrown: {dice}")
   

    