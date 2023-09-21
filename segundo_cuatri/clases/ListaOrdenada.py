from Nodo import Nodo

class ListaOrdenada:
    """
    Una clase para representar una lista ordenada.

    Attributes:
        cabeza (Nodo): El nodo principal de la lista.
    """

    def __init__(self):
        """
        Inicializa una lista ordenada vacía.
        """
        self.cabeza = None

    def estaVacia(self):
        """
        Comprueba si la lista está vacía.

        Returns:
            bool: True si la lista está vacía, False de lo contrario.
        """
        return self.cabeza == None
    
    def agregar(self, item):
        """
        Agrega un elemento a la lista en orden ascendente.

        Args:
            item: El elemento que se va a agregar a la lista.
        """
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else: 
                previo = actual
                actual = actual.obtenerSiguiente()
        temp = Nodo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)

    def tamanio(self):
        """
        Calcula el tamaño de la lista.

        Returns:
            int: El número de elementos en la lista.
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
            item: El elemento que se va a buscar en la lista.

        Returns:
            bool: True si el elemento se encuentra en la lista, False de lo contrario.
        """
        actual:Nodo = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True 
                else:
                    actual = actual.obtenerSiguiente()
        return encontrado
    
    def remover(self, item):
        """
        Elimina un elemento de la lista.

        Args:
            item: El elemento que se va a eliminar de la lista.
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
        if actual == None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())

    def ver(self):
        """
        Muestra los elementos de la lista en orden.

        Example:
            Cabeza->1->19->196->197->None
        """
        print('Cabeza', end= '->')
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end= '->')
                actual = actual.obtenerSiguiente()
        print('None')

# # Crear una instancia de ListaOrdenada
# miLista = ListaOrdenada()

# # Ejemplo de uso
# miLista.ver()
# miLista.agregar(19)
# miLista.agregar(196)
# miLista.agregar(197)
# miLista.agregar(1)

# miLista.ver()

# print(miLista.tamanio())

# miLista.remover(19)

# print(miLista.tamanio())

# miLista.ver()

# print(miLista.buscar(197))
