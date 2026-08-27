tuumia = int(input('Anna tuumat: '))
while tuumia >= 0:
    print(f"{tuumia} tuumaa on {tuumia * 2.54} cm")
    break
else:
    print('Ei saa kirjoittaa negatiivista tuumamäärää!')