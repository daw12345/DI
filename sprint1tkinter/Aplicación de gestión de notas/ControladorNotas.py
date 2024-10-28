import tkinter as tk
from tkinter import messagebox
import threading
import requests
from io import BytesIO
from PIL import Image, ImageTk 


class ControladorNotas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista


        # Asigna los métodos a los botones de la vista
        self.vista.button1.config(command=self.agregar_nota)  # Guardar nota
        self.vista.button3.config(command=self.eliminar_nota)  # Eliminar nota
        self.vista.button2.config(command=self.cargar_notas)   # Cargar notas
        self.vista.button4.config(command=lambda: self.descargar_imagen())  # Descargar imagen

        # Vincula el evento de clic en la ventana
        self.vista.w.bind("<Button-1>", self.actualizar_coordenadas)

    def actualizar_listbox(self):
        self.vista.listbox_notas.delete(0, tk.END)  # Limpia el Listbox
        notas = self.modelo.obtener_notas()  # Obtiene las notas del modelo

        for nota in notas:
            self.vista.listbox_notas.insert(tk.END, nota)  # Inserta cada nota en el Listbox

    def agregar_nota(self):
        nueva_nota = self.vista.entry_nota.get()
    
        # Guarda la nota, independientemente de si está vacía o no
        self.modelo.agregar_nota(nueva_nota)
        self.vista.entry_nota.delete(0, tk.END)  # Limpia el campo de entrada
        self.modelo.guardar_notas()  # Guarda las notas en el archivo
        self.actualizar_listbox()  # Actualiza la lista en la vista


    def eliminar_nota(self):
        indices_seleccionados = self.vista.listbox_notas.curselection()

        if indices_seleccionados:
            indices = sorted(map(int, indices_seleccionados), reverse=True)

            for indice in indices:
                self.modelo.eliminar_nota(indice)

            self.actualizar_listbox()  # Actualiza la vista después de eliminar las notas
        else:
            messagebox.showwarning("Advertencia", "Selecciona una nota para eliminar.")

    def guardar_notas(self):
        self.modelo.guardar_notas()
        messagebox.showinfo("Guardado", "Las notas se han guardado correctamente.")

    def cargar_notas(self):
        self.modelo.cargar_notas()  # Carga las notas desde el archivo
        if not self.modelo.obtener_notas():  # Verifica si hay notas cargadas
            messagebox.showinfo("Información", "No hay notas para cargar.")
        self.actualizar_listbox()    # Actualiza la lista en la vista para mostrar las notas cargadas

    def descargar_imagen(self):
        url = 'https://inaturalist-open-data.s3.amazonaws.com/photos/4608133/original.jpg'  # URL de la imagen
        hilo = threading.Thread(target=self.iniciar_imagen, args=(url,))
        
        #Cargando..
        self.vista.imagen.config(text="Cargando..")
        hilo.start()
        
    def iniciar_imagen(self, url):
        try:
            res = requests.get(url)
            res.raise_for_status()  # Lanza una excepción si la descarga falla
            imagen = Image.open(BytesIO(res.content))  # Carga la imagen
            imagen = imagen.resize((200, 200))  # Redimensiona la imagen
            imagen_tk = ImageTk.PhotoImage(imagen)  # Convierte a formato Tkinter

            # Actualiza la interfaz en el hilo principal
            self.vista.imagen.config(image=imagen_tk)
            self.vista.imagen.image = imagen_tk  # Mantiene una referencia
        except requests.exceptions.RequestException as e:
            # Muestra un mensaje de error en caso de fallar
            messagebox.showerror("Error", f"Error al descargar la imagen: {e}")
        
    def actualizar_coordenadas(self, event):
        x = event.x
        y = event.y
        self.vista.coor.config(text=f"Coordenadas del click: x=[{x}], y=[{y}]")
