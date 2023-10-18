import tkinter as tk
from tkinter import messagebox

import busca_largura
import busca_profundidade
import busca_gulosa
import busca_a

def executar_busca_largura():
    grafo = busca_largura.carregar_grafo()
    inicio = (0, 0)  
    objetivo = (2, 3)  # Defina o objetivo aqui
    busca_largura.busca_largura(grafo, inicio, objetivo)
    
def executar_busca_profundidade():
    grafo = busca_profundidade.carregar_grafo()
    inicio = (0, 0)  # Defina o ponto de partida aqui
    objetivo = (3, 5)  # Defina o objetivo aqui
    busca_profundidade.busca_profundidade(grafo, inicio, objetivo)
    
def executar_busca_gulosa():
    grafo = busca_gulosa.carregar_grafo()
    inicio = (0, 0)  # Defina o ponto de partida aqui
    objetivo = (4, 5)  # Defina o objetivo aqui
    busca_gulosa.busca_gulosa(grafo, inicio, objetivo)
    
def executar_busca_a_estrela():
    grafo = busca_a.carregar_grafo()
    inicio = (0, 0)  # Defina o ponto de partida aqui
    objetivo = (1, 3)  # Defina o objetivo aqui
    busca_a.busca_a_estrela(grafo, inicio, objetivo)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Algoritmo de Busca")
    root.geometry("400x300")

    button_back = tk.Button(root, text="Busca em Largura", command=executar_busca_largura)
    button_back.pack()

    button_back = tk.Button(root, text="Busca em Profundidade", command=executar_busca_profundidade)
    button_back.pack()

    button_back = tk.Button(root, text="Busca Gulosa", command=executar_busca_gulosa)
    button_back.pack()

    button_back = tk.Button(root, text="Busca A*", command=executar_busca_a_estrela)
    button_back.pack()

    root.mainloop()
