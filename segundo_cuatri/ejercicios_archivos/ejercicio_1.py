# Crear un programa que abra un fichero en modo lectura y escritura, si no existe lo creará, y
# añadir la frase ‘Este es el ejercicio 1’.

import io

frase = 'Este es el ejercicio 1'

archivo = open('ejemplo_nuevo.txt', 'w+')
archivo.write(frase)
archivo.close()
