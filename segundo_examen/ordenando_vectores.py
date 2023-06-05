# Escribir un programa que lea tres números y los guarde en un vector. A
# continuación, los ordenará y guardará los valores ordenados en otro vector.
# Finalmente sacará ambos vectores por la pantalla

from array import array

POSICIONES = 3

# miArray = array('i', [0] * POSICIONES)
miArray = []
miOtroArray = array('i', [0] * POSICIONES)
arrayOrdenado = []

for i in range(POSICIONES):
    elementos = int(input('Ingresa un numero entero: '))

    # miArray[i] = elementos
    miArray.append(elementos)

    

for k in range(POSICIONES):
    for e in range(0, POSICIONES - k - 1):
        if miArray[e] > miArray[e + 1]:
            miArray[e], miArray[e + 1] = miArray[e + 1], miArray[e]


print(miArray)


