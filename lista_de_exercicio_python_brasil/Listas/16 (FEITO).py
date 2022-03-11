'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
seguintes intervalos de valores:

    $200 - $299 0
    $300 - $399 1
    $400 - $499 2
    $500 - $599 3
    $600 - $699 4
    $700 - $799 5
    $800 - $899 6
    $900 - $999 7
    $1000 em diante 8

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.


'''

salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]
contagem_de_faixa_salarial = [0] * 9

for salario in salarios:
    indice = salario // 100 -2
    indice_maximo = len(contagem_de_faixa_salarial)-1
    indice = min(indice, indice_maximo)
    contagem_de_faixa_salarial[indice] += 1



print(contagem_de_faixa_salarial)