#Escribe un programa en Python que permita al usuario registrar contactos. El programa debe
#permitir al usuario ingresar el nombre y el número de teléfono de cada contacto. Luego, el programa
#debe permitir al usuario buscar un contacto por su nombre y mostrar su número de teléfono
#correspondiente.

#Diccionario
#Clave=Nombre
#valor:Numero de telefono 


#Nombre:?
#Numero de telefono:?

import os
control = True

diccionario_registro={}
#Funcion para borrar la pantalla
def fnt_pantalla():
    os.system("cls")
    
#Funcion que pide los datos al usuario
def fnt_resgistrar():
    fnt_pantalla()
    nombre=input('Ingrese el nombre del contacto:')
    numero=input('Ingrese el numero de telefono:')
    diccionario_registro[nombre]=numero    
    if nombre == ''  or numero == '':
        input('Rellene nuevamente los datos')
    else:
        diccionario_registro[nombre] = numero
        input('Datos rellenados con exito')    
               
def fnt_consultar():
    global diccionario_registro
    fnt_pantalla()
    nombre = input('Ingrese el nombre del contacto que desea buscar: ')
    if nombre in diccionario_registro:
        print(f'Número de teléfono de {nombre}: {diccionario_registro[nombre]}')
        input('Contacto encontrado exitosamente ')
    else:
        input('El contacto no se encuentra registrado,intentelo nuevamente.')
        
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
    opcion=input('<<<<<<<< Menu de opciones >>>>>>>>>>>>>>\n0.Salir\n1.Registar\n2.Buscar contacto\n->')
    fnt_selector(opcion)


