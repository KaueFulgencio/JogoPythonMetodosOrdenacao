import tkinter as tk
from tkinter import messagebox

import busca_largura
import busca_profundidade
import busca_gulosa
import busca_a

def busca_largura():
    #messagebox.showinfo("Busca em Largura", "Você selecionou Busca em Largura")
    busca_largura.busca_largura(grafo, inicio, objetivo)
    
def busca_profundidade():
    messagebox.showinfo("Busca em Profundidade", "Você selecionou Busca em Profundidade")
    busca_profundidade.busca_profundidade(grafo, inicio, objetivo, visitados)

def busca_gulosa():
    messagebox.showinfo("Busca Gulosa", "Você selecionou Busca Gulosa")
    busca_gulosa.busca_gulosa(grafo, inicio, objetivo)

def busca_a_estrela():
    messagebox.showinfo("Busca A*", "Você selecionou Busca A*")
    busca_a.busca_a_estrela(grafo, inicio, objetivo)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Algoritmo de Busca")
    root.geometry("400x300")

    button_back = tk.Button(root, text="Voltar para o Menu", command=root.destroy)
    button_back.pack()

    root.mainloop()
