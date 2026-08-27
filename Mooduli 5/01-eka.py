money = int(input("How many money do you have?: "))
given_money = 0
while given_money < money + 5:
    print('Haha, brokie! Here is a dollar!')
    given_money += 1
    if given_money == money:
        print("Now you have money!")
        break