# Hacer un programa que permita leer 20 números enteros (positivos y negativos)
# distintos de cero. Mostrar el vector tal como fue ingresado y luego mostrar los
# positivos ordenados en forma decreciente y por último mostrar los negativos
# ordenados en forma creciente.

from array import array

POSICIONES = 6

miArray = array('i', [0] * POSICIONES)
positivos = []
negativos = []

for i in range(POSICIONES):
    elementos = int(input('Agrega un numero positivo o negativio: '))
    miArray[i] = elementos


for k in miArray:
    if k < 0:
        negativos.append(k)
    else:
        positivos.append(k)

n = len(positivos)

for e in range(n):
    for h in range(0, n - e - 1):
        if positivos[h] > positivos[h + 1]:
            positivos[h], positivos[h + 1] = positivos[h + 1], positivos[h]

n = len(negativos)

for s in range(n):
    for t in range(0, n - s - 1):
        if negativos[t] > negativos[t + 1]:
            negativos[t], negativos[t + 1] = negativos[t + 1], negativos[t]

print(miArray)
print(positivos)
print(negativos)