import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from busca import carregar_grafo, executar_busca
import busca_largura
import busca_gulosa
import busca_profundidade
import busca_a

def open_busca(algoritmo, grafo, inicio, objetivo):
    def open_busca_internal():
        resultado = executar_busca(grafo, algoritmo, inicio, objetivo)
        if resultado:
            tk.messagebox.showinfo("Resultado", "Caminho encontrado!")
        else:
            tk.messagebox.showinfo("Resultado", "Caminho não encontrado.")
    return open_busca_internal


root = tk.Tk()
root.title("Menu de Algoritmos de Busca")
root.geometry("800x600")
root.resizable(0, 0)

# Ajuste o caminho para a imagem de fundo
background_path = os.path.join("images", "background.jpg")

bg_image = Image.open(background_path)
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

button_largura = tk.Button(canvas, text="Busca em Largura", command=open_busca(busca_largura.busca_largura, grafo, inicio, objetivo))
button_largura.place(relx=0.1, rely=0.5)

button_profundidade = tk.Button(canvas, text="Busca em Profundidade", command=open_busca(busca_profundidade.busca_profundidade, grafo, inicio, objetivo))
button_profundidade.place(relx=0.3, rely=0.5)

button_gulosa = tk.Button(canvas, text="Busca Gulosa", command=open_busca(busca_gulosa.busca_gulosa, grafo, inicio, objetivo))
button_gulosa.place(relx=0.55, rely=0.5)

button_a_estrela = tk.Button(canvas, text="Busca A*", command=open_busca(busca_a.busca_a_estrela, grafo, inicio, objetivo))
button_a_estrela.place(relx=0.74, rely=0.5)

root.mainloop()
