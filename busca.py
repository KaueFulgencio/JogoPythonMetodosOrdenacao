import tkinter as tk
from tkinter import messagebox
import busca_largura

def busca_largura():
    #messagebox.showinfo("Busca em Largura", "Você selecionou Busca em Largura")
    busca_largura.busca_largura(grafo, inicio, objetivo)
    
def busca_profundidade():
    messagebox.showinfo("Busca em Profundidade", "Você selecionou Busca em Profundidade")

def busca_gulosa():
    messagebox.showinfo("Busca Gulosa", "Você selecionou Busca Gulosa")

def busca_a_estrela():
    messagebox.showinfo("Busca A*", "Você selecionou Busca A*")

if __name__ == "__main__":
    # Script de busca é executado apenas quando executado diretamente
    root = tk.Tk()
    root.title("Algoritmo de Busca")
    root.geometry("400x300")

    button_back = tk.Button(root, text="Voltar para o Menu", command=root.destroy)
    button_back.pack()

    root.mainloop()
