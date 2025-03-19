while True:
    with open("aula1.txt", "r") as f:
        conteudo = f.read()
    
    linha = str(input(f"Linha: "))

    with open("aula1.txt", "w") as f:
        f.write(conteudo+linha+"\n")

    op = input("Deseja parar (S/N)? ")
    if op=="S" or op=="s":
        break
