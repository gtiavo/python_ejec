import random


lista =[]

for i in range(10000):
    lista.append(random.randint(1, 1000))



def ordenamientoPorSeleccion(unaLista):
    for llenar in range(len(unaLista)-1,0,-1):
        pMay=0
        for ubic in range(1,llenar+1):
            if unaLista[ubic]>unaLista[pMay]:
                pMay = ubic 
        unaLista[llenar], unaLista[pMay] = unaLista[pMay] , unaLista[llenar]
    return unaLista



ordenamientoPorSeleccion(lista)

print(lista)
print(len(lista))
lista = set(lista)
print(lista)
print(len(lista))
