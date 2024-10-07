class Factura:
    def __init__(self, id_factura, fechaEmision, valorTotal, estado):
        self.id_factura = id_factura
        self.fechaEmision = fechaEmision
        self.valorTotal = valorTotal
        self.estado = estado

    def registrarFactura(self):
        print('Registrando factura...')
        pass

    def seleccionarFactura(self):
        print('Mostrando factura...')
        pass

    def modificarFactura(self):
        print('Modificando factura...')
        pass
    
    def eliminarFactura(self):
        print('Eliminando factura...')
        pass
