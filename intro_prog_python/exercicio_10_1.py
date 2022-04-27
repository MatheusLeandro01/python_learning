class Televisao:
    def __init__(self):
        self.tamanho = 40
        self.marca = "Samsung"

tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.tamanho = 65
tv_sala.marca = "LG"

tv_quarto.tamanho = 50
tv_quarto.marca = "Toshiba"

print(f'As características da tv da sala são: Tamanho = {tv_sala.tamanho} polegadas e Marca = {tv_sala.marca}. ')
print(f'As características da tv do quarto são: Tamanho = {tv_quarto.tamanho} polegadas e Marca = {tv_quarto.marca}. ')