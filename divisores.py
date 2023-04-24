#  Hacer un algoritmo que permita ingresar un número natural luego por pantalla
# informar todos sus divisores.

numero = int(input('ingresa un nuemro natural: '))

print(f'El numero {numero} es divisible por...')
for i in range(1,numero + 1):
    if numero % i == 0:
        print(f'El numero {i}')