'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
as taxas de crescimento.
'''

#'''
#eu
pais_a = 100_000
pais_b = 300_000

contador_de_ano = 0

while pais_a < pais_b:
    contador_de_ano += 1
    pais_a += (pais_a * 0.03)
    pais_b += (pais_b * 0.015)
    print(f'No ano "{contador_de_ano}" O "País A" possuirá "{int(pais_a)}" Habitantes e o Pais B possuirá "{int(pais_b)}" Habitantes.')

#'''

'''
populacao_a = 80_000
populacao_b = 200_000
taxa_de_crescimento_de_a = 1.03
taxa_de_crescimento_de_b = 1.015
anos = 0

while populacao_a < populacao_b:
    print(f'Populações no ano {anos}')
    print(f'População de A: {populacao_a}')
    print(f'População de B: {populacao_b}')
    anos += 1
    populacao_a *= taxa_de_crescimento_de_a
    populacao_b *= taxa_de_crescimento_de_b
'''