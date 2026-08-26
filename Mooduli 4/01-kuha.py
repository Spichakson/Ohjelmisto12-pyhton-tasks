pituus = float(input('Kuhan pituus: '))
alamit = 37 - pituus

if pituus < 37:
    print(f'Kuhan pituus on {pituus} cm, joka on {alamit} cm alimmasta sallitusta pyyntimitasta puuttuu. Ne pitää palauttaa järveen.')
else:
    print('Se on ihan hyvä salis!')
