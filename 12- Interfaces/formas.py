from abc import ABC, abstractmethod

class FormasInterface(ABC):
    @abstractmethod
    def get_perimetro(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass
