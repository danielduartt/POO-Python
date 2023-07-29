'''
Esconder certas partes para proteger a classe em si
'''
'''
Encapsulamento em outras linguagens:
public = acessado dentro e fora da classe
protected = dentro da classe e filhas
private = só dentro da classe 
Pq usar? => proteger a aplicação
'''
'''
Em python:
_(fraco) ou __(forte) = private 

'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {} #publico, acessível dentro e fora

    def setDados(self, id, nome):
        if 'cliente' not in self.__dados:
            self.__dados['cliente'] = {id: nome}
        else:
            self.__dados['cliente'].update({id: nome})
    def ListarDados(self):
        for k, v in self.__dados['cliente'].items():
            print(f"Id:{k} / Nome: {v}")

    def ApagaCliente(self, id):
        del self.__dados['cliente'][id]

bd = BaseDeDados()
bd.setDados(1, 'Otávio')
bd.setDados(2, 'Rose')
bd.__dados = 'Outra coisa'#o python renoamea o atributo, cria um outro atributo
print(bd.__dados)
print(bd._BaseDeDados__dados) # valor real

'''
Posso acessar com métodos get(pegar) e set(definir) 



'''