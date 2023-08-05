class MinhaClasse:
    estatico = 'Lhama'


    def __init__(self, estado):
        self.estado = estado
    #   self.estatico = 'Lhama'
    # É mais interessante mexer em um atributo de classe no contexto do obj
    def print_estatico(self):
        print(self.estatico)

    def mudar_estatico(self):
        self.estatico = 'Programador'

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Programador'

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico() #A partir do obj1, foi acessado o contexto de classe, que foi mudada
#essa mudança repercutiu para todos os outros objetos

obj1.print_estatico()
obj2.print_estatico()

#Variáveis de Classes são variáveis estáticas
#Quando uma vairável de classe é declarada, então uma única cópia dessa variável
#é criada e compartilhada com os obj a nível de classe
'''
Quando altero os valores dessa variável de classe, altero tbm o contexto de classe geral, que, por sua vez, tbm altera o contexto do obj 

'''