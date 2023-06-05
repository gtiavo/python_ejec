# Desarrollar un algoritmo que permita la carga de un vector de 10 posiciones.
# Generar una rutina que transcriba el contenido del vector a otro vector en orden
# inverso.

from array import array

POSICIONES = 10

miArray = array('i', [1,2,3,4,5,6,7,8,9,10])
miOtroArray = array('i', [0] * POSICIONES)


for i in miArray:
   for j in miOtroArray:
      miOtroArray[POSICIONES - i] = i

print(miArray)
print(miOtroArray)

