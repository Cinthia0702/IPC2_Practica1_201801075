class Nodo:
    def __init__(self,informacion):
        self.informacion=informacion
        self.izquierda=None
        self.derecha=None

class Usuario:
    def __init__(self,nombre, apellido, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono