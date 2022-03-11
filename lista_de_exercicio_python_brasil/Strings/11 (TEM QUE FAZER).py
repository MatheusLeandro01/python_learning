'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

palavra = 'DevPro'.upper()
print('*Descubra a Palavra*')
print('Palavra: ', end='')
for letra in palavra:
    print('_ ', end = '')

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()

while not conjunto_letras_palavra.issubset(conjunto_letras_digitadas):
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavra:
        print('A palavra é: ', end='')
        for letra in palavra:
            print(f'_ ', end='')