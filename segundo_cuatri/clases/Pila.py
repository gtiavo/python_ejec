class Pila:
    def __init__(self):
        self.lista = []

    def apilar(self, item):
        self.lista.append(item)
        print(f'\nElemento {item} apilado, lista actualizada: {self.lista}')

    def vacia(self):
        if len(self.lista) == 0:
            return True
        else: 
            False

    def desapilar(self):
        if self.vacia():
            print('\nNo se puede desapilar, la lista esta vacia')
        else:
            print(f'\nElemento {self.lista.pop()} desapilado, lista actualizada: {self.lista}')
    
    def tamanio(self):
        print(f'\nLa pila tiene {len(self.lista)} elemetos')

    def mostrar(self):
        for i in range(1 , len(self.lista) + 1):
            print(f'[ {self.lista[- i]} ]')
    
    def listaCompleta(self):
        return self.lista