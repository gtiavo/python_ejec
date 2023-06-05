#  Realizar un programa que solicite el valor hora de un empleado. Posteriormente se
# ingresa el nombre del empleado, la antigüedad y la cantidad de horas trabajadas en
# el mes. El programa debe calcular el importe a cobrar de la siguiente forma:
# -El subtotal resulta de multiplicar el valor hora por la cantidad de horas trabajadas
# -Al subtotal hay que sumarle la cantidad de años trabajados multiplicados por $30
# -A este resultado hay que restarle el 13% en concepto de descuentos.
# Mostrar por pantalla el recibo del empleado con el nombre, la antigüedad, el valor hora, el
# total a cobrar en bruto, el total de descuentos y el valor neto a cobrar.

valorHora = 0
nombreEmpleado = ''
antiguedad = 0
cantidadHorasTrabajadas = 0
while valorHora == 0:
    try:
        valorHora = int(input('Ingresa el valor hora trabajada: '))
    except:
        print('no es un formato valido')
while len(nombreEmpleado) == 0:
    try:
        nombreEmpleado = str(input('Ingresa tu nombre: '))
    except:
        print('no es un formato valido')
while antiguedad == 0:
    try:
        antiguedad = int(input('ingresa tu antiguedad: '))
    except:
        print('no es un formato valido')
while cantidadHorasTrabajadas == 0:
    try:
        cantidadHorasTrabajadas = int(input('ingresa la cantidad de horas trabajadas: '))
    except:
        print('no es un formato valido')




subtotal = valorHora * cantidadHorasTrabajadas
totalBruto = subtotal + antiguedad * 30
totalDescuento = totalBruto * 0.13
totalNeto = totalBruto - totalDescuento

print(f'-----------------------------------------')
print(f'Recibo de sueldo de:     {nombreEmpleado}')
print(f'-----------------------------------------')
print(f'ANTIGUEDAD                   {antiguedad}')
print(f'VALOR HORA                   {valorHora}')
print(f'-----------------------------------------')
print(f'TOTAL BRUTO                   {totalBruto}')
print(f'DESCUENTO                     {totalDescuento}')
print(f'TOTAL NETO                    {totalNeto}')
print(f'-----------------------------------------')