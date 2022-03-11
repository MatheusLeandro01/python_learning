'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:

1 - Mostre a quantidade de valores que foram lidos;
2 - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
3 - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
4 - Calcule e mostre a soma dos valores;
5 - Calcule e mostre a média dos valores;
6 - Calcule e mostre a quantidade de valores acima da média calculada;
7 - Calcule e mostre a quantidade de valores abaixo de sete;
8 - Encerre o programa com uma mensagem;

'''
'''
nota = float(input('Informe uma nota: '))
valores_na_ordem = [] #1
valores = soma = 0

while nota != -1:
    valores += 1    
    valores_na_ordem.append(nota) #1
    soma += nota
    media = soma / valores

    nota = float(input('Informe uma nota: '))

    
print(f'Foram lidos {valores} valores')

print()

print(f'Valores na ordem: {valores_na_ordem}')

print()

#Inverso um abaixo do outro:
valores_na_ordem.reverse()
print('Valores na ordem inversa um abaixo do outro: ')
for c in range(valores):
    print(valores_na_ordem[c])

print()

print(f'A soma dos valores é igual à: {soma}')

print()

print(f'A media dos valores é igual à: {media}')

print()

print('Valores acima da média: ')
valores_na_ordem.reverse()
for c in valores_na_ordem:
    if c > media:
        print(c)

print()

print('Valores abaixo de 7: ')
for c in valores_na_ordem:
    if c < 7:
        print(c)

print()

print('Deu bom galera, valeu falowwwwww!!!!!')
'''


#Renzo
notas = [] #lista

while True:
    entrada = str(input('Digite um número: ')) #Estou recebendo valores
    if entrada == '-1': #se o valor for == a -1 então, já quero que pare por ai.
        break
    notas.append(float(entrada)) # senão eu vou querer armazenar na minha lista (notas)

tamanho = len(notas)
print(f'Foram lidas {tamanho} notas.')

print(', '.join([str(nota) for nota in notas]))

notas.reverse()

for nota in notas:
    print(nota)

soma = sum(notas)

print(f'Soma das notas é: {soma}')

media = soma / tamanho

print(f'Media das notas: {media}')

print('Notas acima da média: ')

print(' '.join([str(nota) for nota in notas if nota > media]))

print('Notas abaixo de 7: ')

print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Encerrado o programa de estatistica de notas: ')