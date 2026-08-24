total_g = float(input('How many gramms?: '))
kilos = int((total_g // 1000 ))
gramms = int((total_g % 1000))
print(f"{kilos} kg and {gramms} g")
