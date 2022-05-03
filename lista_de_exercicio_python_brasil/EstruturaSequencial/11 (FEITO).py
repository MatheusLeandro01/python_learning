'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''

n1 = int(input('Informe um valor inteiro: '))
n2 = int(input('Informe outro valor inteiro: '))
n3 = float(input('Informe um valor real: '))

dobro_do_primeiro_com_metade_do_segundo = (n1*2) * (n2/2)
soma_do_triplo_do_primeiro_com_o_terceiro = (n1*3) + n3
terceiro_ao_cubo = n3 ** 3

print(f'Resposta letra A: {dobro_do_primeiro_com_metade_do_segundo}')
print(f'Resposta letra B: {soma_do_triplo_do_primeiro_com_o_terceiro}')
print(f'Resposta letra C: {terceiro_ao_cubo}')