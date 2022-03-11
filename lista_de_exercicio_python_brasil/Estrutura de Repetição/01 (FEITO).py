'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

'''
#EU
nota = float(input('Informe uma nota: '))
while nota > 10 or nota < 0:
    nota = float(input('Valor inválido, informe uma nota entre zero e dez: '))

print('Parabéns valor informado corretamente.')
'''

'''
while True:
    try:
        numero = int(input('Digite um valor de 0 a 10: '))
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    else:
        #if 0 <= numero <= 10:
        if numero >= 0 and numero <= 10:
            print(f'Número informado é: {numero}')
            break
        else:
            print('O número deve estar entre 0 e 10')


'''























#COnsegui replicar perfeitamente.
while True:
    try:
        numero = int(input('Informe um valor entre 0 e 10: '))
    except ValueError:
        print('Informe um valor inteiro')
    else:
        if numero >= 0 and numero <=10:
            print(f'O valor Digitado foi: {numero}') #o numero precisa estar entre 0 e 10
            break
        else:
            print('Valor inválido, informe um valor entre 0 e 10')