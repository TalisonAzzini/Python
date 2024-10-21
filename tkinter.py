import tkinter as tk

# Função para somar os dois números
def somar():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        resultado = n1 + n2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

# Função para subtrair os dois números
def subtrair():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        resultado = n1 - n2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

# Função para multiplicar os dois números
def multiplicar():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        resultado = n1 * n2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

# Função para dividir os dois números
def dividir():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        resultado = n1 / n2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de dois números")

# Criação dos widgets
label_n1 = tk.Label(janela, text="Digite o primeiro número:")
label_n1.pack()

# Cria o primeiro label
entry_n1 = tk.Entry(janela)
entry_n1.pack()

# Cria o segundo label
label_n2 = tk.Label(janela, text="Digite o segundo número:")
label_n2.pack()

entry_n2 = tk.Entry(janela)
entry_n2.pack()

# Botoes
botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.pack()

botao_subtrair = tk.Button(janela, text="Subtrair", command=subtrair)
botao_subtrair.pack()

botao_mult = tk.Button(janela, text="Multiplicar", command=multiplicar)
botao_mult.pack()

botao_sub = tk.Button(janela, text="Dividir", command=dividir)
botao_sub.pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

# Executa a janela
janela.mainloop()
