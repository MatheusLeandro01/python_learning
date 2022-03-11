'''
Faça um programa que leia 5 números e informe o maior número.
'''
'''
#Eu
maior_numero = 0
for c in range(5):
    numero = float(input(f'Digite o {c+1}º valor: '))
    if numero > maior_numero:
        maior_numero = numero
    else:
        maior_numero = maior_numero
print(f'O maior valor é {maior_numero}')
'''


'''

maximo = float(input('Digite um valor: '))

for _ in range(4):
    maximo = max(maximo, float(input('Digite um valor: ')))
    print(f'Número máximo encontrado até agora é: {maximo}')
'''

maximo = 0
for _ in range (4):
    maximo = max(maximo, float(input(f'Digite um valor {_+1}º: '))) # função MAX serve para comparar valores dentro dos parentes
    print(f'Número máximo encontrado até agora é: {maximo}')