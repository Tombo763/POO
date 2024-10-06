class Categoria: #CRUD
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre
    
    def crearUsuario(self):
        print('Creando usuario...')
        pass

    def modificarUsuario(self):
        print('Modificando usuario...')
        pass

    def seleccionarUsuario(self):
        print('Seleccionando usuario...')
        pass

    def borrarUsuario(self):
        print('Borrando usuario...')
        pass

class Libro:
    def __init__(self, ISBN, autor, editorial, anoPublicacion, categoria):
        self.ISBN = ISBN
        self.autor = autor
        self.editorial = editorial
        self.anoPublicacion = anoPublicacion
        self.categoria = categoria

class Tipo_usuario:
    def __init__(self, id_tipo_usuario, nombre):
        self.id_tipo_usuario = id_tipo_usuario
        self.nombre = nombre

class Usuario(Tipo_usuario): #HERENCIA
    def __init__(self, idUsuario, nombre, direccion, telefono, correoElectronico, id_tipo_usuario):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correoElectronico = correoElectronico
        self.id_tipo_usuario = id_tipo_usuario

class Reserva:
    def __init__(self, id_reserva):
        self.id_reserva = id_reserva

class Bibliotecario:
    def __init__(self, id_bibliotecario, nombre, telefono, correoElectronico):
        self.id_bibliotecario = id_bibliotecario
        self.nombre = nombre
        self.telefono = telefono
        self.correoElectronico = correoElectronico

class Prestamo:
    def __init__(self, id_prestamo, fechaInicio, fechaDevolucion, estadoPrestamo):
        self.id_prestamo = id_prestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.estadoPrestamo = estadoPrestamo

class Multa:
    def __init__(self, id_multa, valor, fechaEmision, estado):
        self.id_multa = id_multa
        self.valor = valor
        self.fechaEmision = fechaEmision
        self.estado = estado

class Distribuidor:
    def __init__(self, id_distribuidor, nombre, direccion, telefono, correoElectronico):
        self.id_distribuidor = id_distribuidor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correoElectronico = correoElectronico

class Boleta:
    def __init__(self, id_boleta, fechaEmision, valorTotal, estado):
        self.id_boleta = id_boleta
        self.fechaEmision = fechaEmision
        self.valorTotal = valorTotal
        self.estado = estado

class Compra:
    def __init__(self, id_compra, fechaCompra, cantidadLibros, valorTotal):
        self.id_compra = id_compra
        self.fechaCompra = fechaCompra
        self.cantidadLibros = cantidadLibros
        self.valorTotal = valorTotal

class Factura:
    def __init__(self, id_factura, fechaEmision, valorTotal, estado):
        self.id_factura = id_factura
        self.fechaEmision = fechaEmision
        self.valorTotal = valorTotal
        self.estado = estado
