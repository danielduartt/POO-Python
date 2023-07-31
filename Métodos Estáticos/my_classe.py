

class MinhaClasse:
    def __init__(self, estado):
        self.estado = estado

    @staticmethod
    def metodo_estatico(): #sem acesso a outros elementos da classe, usado como especificador
        #print(self.estado) #self nao é definido
        print("Estou no método estático :D")

class Error:
    @staticmethod
    def protocolo():
        print("Erro de protocolo")
    @staticmethod
    def entrada():
        print("Parâmetros incorretos")


obj = MinhaClasse(True)
#obj.metodo_estatico()
MinhaClasse.metodo_estatico()
Error.entrada() #Não precisa de um objeto atuando sobre isso



