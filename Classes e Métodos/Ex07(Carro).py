'''
Crie uma classe que modele um carro
(a) Atributos: marca, ano e prec¸o
(b) Metodos: mostrar prec¸o e de exibic¸ ´ ao dos dados ˜
Leia os dados de 5 carros e um valor p, Mostre as informac¸oes de todos os carros com ˜
prec¸o menor que p.
'''

class Carro():
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def __str__(self):
        return f"Carro: {self.marca}\nAno: {self.ano}\nPreço: {self.preco}R$ "

    def ExibirPreco(self):
        print(f'Preço do Carro com Marca {self.marca}: {self.preco}R$')

    def PrintCarro(self):
        print(f"Carro: {self.marca}\nAno: {self.ano}\nPreço: {self.preco}R$ ")
        print("----------------------------------------------------------------------")

carros = list()

for i in range(0, 5):
    marca = input(f'Digite a marca do carro{i + 1}: ')
    ano = int(input(f"Digite o ano do carro{i + 1}: "))
    preco = float(input(f"Digite o preço do carro{i + 1}: "))
    carro = Carro(marca, ano, preco)
    carros.append(carro)
menorPreco = min(carros, key=lambda carro: carro.preco)
print("--------Carros Cadastrados----------")
for i in carros:
    print(f"{i.PrintCarro()}")

print("----------Menor Preço---------------")
print(f"Marca: {menorPreco.marca}\tPreço: {menorPreco.preco}R$")
