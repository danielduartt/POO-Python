from formas import FormasInterface
from typing import Type

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        print(f"Perímetro medido: {terreno.get_perimetro()}")

    def medir_area(self, terreno: Type[FormasInterface]):
        print(f"Área medida: {terreno.get_area()}")

