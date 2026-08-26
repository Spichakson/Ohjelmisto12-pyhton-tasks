hyttiluoka = input('Minkä hyttiluokan haluaisit?: ')

lux = 'LUX on parvekkellinen hytti yläkannella'
a = 'A on ikkunallinen hytti autokannen yläpuolella'
b = 'B on ikkunaton hytti autokannen yläpuolella'
c = 'C on ikkunaton hytti autokanella yläpuolella'

if hyttiluoka == 'lux' or hyttiluoka == 'LUX':
    print(lux)
elif hyttiluoka == 'a' or hyttiluoka == 'A':
    print(a)
elif hyttiluoka == 'b' or hyttiluoka == 'B':
    print(b)
elif hyttiluoka == 'c' or hyttiluoka == 'C':
    print(c)
else: 
    print('Virheellinen hyttiluokka!')

