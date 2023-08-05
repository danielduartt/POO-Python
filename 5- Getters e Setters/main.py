

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco *(percentual/100))

#------------------------------Tipo Proteção--------------------------------------
    # Getter = obtem um valor
    @property #mesmo nome da variável(preco)
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valorDesejado):
        if isinstance(valorDesejado, str):
            valorDesejado = valorDesejado.strip().replace('R$', '')
            valorDesejado = float(valorDesejado)
        self._preco = valorDesejado
#---------------------------------Getter e Setter para nome----------------------------
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nomeDesejado):
        self._nome = nomeDesejado.strip().upper()
    pass


p1 = Produto("Camiseta", 50)
p1.desconto(10)
print(p1.nome)
print(p1.preco)
p2= Produto("Caneca",'15')
p2.desconto(10)
print(p2.nome)
print(p2.preco)


