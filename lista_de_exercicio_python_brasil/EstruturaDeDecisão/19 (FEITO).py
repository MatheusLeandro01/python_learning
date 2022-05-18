'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 

'''
#'''
numero = 123 #int(input('Inform um valor entre 0 e 999: '))

centenas_str = dezenas_str = unidade_str = '' #Criou três variáveis do tipo string

partes_numericas = 0 #vai servir para o final (Na horas das 'virgulas' e 'e'.)


centenas_int, numero = divmod(numero, 100) #divmod 'numero // 100' -> centenas_int(valor inteiro) -> numero(resto da divisão de numero // 100)
if centenas_int == 1:
    centenas_str = ('1 Centena')
    partes_numericas += 1
elif centenas_int > 1:
    centenas_str = (f'{centenas_int} Centenas')
    partes_numericas += 1

'''
numero = 123

centena, numero = divmod(numero, 100) #aprensenta o resultado da divisão inteira e também o resto da divisão
print(centena)#EX 123 // 100 = 1 -> Resto da divisão 123 // 100 = 23.


print(numero) # Anteriormente a variável "número" era igual a "123" após utilizar a função divmod == 23(resto)

dezena, numero = divmod(numero, 10)
print(dezena)# 23 // 10 = 2 -> resto da divisão 23 / 10 = 3

print(numero) # O resto da divisão de 23/10 = 3
'''


dezenas_int, numero = divmod(numero, 10)
if dezenas_int == 1:
    dezenas_str = ('1 Dezena')
    partes_numericas += 1
elif dezenas_int > 1:
    dezenas_str = (f'{dezenas_int} Dezenas')
    partes_numericas += 1


if numero == 1:
    unidade_str = ('1 Unidade')
    partes_numericas += 1
elif numero > 1:
    unidade_str = (f'{numero} Unidades')
    partes_numericas += 1


if partes_numericas == 0:
    print('Não possui centenas, dezenas ou unidades.')
elif partes_numericas == 1:
    print(centenas_str + dezenas_str + unidade_str)
elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidade_str}')
elif partes_numericas == 2:
    if centenas_str != '':
        segunda_parte = dezenas_str + unidade_str
        print(f'{centenas_str} e {segunda_parte}')
    else:
        print(f'{dezenas_str} e {unidade_str}')


#print(centenas_str, dezenas_str, unidade_str)
#'''



'''
numero = 326

centena, numero = divmod(numero, 100) #326/100 dá 3 e sobra 26
print(f'{centena} centena')
#print(numero)


dezena, numero = divmod(numero, 10) #26/10 dá 2 e sobra 6
print(f'{dezena} dezena')
#print(numero)

unidade = numero #6 é a sobra
print(f'{unidade} Unidade')


n1, n2 = divmod(10, 2) # DIVMOD n1 é o resultado da divisão de 10 / 2 e n2 é o resto da divisão de 10 / 2

print(n1, n2)
'''







# FIZ SOZINHO (MESMA COISA DE CIMA)

'''
numero = 16

centenas_str = dezenas_str = unidades_str = ''

contador = 0

centenas_int, numero = divmod(numero, 100)
if centenas_int == 1:
    centenas_str = ('1 Centena')
    contador += 1
elif centenas_int > 1:
    centenas_str = (f'{centenas_int} Centenas')
    contador += 1


dezenas_int, numero = divmod(numero, 10)
if dezenas_int == 1:
    dezenas_str = ('1 Dezena')
    contador += 1
elif dezenas_int > 1:
    dezenas_str = (f'{dezenas_int} Dezenas')
    contador += 1

if numero == 1:
    unidades_str = ('1 Unidade')
    contador += 1
elif numero > 1:
    unidades_str = (f'{numero} Unidades')
    contador += 1

if contador == 0:
    print('Não há centenas, dezenas ou unidades.')
elif contador == 1:
    print(centenas_str + dezenas_str + unidades_str)
elif contador == 2:
    if centenas_str != '':
        print(f'{centenas_str} e {dezenas_str + unidades_str}')
    else:
        print(f'{dezenas_str} e {unidades_str}')
elif contador == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidades_str}')

'''