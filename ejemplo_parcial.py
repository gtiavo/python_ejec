# Escribir un algoritmo que permita cargar un vector de 10 numeros enteros (positivos o negativos)
#  entre -100 y 100. No debe aceptar valores fuera de este intervalo, 
# al finalizar la carga se debe imprimir por pantalla el resultado de la misma.
#  Luego de la carga se debe proporcionar un menú (debe estar en un ciclo) con las siguientes opciones:

# Realizar la sumatoria de los valores positivos pares 
# Realizar el conteo de los valores negativos
# Calcular el promedio de todos los valores ingresados
# Obtener el menor de todos los números ingresados
# Obtener el número que más veces se repite en el vector
# Generar un vector destino y copiar (en las mismas posiciones)
#  los valores positivos de las posiciones impares, en el resto copiar el valor 0.
# Salir del programa

from array import array

RANGO = 10
LIMIT_SUP = 100
LIMIT_INF = -100

numeros = array('i', range(RANGO))
numeros_copia = array('i', range(RANGO))

def is_int(valor: str):
    true_or_not = False
    try:
        int(valor)
        true_or_not = True 
    except Exception as e:
        true_or_not = False
    return true_or_not

def esta_dentro_de_los_limites(numero:int):
    return LIMIT_SUP >= int(numero) >= LIMIT_INF

def intro_input(message:str):
    numero = input(message)
    if is_int(numero):
        numero = int(numero)
        if not esta_dentro_de_los_limites(numero):
                print('Debes ingresar un numero entre los rangos premitidos')
        else:
            return numero
    else:
        print(f'{numero} es un valor incorrecto, intenta nuevamente')

def imprir_vector(numeros:array):
    print('')
    for n in range(RANGO):
        if n == 0:
            num_print = f'[{numeros[n]},'
        elif n == RANGO - 1:
            num_print = f'{numeros[n]}]'
        else:
            num_print = f'{numeros[n]},'
        print(num_print, end='')
    print('')

def menu():
    print('')
    print('------------ MENU -------------')
    print('')
    print('1 - Sumatoria de los valores positivos pares')
    print('2 - Conteo de los valores negativos')
    print('3 - Promedio de todos los valores ingresados')
    print('4 - El menor de todos los números ingresados')
    print('5 - El número que más veces se repite en el vector')
    print('6 - Un vector destino y copiar (en las mismas posiciones) los valores positivos de las posiciones impares, en el resto copiar el valor 0')
    print('7 - Salir')
    print('')

def suma_positivos_def(numeros):
    suma_positivos = 0
    for numero in numeros:
        if numero > 0:
            suma_positivos += numero
    print(f'La suma de numeros positivos es de {suma_positivos}')
    print('')
    input('Presiona enter para continuar...')

def cantidad_num_negativos(numeros):
    count = 0
    for numero in numeros:
        if numero < 0:
            count += 1
    print(f'La cantidad de numeros negativos ingresados es de {count}')
    input('Presiona enter para continuar...')

def el_promedio_num(numeros):
    suma_numeros = 0
    for n in numeros:
        suma_numeros += n
    promedio = suma_numeros / RANGO
    print(f'El promedio de todos los numeros ingresados es de: {promedio}')
    input('Presiona enter para continuar...')

def el_num_menor(numeros):
    el_menor = None
    for n in numeros:
        if el_menor == None:
            el_menor = n
        elif n < el_menor:
            el_menor = n
    print(f'El menor de los numeros ingresados es: {el_menor}')
    input('Presiona enter para continuar...')

def el_num_mas_repetido(numeros):
    el_mas_repetido = None
    cantidad_veces_repetido = 0
    for n in numeros:
        count = 0
        for i in numeros:
            if n == i:
                count += 1
        if count > 1 and cantidad_veces_repetido < count:
            el_mas_repetido = n
            cantidad_veces_repetido = count
    print(f'El numero ingresado que mas veces se repite en el vector es: {el_mas_repetido}')
    input('Presiona enter para continuar...')

def opcion6(numeros):
    for i in range(RANGO):
        if i % 2 != 0 and numeros[i] > 0:
            numeros_copia[i] = numeros[i]
        else:
            numeros_copia[i] = 0
    print(numeros)
    print(numeros_copia)
    input('Presiona enter para continuar...')
    
def swich(opcion):
    if opcion == 1:
       suma_positivos_def(numeros)
    elif opcion == 2:
        cantidad_num_negativos(numeros)
    elif opcion == 3:
        el_promedio_num(numeros)
    elif opcion == 4:
       el_num_menor(numeros)
    elif opcion == 5:
       el_num_mas_repetido(numeros)
    elif opcion == 6:
        opcion6(numeros)
    elif opcion == 7:
        print('Gracias por usar el programa')
    else:
        print(f'La opcion {opcion} no es valida, selecciona otra.')


for i in range(RANGO):
    numero = ""
    while not (is_int(numero) and esta_dentro_de_los_limites(numero)):
        numero = intro_input(f'{i + 1} - Ingresa un numero entero del -100 al 100: ')
    numeros[i] = numero

imprir_vector(numeros)


opcion = 0

while opcion != 7:
   
    menu()
    opcion = int(input('Selecciona una opcion (1-7): '))
    print('')
   
    swich(opcion)

