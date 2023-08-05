'''
Implemente uma classe para representar em vetor (x,y,z) no R3
. Implemente os metodos ´
para calcular a soma, subtrac¸ao, produto vetorial, produto escalar e m ˜ odulo.
'''

class VetorR3():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x} i, {self.y} j, {self.z} k) "
    def __add__(self, other):
        valorX = self.x + other.x
        valorY = self.y + other.y
        valorZ = self.z + other.z
        return VetorR3(valorX, valorY, valorZ)

    def __sub__(self, other):
        valorX = self.x - other.x
        valorY = self.y - other.y
        valorZ = self.z - other.z
        return VetorR3(valorX, valorY, valorZ)

    def produtoVetorial(self, other):
        x_resultado = self.y * other.z - self.z * other.y
        y_resultado = self.z * other.x - self.x * other.z
        z_resultado = self.x * other.y - self.y * other.x
        return VetorR3(x_resultado, y_resultado, z_resultado)

    def produto_escalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def modulo(self):
        return VetorR3(self.x ** 2, self.y ** 2, self.z ** 2) ** 0.5






