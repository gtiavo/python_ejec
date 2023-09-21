import random
import os
from clases.Pila import Pila 

capacidad = 5
vidas = 5
listaNumAleatorios = Pila()

activo = True
for i in range(capacidad):
    listaNumAleatorios.apilar( random.randint(10, 99))

listaNumAleatorios.mostrar()

while activo:

    input('Prsione enter para continuar')
    os.system('cls')

    if listaNumAleatorios.vacia():
        activo = False
        print('**** Gano el Juego ****')
        print('Juego terminado')
    else:
        if vidas == 0:
            print('**** Perdio el Juego ****')
            print('Juego terminado')
            activo = False

        else:   
            desapilarNum = int(input(f'Ingrese el numero a desapilar, tiene {vidas} oportunidase: '))
            if listaNumAleatorios.lista[-1] == desapilarNum:
                listaNumAleatorios.desapilar()
                print(f'Acerto, numero desapilado: {desapilarNum}')
            else:
                vidas = vidas -1 
                print(f'Fallo, le quedan {vidas} oportunidades')
    
    



