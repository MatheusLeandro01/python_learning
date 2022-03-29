'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

temperatura_em_graus_fahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '))
conversao_para_graus_celsius = 5 * ((temperatura_em_graus_fahrenheit-32) / 9)

print(f'{temperatura_em_graus_fahrenheit}º Fahrenheit é igual a {conversao_para_graus_celsius:.2f}º Celcius.')