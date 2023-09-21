from ListaNoOrdenada import ListaNoOrdenada
from random import randint

limite = 3
rango_datos_a_eliminar = 2
colores = ListaNoOrdenada()
nombres = ListaNoOrdenada()
numeros = ListaNoOrdenada()

for i in range(limite):
    colores.agregar(input('ingresa un color: '))
    nombres.agregar(input('ingresa un nombre: '))
    numeros.agregar(randint(1990, 2045))

print('Listado')
colores.ver()
nombres.ver()
numeros.ver()

print('Elimina datos')

for i in range(rango_datos_a_eliminar):
    colores.remover(input('ingresa el color a remover: '))

for i in range(rango_datos_a_eliminar):
    nombres.remover(input('ingresa el nombre a remover: '))

for i in range(rango_datos_a_eliminar):
    numeros.remover(int(input('ingresa el numero a remover: ')))

print('Listado')
colores.ver()
nombres.ver()
numeros.ver()

colores.anexar(input('Agregue un color al final de la lista: '))

print('Anexar')
colores.ver()

print(f'La cantidad de elementos contenidos en la lista numeros es de: {numeros.tamanio()}')