from clases.Pila import Pila
import os

activo = True

nombres = Pila()

while activo:

    os.system('cls')

    print('Menu')
    print('1 - Apilar nombre')
    print('2 - Desapilar nombre')
    print('3 - Salir')

    try:
        option = int(input('\nIngrese una de las opciones(1 - 2 - 3) y presione enter: '))

        if option == 1:

            os.system('cls')
            start = True
            while start:

                nombre = input('ingrese un nombre o solo presione enter para salir: ').lstrip().rstrip().capitalize()
        
                if len(nombre) > 0:
                    nombres.apilar(nombre)
                else:
                    start = False

            input('\nPreione enter para continuar')
            
        elif option == 2:

            os.system('cls')
            nombres.desapilar()
            input('\nPreione enter para continuar')

        elif option == 3:

            os.system('cls')
            activo = False
            if nombres.vacia():
                print('\nLa lista de nombres esta vacia')
            else:
                nombres.mostrar()
            print('\nPrograma terminado')

        else:
            print(f'\nLa opcion {option} no es valida, intente nuevamente')
            input('\nPreione enter para continuar')


    except:
        print('La opcion ingresada no tiene un formato valido')
        input('Presiona enter para continuar')


    

    