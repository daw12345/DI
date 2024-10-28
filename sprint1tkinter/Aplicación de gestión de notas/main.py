import tkinter as tk
from NotasModel import NotasModel
from VistaNotas import VistaNotas
from ControladorNotas import ControladorNotas

def main():
    w = tk.Tk()
    modelo = NotasModel("notas.txt")
    vista = VistaNotas(w)
    controlador = ControladorNotas(modelo, vista)
    w.mainloop()

if __name__ == "__main__":
    main()