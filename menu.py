import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def open_busca_largura():
    import busca_largura
    resultado = busca_largura.main()

    tk.messagebox.showinfo("Tela da Busca em Largura", "Você está na tela da Busca em Largura")

    if resultado:
        tk.messagebox.showinfo("Resultado", "Caminho encontrado!")
    else:
        tk.messagebox.showinfo("Resultado", "Caminho não encontrado")

def open_busca_profundidade():
    import busca_profundidade
    resultado = busca_profundidade.main()

    tk.messagebox.showinfo("Tela da Busca em Profundidade", "Você está na tela da Busca em Profundidade")

    if resultado:
        tk.messagebox.showinfo("Resultado", "Caminho encontrado!")
    else:
        tk.messagebox.showinfo("Resultado", "Caminho não encontrado")

def open_busca_gulosa():
    import busca_gulosa
    resultado = busca_gulosa.main()

    tk.messagebox.showinfo("Tela da Busca Gulosa", "Você está na tela da Busca Gulosa")

    if resultado:
        tk.messagebox.showinfo("Resultado", "Caminho encontrado!")
    else:
        tk.messagebox.showinfo("Resultado", "Caminho não encontrado")

def open_busca_a_estrela():
    import busca_a
    resultado = busca_a.main()

    tk.messagebox.showinfo("Tela da Busca A*", "Você está na tela da Busca A*")

    if resultado:
        tk.messagebox.showinfo("Resultado", "Caminho encontrado!")
    else:
        tk.messagebox.showinfo("Resultado", "Caminho não encontrado")

root = tk.Tk()
root.title("Menu de Algoritmos de Busca")
root.geometry("800x600")
root.resizable(0, 0)

background_path = os.path.join("images", "background.jpg")

bg_image = Image.open(background_path)
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

button_largura = tk.Button(canvas, text="Busca em Largura", command=open_busca_largura)
button_largura.place(relx=0.1, rely=0.5)

button_profundidade = tk.Button(canvas, text="Busca em Profundidade", command=open_busca_profundidade)
button_profundidade.place(relx=0.3, rely=0.5)

button_gulosa = tk.Button(canvas, text="Busca Gulosa", command=open_busca_gulosa)
button_gulosa.place(relx=0.55, rely=0.5)

button_a_estrela = tk.Button(canvas, text="Busca A*", command=open_busca_a_estrela)
button_a_estrela.place(relx=0.74, rely=0.5)

root.mainloop()
