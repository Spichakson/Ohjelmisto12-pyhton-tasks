sukupuoli = input('Mikä on sinun sukupuoli?: ')
miesten = 'Sinulle normaali hemoglobiiniarvo on välillä 117-175 g/l'
naisten = 'Sinulle normaali hemoglobiiniarvo on välillä 134-195 g/l'

if sukupuoli == 'mies':
    print(miesten)
elif sukupuoli == 'nainen':
    print(naisten)
else:
    print('Yritä uudelleen!')