import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("abrir", "abierto")


def salir():
    root.destroy()


def info():
    messagebox.showinfo("info", "info sin importancia")


root = tk.Tk()
root.geometry("300x300")

menuMain = tk.Menu(root)
root.config(menu=menuMain)

menuArchivo = tk.Menu(menuMain, tearoff=0)
menuMain.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.add_command(label="Abrir", command=abrir)
menuArchivo.add_command(label="Salir", command=salir)


menuAyuda = tk.Menu(menuMain, tearoff=0)
menuMain.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=info)


root.mainloop()