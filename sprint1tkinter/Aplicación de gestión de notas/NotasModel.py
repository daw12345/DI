class NotasModel:
    def __init__(self, archivo):
        self.notas = []
        self.archivo = archivo  # Guarda el archivo de notas
    
    def agregar_nota(self, nueva_nota):
        self.notas.append(nueva_nota)
    
    def eliminar_nota(self, indice):
        if 0 <= indice < len(self.notas):
            del self.notas[indice]

    def obtener_notas(self):
        return self.notas
    
    def guardar_notas(self):
        with open(self.archivo, 'w') as archivo:
            for nota in self.notas:
                archivo.write(nota + '\n')

    def cargar_notas(self):
        try:
            with open(self.archivo, 'r') as archivo:
                self.notas = [linea.strip() for linea in archivo]  # Carga todas las notas
        except FileNotFoundError:
            self.notas = []  # Si no existe el archivo, inicializa como lista vacía
            print("El archivo 'notas.txt' no existe. Se inicializa una lista vacía.")


