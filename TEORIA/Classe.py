class Pessoa:
    def __init__(self, *filhos, nome=None, idade=32): #MÉTODO CONSTRUTOR/ESPECIAL
        self.nome = nome
        self.idade = idade #ATRIBUTO DE DADOS
        self.filhos = list(filhos) #ATRIBUTO COMPLEXO

    def cumprimentar(self): #método
        return 'Olá'


if __name__ == '__main__':  
    matheus = Pessoa('Matheus', 'Leandro', 'Victor', nome = 'Theus') #OBJETO  #INSTÂNCIA DA CLASSE
    matheus.esposa = 10 #ATRIBUTO DINÂMICO    


    for filho in matheus.filhos:
        print(filho)

'''
class Pessoa:
    def __init__(self, idade=None, nome='', *filhos):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

if __name__ == ('__main__'):
    victor = Pessoa(nome='Victor', idade=5) #Filho de Matheus
    marcelo = Pessoa(nome='Marcelo', idade=3)#Filho de Matheus
    matheus = Pessoa(23, 'Matheus', victor, marcelo) #Pai de Victor e Marcelo
    victor.filhos = 'Victorzinho JR'
    matheus.neto = 'Victorzinho JR' #Atributo dinâmico -> atributo criado para o objeto "matheus" após o método construtor
    for filho in matheus.filhos:
        print(filho.nome, filho.idade, filho.filhos)
    print(matheus.neto)

    print(victor.__dict__)
    print(marcelo.__dict__)
    print(matheus.__dict__)
'''