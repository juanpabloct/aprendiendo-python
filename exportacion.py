import json
#Esta funcion es del menu de opciones
seleccion= lambda:  input('Que te gustaria hacer: ')
def mostrar_menu():
    print(""" Selecciona una de estas opciones: 
              1. Mostrar la cantidad de estudiantes
              2. añadir estudiantes
              3. eliminar estudiante
              4. mostrar todos los estudiantes
              5. borrar todos""")  
    return seleccion()
def longitud_estudiantes(estudiantes):
    longitud=len(estudiantes)
    print(f'La cantidad de estudiantes es {longitud}')
def añadir_estudiantes(estudiantes):
    nombre=input('Escribe tu nombre: ')
    apellido= input('escribe tu apellido: ')
    Ti=input('escribe tu tarjeta de identidad: ')
    estudiante={'nombre':nombre, 'apellido':apellido, 'Ti':Ti}
    return estudiante
estudiantes=[]
