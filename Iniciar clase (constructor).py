class Auto: #Es el modelo o la idea de nuestro objeto
    def __init__(self,marca,modelo): #def init inicia la clase en un espacio de memoria (constructor).
        self.__marca = marca
        self.__modelo = modelo
    
    def obtener_marca(self):
        return self.__marca
    
    def obtener_modelo(self):
        return self.__modelo