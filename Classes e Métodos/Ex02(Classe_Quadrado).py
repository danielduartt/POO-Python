'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, lado):
        self.lado = int(lado)
        self.historico = list()

    def MudarValor(self, novo_valor):
        if self.lado == novo_valor:
            print(f"O quadrado ja possui {self.lado}", end='')
            print(" lados" if self.lado > 1 else " lado")
            return
        else:
            self.historico.append(self.lado)
            self.lado = novo_valor
    def RetonarValor(self):
            self.lado = self.historico[0]
            self.historico.pop()

    def Area(self):
        print(f"área do quadrado: {self.lado ** 2}")

    def verHistorico(self):
        try:
            print(self.historico[0])
        except IndexError:
            print("Não há nada no histórico")


q1 = Quadrado('4')
q1.Area()
print("-----------Mudando Valor para 16----------------------")
q1.MudarValor(16)
q1.Area()
print("------------Vendo o Histórico-------------------------")
print(q1.historico[0])
print("-----------Retornando o Valor do Histórico(4)---------")
q1.RetonarValor()
q1.Area()
print("------------Vendo o Método 'VerHistorico'-------------")
q1.verHistorico()
print('-----------------Mudando valor para 20----------------')
q1.MudarValor(20)
q1.Area()
print("------------Vendo o Método 'VerHistorico'-------------")
q1.verHistorico()

