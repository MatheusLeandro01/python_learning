'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

n1 = float(input('Informe a 1º Nota: '))
n2 = float(input('Informe a 2º Nota: '))
n3 = float(input('Informe a 3º Nota: '))
n4 = float(input('Informe a 4º Nota: '))

media = (n1 + n2 + n3 + n4) / 4

print(f'A média do ano é: {media:.1f}')