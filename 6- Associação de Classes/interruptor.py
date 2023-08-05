
from typing import Type


class Interruptor:
    def __init__(self, comodo: str) -> None: #Usando as type notations
        self.__comodo = comodo

    def acender(self) -> None:
        print(f'Acendendo {self.__comodo}')

    def apagar(self) -> None:
        print(f"Apagando {self.__comodo}")
#Associando as Duas Classes
class Pessoa:
    def acender_luz(self, interruptor: Type[Interruptor]) -> None: #A classe interruptor torna-se uma tipagem
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]) -> None:
        interruptor.apagar()

    def dormir(self):
        print("Foi dormir")



Lhama = Pessoa()
interruptor_quarto = Interruptor('Quarto')

interruptor_quarto.acender()#chamada direta
print("---------------------------------------------------")
Lhama.acender_luz(interruptor_quarto)



