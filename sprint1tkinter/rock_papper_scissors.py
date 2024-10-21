import tkinter as tk
from tkinter import messagebox
import random

# Función que determina el resultado de la jugada
def determinar_resultado(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate", None
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or \
         (jugador1 == "Papel" and jugador2 == "Piedra") or \
         (jugador1 == "Tijera" and jugador2 == "Papel"):
        return "Gana el jugador 1", "Jugador 1"
    else:
        return "Gana el jugador 2", "Jugador 2"

# Función para mostrar los resultados de cada partida
def mostrar_resultado(jugador1, jugador2, resultado, mensaje):
    mensaje_resultado.set(f"El jugador 1 sacó {jugador1}, el jugador 2 sacó {jugador2}. {resultado}. {mensaje}")

# Función para actualizar los puntos
def actualizar_puntos():
    global puntos_jugador1, puntos_jugador2
    if jugador_ganador == "Jugador 1":
        puntos_jugador1 += 1
    elif jugador_ganador == "Jugador 2":
        puntos_jugador2 += 1

    puntos_jugador1_var.set(f"Puntos Jugador 1: {puntos_jugador1}")
    puntos_jugador2_var.set(f"Puntos Jugador 2: {puntos_jugador2}")

    # Verificar si alguien ganó la partida
    if puntos_jugador1 == 3:
        messagebox.showinfo("Fin del Juego", "El jugador 1 ha ganado la partida!")
        reiniciar_partida()
    elif puntos_jugador2 == 3:
        messagebox.showinfo("Fin del Juego", "El jugador 2 ha ganado la partida!")
        reiniciar_partida()

# Función para reiniciar la partida
def reiniciar_partida():
    global puntos_jugador1, puntos_jugador2
    puntos_jugador1, puntos_jugador2 = 0, 0
    puntos_jugador1_var.set(f"Puntos Jugador 1: {puntos_jugador1}")
    puntos_jugador2_var.set(f"Puntos Jugador 2: {puntos_jugador2}")
    mensaje_resultado.set("")
    jugador1_opcion.set("")
    jugador2_opcion.set("")
    reiniciar_jugada()

# Función para manejar la elección de un jugador en un juego de 1 vs máquina
def jugar_1vs1(opcion):
    opciones = ["Piedra", "Papel", "Tijera"]
    jugador1 = opcion
    jugador2 = random.choice(opciones)
    resultado, ganador = determinar_resultado(jugador1, jugador2)
    mensaje = f"{jugador2} gana a {jugador1}" if ganador else ""
    mostrar_resultado(jugador1, jugador2, resultado, mensaje)
    global jugador_ganador
    jugador_ganador = ganador
    actualizar_puntos()

# Función para manejar la elección de dos jugadores
def jugar_2vs2():
    jugador1 = jugador1_opcion.get()
    jugador2 = jugador2_opcion.get()
    
    if jugador1 and jugador2:
        resultado, ganador = determinar_resultado(jugador1, jugador2)
        mensaje = f"{jugador2} gana a {jugador1}" if ganador else ""
        mostrar_resultado(jugador1, jugador2, resultado, mensaje)
        global jugador_ganador
        jugador_ganador = ganador
        actualizar_puntos()
        reiniciar_jugada()

# Función para reiniciar la selección de jugadas
def reiniciar_jugada():
    jugador1_opcion.set("")
    jugador2_opcion.set("")

# Función para manejar la selección de la jugada del jugador 1 en el modo 2vs2
def seleccionar_jugada_2vs2_jugador1(opcion):
    jugador1_opcion.set(opcion)
    if jugador2_opcion.get():  # Si el jugador 2 ya eligió, jugamos
        jugar_2vs2()

# Función para manejar la selección de la jugada del jugador 2 en el modo 2vs2
def seleccionar_jugada_2vs2_jugador2(opcion):
    jugador2_opcion.set(opcion)
    if jugador1_opcion.get():  # Si el jugador 1 ya eligió, jugamos
        jugar_2vs2()

# Función para iniciar el juego 1vs1
def iniciar_1vs1():
    global modo_juego
    modo_juego = '1vs1'
    ventana_seleccion_jugada = tk.Toplevel(ventana_principal)
    ventana_seleccion_jugada.title("Selección Jugada (1 Jugador)")

    # Botones para las opciones
    tk.Button(ventana_seleccion_jugada, text="Piedra", command=lambda: seleccionar_jugada_1vs1("Piedra")).pack(pady=10)
    tk.Button(ventana_seleccion_jugada, text="Papel", command=lambda: seleccionar_jugada_1vs1("Papel")).pack(pady=10)
    tk.Button(ventana_seleccion_jugada, text="Tijera", command=lambda: seleccionar_jugada_1vs1("Tijera")).pack(pady=10)

    # Mover la ventana a una posición aleatoria y hacer que se mueva linealmente
    mover_ventana_random(ventana_seleccion_jugada, modo="1vs1")
    mover_ventana_lineal(ventana_seleccion_jugada)

# Función para iniciar el juego 2vs2
def iniciar_2vs2():
    global modo_juego
    modo_juego = '2vs2'
    ventana_seleccion_jugada = tk.Toplevel(ventana_principal)
    ventana_seleccion_jugada.title("Selección Jugada (2 Jugadores)")

    # Jugador 1
    tk.Button(ventana_seleccion_jugada, text="Piedra", command=lambda: seleccionar_jugada_2vs2_jugador1("Piedra")).pack(pady=10)
    tk.Button(ventana_seleccion_jugada, text="Papel", command=lambda: seleccionar_jugada_2vs2_jugador1("Papel")).pack(pady=10)
    tk.Button(ventana_seleccion_jugada, text="Tijera", command=lambda: seleccionar_jugada_2vs2_jugador1("Tijera")).pack(pady=10)

    # Jugador 2
    tk.Button(ventana_seleccion_jugada, text="Piedra", command=lambda: seleccionar_jugada_2vs2_jugador2("Piedra")).pack(pady=10)
    tk.Button(ventana_seleccion_jugada, text="Papel", command=lambda: seleccionar_jugada_2vs2_jugador2("Papel")).pack(pady=10)
    tk.Button(ventana_seleccion_jugada, text="Tijera", command=lambda: seleccionar_jugada_2vs2_jugador2("Tijera")).pack(pady=10)

    # Mover la ventana a una posición aleatoria y hacer que se mueva linealmente
    mover_ventana_random(ventana_seleccion_jugada, modo="2vs2")
    mover_ventana_lineal(ventana_seleccion_jugada)

# Función para manejar la jugada en 1 jugador
def seleccionar_jugada_1vs1(opcion):
    jugar_1vs1(opcion)

# Función que maneja el menú de selección de juego
def crear_menu():
    tk.messagebox.showinfo(title="WARNING", message="WARNING: SPEED UP")
    menu_principal = tk.Menu(ventana_principal)
    ventana_principal.config(menu=menu_principal)

    # Menú "Juego"
    menu_juego = tk.Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Juego", menu=menu_juego)
    
    # Opciones en el menú "Juego"
    menu_juego.add_command(label="1 Jugador (vs Máquina)", command=iniciar_1vs1)
    menu_juego.add_command(label="2 Jugadores", command=iniciar_2vs2)
    menu_juego.add_separator()
    menu_juego.add_command(label="Salir", command=ventana_principal.quit)

# Función para mover la ventana a una posición aleatoria
def mover_ventana_random(ventana, modo):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()

    # Ajustar dimensiones de la ventana según el modo
    if modo == "1vs1":
        ventana_width = 200
        ventana_height = 200
    else:  # "2vs2"
        ventana_width = 300
        ventana_height = 300

    # Posicionar ventana de forma aleatoria en la pantalla
    random_x = random.randint(0, screen_width - ventana_width)
    random_y = random.randint(0, screen_height - ventana_height)

    ventana.geometry(f"{ventana_width}x{ventana_height}+{random_x}+{random_y}")

# Función para mover la ventana linealmente
def mover_ventana_lineal(ventana):
    def mover():
        # Obtener la posición actual de la ventana
        x = ventana.winfo_x()
        y = ventana.winfo_y()

        # Mover la ventana de manera aleatoria en diferentes direcciones
        direction = random.choice(['right', 'down', 'left', 'up'])

        if direction == 'right' and x + 10 + ventana.winfo_width() < ventana.winfo_screenwidth():
            ventana.geometry(f"+{x + 20}+{y}")
        elif direction == 'down' and y + 10 + ventana.winfo_height() < ventana.winfo_screenheight():
            ventana.geometry(f"+{x}+{y + 20}")
        elif direction == 'left' and x - 10 >= 0:
            ventana.geometry(f"+{x - 20}+{y}")
        elif direction == 'up' and y - 10 >= 0:
            ventana.geometry(f"+{x}+{y - 20}")

        # Mover la ventana cada 100 ms (hacerlo más rápido)
        ventana.after(100, mover)

    mover()

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Juego Piedra, Papel, Tijera HARDCORE!!!!!!!!!!!!")

# Crear el menú
crear_menu()

# Variables para los puntos
puntos_jugador1 = 0
puntos_jugador2 = 0
jugador_ganador = None

# Variables para almacenar las opciones de los jugadores
jugador1_opcion = tk.StringVar()
jugador2_opcion = tk.StringVar()

# Crear etiquetas para mostrar puntos
puntos_jugador1_var = tk.StringVar(value=f"Puntos Jugador 1: {puntos_jugador1}")
puntos_jugador2_var = tk.StringVar(value=f"Puntos Jugador 2: {puntos_jugador2}")
tk.Label(ventana_principal, textvariable=puntos_jugador1_var).pack()
tk.Label(ventana_principal, textvariable=puntos_jugador2_var).pack()

# Crear la etiqueta para mostrar el resultado
mensaje_resultado = tk.StringVar(value="")
tk.Label(ventana_principal, textvariable=mensaje_resultado).pack()

# Iniciar la aplicación
ventana_principal.mainloop()
