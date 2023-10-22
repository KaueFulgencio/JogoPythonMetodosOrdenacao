import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def open_busca_largura():
    root.destroy()
    import busca
    busca.busca_largura()

def open_busca_profundidade():
    root.destroy()
    import busca
    busca.busca_profundidade()

def open_busca_gulosa():
    root.destroy() #fecha o menu principal
    import busca
    busca.busca_gulosa()

def open_busca_a_estrela():
    root.destroy()
    import busca
    busca.busca_a_estrela()

# Configuração da janela
root = tk.Tk()
root.title("Menu de Algoritmos de Busca")
root.geometry("800x600")
root.resizable(0, 0)

# Carrega a imagem de fundo
bg_image = Image.open("images/background.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# Botões
button_largura = tk.Button(canvas, text="Busca em Largura", command=open_busca_largura)
button_largura.place(relx=0.1, rely=0.5)

button_profundidade = tk.Button(canvas, text="Busca em Profundidade", command=open_busca_profundidade)
button_profundidade.place(relx=0.3, rely=0.5)

button_gulosa = tk.Button(canvas, text="Busca Gulosa", command=open_busca_gulosa)
button_gulosa.place(relx=0.55, rely=0.5)

button_a_estrela = tk.Button(canvas, text="Busca A*", command=open_busca_a_estrela)
button_a_estrela.place(relx=0.74, rely=0.5)

# Iniciar a janela
root.mainloop()
