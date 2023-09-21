class Cola:
    def __init__(self):
        self.lista = []

    def encolar(self, item):
        self.lista.append(item)
        print(f'\nElemento {item} encolado, lista actualizada: {self.lista}')

    def vacia(self):
        if len(self.lista) == 0:
            return True
        else: 
            False

    def desencolar(self):
        if self.vacia():
            print('\n No se puede desencolar, la lista esta vacia')
        else:
            print(f'\n Elemento {self.lista.pop(0)} desencolado, lista actualizada: {self.lista}')
    
    def tamanio(self):
        print(f'\n La cola tiene {len(self.lista)} elemetos')

    def mostrar(self):
        return self.lista