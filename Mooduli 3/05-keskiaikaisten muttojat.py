leiviskät = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))


luoditG = (((leiviskät * 20 + naulat) * 32 + luodit)) * 13.3

result = (f'Massa on {luoditG // 1000} kg {luoditG % 1000: .2f} gr.')

print(result)





