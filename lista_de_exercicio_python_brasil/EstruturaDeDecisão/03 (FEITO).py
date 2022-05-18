'''
#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = str(input('Informe "F" para feminino ou "M" para masculino: ')).upper() #para transformar todas as letras em maiúsculo

if letra == 'F':
    print('Feminino!')
elif letra == 'M':
    print('Masculino')
else:
    print('Valor inválido')