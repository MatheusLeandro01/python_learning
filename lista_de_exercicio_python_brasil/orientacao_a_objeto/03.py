class Televisao: #definindo minha classe
    def __init__(self): #método construtor #tudo o que fica "entre parenteses" é chamada de "Parametro"
        self.canal = 11 #atributo do objeto -> self representa o objeto em si.
        self.ligada = True
        n2 = 10 #variável local do método -> NÃO É UM ATRIBUTO DO OBJETO

tv_quarto_1 = Televisao() #var1 é um objeto que utiliza a classe Televisao() "var1 é um instancia de Televisao"
tv_quarto_1.canal = 4
tv_quarto_1.ligada = False

tv_sala_principal = Televisao()
tv_sala_principal.canal = 15
tv_sala_principal.ligada = True


'''
Dúvidas:
    Oque é o objeto?
'''