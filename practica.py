import json
from os import close

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
subir.write(json.dumps(datos)) 
