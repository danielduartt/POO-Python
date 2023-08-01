from typing import Type

class Casa:

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def acender_luz(self) -> None:
        print("Acendendo Luz...")

    def get_endereco(self) -> str:
        return self.__endereco

    def set_endereco(self, local: str) -> None:
        if isinstance(local, str):
            self.__endereco = local
        else:
            raise ValueError

class Pessoa:
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luz()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

#Ações de um OBJ dependem de outro OBJ
#Contudo uma classe acaba sendo muito acoplada a outra, o que não é muito boms
casa_Do_amigo = Casa('São Francisco')
ana = Pessoa('Ana', casa_Do_amigo)
ana.entrar_no_local()
ana.apresentar_local()
