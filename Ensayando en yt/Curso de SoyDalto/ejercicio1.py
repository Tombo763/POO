class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    #Hemos creado la clase hasta acá.
    def estudiar(self):
        print('Estoy estudiando...')


nombre = input('Dígame su nombre: ')
edad = input('Dígame su edad (sólo el número): ')
curso = input('Dígame su curso: ')

estudiante = Estudiante(nombre, edad, curso)

print(f'''
    DATOS DEL ESTUDIANTE: \n
    Nombre: {estudiante.nombre}.
    Edad: {estudiante.edad} años.
    Curso: {estudiante.curso}.''') 

estudiar = input()
if estudiar.lower == 'estudiar':
    estudiante.estudiar()
