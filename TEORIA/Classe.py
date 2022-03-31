class Pessoa:
    olhos = 2 # atributo de classe

    def __init__(self, idade=None, nome='', *filhos):
        self.idade = idade #atributo de objeto ou atributo de Instância
        self.nome = nome
        self.filhos = list(filhos) #atributo complexo

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
    print(matheus.olhos) # imprimindo a minha instância de atributo de classe