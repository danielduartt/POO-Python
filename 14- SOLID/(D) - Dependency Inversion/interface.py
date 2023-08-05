from abc import ABC, abstractmethod


class Repositorio(ABC):

    @abstractmethod
    def inserir(self, dado: any) -> None:
        pass

    @abstractmethod
    def deletar(self, dado: any) -> None:
        pass
