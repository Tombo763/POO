class Libro:
    def __init__(self, ISBN, autor, editorial, anoPublicacion, categoria):
        self.ISBN = ISBN
        self.autor = autor
        self.editorial = editorial
        self.anoPublicacion = anoPublicacion
        self.categoria = categoria
        
    def crearLibro(self):
        print('Creando libro...')
        pass

    def modificarLibro(self):
        print('Modificando libro...')
        pass

    def seleccionarLibro(self):
        print('Seleccionando libro...')
        pass

    def borrarLibro(self):
        print('Borrando libro...')
        pass
