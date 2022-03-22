'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''
class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circuferencia = 4 
        self.material = 'Papel'
        
    def mostra_cor(self):
        return self.cor
    
    def troca_cor(self, cor):
        self.cor = cor

circulo_primeiro = CirculoPerfeito() #Objeto circulo_primeiro
circulo_segundo = CirculoPerfeito()

print(type(circulo_primeiro))

print(circulo_primeiro.mostra_cor())
print(circulo_segundo.mostra_cor())

print()

circulo_primeiro.troca_cor('Verde')
circulo_segundo.troca_cor('Rosa')

print(circulo_primeiro.mostra_cor())
print(circulo_segundo.mostra_cor())