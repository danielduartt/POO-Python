class Pessoa:
    def __init__(self, nome, idade, comendo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
    def comer(self, alimento):
        if self.comendo:
            print("termine de comer primeiro")
            return #para e não executa mais nada
        else:
            self.comendo = True
            print(f"{self.nome} está comendo {alimento}")
    def TerminarDeComer(self):
        if self.comendo:
            self.comendo = False
            return
        else:
            print("Você não está comendo nada,BESTA")



pessoa1 = Pessoa('Daniel', 20)
print(f"{'Nome':<2}", f"{'Idade':<6}", f"{'Comendo':>4}", f"{'Falando':>2}")
print(pessoa1.nome, end=' ')
print(pessoa1.idade, end=' ')
print(f"{pessoa1.comendo:>4}", end=' ')
print('{:>8}'.format(pessoa1.falando))
print("~"*26)
pessoa1.comer("feijão")
print(pessoa1.comendo)
pessoa1.comer("feijão")
pessoa1.TerminarDeComer()
print(pessoa1.comendo)
pessoa1.TerminarDeComer()



