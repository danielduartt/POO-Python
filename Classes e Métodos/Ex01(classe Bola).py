'''
Classe Bola: Crie uma classe que modele uma bola:
q- Atributos: Cor, circunferência, material
b- Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocaCor(self, cor):
        if self.cor == cor:
            print(f"A bola ja é da cor {self.cor}")
            return
        self.cor = cor
    def mostrarCor(self):
        print(f"A bola é da cor: {self.cor}")


bola = Bola('branco', '20', 'sacola')
bola.mostrarCor()
bola.trocaCor('azul')

bola.mostrarCor()
bola.trocaCor('azul')



