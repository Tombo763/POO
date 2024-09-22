'''Herencia:
class NombreSubClase(NombreClaseSuperior):

class ClaseBase:
    Cuerpo de la clase base.

class DervicadoClase(ClaseBase):
    Cuerpo de la clase derivada.'''

class Pokemon:
    pass

    def __init__(self, nombre, tipo):
        self.nombre = nombre #Este nombre es para modificar el nombre Charmander --> Pepito.
        self.tipo = tipo

    def descripcion(self):
        return f'{self.nombre} es un pokemon de tipo {self.tipo}.'
    
class Pikachu(Pokemon):
    def ataque(self, tipoAtaque):
        return f'{self.nombre} tiene el tipo de ataque: {tipoAtaque}.'

class Charmander(Pokemon):
    def ataque(self, tipoAtaque):
        return f'{self.nombre} tiene el tipo de ataque: {tipoAtaque}.'

#Creamos nuestro objeto.
nuevo_pokemon = Pikachu('Pepito','Eléctrico')
print(nuevo_pokemon.descripcion())
#Quiero trabajar con la clase específica pikachu
print(nuevo_pokemon.ataque('impactrueno'))