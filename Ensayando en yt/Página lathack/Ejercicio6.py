'''Crear una clase llamada Marino con un método que sea hablar, en donde muestre
un mensaje que diga "Hola, soy un animal marino". Luego, crear una clase pulpo
que herede de marino, pero modificar el mensaje por "Hola soy pulpo". Por
último crear una clase foca, heredada de marino, pero que tenga un atributo
nuevo llamado mensaje y que muestre ese mensaje como parámetro.'''

class Marino:
    def __init__(self):
        pass
    
    def hablar(self):
        print('Hola, soy un animal marino.')

class Pulpo(Marino):
    def hablar(self):
        print('Hola, soy un pulpo.')

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)

animalMarino = Marino()
animalMarino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar('Hola, soy una foca.')