from formas import FormasInterface

class TerrenoQuadrado(FormasInterface):
     def __init__(self, lado: float) -> None:
         self.lado = lado

     def get_perimetro(self) -> float:
         perimetro = self.lado * 4
         return perimetro

     def get_area(self) -> float:
         return self.lado * self.lado
     