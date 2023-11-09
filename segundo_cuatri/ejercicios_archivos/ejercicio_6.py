# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con
# la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el
# fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import io

n = int(input('ingrese una tabla de multiplicar del 1 al 10: '))
m = int(input('ingrese desde que linea quiere empezar a ver del 1 al 10: '))

try:
    with open(f'tabla-{n}.txt', 'r') as archivo:
        lineas = archivo.readlines()
        print(lineas[m])
except:
    print(f'La tabla del {n} no existe')