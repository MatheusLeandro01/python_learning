class Pessoa:
    def __init__(self, nome=None, idade=23):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        pass

p = Pessoa('Matheus')
print(p.nome)