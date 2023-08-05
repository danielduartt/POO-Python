from interface import Repositorio


class MySqlRepositorio(Repositorio):

    def inserir(self, dado: any) -> None:
        print(f"Inserindo {dado} no banco MySql")

    def deletar(self, dado: any) -> None:
        print(f"Deletando {dado} no banco MySql")