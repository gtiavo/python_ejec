from Nodo import Nodo 

class ListaNoOrdenada:
    """
    Clase para representar una lista enlazada no ordenada.

    Atributos:
        cabeza: La referencia al primer nodo en la lista.
    """

    def __init__(self):
        """
        Inicializa una lista enlazada vacía.
        """
        self.cabeza = None

    def estaVacia(self):
        """
        Verifica si la lista está vacía.

        Returns:
            True si la lista está vacía, False en caso contrario.
        """
        return self.cabeza == None
    
    def agregar(self, item):
        """
        Agrega un elemento al principio de la lista.

        Args:
            item: El elemento que se agregará a la lista.
        """
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def tamanio(self):
        """
        Obtiene el número de elementos en la lista.

        Returns:
            El número de elementos en la lista.
        """
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.obtenerSiguiente()
        return contador
    
    def buscar(self, item):
        """
        Busca un elemento en la lista.

        Args:
            item: El elemento que se desea buscar.

        Returns:
            True si el elemento se encuentra en la lista, False en caso contrario.
        """
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    
    def remover(self, item):
        """
        Elimina un elemento de la lista.

        Args:
            item: El elemento que se desea eliminar.
        """
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())

    def ver(self):
        """
        Muestra los elementos de la lista en orden.

        La salida se muestra en el formato "Cabeza -> elemento1 -> elemento2 -> ... -> None".
        """
        print('Cabeza', end= '->')
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end= '->')
                actual = actual.obtenerSiguiente()
        print('None')

    def buscarIndice(self, indice):
        """
        Busca un elemento en la lista por su índice.

        Args:
            indice: El índice del elemento que se desea buscar.

        Returns:
            El elemento encontrado en el índice especificado o 'None' si el índice es inválido.
        """
        actual = self.cabeza
        posicion = 0
        while posicion != indice:
            actual = actual.obtenerSiguiente()
            posicion += 1
        
        if actual == None:
            return 'None'
        else:
            return actual.dato
        
    def anexar(self, item):
        """
        Agrega un elemento al final de la lista.

        Args:
            item: El elemento que se agregará al final de la lista.
        """
        temp = Nodo(item)
        actual = self.cabeza
        previo = None
        while actual != None:
            previo = actual
            actual = actual.obtenerSiguiente()
        if previo == None:
            self.agregar(item)
        else:
            previo.asignarSiguiente(temp)


# Ejemplo de uso de la lista enlazada
miLista = ListaNoOrdenada()

miLista.ver()
miLista.agregar(19)
miLista.agregar(196)
miLista.agregar(197)

miLista.ver()

print(miLista.tamanio())

miLista.remover(196)

print(miLista.tamanio())

miLista.anexar(1111)

miLista.ver()

print(miLista.buscar(197))
print(miLista.buscarIndice(2))