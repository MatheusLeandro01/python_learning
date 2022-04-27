idade = int(input('Informe sua idade: '))

if idade < 18:
    print('É menor de idade')
elif idade >= 65:
    print('É aposentado')
else:
    print('É maior de idade')
