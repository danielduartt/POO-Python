'''
PRINCÍPIO DA SUBSTITUIÇÃO DE LISKOV
objA e objB devem ter a mesma funcionalidade
Herança deve ser uma complementação! não se pode mexer de qualquer forma, deve-se complementar 
'''

class PessoaA:
    def se_apresentar(self):
        print("Olá, sou a pessoa A")

class PessoaB(PessoaA):
    def __init__(self) -> None:
        super().__init__()
    #recebi um método por herança, mas modifiquei ele => Qubra do princípi ode liskov
    def se_apresentar(self):
        print("Estou alterando esse método")

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

