
from clases.Cola import Cola

personajes = [('Tony Stark', 'Iron Man'), ('Steve Rogers', 'Capitán América'), ('Natasha Romanoff','Black Widow'), ('Bruce Banner', 'Hulk'), ('Thor Odinson', 'Thor'), ('Clint Barton', 'Hawkeye'), ('WandaMaximoff', 'Scarlet Witch'), ('Vision', 'Vision'), ('Peter Parker', 'Spider-Man'), ('Carol Danvers', 'CapitanaMarvel'), ('Nick Fury', 'Nick Fury'), ('Loki Laufeyson', 'Loki'), ('Phil Coulson', 'Phil Coulson'), ('Maria Hill','Maria Hill'), ('James Rhodes', 'War Machine'), ('Sam Wilson', 'Falcon'), ('Peggy Carter', 'PeggyCarter'), ('Bucky Barnes', 'Winter Soldier'), ('Thanos', 'Thanos'), ('Gamora', 'Gamora'), ('Nebula','Nebula'), ('Drax el Destructor', 'Drax el Destructor'), ('Groot', 'Groot'), ('Rocket Raccoon', 'RocketRaccoon'), ('Peter Quill', 'Star-Lord')]

superHeroes = Cola()

for i in personajes:
    superHeroes.encolar(i)
 
print("{:<8} {:<20}".format('Personaje', 'Actor'))


for i in superHeroes.mostrar():
    Personaje, Actor = i
    print("{:<8} {:<20}".format(Personaje, Actor))