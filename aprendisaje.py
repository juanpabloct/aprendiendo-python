'''valor1=input('Escribe cualquier numero')

valor1=int(valor1)
print(type(valor1))
print(valor1)
def escribame(valor1, valor2):
    if valor1 == str():
        valor1= int(valor1)
        print(type(valor1))
    if valor1 == 0:
        print('no hay nada')
    
    else: 
        return valor1 + valor2

resultado=escribame(valor1, 454 )
print(resultado)'''

#Ejercicios #1 de reto

import random
mayor='mayor'
menor='menos'
edad= random.randint(0, 40)
texto='Juanito tiene {0} años y es {1} de edad'
print(texto)
if edad >= 18:
    print(texto.format(edad, mayor))
else:
    print(texto.format(edad, menor))

# Ejercicio #2 de reto
estudiantes = [
      {
          'nombre': 'Andrea',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'Carlos',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Juanita',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Olga',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'Jorge',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Daniela',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Erika',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'Luis',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Maria',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Sara',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'Agustín',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Mariana',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Isabel',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'William',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Marta',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Andrea',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'Julian',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Carmen',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Victoria',
          'edad': 15,
          'sexo': 'F'
      },
      {
          'nombre': 'Victor',
          'edad': 16,
          'sexo': 'M'
      },
      {
          'nombre': 'Juanita',
          'edad': 17,
          'sexo': 'F'
      },
      {
          'nombre': 'Jesus',
          'edad': 15,
          'sexo': 'M'
      },
      {
          'nombre': 'Susana',
          'edad': 16,
          'sexo': 'F'
      },
      {
          'nombre': 'Michael',
          'edad': 17,
          'sexo': 'M'
      },
]
feminas=[]
varones=[]
for cuentame in range(0, len(estudiantes)):
    list_students=estudiantes[cuentame]
    sexo_students= list_students['sexo'] 
    if 'M' == sexo_students:
        varones.append(sexo_students)
        print(varones)
        print(len(varones))
    if 'F' == sexo_students:
        feminas.append(sexo_students)
        print(feminas)
        print(len(feminas))
buscador=input('Escribe un nombre de la lista')


vacas=[{
    'nombre': 'pitufina',
    'raza': 'Hoistenin',
    'edad': 2
},
{
    'nombre': 'amanda',
    'raza': 'gir',
    'edad': 4
    },
]
grupos=[]
for contador in range(0, len(vacas)):
    lista= vacas[contador]
    vaca= lista['nombre']
    grupos.append(vaca)    
    print(type(vacas))

