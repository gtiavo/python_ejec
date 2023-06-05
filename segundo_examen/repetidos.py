from array import array

POSICIONES = 5

numeros = array('i', range(POSICIONES))
numeros_copia = array('i', range(POSICIONES))

def is_num(entrada:str):
    try:
        int(entrada)
        return True
    except:
        return False

for i in range(POSICIONES):
    numero = ''
    while not(is_num(numero)):
        numero = input(f'{i + 1} - Ingresa un numero entero: ')
        if not is_num(numero):
            print('El formato no espermitido')

    numeros[i] = int(numero)

for n in range(POSICIONES):
    count = 0
    for h in numeros:
        if numeros[n] == h:
            count += 1
    if count > 1:
        numeros_copia[n] = 0
    else:
        numeros_copia[n] = numeros[n]

print(numeros)
print(numeros_copia)
