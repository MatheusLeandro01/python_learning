'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

quanto_ganha_hora = float(input('Quanto você ganha por hora? '))
numero_de_horas_trabalhadas = int(input('Quantas horas trabalhou? '))


salario_mes = quanto_ganha_hora * numero_de_horas_trabalhadas

print(f'R$ {salario_mes}.')