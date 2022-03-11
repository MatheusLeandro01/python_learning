'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
'''
#Renzo
'''
def imprimir_triangulo_de_numeros(n: int):
    for i in range(1, n+1):
        for _ in range(i):
            print(i, end='   ')
        print('  ')

print(imprimir_triangulo_de_numeros(5))
'''


def imprimir (n: int):
    for i in range(1, n+1):
        for _ in range(i):
            print(i, end='   ')
        print(' ')

print(imprimir(3))