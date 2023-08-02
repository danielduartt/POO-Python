class PessoaA:

    def se_apresentar(self):
        print("Olá, sou a pessoa A")

class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()
    def se_apresentar(self):
        print("Olá, sou a pessoa B")


class PessoaC(PessoaB):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print("Olá, sou a pessoa C")


pessoa = PessoaA()
pessoa2 = PessoaB()
pessoa3 = PessoaC()
pessoa.se_apresentar()
pessoa2.se_apresentar()
pessoa3.se_apresentar()