'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustive
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro:float, quantidade_combustivel:float):
        self.tipoCombustivel = tipo_combustivel
        self.valorLitro = valor_litro
        self.quantidadeCombustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valorLitro
        self.quantidadeCombustivel -= litros_abastecidos
        print(f'Foram abastecidos {litros_abastecidos:.2f} litros a um valor de R$ {valor:.2f}')
        print(f'Sobraram na bomba {self.quantidadeCombustivel:.2f} Litros.')

    def abastecer_por_litro(self, valor:float):
        litros_que_eu_quero = valor * self.valorLitro
        self.quantidadeCombustivel -= valor
        print(f'{valor} litros custam R$ {litros_que_eu_quero:.2f}.')
        print(f'Caso compre, irá sobrar {self.quantidadeCombustivel:.2f} Litros de combustível.')

    
bomba = BombaCombustivel('Gasolina', 4.59, 100)

print(bomba.abastecer_por_valor(100))
print(bomba.abastecer_por_litro(50))