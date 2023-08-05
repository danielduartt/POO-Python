class A:
    vc = 123

class B:
    vc = 123
    def __init__(self):
        self.vc = 321

a1 = A()
a2 = A()
print("------------------Vc = 123-------------------")
A.vc = 123
print(a1.vc)
print(a2.vc)
print(A.vc)
print("-------------------Vc = 321-------------------")
A.vc = 321 #Muda para todos
print(a1.vc)
print(a2.vc)
print(A.vc)
print("-------------------a1.vc = 321-----------------")
a1.vc = 234
print(a1.vc) #ele procura a variável na instancia, caso nao ache, procura na classe
print(a2.vc)
print(A.vc)
print("-----------------------Dict---------------------")
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
print("-----------Comparando Prop de classe e Prop de Instância--------")
b1 = B()
b2 = B()
print(b1.vc)
print(b2.vc)
print(B.vc)
print("-------------------------------------------------------------------")
