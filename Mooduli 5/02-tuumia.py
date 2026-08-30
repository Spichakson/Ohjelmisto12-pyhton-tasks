tuumia = int(input('Anna tuumat: '))
while tuumia >= 0:
    print(f"{tuumia} tuumaa on {tuumia * 2.54} cm")
    tuumia = int(input('Anna tuumat: '))
else:
    print('Ei voi kirjoittaa negatiivista tuumamäärää!')
    