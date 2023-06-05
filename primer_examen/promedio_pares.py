# Diseñar un algoritmo que permita ingresar por pantalla 10 números naturales.
# Calcular el promedio de los números pares. Luego mostrar por pantalla el
# resultado.

numeros_pares = 0
cantidad_numeros = 0
for i in range(1, 11):
    numero = 0
    while numero <= 0:
        numero = int(input(f'{i} - Agrega {"un numero" if i == 1 else "otro numero" } natural: '))
        if numero <= 0:
            print('El numero ingresado debe ser un numero natural')
    if numero % 2 == 0:
        numeros_pares += numero
        cantidad_numeros += 1

promedio = numeros_pares / cantidad_numeros


print(f'El promedio de numeros pares ingresados es de {round(promedio, 2)}')
