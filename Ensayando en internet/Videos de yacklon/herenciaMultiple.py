'''
- Herencia Múltiple:

class Base_uno:
    pass

class Base_dos:
    pass

class DerivadoMultiple(Base_uno, Base_dos):
    pass
    
 - Herencia Multinivel:

class Base:
    pass

class Derivado_uno(Base):
    pass

class Derivado_dos(Derivado_uno):
    pass
    
'''

#Creamos un smartphone pero antes debemos dividirlo.
class Telefono:
    def __init__(self):
        pass

    def llamar(self): #¿Qué acciones hace un teléfono?
        print('Llamando...')

    def ocupado(self):
        print('Tono ocupado...')

class Camara(Telefono):
    def __init__(self):
        pass
    
    def tomar_fotografia(self):
        print('Tomando foto...')

class Reproduccion(Telefono):
    def __init__(self):
        pass
    
    def reproduccionDeMusica(self):
        print('Reproduciendo música...')
    
    def reproducirUnVideo(self):
        print('Reproduciendo video...')

class Smartphone(Camara,Reproduccion): #Su única función es combinar clases sin más. #OJO: no va la clase Telefono sino se produce un error por ambigüedad.
    def __del__(self): #Se usa para limpiar los recursos. Así los objetos y clases utilizadas se borran de la memoria cuando no se usan. (proyecto)
        #print('¡Teléfono apagado!') #Se usa para tener la referencia que se usa la clase
        pass

movil = Smartphone()

#print(movil.tomar_fotografia()) --> Tomando foto.. / None / ¡Teléfono apagado!, estos dos últimos provienen del destructor.
movil.tomar_fotografia() #La usaré para que no devuelva un NONE en la consola ya que no hay un RETURN explícito.