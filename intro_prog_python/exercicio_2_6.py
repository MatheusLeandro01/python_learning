# Modifique o programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$ 750

salario = 750 #variável chamada "salário" que recebe o valor "1500"
aumento = 15 # variável chamada "aumento" que recebe o valor "5' -> no caso será: 5%
valor_novo_salario = salario + ((salario * aumento) / 100) #lógica matemárica para aumentar o salário em 5%
print(f'O salário atual é: R$ {salario}, com a atualização fica: R$ {valor_novo_salario}')