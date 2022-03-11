'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''
'''
#Eu
valor1 = 'Brasil Hexa 2006'
valor2 = 'Brasil Hexa 2006'#'Brasil! Hexa 2006!'

print(f'Tamanho de valor 1: {len(valor1)} caracteres')
print(f'Tamanho de valor 2: {len(valor2)} caracteres')

if valor1 == valor2:
    print('As duas strings são de conteúdos iguais')
else:
    print('As duas strings possuem conteúdos diferentes.')

if len(valor1) == len(valor2):
    print('As duas strings são de valores iguais')
else:
    print('As duas strings possuem valores diferentes.')
'''


#Renzo

s1 = str(input('info 1: '))
s2 = str(input('info 2: '))

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'"{s1}": {tamanho1} caracteres.')
print(f'"{s2}": {tamanho2} caracteres.')

comparação_de_tamanho = 'Diferentes' #len
comparação_de_conteudo = 'diferente' # se é igual(==)


if s1 == s2:
    comparação_de_conteudo = 'Igual'
    comparação_de_tamanho = 'Iguais'
elif tamanho1 == tamanho2:
    comparação_de_tamanho = 'Iguais'

print(f'Os conteúdos são: {comparação_de_conteudo}.')
print(f'O tamanho é: {comparação_de_tamanho}.')