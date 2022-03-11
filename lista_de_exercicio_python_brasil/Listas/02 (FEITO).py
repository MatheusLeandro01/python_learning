#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

'''
#eu
lista = []

for c in range(1, 11):
    valor = float(input(f'Informe o {c}º valor real: '))
    lista.append(valor)
print(lista[-1: : -1])
'''


# Renzo
# Mais simples
lista = []

for c in range(3):
    valor = float(input(f'Informe valor {c} inteiro: '))
    lista.append(valor)
lista.reverse()
print(lista)