import tkinter as tk

def show():

    tag = tk.Label(root, text=f"Seleccionaste: {', '.join([list.get(i) for i in list.curselection()])}")
    tag.pack()

root = tk.Tk()
root.geometry("300x300")

list = tk.Listbox(root, selectmode=tk.MULTIPLE)

# Añadir elementos a la lista
list.insert(tk.END, "Peras")
list.insert(tk.END, "Melones")
list.insert(tk.END, "Cocos")

list.pack()

button = tk.Button(root, text="Seleccionar", command=show)
button.pack()

root.mainloop()
