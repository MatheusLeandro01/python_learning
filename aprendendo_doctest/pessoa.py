'''
    exemplo:
    >>> pessoa = Pessoa()
    >>> pessoa.altura
    175
    >>> pessoa.crescer()
    >>> pessoa.altura
    177
'''
class Pessoa():
    def __init__(self):
        self.altura = 175

    def crescer(self):
        self.altura += 2