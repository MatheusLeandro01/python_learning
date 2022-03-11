'''
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida 
mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''

nome = input('Informe seu nome: ').upper()

nome_invertido_por_letra = ''.join(reversed(nome))


nome_invertido_por_palavra = ' '.join(reversed(nome.split()))

print(nome_invertido_por_palavra)
print(nome_invertido_por_letra)
print(nome)




'''
nome = 'Matheus leandro da Silva Rosa'.upper()


contrario_letra = nome[::-1]
contrario_palavra = ' '.join(reversed(nome.split()))

print(contrario_letra)
print(contrario_palavra)
print(nome)
'''