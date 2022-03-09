'''
Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''
#Minha versão
saque = 999

notas_de_100 = notas_de_50 =  notas_de_10 = notas_de_5 = notas_de_1 = 0

notas_de_100, saque = divmod(saque, 100)
if notas_de_100 == 1:
    notas_de_100_str = '1 Nota de 100'
    print(notas_de_100_str)
elif notas_de_100 > 1:
    notas_de_100_str = f'{notas_de_100} Notas de 100'
    print(notas_de_100_str)

notas_de_50, saque = divmod(saque, 50)
if notas_de_50 == 1:
    notas_de_50_str = '1 Nota de 50'
    print(notas_de_50_str)
elif notas_de_50 > 1:
    notas_de_50_str = f'{notas_de_50} Notas de 50'
    print(notas_de_50_str)

notas_de_10, saque = divmod(saque, 10)
if notas_de_10 == 1:
    notas_de_10_str = '1 Nota de 10'
    print(notas_de_10_str)
elif notas_de_10 > 1:
    notas_de_10_str = f'{notas_de_10} Notas de 10'
    print(notas_de_10_str)

notas_de_5, saque = divmod(saque, 5)
if notas_de_5 == 1:
    notas_de_5_str = '1 Nota de 5'
    print(notas_de_5_str)
elif notas_de_5 > 1:
    notas_de_5_str = f'{notas_de_5} Notas de 5'
    print(notas_de_5_str)

notas_de_1, saque = divmod(saque, 1)
if notas_de_1 == 1:
    notas_de_1_str = '1 Nota de 1'
    print(notas_de_1_str)
elif notas_de_1 > 1:
    notas_de_1_str = f'{notas_de_1} Notas de 1'
    print(notas_de_1_str)