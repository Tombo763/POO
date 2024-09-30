'''Crear una clase Fabrica que tenga los atributos de llantas, color y precio; luego crear dos clases más que hereden de Fabrica, las cuales
son moto y auto. Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por último, crear objetos para cada
clase y mostrar por pantalla los atributos de cada uno.'''

class Fabrica: #Creamos la clase padre.
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica): #Creamos una subclase de Fábrica.
    def mostrar_info(self):
        print(f'Moto: Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio}')

class Auto(Fabrica): #Creamos una segunda clase de Fábrica.
    def mostrar_info(self):
        print(f'Auto: Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio}')

# Crear objetos con sus atributos.
moto = Moto(2, 'gris', 1500000)
auto = Auto(4, 'negro', 24000000)

moto.mostrar_info()
auto.mostrar_info()
