from abs_class import AbstractClass

class Filha(AbstractClass):
    def __init__(self):
        super().__init__()
    def apresentar_metodo(self) -> None:
        print(self.atributo)
    #Por regra, devo implementar os métodos abstratos nas classes filhas
    def metodo_abstrato(self) -> None:
        print("Implementando método abstrato")

filha = Filha()
filha.apresentar_metodo()
filha.metodo('Estou aqui')
filha.metodo_abstrato()
'''
#Vai gerar um erro, pois estou instancinado da classe abstrata
absClass = AbstractClass() #estou instanciando, o que não pode ser feito com uma classe abstrata
absClass.metodo('Fazendo algo...')
'''