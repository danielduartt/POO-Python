from typing import Type
'''
IDEIA DO PRINCÍPIO DE LISKOV 
OS SUBTIPOS TEM OS MESMOS MÉTODOS 

'''
class Animal: #ELEMENTO GENÉRICO

    def comer(self) -> None:
        print("Animal comendo...")
        print()

    def domir(self) -> None:
        print("Animal dormindo ZzZZzzZzZz")
        print()

    def andar(self) -> None:
        print("Animal andando...")
        print()

#Subtipos da classe 'Animal'
#ESPECIFICANDO A CADA SUBTIPO
class Aves(Animal):

    def __init__(self) -> None:
        super().__init__()

    def cantar(self) -> None:
        print("Ave cantarolando laLalalalaLAlA")
        print()

class Pinguim(Aves):

    def __init__(self) -> None:
        super().__init__()

    def escorregar(self) -> None:
        print("O pinguim está escorregando")

class Pessoa:

    def obsevar(self, animal: Type[Animal]) -> None:
        animal.comer()



roberto = Pessoa()
pinguim = Animal()
roberto.obsevar(pinguim)