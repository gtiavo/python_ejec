class Alumno:
    nombre = ''
    nota = 0

    # @property
    # def nombre(self):
    #     return self.nombre
    
    # @nombre.setter
    # def nombre(self, nombre):
    #     self.nombre = nombre

    # @property
    # def nota(self):
    #     return self.nota
    
    # @nota.setter
    # def nota(self, nota):
    #     self.nota = nota

    def __str__(self):
        return(f'''{self.nombre} - {self.nota}  ''')
        



alumno_1 = Alumno()

alumno_1.nombre = 'Gustavo'
alumno_1.nota = 10

print(alumno_1)
