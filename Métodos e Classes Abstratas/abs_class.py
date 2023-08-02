from abc import ABC, abstractmethod

class AbstractClass(ABC): #transformo essa classe em abstrata
    #porém só se torna abstrata se houver um método abstrato

    def __init__(self) -> None:
        self.atributo = "Olá, Mundo"

    def metodo(self, elemento: str) -> None:
        print(elemento)

    @abstractmethod #=> método abstrato
    def metodo_abstrato(self) -> None:
        pass