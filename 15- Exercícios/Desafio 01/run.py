from elevador import Elevador
elevador = Elevador()

while True:
    andar = input("Defina um andar: ")
    if andar.isnumeric():
        andar = int(andar)
        elevador.locomover(andar)
        print()
    else:
        print("Pfv, coloque um valor numérico <3 ")
