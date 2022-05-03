class Pessoa:
    def __init__(self, altura=None, nome=10.3, idade=23):
        self.altura = altura
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def crescer(self, altura=1):
        self.altura +=altura