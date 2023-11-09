# Crear un programa que abra el fichero editado anteriormente y muestre el estado del fichero,
# el modo en el que fue abierto, el nombre y la codificación de caracteres del mismo.

import io

archivo = open('ejemplo_nuevo.txt', 'r')

nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding

archivo.close()

print(nombre)
print(modo)
print(encoding)