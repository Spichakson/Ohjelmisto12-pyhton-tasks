while True:
    number = input('Please, enter a number : ')
    if number != '':
        number = int(number)
        primeN = True
        for i in range(2, number):
            if number % i == 0:
                primeN = False
        if primeN == True:
            print('This is a prime number!')
        else:
            print('This is not a prime number!')
    else:
        print("Come back again!")
        quit()
