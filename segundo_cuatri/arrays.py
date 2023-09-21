
# vector = []
# posiciones = 10

# for i in range(10):
#     numero = 0
#     while numero < 1000 or numero > 2000:
#         numero = int(input(f'{i + 1} - ingrese un numero: '))
#         vector.append(numero)

# print(vector)

# rango = 0
# vector = []
# vector2 = []

# for i in range(100, 201):
#     vector.append(i)

# while rango <= 200:
#     if rango >= 100:
#         vector2.append(rango)
#     rango += 1

# print(vector)
# print(vector2)


vector = []
vector2 = []

for i in range(10):
    numero = int(input(f'{i+1} - ingrese un numero: '))
    vector.append(numero)

for h in vector:
    if h % 10 == 3:
        vector2.append(f'*{h}')
    else:
        vector2.append(h)

print(vector2)
