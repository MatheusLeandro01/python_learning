class Televisao: #Criando uma classe -> um novo tipo de dado
    def __init__(self):
        self.ligada = False # atributo do objeto
        self.canal = 2 # atributo do objeto

tv = Televisao() # tv é um objeto da classe Televisao ou tv é uma instância de Televisao
print(tv.ligada)
print(tv.canal)

tv_sala = Televisao() #tv_sala -> objeto da classe Televisao
tv_sala.ligada = True
tv_sala.canal = 4

print(tv.canal)
print(tv_sala.canal)