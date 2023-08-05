class Pessoa:
    from datetime import date
    anoAtual = date.today().year #atributo da classe
    #métodos de classes são referentes as classes

    def __init__(self, nome, idade): #metodos de instância
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):#métodos de instância
        print(self.anoAtual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, nascimento):#cls = pq quero me referir a classe
        #como não temos o self, e sim o cls, podemos acessar um atributo da classe
        idade = cls.anoAtual - nascimento
        return cls(nome, idade)


        pass

p1 = Pessoa('Luiz', 36)
print(p1.idade)
p1.get_ano_nascimento()
print("-----------------------------------")
p2 = Pessoa.por_ano_nascimento('luiz', 1987)
print(p2.idade)
p2.get_ano_nascimento()
#métodos de instância são relacionados com as instância. o método joão vai da um valor dependendo de cada obj
#ja métodos de classe não relacionados as classes


