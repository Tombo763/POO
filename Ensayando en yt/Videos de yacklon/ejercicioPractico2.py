# def --> sirve para crear métodos.
#self --> se refiere al objeto y a "ejecutar" el método.
'''class Matematica:
    def sumar(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.sumar()
print(s.n1 + s.n2)'''

#__init__(seft) --> iniciar
'''class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'M'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.talla)'''

#Calculadora
class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2
 #Para calcular se escribe de la siguiente manera.
operacion = Calculadora(2,3)
print(operacion.producto)
print(operacion.division)
print(operacion.suma)
print(operacion.resta)

