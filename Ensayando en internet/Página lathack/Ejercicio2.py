'''Crea una clase persona. Con atributos nombre y edad. Además, hay que crear
un método cumpleaños, que aumente en 1 la edad de la persona cuando se invoque 
sobre un objeto creado con persona.'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cumpleaños(self):
        self.edad += 1

persona = Persona(input('Ingrese su nombre: '),int(input('Ingrese su edad: ')))
persona.cumpleaños()
persona.cumpleaños()
print(f'{persona.nombre} tiene {persona.edad} años.')