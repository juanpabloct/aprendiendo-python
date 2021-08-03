from ast import dump
import json
from os import close, remove
""" 
file = 'Datos.json'
datos: list = []
try:
    datos = json.load(open(file, 'r'))
except:
    datos = []
mes=input('Escribe un mes: ')
dia=input('Escribe el dia: ')
datos.append({'mes': mes, 'dia': dia})
print(datos)
subir = open(file, 'w')
subir.write(json.dumps(datos))  """
""" with open('Datos.json', 'r') as f:
    leer= f.read()
transformar=json.loads(leer)
print(transformar) """
a=[{'Saludo':'hola', 'despedida':'adios'}, {'Saludo':'hello', 'despedida':'good bay'}, {'Saludo':'good morning', 'despedida':'bood night'}]
llenar=input('Borrar: ')
""" for x in a:
    print(len(a))
    if llenar in a:
        a.pop(1)
print() """
#Practicar json
with open('colores.json', 'r') as f:
    leame=f.read()
    hola=json.loads(leame)
    print(hola)
    color=input('escriba un color: ')
    for x in hola:
        colores=x['nombreColor']
        if colores==color:
            print(x)
