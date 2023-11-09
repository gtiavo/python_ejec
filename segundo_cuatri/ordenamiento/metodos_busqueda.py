def busqueda_in(lista,item):
    if item in lista:
        return True
    return False 

# ***************************************************
def busquedaSecuencial(Lista, item):
    pos = 0
    while pos < len(Lista):
        if Lista[pos] == item:
            return True
        else:
            pos = pos+1
    
    return False
# ***************************************************
def busquedaBinaria(Lista, item):
    #Recuerde que la lista debe estar previamente ordenada
    primero = 0
    ultimo = len(Lista)-1

    while primero<=ultimo:      

        puntoMedio = (primero + ultimo)//2
        #print(Lista[puntoMedio])

        if Lista[puntoMedio] == item:
            return puntoMedio
       # else:
        if item < Lista[puntoMedio]:
            ultimo = puntoMedio-1
        else:
            primero = puntoMedio+1
    
    return False
# ***************************************************
def busquedaBinariaRecursiva(unaLista, item):
    #Recuerde que la lista debe estar previamente ordenada
    if len(unaLista) == 0:
        return False
    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio]==item:
          return True
        else:
          if item<unaLista[puntoMedio]:
            return busquedaBinaria(unaLista[:puntoMedio],item)
          else:
            return busquedaBinaria(unaLista[puntoMedio+1:],item)

