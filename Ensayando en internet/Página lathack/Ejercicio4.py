'''Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto:
En la clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido. Además, esta clase , debe tener un método para mostrar nombre_completo() el cual debe mostrar el nombre acompañado del apellido.
La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir los argumentos nombre y edad. También la clase “Estudiante”, recibe el valor “carrera”, y además contar con un método mostrar_carrera(). Las dos clases son obligatorias.'''

#Se debe definir la clase padre.
class Persona:
	
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
	
	def nombreCompleto(self):
		print(f'{self.nombre}  {self.apellido}.')

#Se define la subclase o clase hija
class Estudiante(Persona):
	def __init__(self, nombre, apellido, carrera):
		super().__init__(nombre, apellido)
		self.carrera = carrera
	
	def mostrar_carrera(self):
		print(self.carrera)

#Ingresamos los atributos del objeto que se ingresaran a la clase
nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
carrera = input('Ingrese su carrera: ')
#Creamos el objeto con los atributos ingresado
estudiante = Estudiante(nombre, apellido, carrera) 
#Se hacen las consultas correspondientes.
estudiante.nombreCompleto()
estudiante.mostrar_carrera()
