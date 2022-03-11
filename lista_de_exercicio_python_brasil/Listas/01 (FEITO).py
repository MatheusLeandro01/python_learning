#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for c in range(1, 6):
    valor = int(input(f'Informe valor {c} inteiro: '))
    lista.append(valor)

print(lista)