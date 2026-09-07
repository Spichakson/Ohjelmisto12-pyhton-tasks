
numbers = []
while True:
    numIn = input("Please, enter a number: ")
    if numIn != "":
        numIn = int(numIn)
        numbers.append(numIn)
    else:
        numbers.sort(reverse=True)
        print(f"Five greatest numbers: {numbers[0:5]}")
        quit()

    