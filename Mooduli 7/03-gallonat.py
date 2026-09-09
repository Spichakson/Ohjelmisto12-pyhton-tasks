def gallonsToLitres(gallons):
    litres = gallons * 3.785
    return litres


while True:
    gallons = input("Enter the gallons value: ")
    if gallons != '':
        gallons = float(gallons)
        if gallons > 0:
            litres = gallonsToLitres(gallons)
            print(litres)
        else:
            print("Unexpected value")  
            break
    else:
        break
    

        