# Realizar un programa que realice los ejercicios 1 y 2 utilizando la estructura with.

import io

with open('archivo_2.txt', 'w+') as archivo:
    archivo.write('Otra frase inspiradora')

with open('archivo_2.txt', 'r') as archivo:
    nombre = archivo.name
    modo = archivo.mode
    encoding = archivo.encoding
print(nombre)
print(modo)
print(encoding)