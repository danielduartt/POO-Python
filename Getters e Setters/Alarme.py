class Pessoa: #Substantivo
    def __init__(self, name: str, idade: int) -> None:
        self.name = name #Substantivo
        self.idade = idade

    def dirigir(self, veiculo: str) -> None: #Verbos
        print(f"Dirigindo um(a) {veiculo}")

    def cantar(self) -> None:
        print("LaLaLa")

    def apresentar_Idade(self) -> int:
        return self.idade
#-------------------------------------------------------------------------------------------------
#Métodos Getters e Setters => cria um mecanismo de acesso para estados
#Os métodos Getters e Setters Tratam os atributos como se fossem estados deu m classe
#Ex:

class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado  #estado privado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        self.__estado = valor





