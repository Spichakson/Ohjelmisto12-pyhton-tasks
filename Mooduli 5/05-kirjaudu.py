username = 'python'
password = 'rules'
tries = 0

while tries != 5:
    enterU = input('Enter username: ')
    enterP = input('Enter password: ')
    if enterU != username or enterP != password:
        tries += 1
        print('Incorrect username or password')
        print(f'You have {5 - tries} tries')
    elif enterU == username and enterP == password:
        print('Welcome!')
        break
else:
    print('Access denied')
    