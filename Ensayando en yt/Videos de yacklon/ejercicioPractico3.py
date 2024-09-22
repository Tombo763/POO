class Persona:
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    
    #Ahora voy a crear métodos a parte del constructor.
    def descripcion(self):
        return f'{self.nombre} tiene {self.año}'

    def comentario(self, frase):
        return f'{self.nombre} dice: {frase}'

    
doctor = Persona('Alessandro',25)
print(doctor.descripcion())
print(doctor.comentario('hola que tal')) #Sólo pide que se ingrese una frase