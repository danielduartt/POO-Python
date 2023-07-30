class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        #self.cpf = cpf = > acessível
        self.__cpf = cpf #privado

    def print_cpf(self):#aki da certo pq a classe tem acesso a esse conteudo
        print(self.__cpf)
    #fora da classe nao á acesso


    def correr(self):
        print("Correndo....")

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('Bebendo..... ')

    def __apresentar_documento(self): #método privado, só pode ser acessado dentro da classe
        print(self.__cpf)

p1 = Pessoa('Ronaldo', 32, '4567859612')
print(p1.nome)
print(p1.idade)
#(p1.cpf)
p1.beber('cerveja')
p1.beber('coca')
