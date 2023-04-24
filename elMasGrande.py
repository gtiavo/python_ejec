# Hacer un algoritmo donde se ingresan 10 números enteros. Mostrar por pantalla el
# número más grande ingresado y en qué posición se ingresó.

numeros = []
mayor = 0

try:
    for i in range(1, 11):
        numero = int(input(f"{f'{i} - Agrega un numero: ' if i == 1 else f'{i} - Agrega otro numero: '}"))
        numeros.append(numero)
except:
    print('El numero ingresado no tiene un formato idoneo')
else:
    for n in numeros:
        if mayor < n:
            mayor = n

    posicionDelMayor = numeros.index(mayor) + 1 

    print(f'El numero mayor ingresado es {mayor}, y se encuentra en la posicion: {posicionDelMayor}' )

    


