class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    
    def ingresar_dato(self):
        self.datos = [int(input('Ingresa dato ' + str(i+1) + ' = ')) for i in range(self.n)]



class OperacionesBasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        s = a + b
        print(f'El resultado de la suma es {s}.')

    def resta(self):
        a,b = self.datos
        r = a - b
        print(f'El resultado de la resta es {r}.')


class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos #Ojo debe llevar una , después de la a sino da error --> TypeError: must be real number, not list
        print(f'El resultado de la raiz cuadrada es: ',math.sqrt(a),'.')

objeto = OperacionesBasicas()
# print(isinstance(objeto,OperacionesBasicas)) --> 'Isinstance' verfica la herencia con un TRUE. Devuelve efectivamente un TRUE.
# print(isinstance(objeto,Raiz)) #Devuelve FALSE.

print(issubclass(Calculadora,OperacionesBasicas)) # --> devuelve un FALSE. Primero se escribe la subclase después la clase. Está mal escrito.
print(issubclass(OperacionesBasicas,Calculadora)) # --> devuelve un TRUE.
print(issubclass(Raiz,Calculadora)) # --> TRUE.