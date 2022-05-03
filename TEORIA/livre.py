<<<<<<< HEAD
class Pessoa:
    olhos = 2
    def __init__(self, nome=None, idade=23, *filhos):
        self.idade = idade
        self.nome = nome
        self.filho = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def metodo_de_classe(cls, nome=None):
        cls.nome = nome



matheus = Pessoa('Matheus', 23)
leandro_dutra = Pessoa('Leandro', 50, matheus)

for filho in leandro_dutra.filho:
    print(f'Nome: {filho.nome}\nIdade: {filho.idade}')

matheus.metodo_estatico()
=======
>>>>>>> 2c75a9ca4678fb4ae00d6885c5ea1a6ff82766c7
