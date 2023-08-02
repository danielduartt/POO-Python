from formas import FormasInterface
from quadrado import TerrenoQuadrado
from retangulo import TerrenoRetangular
from engenheiro import Engenheiro
from typing import Type

eng = Engenheiro("Marcelo")
terrenoQ = TerrenoQuadrado(4)
terrenoR = TerrenoRetangular(2, 3)
print("------------Perimetro do retangulo------------")
eng.medir_perimetro(terrenoR)
print("------------Perimetro do quadrado------------")
eng.medir_perimetro(terrenoQ)