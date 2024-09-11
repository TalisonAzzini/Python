import random

escolhaComp: int
escolhaComp = random.randint(1, 100)

tentativas = int(input("Escolha a quantidade de tentativas: "))
print("\nEscolha um numero de 1 a 100.\nVoce tem", tentativas, "chances de acertar!\nBoa sorte!\n")

while tentativas!=0:
    escolha = int(input("Numero escolhido: "))

    if escolha<=0 or escolha>100:
        print("Numero fora do intervalo!")
    else:
        if escolha!=escolhaComp:
            tentativas = tentativas-1
            if escolha>escolhaComp:
                print("Tente um numero menor!")
            else:
                print("Tente um numero maior!")

            print("Tentativas restantes:", tentativas, "\n")
            if tentativas==0:
                print("GAME OVER!")

        else:
            print("Voce acertou!\nParabens.")
            tentativas=0
