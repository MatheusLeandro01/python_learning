'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, lado = 2): #tamanho do lado
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado(3) # aqui eu mudo o valor do lado   

print(quadrado.lado, quadrado.calcular_area())