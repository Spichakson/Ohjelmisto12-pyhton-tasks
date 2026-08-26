height = int(input('Your heigth: '))


if 140 <= height <= 195:
    age = int(input('How old are you?: '))
    if age >= 8:
     print('You are allowed to use every machine!')
    else:
       print('You are not allowed to go to Tuulirekke')
elif 140 > height >= 100:
    print('You are allowed to use the kwids machines!')
elif height > 195:
    print('You are allowed to use every machine, except Kirnu!')




