# Cinthia Quiñonez 
# 201801075

from listaDobleEn import*

# Se instancia la clase
listaD=ListaDoble()

def nuevoContacto():
    listaD.datos()
    listaD.imprimir()
   
def buscarContacto():
    telefonoBuscar=input('Ingrese el número que desea buscar: ')
    listaD.buscar(telefonoBuscar)

def visualizarContacto():
    listaD.Graficar()

while(True):
    print('<-------------------------------------------------->')
    print('<                    ==========                    >')
    print('<                       Menú                       >')
    print('<                    ==========                    >')
    print('<          1. Ingresar nuevo contacto              >')
    print('<          2. Buscar contacto                      >')
    print('<          3. Visualizar agenda                    >')
    print('<          4. Salir                                >')
    print('<-------------------------------------------------->')
    opcion=int(input('Ingrese una opción: '))
    print()
    if opcion==1:
        nuevoContacto()
    elif opcion==2:
        buscarContacto()
    elif opcion==3:
        visualizarContacto()
    elif opcion==4:
        exit()
    else:
        print('Opción incorrecta')