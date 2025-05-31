# Criador Douglas Magalães de Vasconcelos

import tkinter as tk
from tkinter import messagebox
import requests


def pegar_cotacao():
    try:
        resposta = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        dados = resposta.json()
        cotacao = float(dados['USDBRL']['bid'])
        return cotacao
    except:
        messagebox.showerror("Erro", "Erro ao buscar a cotação. Verifique sua conexão.")
        return None
    


def converter():
    cotacao = pegar_cotacao()
    if cotacao is None:
        return
    
    try:
        valor = float(entrada_valor.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")
        return
    
    if opcao.get() == "real_dolar":
        resultado = valor / cotacao
        label_resultado.config(text=f"R${valor:.2f} = US${resultado:.2f}")
    elif opcao.get() == "dolar_real":
        resultado = valor * cotacao
        label_resultado.config(text=f"US${valor:.2f} = R${resultado:.2f}")
    else:
        messagebox.showerror("Erro", "Selecione uma opção.")
    

# Criando janela
janela = tk.Tk()
janela.title("Financial Vortex")
janela.geometry("400x300")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Conversor de Moeda", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Campo de entrada
entrada_valor = tk.Entry(janela, width=20, font=("Arial", 14))
entrada_valor.pack(pady=10)

# Opções
opcao = tk.StringVar()

radio1 = tk.Radiobutton(janela, text="Real para Dólar", variable=opcao, value="real_dolar", font=("Arial", 12))
radio1.pack()

radio2 = tk.Radiobutton(janela, text="Dólar para Real", variable=opcao, value="dolar_real", font=("Arial", 12))
radio2.pack()

# Botão de converter
botao_converter = tk.Button(janela, text="Converter", command=converter, font=("Arial", 12), bg="green", fg="white")
botao_converter.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

# Rodapé
rodape = tk.Label(janela, text="Cotação em tempo real via API", font=("Arial", 8))
rodape.pack(side="bottom", pady=5)

# Executa a janela
janela.mainloop()
