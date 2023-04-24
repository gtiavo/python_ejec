# Hacer un algoritmo que pida la nota de un examen (un nº real entre 0 y 10) muestre
# por pantalla la calificación de la siguiente forma:
# ● Si la nota es menor que 5 la leyenda “En suspenso”
# ● Si la nota se encuentra entre 5 inclusive y 7 sin incluir la leyenda
# “Aprobado”
# ● Si la nota se encuentra entre 7 inclusive y 9 sin incluir la leyenda
# “Notable”
# ● Si la nota se encuentra entre 9 inclusive y 10 sin incluir la leyenda
# “Sobresaliente”
# ● Si la nota es un 10 la leyenda “Matrícula de honor”.
# Terminar el algoritmo cuando se ingresa cero como nota. En caso que no, vuelve a
# pedir una nota.

nota = 1

while nota != 0:
    try:
        nota = int(input('Ingresa la nota del examen: '))
        if nota > 10 or nota < 0:
            print('debes ingresar una nota entre 0 y 10')
    except:
        print('El formato ingresado no corresponde a un numero entero, ingresa una nota del 0 al 10')
    else:
        if nota < 5 and nota > 0:
            print('En suspenso')
        if 5 <= nota < 7:
            print('Aprobado')
        if 7 <= nota < 9:
            print('Notable')
        if 9 <= nota < 10:
            print('Sobresaliente')
        if nota == 10:
            print('Matricula de honor')