import tkinter as tk

class VistaNotas:
    def __init__(self, w):
        self.w = w

        self.titulo = tk.Label(w, text="Aplicación de gestión de notas")
        self.titulo.pack()

        self.coor = tk.Label(w, text="Coordenadas del click: x={}, y={}")
        self.coor.pack()

        self.listbox_notas = tk.Listbox(w, height=10, width=40)
        self.listbox_notas.pack(padx=10, pady=10)

        self.entry_nota = tk.Entry(w, width=40)
        self.entry_nota.pack()

        self.button1 = tk.Button(w, text="Guardar nota")
        self.button1.pack()

        self.button2 = tk.Button(w, text="Cargar nota")
        self.button2.pack()

        self.button3 = tk.Button(w, text="Eliminar nota")
        self.button3.pack()

        self.button4 = tk.Button(w, text="Descargar imagen")
        self.button4.pack()

        self.imagen = tk.Label(w, text="(Imagen)")
        self.imagen.pack(padx=20)
