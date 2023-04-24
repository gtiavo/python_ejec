# Hacer un algoritmo que permita ingresar por pantalla números naturales al finalizar
# informar:
# ● ¿Cuántos están entre el 50 y 75, ambos inclusive?
# ● ¿Cuántos mayores de 80?
# ● ¿Cuántos menores de 30?
# El algoritmo debe finalizar cuando se ingresa el número 0.

numero = 1
entre50_75 = 0
mayores_80 = 0
menores_30 = 0

while numero != 0:
    
    numero = int(input('Ingresa un numero natural: '))
    if numero < 0:
        print('El numero ingresado debe ser positivo')

    if 50 <= numero <= 75:
        entre50_75 += 1
    if numero > 80:
        mayores_80 += 1
    if numero < 30 and numero > 0:
        menores_30 += 1

print(f"Ingresaste {entre50_75} {'numeros' if entre50_75 > 1 else 'numero'} entre 50 y 75")
print(f"Ingresaste {mayores_80} {'numeros' if mayores_80 > 1 else 'numero'} mayores a 80")
print(f"Ingresaste {menores_30} {'numeros' if menores_30 > 1 else 'numero'} menores a 30")
