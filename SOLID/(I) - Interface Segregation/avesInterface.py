'''Princípio da Segregação da Interfaces'''
#Evitar depender de coisas não utilizadas
from abc import ABC, abstractmethod

'''class AvesInterfaces(ABC):
    @abstractmethod
    def comer(self) -> None:
        pass

    @abstractmethod
    def voar(self) -> None:
        pass

    @abstractmethod
    def gritar(self) -> None:
        pass
'''
class AveVoadoraInterface(ABC):
    @abstractmethod
    def comer(self) -> None:
        pass

    @abstractmethod
    def voar(self) -> None:
        pass

    @abstractmethod
    def gritar(self) -> None:
        pass

class AveNVoadoraInterface(ABC):
    @abstractmethod
    def comer(self) -> None:
        pass
    @abstractmethod
    def gritar(self) -> None:
        pass