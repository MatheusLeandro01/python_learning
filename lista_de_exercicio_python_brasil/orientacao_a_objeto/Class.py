class Soma:
    def __init__(self, n1, n2):
        self.x = n1
        self.z = n2
        print('Objeto Criado!!!')
    def calculandoSoma(self):
        total = self.x + self.z
        return f'Resultado é: {str(total)}'

soma = Soma(10, 20)

total = soma.calculandoSoma()

print(total)