import tkinter as tk

root = tk.Tk()

# Crear una etiqueta
etiqueta = tk.Label(root, text="resheno")
etiqueta.pack()

# Forzar la actualización de la ventana para que calcule el tamaño
root.update_idletasks()

# Obtener el ancho y alto de la ventana
hancho = root.winfo_width()
halto = root.winfo_height()

# Calcular las coordenadas para centrar la ventana
pos_x = (root.winfo_screenwidth() // 2) - (hancho // 2)
pos_y = (root.winfo_screenheight() // 2) - (halto // 2)

# Ajustar el tamaño y la posición de la ventana
root.geometry(f"{hancho}x{halto}+{pos_x}+{pos_y}")

# Iniciar el bucle principal
root.mainloop()
