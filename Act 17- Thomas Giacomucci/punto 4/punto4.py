""""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""

empleados = []
sueldos = []
cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))

for i in range(cantidad_empleados):
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = float(input(f"Ingrese el sueldo de {nombre}: "))
    empleados.append(nombre)
    sueldos.append(sueldo)

print("\nEmpleados y sus sueldos:")

for i in range(cantidad_empleados):
    print(f"{empleados[i]}: {sueldos[i]}")

# Eliminar empleados con sueldo mayor a 10000

for i in range(cantidad_empleados - 1, -1, -1):
    if sueldos[i] > 10000:
        del empleados[i]
        del sueldos[i]

print("\nEmpleados con sueldo menor o igual a 10000:")

for i in range(len(empleados)):
    print(f"{empleados[i]}: {sueldos[i]}")

    
