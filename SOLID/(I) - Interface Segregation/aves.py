from avesInterface import AveVoadoraInterface, AveNVoadoraInterface

class Canario(AveVoadoraInterface):
    def comer(self) -> None:
        print("Canário comendo...")

    def voar(self) -> None:
        print("Canário voando...")

    def gritar(self) -> None:
        print("Canário gritando...")

class Pinguim(AveNVoadoraInterface):
    def comer(self) -> None:
        print("Pinguim comendo...")

    '''
    def voar(self) -> None: #Pinguim não voa, mas tem que ser implementado esse método, por causa da Regra da interface
        None #Para resolver isso, devemos criar uma interface menos generalista
    '''
    def gritar(self) -> None:
        print("Pinguim gritando...")

