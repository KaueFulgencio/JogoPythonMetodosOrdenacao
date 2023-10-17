import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Funções para os algoritmos de busca
def busca_largura():
    messagebox.showinfo("Busca em Largura", "Você selecionou Busca em Largura")

def busca_profundidade():
    messagebox.showinfo("Busca em Profundidade", "Você selecionou Busca em Profundidade")

def busca_gulosa():
    messagebox.showinfo("Busca Gulosa", "Você selecionou Busca Gulosa")

def busca_a_estrela():
    messagebox.showinfo("Busca A*", "Você selecionou Busca A*")

# Configuração da janela
root = tk.Tk()
root.title("Menu de Algoritmos de Busca")
root.geometry("800x600")  

# Desativa o redimensionamento da janela
root.resizable(0, 0) 

# BACKGROUND
bg_image = Image.open("images/background.jpg")  
bg_image = bg_image.resize((800, 600))  
bg_photo = ImageTk.PhotoImage(bg_image)

# Cria um canvas para exibir a imagem de fundo
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Exibe a imagem de fundo no canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# BOTÕES
button_largura = tk.Button(canvas, text="Busca em Largura", command=busca_largura)
button_largura.place(relx=0.1, rely=0.5)  

button_profundidade = tk.Button(canvas, text="Busca em Profundidade", command=busca_profundidade)
button_profundidade.place(relx=0.3, rely=0.5)

button_gulosa = tk.Button(canvas, text="Busca Gulosa", command=busca_gulosa)
button_gulosa.place(relx=0.55, rely=0.5)

button_a_estrela = tk.Button(canvas, text="Busca A*", command=busca_a_estrela)
button_a_estrela.place(relx=0.74, rely=0.5)

# Iniciar a janela
root.mainloop()
