#HERENCIA
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) #CON ESTO TAMBIÉN SE HEREDAN LOS MÉTODOS.
        self.trabajo = trabajo
        self.salario = salario


roberto = Empleado('Roberto',42,'Argentino','Programador',1000000)

print(f'{roberto.nombre} tiene {roberto.edad} años y es {roberto.nacionalidad}.Es {roberto.trabajo} y recibe ${roberto.salario}.')
