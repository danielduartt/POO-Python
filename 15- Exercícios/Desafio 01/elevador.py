
class Elevador:

    def __init__(self) -> None:
        self.__andar = 1

    def locomover(self, valor: int) -> None:
       if valor < 1 or valor > 15:
            self.__mensagem_de_erro()
       else:
            self.__alterar_andar(valor)

    def __mensagem_de_erro(self) -> None:
        print(f"Andar incorreto!, elevador no {self.__andar}° andar")

    def __mensagem_de_alteracao(self) -> None:
       print(f"Elevador indo para o {self.__andar}° andar")

    def __Mensagem_Terreo(self) -> None:
        print("Elevador indo para o terreo")

    def __alterar_andar(self, valor: int) -> None:
        self.__andar = valor
        if valor == 1:
            self.__Mensagem_Terreo()
        else:
            self.__mensagem_de_alteracao()
