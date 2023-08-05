class Cliente:
    def __init__(self, nome, email, plano='basic'):#método construtor
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'premium']#característica do cliente(como se fosse do esclopo global)
        lista_planos = ['basic', 'premium']#variável local dessa função
        if plano in lista_planos:
            self.plano = plano
        else:
            print('Plano inválido')
    def __str__(self):
        return "Nome: %s\nEmail: %s\nPlano: %s" % (self.nome, self.email, self.plano)

#métodos
    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            raise Exception("Plano inválido ")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme or self.plano == 'premium':
            print(f"Vendo Filme: {filme}")
        elif self.plano == 'basic' and plano_filme == 'premium':
            print("Faça upgrade para filme ")
        else:
            print("Plano inválido!")



cliente = Cliente("Daniel", "daniel@gmail.com")
'''print(cliente.plano)
cliente.mudar_plano("premium")
print(cliente.plano)
cliente.plano = "basic"
cliente.ver_filme("Velozes e Fuiosos 9", 'premium')
 
cliente.ver_filme("Velozes e Fuiosos 9", 'premium')'''
print(cliente)








