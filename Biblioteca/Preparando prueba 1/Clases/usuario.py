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
