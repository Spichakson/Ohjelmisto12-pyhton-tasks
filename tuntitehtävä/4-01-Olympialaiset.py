year = int(input('Year: '))

if year % 10 == 4:
     print(f'Olympics were set in {year}!')
elif year == 2020:
    print('Due to COVID-19 olympics were suspended that year')
elif year == 2021:
    print('Dispite it was not an official olympics year, 2020 olympics were set')
else:
    print('Not a year of the olympics')