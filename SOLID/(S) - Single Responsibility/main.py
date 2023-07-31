'''RESPONSABILIDADE ÚNICA'''
class SistemaCadastral:

    '''def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("Acessando o Banco de Dados...")
            print(f"Cadastrar o Usuário {nome}, Idade {idade}")
        else:
            print("Dados Inválidos")
    '''

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print("Acessando o Banco de Dados...")
        print(f"Cadastrar o Usuário {nome}, Idade {idade}")

    @staticmethod
    def __erro(self) -> None:
        print("Dados inválidos")
    pass

#CASO MUDAR ALGO NO CÓDIGO, APENAS PRECISO ALTERAR ALGUMA DESSAS FUNCIONALIDADES
pessoa = SistemaCadastral()
pessoa.cadastrar("Daniel", 20)
