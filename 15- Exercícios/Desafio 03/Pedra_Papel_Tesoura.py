


class Computador:

    def __init__(self):
        self.__listacomp = ['Pedra', 'Papel', 'Tesoura']
        self.__computador = self.escolherValor()

    def escolherValor(self) -> str:
        from random import choice
        return choice(self.__listacomp)

class Player:
    def __init__(self, nome: str, escolha: str) -> None:
        self.nome = nome
        self.__validar_escolha(escolha)

    def __validar_escolha(self, escolha: str) -> None:
        if isinstance(escolha, str):
            self.__escolha = escolha
        else:
            raise ValueError("Valor digitado errado!")
    def alterar_escolha(self, novoValor: str) -> None:
        self.__escolha = novoValor

class Game:
    from typing import Type
    def GameInit(self, player: Type[Player], computer: Type[Computador]) -> None:
        pass


    def Verificar_Vencedor(self, player: Type[Player], computer: Type[Computador]) -> None:
        pass



