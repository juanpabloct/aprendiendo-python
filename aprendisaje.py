valor1=input('Escribe cualquier numero')

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
print(resultado)

#Ejercicios de reto

import random
mayor='mayor'
menor='menor'
edad= random.randint(0, 40)
texto='Juanito tiene {0} años y es {1} de edad'
print(texto)
if edad >= 18:
    print(texto.format(edad, mayor))
else:
    print(texto.format(edad, menor))
