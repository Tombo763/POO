class Prestamo:
    def __init__(self, id_prestamo, fechaInicio, fechaDevolucion, estadoPrestamo):
        self.id_prestamo = id_prestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.estadoPrestamo = estadoPrestamo
    
    def fechaPréstamo(self):
        print('Calculando fecha de préstamo...')
        pass

    def devolverLibro(self):
        print('Calculando fecha de devolución del libro...')
        pass

    def renovarPrestamo(self):
        print('Calculando nueva fecha de devolución...')
        pass
