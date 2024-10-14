import tkinter as tk

def renderizar():
    # Limpiar el canvas antes de dibujar
    canvas.delete("all")
    
    # Obtener las coordenadas del rectángulo
    rect_coords = e1.get().replace(",", " ").split()
    rect_size = e3.get().replace(",", " ").split()  # Obtener el alto y ancho del rectángulo
    
    if len(rect_coords) == 2 and len(rect_size) == 2:  # Debe haber 2 coordenadas y 2 valores de tamaño
        try:
            # Convertir las coordenadas y dimensiones a enteros
            x1, y1 = map(int, rect_coords)
            height, width = map(int, rect_size)
            x2 = x1 + width  # Calcular la segunda coordenada X con el ancho
            y2 = y1 + height  # Calcular la segunda coordenada Y con el alto

            # Dibujar el rectángulo
            canvas.create_rectangle(x1, y1, x2, y2, outline="white", width=2)
        except ValueError:
            print("Las coordenadas y el tamaño del rectángulo deben ser números enteros.")
    else:
        print("Debes ingresar exactamente 2 coordenadas y 2 valores de tamaño para el rectángulo.")

    # Obtener las coordenadas del círculo (x, y) y el radio
    circle_coords = e2.get().replace(",", " ").split()
    radius_value = e4.get()  # Obtener el valor del radio desde e4

    if len(circle_coords) == 2 and radius_value.isdigit():  # Asegurar que haya 2 valores para (x, y) y un radio
        try:
            # Convertir las coordenadas del círculo y el radio a enteros
            cx, cy = map(int, circle_coords)
            radius = int(radius_value)

            # Dibujar el círculo (usando create_oval)
            canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="red", width=2)
        except ValueError:
            print("Las coordenadas del círculo deben ser números enteros.")
    else:
        print("Debes ingresar exactamente 2 coordenadas (x, y) y un valor entero para el radio.")

root = tk.Tk()
root.geometry("900x900")

# Etiqueta y campo de entrada para el rectángulo
rectangle = tk.Label(root, text="Coordenadas del rectángulo (x1, y1):")
rectangle.pack()

e1 = tk.Entry(root)
e1.pack()

rectangle2 = tk.Label(root, text="Alto y ancho del rectángulo (height, width):")
rectangle2.pack()

e3 = tk.Entry(root)
e3.pack()

# Etiqueta y campo de entrada para el círculo
circle = tk.Label(root, text="Centro del círculo (x, y):")
circle.pack()

e2 = tk.Entry(root)
e2.pack()

circle2 = tk.Label(root, text="Radio del círculo:")
circle2.pack()

e4 = tk.Entry(root)
e4.pack()

# Canvas donde se dibujarán las formas
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

# Botón para renderizar las formas
b = tk.Button(root, text="Renderizar", command=renderizar)
b.pack()

root.mainloop()
