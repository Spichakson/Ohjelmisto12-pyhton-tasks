import math

def price_in_sqm(diameter, price):
    area = (math.pi * diameter**2) / 4
    result = (price / area) * 10000
    return result
    

diameter1 = int(input(f"Please, input the diameter of the first pizza in cm: "))
price1 = float(input(f"Please, input the price of the first pizza  in euros: "))
pizza1 = price_in_sqm(diameter1, price1)

diameter2 = int(input(f"Please, input the diameter of the second pizza  in cm: "))
price2 = float(input(f"Please, input the price of the second pizza  in euros: "))
pizza2 = price_in_sqm(diameter2, price2)

if pizza1 < pizza2:
    print('First pizza is cheaper')
elif pizza2 < pizza1:
    print('Second pizza is cheaper')
else:
    print('Both pizzas are even')