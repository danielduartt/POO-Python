from formas import FormasInterface


class TerrenoRetangular(FormasInterface):
    def __init__(self, largura: float, comprimento: float) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def get_perimetro(self) -> float:
        perimetro = 2 * (self.largura + self.comprimento)
        return perimetro

    def get_area(self) -> float:
        return self.largura * self.comprimento
