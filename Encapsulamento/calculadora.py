class Calculadora:
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print("Operação inválida")

    #Quero que o usuário apenas mecha na função calcular
    def __adicionar(self, n1 , n2):
        return n1 + n2

    def __subtrair(self, n1, n2):
        return abs(n1 - n2)

calculadora = Calculadora()

print(calculadora.calcular('+', 10, 2))