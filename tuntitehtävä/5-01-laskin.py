"""""
while True:
    symbol = input('Choose the symbol(+, -, *): ')
    number1 = int(input('Choose first number: '))
    number2 = int(input('Choose second number: '))
    if symbol == '+':
        result = number1 + number2
        print(result)
    elif symbol == '-':
        result = number1 - number2
        print(result)
    elif symbol == '*':
            result = number1 * number2
            print(result)
    else:
         print('Wrong input!')
    end = input("Do you want to end calculations?(y/n): ")
    if end == 'y':
         print('Calculation are ended')
         break
"""




while True:
    menu_list = "Select option: \n1. add \n2. substract \n3. multiply \n0. exit:  "
    selection = input(menu_list)
    number1 = int(input('Choose first number: '))
    number2 = int(input('Choose second number: '))
    if selection == "1":
        print(f'Result: {number1} + {number2} = {number1 + number2}')
    elif selection == "2":
        print(f'Result: {number1} - {number2} = {number1 - number2}')
    elif selection == "3":
        print(f'Result: {number1} * {number2} = {number1 * number2}')
    elif selection == "0":
        break
