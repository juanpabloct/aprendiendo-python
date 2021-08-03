from os import closerange, remove
from typing import Callable
import exportacion
import json
estudiantes=[]
seleccionar=exportacion.mostrar_menu()
def condiciones(seleccionar):
    if seleccionar=='1' or seleccionar=='cantidad de estudiantes':
        exportacion.longitud_estudiantes(estudiantes)
        seleccionar=exportacion.mostrar_menu()
        if seleccionar== '1' or seleccionar== '2' or seleccionar=='3':
                condiciones(seleccionar)
    elif seleccionar== '2' or seleccionar=='añadir estudiante': 
        estudiante=exportacion.añadir_estudiantes(estudiantes)
        estudiantes.append(estudiante)
        with open('Datos.json', 'w') as f:
            dumps=f.write(json.dumps(estudiantes))
        f.close()
        print(estudiantes)
        seleccionar=exportacion.mostrar_menu()
        if seleccionar== '1' or seleccionar== '2' or seleccionar=='3':
            condiciones(seleccionar)
    elif seleccionar=='3':
        for x in estudiantes:
            buscar=input('Escriba la Ti del estudiante a eliminar: ')
            if x['Ti']==buscar:
                consentimiento=input('Deseas borrar este estudiante "Si" o "No": ')
                consentimiento=consentimiento.lower()
                if consentimiento=='si':
                    estudiantes.remove(x)
                    break
        seleccionar=exportacion.mostrar_menu()
        if seleccionar== '1' or seleccionar== '2' or seleccionar=='3':
            condiciones(seleccionar)
    elif seleccionar=='4':
        for contar in estudiantes:
            cantidad=contar
            print(cantidad)
    elif seleccionar =='5':
        estudiantes.clear()
        print(estudiantes)
condiciones(seleccionar)