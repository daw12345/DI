import tkinter as tk
from tkinter import messagebox


def agregar_usuario():
    nombre = entrada_nombre.get()
    edad = barra_edad.get()
    genero = genero_var.get()

    if not nombre:
        messagebox.showwarning("Advertencia", "Debe ingresar un nombre.")
        return

    if genero == "None" or genero == "":
        messagebox.showwarning("Advertencia", "Debe seleccionar un género.")
        return

    lista_usuarios.insert(tk.END, f"{nombre} - {edad} años - {genero}")
    limpiar_formulario()


def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        lista_usuarios.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Debe seleccionar un usuario para eliminar.")


def limpiar_formulario():
    entrada_nombre.delete(0, tk.END)
    barra_edad.set(0)
    genero_var.set(None) 


def salir():
    root.quit()


def guardar():
    messagebox.showinfo("Guardar Lista", "La lista ha sido guardada correctamente.")


def cargar():
    messagebox.showinfo("Cargar Lista", "La lista ha sido cargada correctamente.")



root = tk.Tk()
root.geometry("500x500")
root.title("Registro de Usuarios")


menubar = tk.Menu(root)
root.config(menu=menubar)

archivo_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Guardar Lista", command=guardar)
archivo_menu.add_command(label="Cargar Lista", command=cargar)


tk.Label(root, text="Nombre:").pack(pady=5)
entrada_nombre = tk.Entry(root)
entrada_nombre.pack(pady=5)


tk.Label(root, text="Edad:").pack(pady=5)
barra_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
barra_edad.pack(pady=5)


tk.Label(root, text="Género:").pack(pady=5)
genero_var = tk.StringVar()
genero_var.set(None)

frame_genero = tk.Frame(root)
frame_genero.pack(pady=5)

tk.Radiobutton(frame_genero, text="Masculino", variable=genero_var, value="Masculino").pack(side="left")
tk.Radiobutton(frame_genero, text="Femenino", variable=genero_var, value="Femenino").pack(side="left")
tk.Radiobutton(frame_genero, text="Otro", variable=genero_var, value="Otro").pack(side="left")


btn_agregar = tk.Button(root, text="Añadir Usuario", command=agregar_usuario)
btn_agregar.pack(pady=10)


frame_lista = tk.Frame(root)
frame_lista.pack(pady=10, expand=True, fill="both")

scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
lista_usuarios = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, height=10)
lista_usuarios.pack(side="left", fill="both", expand=True)

scrollbar.config(command=lista_usuarios.yview)
scrollbar.pack(side="right", fill="y")


btn_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario)
btn_eliminar.pack(pady=10)


btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.pack(pady=10)


root.mainloop()
