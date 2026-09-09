names = set()

while True:
    name = input("Please enter a name or press Enter to stop: ")
    if name == "":
        break

    if name in names:
        print("Name already exsists")
    else:
        print("New name")
        names.add(name)

print("List of names: ")
for name in names:
    print(name)