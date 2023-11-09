# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la
# tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por
# pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import io

n = int(input('ingrese un numero entre 1 y 10: '))

try:
    with open(f'tabla-{n}.txt', 'r') as archivo:
        print(archivo.read())
except:
    print(f'La tabla del {n} no existe')