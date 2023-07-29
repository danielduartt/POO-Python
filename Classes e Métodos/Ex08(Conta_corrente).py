'''
Crie uma classe que modele uma conta corrente
(a) Atributos: numero da conta, nome do correntista e saldo ´
(b) Metodos: alterar nome, dep ´ osito e saque; No construtor, saldo ´ e opcional, com valor ´
default zero e os demais atributos sao obrigat ˜ orios.
'''

class ContaCorrente():
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.limite = 1000
    #A) Alterar nome
    def AlterarNome(self, nomeDesejado):
        if nomeDesejado == self.nome:
            print("Você já está com esse nome!")
        elif isinstance(nomeDesejado, str):
            self.nome = nomeDesejado
            return
    #B) Depósito
    def deposito(self, deposito):
        if isinstance(deposito, float) or isinstance(deposito, int):
            valor = self.saldo + deposito
            if valor < self.limite:
                self.saldo += deposito
            else:
                print("Diminua o depósito para não estourar o limte")

    #C) Saque
    def saque(self, valorSaque):
        if isinstance(valorSaque, float) or isinstance(valorSaque, int):
            if self.saldo > 0 and self.saldo > valorSaque:
                self.saldo -= valorSaque
            else:
                print("Saldo abaixo do saque desejado")
    def __str__(self):
        return f"Número da conta: {self.numero}\nNome: {self.nome}\nSaldo: {self.saldo:.2f}"
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nomeDesejado):
        self._nome = nomeDesejado.strip().upper()


p1  = ContaCorrente(132456, "Daniel")
print(p1)
print("----------------------------------------------------")
p1.deposito(999)
print(p1)


