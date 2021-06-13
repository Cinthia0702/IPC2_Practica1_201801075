import os
from nodo import Nodo
from nodo import Usuario

class ListaDoble:
    # Constructor
    def __init__(self):
        self.cabezaLista=None 
        self.colaLista=None
        self.tamaño=0
    # Método imprimir
    def imprimir(self):
        if self.cabezaLista==None:
            print('La lista esta vacia')
        else:
            nodoActual=self.cabezaLista
            while nodoActual!=None:
                print(nodoActual.informacion.nombre,nodoActual.informacion.apellido,nodoActual.informacion.telefono,end='->')
                nodoActual=nodoActual.derecha
            print('None')
    # Método datos
    def datos(self):
        nombre=input('Ingrese nombre: ')
        apellido=input('Ingrese apellido: ')
        telefono=input('Ingrese número de telefono: ')
        print()
        self.insertar(nombre,apellido,telefono)
        self.ordenar(nombre,apellido,telefono)
    # Método insertar
    def insertar(self,nombre,apellido,telefono):
        nuevoNodo=Nodo(Usuario(nombre,apellido,telefono))        
        if self.cabezaLista == None:
            # la cola de la lista es igual a la cabeza de la lista
            self.cabezaLista=self.colaLista=nuevoNodo
        else:
            # nuevoNodo apunta a la cola de la lista
            nuevoNodo.izquierda=self.colaLista
            # cola de la lista apunta al nuevoNodo
            self.colaLista.derecha=nuevoNodo
            self.verificar(nuevoNodo.informacion.telefono)
            # La cola de la lista es el nuevo nodo
            self.colaLista=nuevoNodo
        self.tamaño+=1
    # Método buscar
    def buscar(self,telefonoC):
        nodoActual=self.cabezaLista
        elementoBuscado=False
        if self.cabezaLista==None:
            print('La lista esta vacia')
        else:
            while nodoActual != None:
                if nodoActual.informacion.telefono==telefonoC:
                    print('\nNombre: ',nodoActual.informacion.nombre)
                    print('Apellido: ',nodoActual.informacion.apellido)
                    print('Teléfono: ',nodoActual.informacion.telefono)
                    elementoBuscado=True
                    break
                nodoActual=nodoActual.derecha
            if elementoBuscado:
                print()
            else:
                while True:
                    print('\nEl número de teléfono no existe ¿Desea agregarlo?')
                    print('     1. Si')
                    print('     2. No')
                    opcion=int(input('Ingrese una opción: '))
                    if opcion==1:
                        self.datos()
                        self.imprimir()
                        break
                    elif opcion==2:
                        break
                    else:
                        print('Opción incorrecta')
    # Método verificar
    def verificar(self,telefonoC):
        elementoV=False
        if self.cabezaLista==None:
            print('Lista vacia')
        else:
            nodoA=self.cabezaLista
            while nodoA.derecha!=None:
                if telefonoC in nodoA.informacion.telefono:           
                    print('El contacto ya existe\n')
                    elementoV=True
                nodoA=nodoA.derecha
            if elementoV:
                pass
                #print(nodoA.informacion.nombre,nodoA.informacion.apellido,nodoA.informacion.telefono) 
            else:
                print('El contacto se ha agregado exitosamente\n')
    # Método ordenar apellido
    def ordenarA(self,nombreO,apellidoO,telefonoO):
        nodoNuevo=Nodo(Usuario(nombreO,apellidoO,telefonoO))
        nodoActual=self.cabezaLista
        if self.cabezaLista==None:
            print('Lista vacia')
        else:
            while nodoActual != None:
                nodoNuevo=nodoActual.derecha
                while nodoNuevo !=None:
                    if nodoNuevo.informacion.apellido < nodoActual.informacion.apellido:
                        nodoAux=nodoActual.informacion
                        nodoActual.informacion=nodoNuevo.informacion
                        nodoNuevo.informacion=nodoAux
                    nodoNuevo=nodoNuevo.derecha
                nodoActual=nodoActual.derecha
    # Método ordenar nombre
    def ordenarN(self,nombreO,apellidoO,telefonoO):
        nodoNuevo=Nodo(Usuario(nombreO,apellidoO,telefonoO))
        nodoActual=self.cabezaLista
        if self.cabezaLista==None:
            print('Lista vacia')
        else:
            while nodoActual != None:
                nodoNuevo=nodoActual.derecha
                while nodoNuevo !=None:
                    if nodoNuevo.informacion.nombre < nodoActual.informacion.nombre:
                        nodoAux=nodoActual.informacion
                        nodoActual.informacion=nodoNuevo.informacion
                        nodoNuevo.informacion=nodoAux
                    nodoNuevo=nodoNuevo.derecha
                nodoActual=nodoActual.derecha
    # Método ordenar contactos
    def ordenar(self,nombre,apellido,telefono):
        if self.cabezaLista==None:
            print('Lista vacia')
        else:
            nodoA=self.cabezaLista
            if nodoA.derecha!=None:
                if nodoA.informacion.apellido != apellido:
                    self.ordenarA(nombre,apellido,telefono)
                else:
                    self.ordenarN(nombre,apellido,telefono)
                nodoA=nodoA.derecha
    # Método graficar
    def Graficar(self):
            nodoAct = self.cabezaLista
            nodoAct2 = self.cabezaLista
            f = open("Agenda.dot", "w",encoding="utf-8")
            grafica = 'digraph G{\n'
            nnodo = 1
            nnodo2 = 1
            while   nodoAct.derecha != None:
                grafica +='Nodo'
                grafica +=str(nnodo)
                grafica +='[shape = circle, label =\" Nombre: '
                grafica +=nodoAct.informacion.nombre
                grafica +='\nApellido: '+nodoAct.informacion.apellido
                grafica +='\nTeléfono: '+nodoAct.informacion.telefono
                grafica +='\"]\n'
                nodoAct = nodoAct.derecha
                nnodo = nnodo +1
            grafica += 'Nodo'
            grafica += str(nnodo)
            grafica += '[shape = circle, label =\" Nombre: '
            grafica += nodoAct.informacion.nombre
            grafica += '\nApellido: '+nodoAct.informacion.apellido
            grafica += '\nTeléfono: '+nodoAct.informacion.telefono
            grafica += '\"]\n'
            grafica += 'Cola'
            grafica += '[shape = circle, label =\" None'
            grafica += '\"]\n'
            while nodoAct2.derecha != None:
                grafica += 'Nodo'
                grafica += str(nnodo2)
                grafica += '->'
                grafica += 'Nodo'
                grafica += str(nnodo2+1)
                grafica += '->'
                grafica += 'Nodo'
                grafica += str(nnodo2)
                grafica += '\n'
                nodoAct2 = nodoAct2.derecha
                nnodo2 = nnodo2+1
            grafica += 'Nodo'
            grafica += str(nnodo2)
            grafica += '->'
            grafica += 'Cola\n'
            grafica += '}'
            f.write(grafica)
            f.close()
            os.system("dot -Tpng Agenda.dot -o Agenda.jpg")
            os.system("Agenda.jpg")