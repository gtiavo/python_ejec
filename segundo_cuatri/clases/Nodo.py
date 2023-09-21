
class Nodo:
    """
    Clase para representar un nodo en una lista enlazada.

    Atributos:
        dato: El dato almacenado en el nodo.
        siguiente: La referencia al siguiente nodo en la lista.
    """

    def __init__(self, datoInicial):
        """
        Inicializa un nodo con el dato proporcionado.

        Args:
            datoInicial: El dato que se almacenará en el nodo.
        """
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        """
        Obtiene el dato almacenado en el nodo.

        Returns:
            El dato almacenado en el nodo.
        """
        return self.dato
    
    def obtenerSiguiente(self):
        """
        Obtiene la referencia al siguiente nodo en la lista.

        Returns:
            La referencia al siguiente nodo.
        """
        return self.siguiente
    
    def asignarSiguiente(self, nuevoSiguiente):
        """
        Asigna la referencia al siguiente nodo en la lista.

        Args:
            nuevoSiguiente: La referencia al nuevo siguiente nodo.
        """
        self.siguiente = nuevoSiguiente



