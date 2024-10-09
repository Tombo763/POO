class Multa:
    def __init__(self, id_multa, valor, fechaEmision, estado):
        self.id_multa = id_multa
        self.valor = valor
        self.fechaEmision = fechaEmision
        self.estado = estado
    
    def calcularMulta(self):
        print('Calculando multa...')
        pass
    
    def pagarMulta(self):
        print('Pagando multa...')
        pass
