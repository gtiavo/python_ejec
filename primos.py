
numero = int(input('ingresa un numero: '))

contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

if contador > 2:
    print(f'El numero {numero} no es primo')
else:
    print(f'El numero {numero} es primo')