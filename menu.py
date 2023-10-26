import tkinter as tk
from tkinter import messagebox, Entry
from PIL import Image, ImageTk
import os
import subprocess


def open_busca_largura():
    inicio_x = entrada_inicio.get()
    inicio_y = entrada_inicio2.get()
    objetivo_x = entrada_objetivo.get()
    objetivo_y = entrada_objetivo2.get()

    subprocess.run(["python", "busca_largura.py", inicio_x, inicio_y, objetivo_x, objetivo_y])

    tk.messagebox.showinfo("Tela da Busca em Largura", "Você saiu da tela da Busca em Largura")

def open_busca_profundidade():

    inicio_x = entrada_inicio.get()
    inicio_y = entrada_inicio2.get()
    objetivo_x = entrada_objetivo.get()
    objetivo_y = entrada_objetivo2.get()

    subprocess.run(["python", "busca_profundidade.py", inicio_x, inicio_y, objetivo_x, objetivo_y])

    tk.messagebox.showinfo("Busca em Profundidade", "Você saiu da tela da Busca em Profundidade")

def open_busca_gulosa():
    inicio_x = entrada_inicio.get()
    inicio_y = entrada_inicio2.get()
    objetivo_x = entrada_objetivo.get()
    objetivo_y = entrada_objetivo2.get()

    subprocess.run(["python", "busca_gulosa.py", inicio_x, inicio_y, objetivo_x, objetivo_y])

    tk.messagebox.showinfo("Busca Gulosa", "Você saiu da tela da Busca Gulosa")

def open_busca_a_estrela():
    inicio_x = entrada_inicio.get()
    inicio_y = entrada_inicio2.get()
    objetivo_x = entrada_objetivo.get()
    objetivo_y = entrada_objetivo2.get()

    subprocess.run(["python", "busca_a.py", inicio_x, inicio_y, objetivo_x, objetivo_y])

    tk.messagebox.showinfo("Busca A*", "Você saiu da tela da Busca A*")

root = tk.Tk()
root.title("Menu de Algoritmos de Busca")
root.geometry("600x400")
root.resizable(0, 0)

background_path = os.path.join("images", "background.jpg")

bg_image = Image.open(background_path)
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

label_inicio = tk.Label(root, text="Digite o inicio")
label_inicio.place(relx=0.1, rely=0.14)
entrada_inicio = Entry(root)
entrada_inicio.place(relx=0.1, rely=0.2)
entrada_inicio2 = Entry(root)
entrada_inicio2.place(relx=0.35, rely=0.2)

label_objetivo = tk.Label(root, text="Digite o objetivo")
label_objetivo.place(relx=0.1, rely=0.34)
entrada_objetivo = Entry(root)
entrada_objetivo.place(relx=0.1, rely=0.4)
entrada_objetivo2 = Entry(root)
entrada_objetivo2.place(relx=0.35, rely=0.4)

button_largura = tk.Button(canvas, text="Busca em Largura", command=open_busca_largura)
button_largura.place(relx=0.1, rely=0.6)

button_profundidade = tk.Button(canvas, text="Busca em Profundidade", command=open_busca_profundidade)
button_profundidade.place(relx=0.3, rely=0.6)

button_gulosa = tk.Button(canvas, text="Busca Gulosa", command=open_busca_gulosa)
button_gulosa.place(relx=0.57, rely=0.6)

button_a_estrela = tk.Button(canvas, text="Busca A*", command=open_busca_a_estrela)
button_a_estrela.place(relx=0.74, rely=0.6)

root.mainloop()
