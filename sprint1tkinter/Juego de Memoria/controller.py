
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
from PIL import Image, ImageTk
from datetime import datetime 

from model import GameModel
from view import GameView, MainMenu
from resources import descargar_imagen

class GameController:
    def __init__(self, root):
        self.root = root
        self.player_name = ""  # Nombre del jugador
        self.difficulty = ""   # Dificultad seleccionada
        self.game_model = None  # Modelo de juego
        self.game_view = None   # Vista de juego
        self.selected = []  # Para almacenar las cartas seleccionadas
        self.move_count = 0  # Contador de movimientos
        self.start_time = 0  # Inicializar el tiempo en segundos
        self.images_loaded = False  # Indicador para saber si las imágenes se cargaron
        self.image_urls = [
            "https://www.zoopinto.es/wp-content/uploads/2021/12/pajaro-mascota.jpg",
            "https://www.pestrapid.com/wp-content/uploads/2023/05/como-evitar-plagas-pajaros-aves-casa.jpg",
            "https://i.ytimg.com/vi/r7Sv2l9HguY/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDg_w5jVQeEB8yEimw1Uf3SPLB0ZA",
            "https://hips.hearstapps.com/hmg-prod/images/best-pet-birds-cockatiel-1572839067.jpg?crop=1.00xw:0.833xh;0,0.0611xh&resize=980:*",
            "https://www.latiendahome.com/cms/images/pajaro-durmiendo.jpg",
            "https://s.libertaddigital.com/2023/07/04/1920/1080/fit/blue-wire-patrick-dpa-pajaro-azul-cordon.jpg",
            "https://static.diariofemenino.com/media/97169/c/sonar-con-pajaros-de-colores-alcanzar-el-exito-lg.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaPdCWoCbK_PgrvVzHbT3T9VgXrK4WJXpfuA&s",
            "https://images.ecestaticos.com/DXaLRwKN5eASpM24NkXZ1me4ocg=/0x79:2149x1290/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2F883%2F67f%2F20d%2F88367f20de362b96d0e05f99c6a8b4c6.jpg",
            "https://grandesporques.com/wp-content/uploads/elementor/thumbs/pajaros-extranos-q501hwms3sm529pm2coxspv542y2fnujpukccyw43c.jpg",
            "https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/3953/production/_98457641_xx1920dsc_2777-hr_zgm9i3c.jpg.webp",
            "https://efeverde.com/wp-content/uploads/2022/01/mirlo-picos-polluelos-archivo-efeverde.jpg",
            "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkkSgCBHpl-wRscWwb1BHmooF-Y3EeGM5syUk7jKwWd9VorP2jRoWMM9Vplawkom4H6lGlhkZitHm4bbesS4tDoM1lFFH2Cuz-7McwT531QjevBNC4QZS4TleoviJWqlz1JTMsbkFqAG2A/s1600/810027492_o8G4J-M.jpg",
            "https://grandesporques.com/wp-content/uploads/elementor/thumbs/pajaros-que-hablan-q6y80amunkbecrdxbdybo7111uc921gug9ypplwv5k.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUDyoTv2MKk6r76g4O1sCXAgHKVC74JtZyvg&s",
            "https://images.ecestaticos.com/Oy4alrRif2D8Eu5Anibc3NDnrrk=/0x0:2121x1413/1200x900/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2F555%2Fbad%2Ffe9%2F555badfe997db7dda3094f3836021f98.jpg",
            "https://elasombrario.publico.es/wp-content/uploads/sites/1/2022/02/pajaros.jpeg",
            "https://www.limpiezascontrolair.es/wp-content/uploads/2019/02/El-Problema-De-Los-Nidos-De-Pajaros-En-Los-Conductos-De-Ventilacion-670x423.jpg",
            "https://jardinable.es/wp-content/uploads/2020/06/pajaros-jardin-jardinable-2-618x348.jpg",
            "https://cdn.pixabay.com/photo/2015/04/20/10/23/colorful-birds-730898_640.jpg",
            "https://cdnebasnet.com/data/cache/opt_jpg/eshop/rslpets/images/posts/52-1657869693-1400x1400.jpg",
            "https://www.barakaldotiendaveterinaria.es/blog/wp-content/uploads/2018/02/foto-pajaro-Ossi-Saarinen.jpg",
            "https://laderasur.com/wp-content/uploads/2024/01/carpintero-negro-macho-franco-villalobos-1-2400x1400.jpg",
            "https://www.clinicaveterinariazarpa.com/wp-content/uploads/2022/07/zarpa-blog.jpg",
            "https://www.sopitas.com/wp-content/uploads/2022/11/vuelo-ave-australia-alaska.jpg",
            "https://estaticos-cdn.prensaiberica.es/clip/219f267e-c6e5-4fd5-b5bf-6da6148c7f12_16-9-aspect-ratio_default_0.jpg",
            "https://www.petdarling.com/wp-content/uploads/2018/05/nombre-de-pajaros.jpg",
            "https://i.pinimg.com/236x/d4/3d/3b/d43d3bc4353a1eea39037d9572bc106c.jpg",
            "https://www.zooplus.es/magazine/wp-content/uploads/2021/10/Acaros-en-pajaros.jpeg",
            "https://i0.wp.com/puppis.blog/wp-content/uploads/2019/12/Cual-es-la-forma-correcta-de-alimentar-a-mi-pajaro.jpg?w=1200&ssl=1",
            "https://img.freepik.com/fotos-premium/monton-pajaros-coloridos-estan-estante-madera_1248597-1224.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBmEsU8Pfkwslvta-ua3iwaCcoc8rwqud3YX4652NZ2PKY2BrBkPUvjPncRrVqeuE6-QE&usqp=CAU",
            "https://images.pexels.com/photos/28926326/pexels-photo-28926326/free-photo-of-turaco-elegante-en-habitat-natural.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",

        ]
        self.images = []  # Lista donde almacenaremos las imágenes descargadas

        # Crear el menú principal
        self.main_menu = MainMenu(self.root, self.start_game_callback, self.show_stats_callback, self.quit_callback)

    def start_game_callback(self):
        """Iniciar el juego y seleccionar la dificultad."""
        # Limpiar el estado del juego anterior
        self.game_model = None
        self.game_view = None
        self.selected = []
        self.move_count = 0
        self.start_time = 0
        self.images_loaded = False
        self.images = []
    
        # Mostrar la selección de dificultad
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        """Seleccionar la dificultad y generar el tablero de juego."""
        difficulty = simpledialog.askstring("Selecciona la dificultad", 
                                            "Elige la dificultad: fácil, medio, difícil", 
                                            parent=self.root).lower()
        
        if difficulty is None:
            return  # Regresa al menú principal, no hace nada
        
        # Pedir el nombre del jugador, y si se cancela, volver al menú principal
        self.player_name = self.main_menu.ask_player_name()
        if self.player_name is None:
            return  # Si se cancela, regresamos al menú principal

        if difficulty in ["facil", "medio", "dificil"]:
            self.difficulty = difficulty
            self.game_model = GameModel(self.difficulty)  # Crear el modelo de juego
            self.game_model.load_scores()  # Cargar las puntuaciones desde el archivo
            self.game_model._generate_board()  # Generar el tablero

            # Mostrar ventana de carga mientras se descargan las imágenes
            self.show_loading_window()

            # Iniciar la descarga de imágenes en un hilo
            self.load_images_thread()
        else:
            messagebox.showwarning("Dificultad inválida", "Por favor elige una dificultad válida.")

    def show_loading_window(self):
        """Mostrar ventana de carga mientras las imágenes se descargan."""
        if hasattr(self, 'loading_window') and self.loading_window.winfo_exists():
            self.loading_window.destroy()  # Si la ventana ya existe, la destruimos

        self.loading_window = tk.Toplevel(self.root)  # Crear ventana para la carga
        self.loading_window.title("Cargando imágenes")
        self.loading_label = tk.Label(self.loading_window, text="Cargando imágenes, por favor espere...", font=("Arial", 14))
        self.loading_label.pack(padx=20, pady=20)
        self.loading_window.protocol("WM_DELETE_WINDOW", self.prevent_window_close)  # Evitar cerrar la ventana


    def prevent_window_close(self):
        """Prevenir que la ventana de carga se cierre mientras se están descargando las imágenes."""
        pass

    def load_images_thread(self):
        """Iniciar un hilo para descargar las imágenes sin bloquear la interfaz de usuario."""
        threading.Thread(target=self.load_images).start()

    def load_images(self):
        """Descargar las imágenes desde las URLs y almacenarlas en la lista."""
        try:
            for url in self.image_urls:
                # Iniciar un hilo para descargar la imagen
                threading.Thread(target=self.iniciar_imagen, args=(url,)).start()
        except Exception as e:
            print(f"Error al intentar cargar imágenes: {e}")

    def iniciar_imagen(self, url):
        """Función que descarga la imagen en un hilo separado."""
        # Pasar el callback de la función descargar_imagen
        descargar_imagen(url, self.image_downloaded_callback)

    def image_downloaded_callback(self, imagen):
        """Callback que maneja la imagen descargada."""
        if imagen:
            self.images.append(imagen)  # Añadir la imagen descargada a la lista
        else:
            print("Error al descargar una imagen.")
        
        self.images_loaded = True  # Indicamos que las imágenes están cargadas
        self.check_images_loaded()  # Comprobar si todas las imágenes han sido descargadas

    def check_images_loaded(self):
        """Verificar si todas las imágenes están cargadas y proceder con la vista de juego."""
        if len(self.images) == len(self.image_urls):
            # Aquí puedes proceder con la lógica para continuar con el juego
            print("Todas las imágenes están cargadas")
            # Cerrar la ventana de carga
            self.loading_window.destroy()  # Cerrar la ventana de carga
        
            # Proceder a la creación de la vista del tablero
            if self.game_view:
                self.game_view.frame.destroy()  # Destruir la vista anterior si existe

            self.start_game_window()  # Iniciar la nueva ventana de juego


    def start_game_window(self):
        """Abrir la ventana para mostrar el tablero de juego"""
        self.root.withdraw()  # Ocultar la ventana principal del menú
        game_window = tk.Toplevel(self.root)  # Crear nueva ventana para el juego
        game_window.title("Juego de Memoria")

        # Crear la vista del tablero de juego
        self.game_view = GameView(game_window, self.game_model, self)
        self.game_view.create_board()  # Crear el tablero de juego

        # Iniciar el temporizador y actualizaciones
        self.update_time()  # Llamada recursiva para el temporizador

    def on_card_click(self, index):
        """Acción cuando se hace clic en una carta"""
        # Verificar si ya hay dos cartas volteadas o si el índice ya está en `selected`
        if len(self.selected) == 2 or any(index == selected[0] for selected in self.selected):
            return  # Si ya hay dos cartas volteadas o es la misma carta, no hacer nada

        card_value = self.game_model.board[index]
        self.selected.append((index, card_value))  # Añadir la carta a la lista de cartas volteadas

        # Mostrar temporalmente la carta en la vista
        self.game_view.update_board([(index, card_value)])

        # Verificar si se voltearon dos cartas
        if len(self.selected) == 2:
            self.handle_card_selection()

    def handle_card_selection(self):
        """Verificar si las cartas seleccionadas coinciden"""
        card1_index, card1_value = self.selected[0]
        card2_index, card2_value = self.selected[1]

        if card1_value == card2_value:
            # Las cartas coinciden, actualizarlas en la vista
            self.game_view.update_board(self.selected, matched=True)
            # Comprobar si se ha ganado el juego
            self.check_victory()
        else:
            # Las cartas no coinciden, ocultarlas después de un retraso
            self.root.after(1000, self.game_view.reset_cards, card1_index, card2_index)

        # Incrementar el contador de movimientos y actualizar la vista
        self.increment_move_count()
        # Restablecer las cartas seleccionadas
        self.selected = []

    def increment_move_count(self):
        """Incrementar el contador de movimientos y actualizar la vista"""
        self.move_count += 1
        self.game_view.update_moves(self.move_count)

    def update_time(self):
        """Actualizar el temporizador cada segundo"""
        if self.root.winfo_exists():  # Verificamos si la ventana principal sigue existiendo
            self.start_time += 1
            self.game_view.update_timer(self.start_time)
            self.root.after(1000, self.update_time)  # Llamar a la función cada segundo

    def check_victory(self):
        """Comprobar si todas las cartas han sido emparejadas"""
        if len(self.game_view.matched_cards) == len(self.game_model.board):
            messagebox.showinfo("¡Felicidades!", "¡Has ganado!")
        
            # Guardar la puntuación en el modelo
            self.game_model.save_score(self.player_name, self.move_count, self.start_time)
        
            # Después de un breve retraso, regresar al menú principal
            self.root.after(100, self.return_to_main_menu)


    def return_to_main_menu(self):
        """Redirigir al menú principal sin cerrar la aplicación"""
        self.game_view.frame.destroy()  # Destruir el marco del juego
        self.game_view = None  # Limpiar la referencia de la vista
        self.selected = []  # Limpiar las cartas seleccionadas
        self.move_count = 0  # Reiniciar el contador de movimientos
        self.start_time = 0  # Reiniciar el tiempo
        self.images_loaded = False  # Restablecer el indicador de imágenes cargadas
        self.images = []  # Limpiar la lista de imágenes descargadas

        self.root.deiconify()  # Mostrar el menú principal nuevamente


    def show_stats_callback(self):
        """Mostrar las estadísticas del juego"""
        # Aquí comprobamos si self.game_model es None, pero aún así procedemos a mostrar las puntuaciones
        if self.game_model is None:
            messagebox.showinfo("Estadísticas", "No hay estadísticas disponibles. No se ha jugado ningún juego aún.")
            return

        # Asegúrate de que las puntuaciones estén cargadas (aunque el juego no haya comenzado)
        self.game_model.load_scores()

        scores = self.game_model.scores  # Acceder a las puntuaciones guardadas en el modelo
        stats_message = "Ranking por dificultad:\n"
    
        for difficulty, score_list in scores.items():
            stats_message += f"\n{difficulty.capitalize()}:\n"
            for idx, entry in enumerate(score_list):
                stats_message += f"{idx + 1}. {entry['name']} - Movimientos: {entry['moves']}, Tiempo: {entry['time_taken']}s, Fecha: {entry['date']}\n"

        messagebox.showinfo("Estadísticas", stats_message)



    def quit_callback(self):
        """Cerrar la aplicación"""
        self.root.quit()
