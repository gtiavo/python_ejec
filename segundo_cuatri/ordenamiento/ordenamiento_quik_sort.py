import time

nombres_qs = ['Matilde', 'Jonathan', 'Inés', 'Catalina', 'Joaquím', 'Consuelo', 'Rocío', 'Álvaro', 'Macario', 'Lidia', 'Jeremías', 'Clara', 'Abrahán', 'Dario', 'Atanasio', 'Anastasia', 'Ascensión', 'Octavio', 'Borja', 'Elvira', 'Clotilde', 'Rigoberto', 'Gustavo', 'Benedicto', 'Epifanía', 'Elisa', 'Ananías', 'Evaristo', 'José', 'Calixto', 'Maximiliano', 'Eugenio', 'Esteban', 'Natividad', 'Diego', 'Antonia', 'Cristóbal', 'Onésimo', 'Rebeca', 'Eliseo', 'Jorge', 'Cayo', 'Lourdes', 'Aránzazu', 'Aresio', 'Oriol', 'Lorenzo', 'Severino', 'Mauricio', 'Sergio', 'Claudia', 'Aitor', 'Hugo', 'Otilia', 'Manuel', 'Marina', 'Blas', 'Gonzalo', 'Ricardo', 'Albina', 'Paula', 'Tadeo', 'Rafael', 'Demócrito', 'Raúl', 'Martín', 'Anna', 'Luz', 'Rosendo', 'Teófanes', 'Fulgencio', 'Marcelo', 'Jesús', 'Dorotea', 'Amelia', 'Úrsula', 'Samuel', 'Beltrán', 'Primo', 'Julián', 'Ignacio', 'Odón', 'Basileo', 'Noelia', 'Eusebio', 'Amparo', 'Esiquio', 'Félix', 'Leoncio', 'Leopoldo', 'Sandra', 'Oswaldo', 'Porfirio', 'Guillermo', 'Víctor', 'Ambrosio', 'Oscar', 'Reinaldo', 'Heriberto', 'Germán', 'Pío', 'Amaro', 'Silvia', 'Aristides', 'Nicolás', 'Juvenal', 'Valentín', 'Ariadna', 'Casio', 'Simeón', 'Bárbara', 'Rubén', 'Valeriano', 'Julio', 'Remedios', 'Virgilio', 'Adelaida', 'Priscila', 'María', 'Antero', 'Magdalena', 'Teodosia', 'Baltasar', 'Ezequiel', 'Abel', 'Roque', 'Jerónimo', 'Verónica', 'Jacinto', 'Hilarión', 'Ciro', 'Carolina', 'Jaume', 'Cándida', 'Ángel', 'Emilia', 'Emilio', 'Faustino', 'Carmelo', 'Ismael', 'Roberto', 'Adón', 'Constancio', 'Vladimiro', 'Ifigenia', 'Victorio', 'Mariano', 'Patricia', 'Dolores', 'Albert', 'Feliciano', 'Agustín', 'Vicente', 'Guzmán', 'Manuela', 'Javier', 'Cirino', 'Francesc', 'Arnaldo', 'Antonio', 'Laureano', 'Begoña', 'Raquel', 'Raimundo', 'Alfonso', 'Moisés', 'Dimas', 'Susana', 'Iván', 'Salomé', 'Concepción', 'Leandro', 'Trinidad', 'Almudena', 'Celia', 'Liduvina', 'León', 'Fernando', 'Segismundo', 'Poncio', 'Milagros', 'Gregorio', 'Isabel', 'Eugenia', 'Luisa', 'Toribio', 'Oto', 'Pablo', 'Abdón', 'Araceli', 'Tomas', 'Carlos', 'Fátima', 'Benjamín', 'Gabriel', 'Lorena', 'Amadeo', 'Renato', 'Felipe', 'Mercedes', 'Timoteo', 'Virginia', 'Blanca', 'Ruperto', 'Sansón', 'Andrea', 'Román', 'Marc', 'Mónica', 'Patricio', 'Francisco', 'Isaías', 'Inocencio', 'Pancracio', 'Tobías', 'Absalón', 'Ángela', 'Velerio', 'Alfredo', 'Adela', 'Josep', 'Fermín', 'Salvador', 'Mar', 'Juan', 'Conrado', 'Honorato', 'Beatriz', 'Santiago', 'Esdras', 'Gloria', 'Fabio', 'Isidro', 'Josué', 'Aurora', 'Héctor', 'Tito', 'Alonso', 'Teófila', 'Justino', 'Yolanda', 'Narciso', 'Enrique', 'Ildefonso', 'Lázaro', 'Leocadia', 'Efrén', 'Josefa', 'Victoria', 'Jacobo', 'Damián', 'Nicodemo', 'Dacio', 'Carina', 'Bartolomé', 'Camilo', 'Mario', 'Alipio', 'Rosa', 'Ubaldo', 'Lucas', 'Marcial', 'Donato', 'Sebastián', 'Purificación', 'Lucano', 'Pascual', 'Acacio', 'Gerardo', 'Rodrigo', 'Zaqueo', 'Casimiro', 'Irene', 'Mohamed', 'Jordi', 'Daniel', 'Rita', 'Benigno', 'Ramiro', 'Heliodoro', 'Hildegarda', 'Sonia', 'Nemesio', 'Gertrudis', 'Erico', 'Edgar', 'Elena', 'Bonifacio', 'Venancio', 'Wilfredo', 'Sara', 'Isaac', 'Josafat', 'Ernesto', 'Alejandro', 'Urbano', 'Benito', 'Columba', 'Marcelino', 'Margarita', 'Noé', 'Melchor', 'Rosalia', 'Julia', 'Humberto', 'Laura', 'Columbano', 'Lucía', 'Vanesa', 'Zacarías', 'Alberto', 'Áurea', 'Teresa', 'Leonardo', 'Domingo', 'Sofía', 'Homero', 'Orestes', 'Romualdo', 'Juana', 'Bernarda', 'Cesáreo', 'Encarnación', 'Fidel', 'Rufo', 'Joaquín', 'Casiano', 'Lino', 'Tomás', 'Cleofás', 'Guadalupe', 'Adolfo', 'Alba', 'Anatolio', 'Miguel', 'Nuria', 'Eva', 'Genoveva', 'Belén', 'Jonás', 'Óscar', 'Inmaculada', 'Marta', 'Alejo', 'Natalia', 'Siro', 'Marciano', 'Petronila', 'Edmundo', 'Bernabé', 'Josefina', 'Joan', 'Xavier', 'Lucrecia', 'Adán', 'Aurelio', 'Cristina', 'Adrián', 'Nicomedes', 'Fabiola', 'Oseas', 'Bernardo', 'Mateo', 'Tarsicio', 'Salvio', 'Andrés', 'Probo', 'Eduardo', 'Eduvigis', 'Nazario', 'Cosme', 'Nicanor', 'Jaime', 'Sixto', 'Matías', 'Ester', 'Adalberto', 'Cirilo', 'Ramón', 'Artemio', 'Abelardo', 'Norberto', 'Ángeles', 'Miqueas', 'Esther', 'Montserrat', 'César', 'Fortunato', 'Cipriano', 'Asunción', 'Celso', 'Esperanza', 'Nieves', 'Aureliano', 'Salomón', 'Aarón', 'Baldomero', 'Colombo', 'Ireneo', 'Celina', 'Federico', 'Aurelia', 'Soledad', 'Ceferino', 'Gisela', 'Heraclio', 'Anselmo', 'Leonor', 'Alejandra', 'Francisca', 'Aquiles', 'Gema', 'Pedro', 'Rosario', 'Alicia', 'Míriam', 'Joel', 'Carmen', 'Honorio', 'Fausto', 'Marcos', 'Balduino', 'David', 'Eulalia', 'Luis', 'Cayetano', 'Arcadio', 'Elías', 'Rogelio', 'Vicenta', 'Teodora', 'Facundo', 'Daciano', 'Fabián', 'Bruno', 'Augusto', 'Dámaso', 'Guido', 'Ladislao', 'Cristian', 'Arturo', 'Aniano', 'Pilar', 'Constantino', 'Vidal', 'Claudio', 'Olga', 'Jacob', 'Simón', 'Cecilia', 'Victorino', 'Luciano', 'Ana', 'Godofredo', 'Emiliano']



def ordenamientoRapido(lista):
    inicio = time.time()
    ordenamientoRapidoAuxiliar(lista, 0, len(lista) - 1)
    final = time.time()
    return final -inicio


def ordenamientoRapidoAuxiliar(lista,primero,ultimo):
    if primero < ultimo:
        puntoDeVision = particion(lista, primero, ultimo)
        ordenamientoRapidoAuxiliar(lista, primero, puntoDeVision - 1)
        ordenamientoRapidoAuxiliar(lista, puntoDeVision + 1, ultimo)

def particion(lista, primero,ultimo):
    valorPivote = lista[primero]
    marcaIzq = primero + 1
    marcaDer = ultimo
    hecho = False

    while not hecho:
        while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
            marcaIzq += 1
        while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer -= 1

        if marcaDer < marcaIzq:
            hecho = True
        else:
            lista[marcaIzq], lista[marcaDer] = lista[marcaDer], lista[marcaIzq]

    lista[primero], lista[marcaDer] = lista[marcaDer], lista[primero]
    return marcaDer


tiempo = ordenamientoRapido(nombres_qs)

print(nombres_qs)
print(tiempo)

