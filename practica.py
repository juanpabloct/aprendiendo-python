from typing import TextIO


comida=['Helado', 'pollo', 'Pescado']
print(comida)

comida_favorita=input('Escribe tu comida Favorita: ')
""" print('Desde aca inicia el for')
for cuentame in comida:
    if comida_favorita == cuentame:
        print(f'Me gusta mucho el {comida_favorita}')
    else:
        print(f'No tenemos {comida_favorita}') """
i=1
text='hello'
""" for zeta  in range(comida_favorita):
    print('Hello' + str(zeta)) """

for x in text:
    print(x + str(i))
    i+=1