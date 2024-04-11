#Desarrolla un programa en Python que permita al usuario mantener un inventario de productos. El
# programa debe permitir al usuario ingresar el nombre y la cantidad disponible de cada producto.
#Luego, el usuario debe poder buscar un producto por su nombre y ver cuántos están disponibles en
# el inventario.

import os
control = True

diccionario_inventario={}
#Funcion para borrar la pantalla
def fnt_pantalla():
    os.system("cls")
    
#Funcion que pide los datos del producto
def fnt_resgistrar():
    fnt_pantalla()
    producto=input('Ingrese el nombre del producto:')
    cantidad=input('Ingrese la cantidad del producto:')
    diccionario_inventario[producto]=cantidad    
    if producto == ''  or cantidad == '':
        input('Rellene nuevamente los datos')
    else:
        diccionario_inventario[producto] = cantidad
        input('Producto registrado  con exito')    
               
def fnt_consultar():
    global diccionario_inventario
    fnt_pantalla()
    nombre = input('Ingrese el nombre del contacto que desea buscar: ')
    if nombre in diccionario_inventario:
        print(f'Cantidad disponible  de {nombre}: {diccionario_inventario[nombre]}')
        input('Producto  encontrado exitosamente ')
    else:
        input('El producto no se encuentra en stock ,intentelo nuevamente.')
        
#Se invoca la funcion dependiendo la que se escoja       
def fnt_selector(op):
    global control
    if opcion == '0':
        control=False    
    elif opcion == '1':
        fnt_resgistrar()
    elif opcion == '2':
        fnt_consultar()
        
#Menu de opciones        
while control == True: 
    fnt_pantalla()
    opcion=input('<<<<<<<< Menu de opciones >>>>>>>>>>>>>>\n0.Salir\n1.Registar\n2.Buscar producto\n->')
    fnt_selector(opcion)


