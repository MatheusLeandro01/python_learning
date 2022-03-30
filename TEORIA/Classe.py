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