'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
'''
#eu
soma = 0
for cont in range(1, 6):
    num = float(input(f'Informe o {cont}º valor: '))
    soma += num

media = soma/cont
print(f'A soma entre os 5 valores é: {soma}, e a média é: {media}')
'''

#'''
#Renzo
soma = float(input('Digito um número: '))

for n in range(2, 6):
    soma += float(input('Digito um número: '))
    media = soma / n
    print(f'A soma dos números é {soma}, e a média é {media}')
#'''