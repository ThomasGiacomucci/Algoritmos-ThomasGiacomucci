# ---------------------------------------------------
# Punto 3
# Solicitar por teclado la cantidad de empleados
# que tiene la empresa.
# Crear y cargar una lista con todos los sueldos.
# Imprimir la lista ordenada de menor a mayor.
# ---------------------------------------------------

# Crear lista
sueldos = []

# Pedir cantidad de empleados
cantidad = int(input("Ingrese la cantidad de empleados: "))

# Cargar sueldos
for x in range(cantidad):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    sueldos.append(sueldo)

# Ordenar lista
sueldos.sort()

# Mostrar lista ordenada
print("\nSueldos ordenados de menor a mayor:")
print(sueldos)