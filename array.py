nomes = []
nota1 = []
nota2 = []
medias = []

while True:
    print("----- REGISTRO -----")
    nome = input("Digite o nome do aluno: ")
    num1 = int(input("Digite a primeira nota: "))
    num2 = int(input("Digite a segunda nota: "))
    media = float((num1+num2)/2)

    nomes.append(nome)
    nota1.append(num1)
    nota2.append(num2)
    medias.append(media)

    op = int(input("\nDeseja continuar?\n1 - Sim\n0 - Nao\nOpcao: "))
    print("")
    if op==1:
        continue
    elif op==0:
        break
    else:
        print("Opcao invalida, o programa continuara rodando.\n")

for x in range(len(nomes)):
    print("----- ALUNO -----")
    print(f"Nome: {nomes[x]}")
    print(f"Nota 1: {nota1[x]}")
    print(f"Nota 2: {nota2[x]}")
    print(f"Media: {medias[x]}")
    print("")
