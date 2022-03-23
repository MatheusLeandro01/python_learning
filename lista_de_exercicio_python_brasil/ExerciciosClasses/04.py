'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self):
        if self.idade < 21:            
            vezes_para_crescer = (21 - self.idade) * 0.5            
            return f'Crescimento: {vezes_para_crescer}cm'
            
    
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1
        


pessoa = Pessoa('Matheus', 20, 65, 177)
for _ in range(22):
    pessoa.envelhecer()
    print(f'Idade de {pessoa.nome} é: {pessoa.idade} e sua altura é: {pessoa.altura}')