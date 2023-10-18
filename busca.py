import tkinter as tk
from tkinter import messagebox
import busca_largura
import busca_profundidade
import busca_gulosa
import busca_a

def executar_busca(algoritmo, inicio, objetivo):
    try:
        grafo = algoritmo.carregar_grafo()
        resultado = algoritmo.busca(grafo, inicio, objetivo)
        if resultado:
            messagebox.showinfo("Resultado", "Caminho encontrado!")
        else:
            messagebox.showinfo("Resultado", "Caminho não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def criar_janela():
    root = tk.Tk()
    root.title("Algoritmo de Busca")
    root.geometry("400x300")

    botao_busca("Busca em Largura", busca_largura, (0, 0), (2, 3))
    botao_busca("Busca em Profundidade", busca_profundidade, (1, 0), (1, 2))
    botao_busca("Busca Gulosa", busca_gulosa, (0, 0), (4, 5))
    botao_busca("Busca A*", busca_a, (0, 0), (1, 3))

    root.mainloop()

def botao_busca(texto, algoritmo, inicio, objetivo):
    button = tk.Button(root, text=texto, command=lambda algo=algoritmo, ini=inicio, obj=objetivo: executar_busca(algo, ini, obj))
    button.pack()

if __name__ == "__main__":
    root = None  # Declare a variável root no escopo global

    criar_janela()
