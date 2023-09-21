class Persona:
    nombre:str
    edad:int

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayor_de_edad(self):
        if self.edad < 17:
            return f'{self.nombre} es menor de edad'
        else:
            return f'{self.nombre} es mayor de edad'
        

gustavo = Persona('Gustavo', 16)

print(gustavo.mayor_de_edad())