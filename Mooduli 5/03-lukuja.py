eka = input('Anna luku: ')
if eka != '':
    eka = int(eka)
lukuS = eka
lukuP = eka

while True:
    luku = input('Anna luku: ')
    if luku == '':
        break
    luku = int(luku)
    if luku > lukuS:
        lukuS = int(luku)
    if luku < lukuP:
        lukuP = int(luku)
    
print(f'Suurin luku on {lukuS}')
print(f'Pienin luku on {lukuP}')   


