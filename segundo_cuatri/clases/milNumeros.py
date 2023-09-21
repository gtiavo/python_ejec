from ListaOrdenada import ListaOrdenada
from random import randint

rango = 1000
numeros = ListaOrdenada()

for i in range(rango):
    numeros.agregar(randint(5, 300))


numeros.ver()