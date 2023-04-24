# Hacer un algoritmo donde se Ingresan los siguientes datos de 5 alumnos:
# ● nota (float),
# ● Edad = (entero)
# Mostrar por pantalla la mejor nota y qué edad tenía

import os

edad:int = 0
mejorNota = 0
edad_por_mejor_nota = 0

for i in range(1, 6):
    nota:float = -1
    while nota < 0 or nota > 10:
        print(f'INGRESE LOS DATOS DEL {i}° Alumno')
        nota = float(input('ingresa la nota obtenida: '))
        if nota < 0 or nota > 10:
            print('La nota debe ser entre 1 y 10')
    edad = int(input('Ingresa tu edad por favor: '))
    os.system('cls')
    if nota > mejorNota:
        mejorNota = nota
        edad_por_mejor_nota = edad

print(mejorNota, edad_por_mejor_nota)

