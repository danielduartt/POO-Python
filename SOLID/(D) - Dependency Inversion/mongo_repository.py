from interface import Repositorio


class MongoDB(Repositorio):

    def inserir(self, dado: any) -> None:
        print(f"Inserindo {dado} no banco MondoDB")

    def deletar(self, dado: any) -> None:
        print(f"Deletando {dado} no banco MongoDB")