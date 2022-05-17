'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que
custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor.
  Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
  considere latas cheias.
'''
import math

area_a_ser_pintada = float(input('Informe o valor da área em m²: ')) #area em metros quadrados
area_com_folga = area_a_ser_pintada * 1.1
litros_por_metro = 6
litros_a_serem_usados = math.ceil(area_com_folga / litros_por_metro)

#LATAS
litros_por_latas = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_latas) #Informa a quantidade de latas
valor_com_apenas_latas = numero_de_latas * 80 #Informa o Custo das latas

#GALÕES
litros_por_galoes = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galoes)
valor_com_apenas_galoes = numero_de_galoes *25

print(f'Você precisa de {litros_a_serem_usados} Litros')
print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R${valor_com_apenas_latas}')
print(f'Você deverá usar {numero_de_galoes} galoes de 3.6 litros, no valor de R${valor_com_apenas_galoes}')
print()

#Compra de tintas otimizada

#LATAS
litros_por_latas = 18
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_latas) #Informa a quantidade de latas
valor_com_apenas_latas = numero_de_latas * 80 #Informa o Custo das latas

#GALÕES
litros_por_galoes = 3.6
sobra_da_lata = litros_a_serem_usados - (numero_de_latas * litros_por_latas)
#litros_faltantes =
numero_de_galoes = math.ceil(sobra_da_lata / litros_por_galoes)
valor_com_apenas_galoes = numero_de_galoes * 25

print(f'Você precisa de {litros_a_serem_usados} Litros')
print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R${valor_com_apenas_latas}')
print(f'Você deverá usar {numero_de_galoes} galoes de 3.6 litros, no valor de R${valor_com_apenas_galoes}')
print(f'Custo total de R${valor_com_apenas_galoes + valor_com_apenas_latas}')
