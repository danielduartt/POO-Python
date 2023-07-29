

class NPC:
    def __init__(self, nome, time , forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f"Nome......: {self.nome}")
        print(f"Time......: {int(self.time)}")
        print(f"Força.....: {int(self.forca)}")
        print(f"Munição...: {int(self.municao)}")
        print(f"Vivo......: {'sim' if self.vivo else 'não'}")
        print(f"Energia...: {float(self.energia)}")
        print("-------------------------------------------------")


#classe soldado vai herdar os atributos do NPC
class Soldado(NPC):

    def __init__(self, nome, time): #sobrescreve os contrutor da classe pai
        self.forca = 120
        self.municao = 100
        super().__init__(nome, time, self.forca, self.municao) #o super chama o construstor da classe pai

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 50
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 300
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)#super é para invocar um método ou prop da classe pai
    def inf(self):
        super().info()

s1 = Guarda("olho vivo", 1)
s2 = Soldado("Bala na agulha", 1)
s3 = Elite("Ninja", 1)
s4 = Guarda("Super atento", 2)
s5 = Elite("Sua mãe", 2)
s6 = Guarda("20COmer", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()

