# ---------------------------------------------------
# Punto Extra 2
# Registrar nombres de 5 vendedores y sus ventas.
# Ordenar de mayor a menor según ventas.
# Mostrar listado ordenado e informar
# quién fue el que menos vendió.
# ---------------------------------------------------

# Crear listas
vendedores = []
ventas = []

# Cargar datos
for x in range(5):

    nombre = input("Ingrese el nombre del vendedor: ")
    monto = float(input("Ingrese el total vendido: "))

    vendedores.append(nombre)
    ventas.append(monto)

# Ordenar de mayor a menor
for x in range(4):

    for y in range(x + 1, 5):

        if ventas[x] < ventas[y]:

            # Intercambiar ventas
            aux_venta = ventas[x]
            ventas[x] = ventas[y]
            ventas[y] = aux_venta

            # Intercambiar vendedores
            aux_nombre = vendedores[x]
            vendedores[x] = vendedores[y]
            vendedores[y] = aux_nombre

# Mostrar lista ordenada
print("\nLista ordenada de ventas:")

for x in range(5):
    print(vendedores[x], "-", ventas[x])

# Mostrar quien menos vendió
print("\nEl vendedor que menos vendió fue:")
print(vendedores[4], "-", ventas[4])