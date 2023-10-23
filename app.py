import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MenuBuscaApp:
    def __init__(self, root, grafo, busca_functions):
        self.root = root
        self.root.title("Menu de Algoritmos de Busca")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)

        self.grafo = grafo

        bg_image = Image.open("images/background.jpg")
        bg_image = bg_image.resize((800, 600))
        bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

        self.busca_functions = busca_functions

    def open_busca(self, algoritmo):
        def open_busca_internal():
            inicio = (0, 0)
            objetivo = (4, 5)
            resultado = self.busca_functions[algoritmo](self.grafo, inicio, objetivo)
            if resultado:
                tk.messagebox.showinfo("Resultado", "Caminho encontrado!")
            else:
                tk.messagebox.showinfo("Resultado", "Caminho não encontrado.")

        return open_busca_internal

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        for algoritmo, label in self.busca_functions.items():
            button = tk.Button(buttons_frame, text=label, command=self.open_busca(algoritmo))
            button.pack(side=tk.LEFT, padx=10)

def main():
    root = tk.Tk()
    grafo = {}  

    busca_functions = {
        "busca_largura": "Busca em Largura",
        "busca_profundidade": "Busca em Profundidade",
        "busca_gulosa": "Busca Gulosa",
        "busca_a_estrela": "Busca A*",
    }

    app = MenuBuscaApp(root, grafo, busca_functions)
    app.create_buttons()

    root.mainloop()

if __name__ == "__main__":
    main()
