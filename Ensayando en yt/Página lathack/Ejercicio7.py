'''La primera debe ser "Universidad" con atributos como nombre (donde se almacena
el nombre de la universidad). La segunda llamada carrera, con los atributos especialidad
(en donde me guarda la especialidad de un estudiante). Y por último, una llamada
Estudiante, con atributos como nombre y edad. El programa debe imprimir la especialidad,
edad, nombre y universidad de dicho estudiante con un objeto llamado persona.'''

class Universidad:
    def __init__(self, nombreUniversidad):
        self.nombreUniversidad = nombreUniversidad

class Carrera:
    def carrera(self, nombreCarrera):
        self.nombreCarrera = nombreCarrera

class Estudiante(Universidad,Carrera):
    def datos(self, nombreEstudiante, edad):
        self.nombreEstudiante = nombreEstudiante
        self.edad = edad
        print(f'''El nombre del estudiante es: {self.nombreEstudiante}.
Edad: {self.edad} años.
Su carrera es: {self.nombreCarrera}.
Estudia en: {self.nombreUniversidad}.''')

persona = Estudiante('Hardvard')
persona.carrera('Ingenieria Mecatrónica')
persona.datos('Mike',19)