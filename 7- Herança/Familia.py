

class Mae:

    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print("Comendo")

    def estudar(self) -> None:
        print('Estudando')


class Filha(Mae):


    def __init__(self):
        super().__init__('Rua do Bolo')



clara = Filha()
clara.estudar()
print(clara.endereco)
