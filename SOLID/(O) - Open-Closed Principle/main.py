'''Princípio Aberto-Fechado'''
#Entradas diferentes geram ações diferentes

#Comportamento Fechado
class Circo:
    def apresentar(self, tipo: int) -> None:
        if tipo == 1:
            self.apresentar_matabarismo()
        elif tipo == 2:
            self.apresentar_palhaco()
    def apresentar_matabarismo(self) -> None:
        print("Malabarista Apresentando....")

    def apresentar_palhaco(self) -> None:
        print("Palhaço Apresentando seu Show")

circo = Circo()
circo.apresentar(2) #Caso queira colocar um terceiro tipo, tenho que alterar código
print("--------------------------------------------------------------")
#Conceito de Módulo Aberto
'''
Módulo considerado aberto se ainda estiver disponível para extensão
'''
class Circo2:
    def apresentar(self, apresentador: any) -> None:
        apresentador.apresentar_show()
class Malabarista:
    def apresentar_show(self) -> None:
        print("Malabarista Apresentando seu Show")

class Palhaco:
    def apresentar_show(self) -> None:
        print("Palhaço Apresentando seu Show")
class Domador:
    def apresentar_show(self) -> None:
        print("Domador Apresentando seu Show")


circo2 = Circo2()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()
circo2.apresentar(malabarista)
circo2.apresentar(palhaco)
circo2.apresentar(domador)
#to passando no lugar de apresentador => malabarista que é da classe Malabarista e tem o método apresentar_malabarismo
