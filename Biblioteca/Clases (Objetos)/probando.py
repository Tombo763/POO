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
        
    def crearLibro(self):
        print('Creando libro...')
        pass

    def modificarLibro(self):
        print('Modificando libro...')
        pass

    def seleccionarLibro(self):
        print('Seleccionando libro...')
        pass

    def borrarLibro(self):
        print('Borrando libro...')
        pass

class Tipo_usuario:
    def __init__(self, id_tipo_usuario, nombre):
        self.id_tipo_usuario = id_tipo_usuario
        self.nombre = nombre
    
    def crearTipo_usuario(self):
        print('Creando tipo de usuario...')
        pass

    def modificarTipo_usuario(self):
        print('Modificando tipo de usuario...')
        pass

    def seleccionarTipo_usuario(self):
        print('Seleccionando tipo de usuario...')
        pass

    def borrarTipo_usuario(self):
        print('Borrando tipo de usuario...')
        pass

class Usuario(Tipo_usuario): #HERENCIA
    def __init__(self, idUsuario, nombre, direccion, telefono, correoElectronico, id_tipo_usuario):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correoElectronico = correoElectronico
        self.id_tipo_usuario = id_tipo_usuario
    
    def crearUsuario(self):
        print('Creando usuario')
        pass

    def seleccionarTipo_usuario(self):
        print('Seleccionando usuario...')
        pass

    def modificarUsuario(self):
        print('Modificando usuario...')
        pass

    def eliminarUsuario(self):
        print('Eliminando usuario...')
        pass

class Reserva:
    def __init__(self, id_reserva):
        self.id_reserva = id_reserva
    
    def crearReserva(self):
        print('Creando reserva...')
        pass

    def seleccionarReserva(self):
        print('Mostrando reservas...')
        pass

    def modificarReserva(self):
        print('Modificando reserva...')
        pass

    def eliminarReserva(self):
        print('Eliminado reserva...')

class Bibliotecario:
    def __init__(self, id_bibliotecario, nombre, telefono, correoElectronico):
        self.id_bibliotecario = id_bibliotecario
        self.nombre = nombre
        self.telefono = telefono
        self.correoElectronico = correoElectronico
    
    def registrarBibliotecario(self):
        print('Registrando bibliotecario...')
        pass

    def seleccionarBibliotecario(self):
        print('Mostrando bilbiotecario...')
        pass

    def modificarBibliotecario(self):
        print('Modificando bilbiotecarios...')
        pass

    def eliminandoBibliotecario(self):
        print('Eliminando bibliotecario...')
        pass

class Prestamo:
    def __init__(self, id_prestamo, fechaInicio, fechaDevolucion, estadoPrestamo):
        self.id_prestamo = id_prestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.estadoPrestamo = estadoPrestamo
    
    def registroPrestamo(self):
        print('Registrando préstamo...')
        pass

    def seleccionarPrestamo(self):
        print('Selecionando préstamo...')
        pass

    def modificarPrestamo(self):
        print('Modificando préstamo...')
        pass

    def eliminarPrestamo(self):
        print('Eliminando préstamo...')
        pass

class Multa:
    def __init__(self, id_multa, valor, fechaEmision, estado):
        self.id_multa = id_multa
        self.valor = valor
        self.fechaEmision = fechaEmision
        self.estado = estado
    
    def registrarMulta(self):
        print('Registrando multa...')
        pass

    def seleccionarMulta(self):
        print('Mostrando multas...')
        pass

    def modificarMulta(self):
        print('Modificando multa...')
        pass

    def eliminarMulta(self):
        print('Eliminando multa...')
        pass

class Distribuidor:
    def __init__(self, id_distribuidor, nombre, direccion, telefono, correoElectronico):
        self.id_distribuidor = id_distribuidor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correoElectronico = correoElectronico
    
    def registrarDistribuidor(self):
        print('Reistrando distribuidor...')
        pass

    def seleccionarDistribuidor(self):
        print('Mostrando distribuidor...')
        pass

    def modificarDistribuidor(self):
        print('Modificando distribuidor...')
        pass

    def eliminarDistribuidor(self):
        print('Eliminando distribuidor...')
        pass

class Boleta:
    def __init__(self, id_boleta, fechaEmision, valorTotal, estado):
        self.id_boleta = id_boleta
        self.fechaEmision = fechaEmision
        self.valorTotal = valorTotal
        self.estado = estado
    
    def registrarBoleta(self):
        print('Registrando boleta...')
        pass

    def seleccionarBoleta(self):
        print('Mostrando boleta...')
        pass

    def modificarBoleta(self):
        print('Modificando boleta...')
        pass
    
    def eliminarBoleta(self):
        print('Eliminando boleta...')
        pass

class Compra:
    def __init__(self, id_compra, fechaCompra, cantidadLibros, valorTotal):
        self.id_compra = id_compra
        self.fechaCompra = fechaCompra
        self.cantidadLibros = cantidadLibros
        self.valorTotal = valorTotal
    
    def registrarCompra(self):
        print('Registrando compra...')
        pass

    def seleccionarCompra(self):
        print('Mostrando compra...')
        pass

    def modificarCompra(self):
        print('Modificando compra...')
        pass
    
    def eliminarCompra(self):
        print('Eliminando compra...')
        pass


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
