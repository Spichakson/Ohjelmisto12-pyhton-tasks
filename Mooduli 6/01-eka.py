names = []

name = input('Enter first name or press Enter to stop: ')
while name != "":
    names.append(name)
    name = input('Enter next name or press Enter to stop: ')
else:
    for name in names:
        print(name)


