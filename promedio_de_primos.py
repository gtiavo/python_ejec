# Desarrollar un algoritmo que permita ingresar 10 números naturales, 
# luego informar por pantalla el promedio de los números primos ingresados.
# En caso de que no se hayan ingresado números primos mostrar el mensaje "No se ingresaron números primos"


cantidad_numeros_primos = 0
numeros_primos = 0
for i in range(1, 11):
    numero = 0
    while numero <= 0:
        numero = int(input(f'{i} - Ingresa {"un numero" if i < 1 else "otro numero"} natural: '))
        if numero <= 0:
            print('EL numero ingresado debe ser un numero natural')

    contador = 0
    for n in range(1, numero + 1):
        if numero % n == 0:
            contador += 1
    if contador == 2:
        cantidad_numeros_primos += 1
        numeros_primos += numero

promedio_numeros_primos = 0
if cantidad_numeros_primos != 0:
    promedio_numeros_primos = numeros_primos/cantidad_numeros_primos

print(numeros_primos, cantidad_numeros_primos)
if promedio_numeros_primos == 0:
    print('No ah ingresado numeros primos')
else:
    print(f'El promedio de numeros primos ingresados es de: {round(promedio_numeros_primos, 2)}')