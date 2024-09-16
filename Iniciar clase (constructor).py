class Auto: #Es el modelo o la idea de nuestro objeto
    def __init__(self,marca,modelo): #def init inicia la clase en un espacio de memoria (constructor).
        self.__marca = marca
        self.__modelo = modelo
    
    def obtener_marca(self):
        return self.__marca
    
    def obtener_modelo(self):
        return self.__modelo
    
    def arrancar(self):
        print(f"El {self.__marca} {self.__modelo} está arrancando.")

class AutoDeportivo(Auto):
    def __init__(self,marca,modelo,velocidad_maxima):
        super().__init__(marca,modelo)
        self.__velocidad_maxima = velocidad_maxima
    
    def obtener_velocidad_maxima(self):
        return self.__velocidad_maxima
    
    def arrancar(self):
        super().arrancar()
        print(f"El {self.obtener_marca()} {self.obtener_modelo()} \ está listo para correr a una velocidad de {self.__velocidad_maxima} km/h.")