'''
Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a m ´ edia do aluno. ´
(a) Permita ao usuario entrar com os dados de 5 alunos. ´
(b) Encontre o aluno com maior media geral. ´
(c) Encontre o aluno com menor media geral ´
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovação.
'''

class Aluno:

    def __init__(self, nome, curso, n1, n2, n3):
        self.nome = nome
        self.curso = curso
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
    def media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media
    def get_Name(self):
        return self.nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nomedefinido):
        self._nome = nomedefinido.strip().upper()
        return

#A)
alunos = list()
for i in range(2):
    nome = str(input(f"Digite o nome do aluno {i + 1}: "))
    curso = str(input(f"Digite o curso do aluno {i + 1}: "))
    n1 = float(input("Digite a nota 01: "))
    n2 = float(input("Digite a nota 02: "))
    n3 = float(input("Digite a nota 03: "))
    aluno = Aluno(nome, curso, n1, n2, n3)
    alunos.append(aluno)

#B) e C)
maior = 0
menor = 0
for i in range(0, len(alunos)):
    if i == 0:
       maior = alunos[i].media()
       menor = maior
    elif alunos[i].media() > maior:
        maior = alunos[i].media()
    elif alunos[i].media() < menor:
        menor = alunos[i].media()
#outra forma
maior_media = max(alunos, key = lambda aluno: aluno.media())
menor_media = min(alunos, key = lambda aluno: aluno.media())

aprovados = list()
reprovados = list()

#D)
for aluno in alunos:
    if aluno.media() >= 6:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

#Imprimindo os dados
print("-------------Maior Média-------------")
print(f"Nome: {maior_media.get_Name()}")
print(f"Média: {maior}")
print("-------------Menor Média-------------")
print(f"Nome: {menor_media.get_Name()}")
print(f"Média: {menor}")
print("------Reprovados e Aprovados---------")
print("REPROVADOS:")
for i in reprovados:
    print(f"    *{i.nome}")
print("APROVADOS:")
for k in aprovados:
    print(f"    *{k.get_Name()}")










