'''Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
Persona y Estudiante. La clase Persona tendrá los atributos nombre y edad y un método que
el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y también 
tendrá un atributo adicional: grado y un método que imprima el grado del estudiante. Deberás
utilizar super en el método de inicialización para reutilizar el código de la clase padre.
Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos 
para asegurarte de que todo funcione correctamente.'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrarNombre(self):
        print(f'''Nombre: \n {self.nombre} \n Edad: {self.edad}.''')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado  
    
    def mostrarGrado(self):
        print(f'Grado: \n {self.grado}')

estudiante = Estudiante("Alessandro","24","5to")
estudiante.mostrarNombre()
estudiante.mostrarGrado()
