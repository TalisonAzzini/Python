def soma():
    print("----- SOMA -----")
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o primeiro numero: "))
    soma = (num1+num2)
    print("A soma entre os numeros e:", soma)
    print("")
    return soma

def subtracao():
    print("----- SUBTRACAO -----")
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o primeiro numero: "))
    sub = (num1-num2)
    print("A subtracao entre os numeros e:", sub)
    print("")
    return sub

def divisao():
    print("----- DIVISAO -----")
    num1 = int(input("Digite o dividendo: "))
    num2 = int(input("Digite o divisor: "))
    divisao = (num1/num2)
    print("A divisao entre os numeros e:", divisao)
    print("")
    return divisao

def multiplicacao():
    print("----- MULTIPLICACAO -----")
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    mult = (num1*num2)
    print("A multiplicacao entre os numeros e:", mult)
    print("")
    return mult

while True:
    print("----- MENU -----")
    print("1 - Soma\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n0 - Sair")
    op = int(input("Opcao:"))
    print("")

    if op==1:
        soma()
    elif op==2:
        subtracao()
    elif op==3:
        multiplicacao()
    elif op==4:
        divisao()
    elif op==0:
        break
    else:
        print("Opcao invalido!")
