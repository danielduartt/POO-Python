'''
Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga ´
de operador, os metodos para fazer as operac¸ ´ oes de soma, subtrac¸ ˜ ao e produto entre ˜
dois numeros.
'''
class NumComplexo():
    def __init__(self, real, complexo):
        self.real = real
        self.complexo = complexo

    def __str__(self):
        return f"{self.real} +- {self.complexo}i"

    @property
    def real(self):
        return self._real
    def complexo(self):
        return self._complexo

    @real.setter
    def real(self, realDesejado):
        if isinstance(realDesejado, int):
            self._real = realDesejado
    def complexo(self, valor):
        if isinstance(valor, int):
            self._complexo = valor


    def __add__(self, other):
        parteReal = self.real + other.real
        parteComplexa = self.complexo + other.complexo
        return NumComplexo(parteReal, parteComplexa)
    def __sub__(self, other):
        parteReal = self.real - other.real
        parteComplexa = self.complexo - other.complexo
        return NumComplexo(parteReal, parteComplexa)
    def __mul__(self, other):
        parteReal = self.real * other.real
        parteComplexa = self.complexo * other.complexo
        return NumComplexo(parteReal, parteComplexa)




n1 = NumComplexo(10, 20)
print(n1)
n2 = NumComplexo(2, 4)
print(n2)
soma = n1 + n2
print(f"Soma: {soma}")
sub = n1 - n2
print(f"Subtração: {sub}")
mult = n1 * n2
print(f"Multiplicação: {mult}")







