class Email:
    def __init__(self):
        self.enviado = False
    
    def enviar_correo(self):
        self.enviado = True
    
mi_correo = Email()
print(mi_correo.enviado)
#Ojo que ambos métodos son self.enviado y si lo busco me aparece solo en __init__.
mi_correo.enviar_correo()
print(mi_correo.enviado)