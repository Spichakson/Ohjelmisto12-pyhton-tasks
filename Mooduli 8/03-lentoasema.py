airports = {}

while True:
    print("Options:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print(f"Airport {name} ({icao}) added successfully!")
    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print(f"Airport name: {airports[icao]}")
        else:
            print("Airport not found!")  
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Wrong choice, please select 1, 2, or 3.")