# Escribir un programa que permita cargar un vector de 10 números y luego muestre un menú con las siguientes opciones:

# Promedio de todos
# Mayor de los primos
# Cantidad de impares
# Menor de todos
# Salir del programa
# El menú se debe ejecutar en un ciclo siempre y cuando no se seleccione la opción "5 Salir del programa"


from array import array

POSICIONES = 5

miArray = array('i', range(POSICIONES))

print('---BIENVENIDOS A MI PROGRAMA---')

for i in range(POSICIONES):
    miArray[i] = int(input(f'{i + 1} - Ingresa { "un numero: " if i == 0 else "otro numero: "}'))

opcion = 0

while opcion != 5:

    print('')
    print('Selecciona una opcion para cotinuar: ')
    print('1 - Si desea conocer el promedio de los numeros ingresados, ingrese 1')
    print('2 - Si desea conocer el mayor de los primos de los numeros ingresados, ingrese 2')
    print('3 - Si desea conocer la cantidad de impares de los numeros ingresados, ingrese 3')
    print('4 - Si desea conocer el menor de todos los numeros ingresados, ingrese 4')
    print('5 - Si desea salir del programa, ingrese 5')
    print('')
    opcion = int(input('Ingrese una opcion y presione enter: '))
    print('')

    if opcion == 1:

        suma = 0
        for numero in miArray:
            suma += numero
        promedio = suma / POSICIONES
        print(f'El promedio de los numeros ingresados es de {promedio}')
        input('Presione enter para continuar...')

    elif opcion == 2:

        primos = []
        el_mayor_primo = 0
        for numero in miArray:
            count = 0
            for divisor in range(1, numero):
                if numero % divisor == 0:
                    count += 1        
            if count < 2 and count > 0:
                    primos.append(numero)    
        for i in primos:
            if i > el_mayor_primo: 
                el_mayor_primo = i
        print(f'El mayor de los numeros primos ingresados es el: {el_mayor_primo}')
        print('')
        input('Presione enter para continuar...')

    elif opcion == 3:

        count = 0
        for i in miArray:
            if i % 2 != 0:
                count += 1
        print(f'La cantidad de numeros impares ingresados es de: {count}')
        input('Presione enter para continuar...')

    elif opcion == 4:

        el_menor = ''
        for i in miArray:
            if el_menor == '':
                el_menor = i
            elif i < el_menor:
                el_menor = i
        print(f'El numero menor ingresado es el: {el_menor}')
        input('Presione enter para continuar...')

    elif opcion == 5:

        print('Gracias por utilizar el programa, adios')
        
    else:
        print('El numero ingresado no corresponde a un opcion valida, intenta con otra')