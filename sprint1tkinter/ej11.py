import tkinter as tk


def actualizar_valor(valor):
    tag.config(text=f"Valor seleccionado: {valor}")


root = tk.Tk()
root.geometry("300x200")



barra_deslizante = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
barra_deslizante.pack(pady=20)


tag = tk.Label(root, text="Valor seleccionado: 0")
tag.pack(pady=10)


root.mainloop()
