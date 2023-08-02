'''INVERSÃO DE DEPENDÊNCIA'''
from typing import Type
from interface import Repositorio
from mysql_repository import MySqlRepositorio
from mongo_repository import MongoDB



class Usuario():

    def __init__(self, repository: Type[Repositorio]) -> None:
        self.__repository = repository


    def armazenar_dados(self, dado: any) -> None:
        self.__repository.inserir(dado)

    def remover_dados(self, dado: any) -> None:
        self.__repository.deletar(dado)


usuario = Usuario(MongoDB())#injetando um Obj dentro de usuário
usuario.armazenar_dados(23)

bd = MySqlRepositorio()
usuario2 = Usuario(bd)
usuario2.armazenar_dados(999)

'''
Tem um problema nisso tudo, se eu precisar criar um repositorio de MongoDB(por exemplo)
vou ter que criar uma classe com os mesmos métodos que as demais 
Para resolver isso, seria interessante criar uma <interface> repositório
Daí criar essas novas classes 

'''