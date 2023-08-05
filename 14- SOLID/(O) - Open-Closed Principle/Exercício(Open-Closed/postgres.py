class PostgresDB:

    def __init__(self) -> None:
        self.__conexao = 'Postgres'

    def conectar(self) -> str:
        print("Conectando ao Banco Postgres...")
        return self.__conexao

    def desconectar(self) -> str:
        print("Desconectando ao bando Postgres...")
        return self.__conexao

