# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el
# nombre tabla-n.txt la tabla de multiplicar de ese número. Donde n es el número introducido.
# Guarde en el archivo tabla-n.txt la tabla resuelta de n.

import io 

n = int(input('ingrese la tabla de multiplicar que desea ver, (entre 1 al 10): '))

with open(f'tabla-{n}.txt', 'w') as archivo:
    for i in range(11):
        tabla = f'{n} x {i} = {n*i}' if i == 0 else f'\n{n} x {i} = {n*i}'
        archivo.write(tabla)
