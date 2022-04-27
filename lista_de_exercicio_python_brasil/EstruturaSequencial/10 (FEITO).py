'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temp_em_graus_celsius = float(input('Informe a temperatura em cº: '))

converter_para_fahrenheit = (temp_em_graus_celsius * 1.8) + 32

print(f'{temp_em_graus_celsius}ºC -> {converter_para_fahrenheit:.1f}ºF')