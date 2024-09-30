'''Realiza un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta, multiplicacion y 
division. Utilizar un método para cada una e imprimir el resultado obtenido. Llamar
a la clase Calculadora.'''

class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

class Operaciones(Calculadora):
    def suma(self):
        print('El resultado de la suma es:', self.n1 + self.n2)
        return self.n1 + self.n2
    
    def resta(self):
        print('El resultado de la resta es:', self.n1 - self.n2)
        return self.n1 - self.n2
    
    def multiplicacion(self):
        print('El resultado de la multiplicación es:', self.n1 * self.n2)
        return self.n1 * self.n2
    
    def division(self):
        while True:
            if self.n2 == 0:
                self.n2 = int(input("Ingresa un valor válido para n2: "))
            else:
                print('El resultado de la división es:', self.n1 / self.n2)
                return self.n1 / self.n2

#----------------------------------------------------------------------------------

n1 = int(input('Ingresa un valor: '))

while True:
    n2 = int(input('Ingresa el segundo valor: '))

    respuesta = Operaciones(n1, n2)

    decision = int(input('''Ingresa el número de la operación que deseas realizar y 0 para finalizar:
                   1. Suma.
                   2. Resta.
                   3. Multiplicación.
                   4. División.
                    ¿Qué deseas realizar?: '''))

    if decision == 1:
        print('Sumando...')
        n1 = respuesta.suma()

    elif decision == 2:
        print('Restando...')
        n1 = respuesta.resta()

    elif decision == 3:
        print('Multiplicando...')
        n1 = respuesta.multiplicacion()

    elif decision == 4:
        print('Dividiendo...')
        resultado = respuesta.division()
        n1 = resultado

    elif decision == 0:
        print('Terminamos')
        break

    else:
        print('Debes seleccionar un valor del 1 al 4 para continuar.')
