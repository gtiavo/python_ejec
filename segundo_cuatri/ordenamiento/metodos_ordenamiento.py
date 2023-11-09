
#****************************************************
def ordenamientoRapido(unaLista):
    ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
    if primero<ultimo:
        puntoDivision = particion(unaLista,primero,ultimo)
        ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
        ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)

def particion(unaLista,primero,ultimo):
    valorPivote = unaLista[primero]
    marcaIzq = primero+1
    marcaDer = ultimo
    hecho = False
    while not hecho:
       # print(f"{unaLista} Pivote:{valorPivote} posiciones Izq {marcaIzq}= {unaLista[marcaIzq]} ultimo {marcaDer}={unaLista[marcaDer]}")
        while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1

        while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer -1

        if marcaDer < marcaIzq:
            hecho = True
        else:
            unaLista[marcaIzq],unaLista[marcaDer] =  \
            unaLista[marcaDer],unaLista[marcaIzq]
    
    unaLista[primero], unaLista[marcaDer] =  \
    unaLista[marcaDer], unaLista[primero]
    return marcaDer

#****************************************************

def ordenamientoBurbuja(unaLista2):
    for numPasada in range(len(unaLista2)-1,0,-1):
        for i in range(numPasada):
            if unaLista2[i]>unaLista2[i+1]:
                temp = unaLista2[i]
                unaLista2[i] = unaLista2[i+1]
                unaLista2[i+1] = temp
    return unaLista2

#****************************************************
def ordenamientoPorSeleccion(unaLista):
    for llenar in range(len(unaLista)-1,0,-1):
        pMay=0
        for ubic in range(1,llenar+1):
            if unaLista[ubic]>unaLista[pMay]:
                pMay = ubic 
        unaLista[llenar], unaLista[pMay] = unaLista[pMay] , unaLista[llenar]
    return unaLista

#****************************************************

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1