def media():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    media = float((num1+num2)/2)
    return media

nomes = []
notas = []
while True:
    print("----- REGISTRO -----")
    nomes.append(input("Digite o nome do aluno: "))
    notas.append(media())

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
        print("Nome:"+nomes[x])
        print("Nota:",notas[x])
        print("")
