# ---------------------------------------------------
# Punto 5
# Crear una lista con nombres de 5 países y otra
# lista paralela con la cantidad de habitantes.
# Ordenar alfabéticamente e imprimir.
# Luego ordenar por cantidad de habitantes
# de mayor a menor e imprimir nuevamente.
# ---------------------------------------------------

# Crear listas
paises = []
habitantes = []

# Cargar datos
for x in range(5):

    pais = input("Ingrese el nombre del país: ")
    cantidad = int(input("Ingrese la cantidad de habitantes: "))

    paises.append(pais)
    habitantes.append(cantidad)

# Ordenar alfabéticamente
for x in range(4):

    for y in range(x + 1, 5):

        if paises[x] > paises[y]:

            # Intercambiar países
            aux_pais = paises[x]
            paises[x] = paises[y]
            paises[y] = aux_pais

            # Intercambiar habitantes
            aux_hab = habitantes[x]
            habitantes[x] = habitantes[y]
            habitantes[y] = aux_hab

# Mostrar orden alfabético
print("\nPaíses ordenados alfabéticamente:")

for x in range(5):
    print(paises[x], "-", habitantes[x])

# Ordenar por habitantes de mayor a menor
for x in range(4):

    for y in range(x + 1, 5):

        if habitantes[x] < habitantes[y]:

            # Intercambiar habitantes
            aux_hab = habitantes[x]
            habitantes[x] = habitantes[y]
            habitantes[y] = aux_hab

            # Intercambiar países
            aux_pais = paises[x]
            paises[x] = paises[y]
            paises[y] = aux_pais

# Mostrar orden por habitantes
print("\nPaíses ordenados por habitantes:")

for x in range(5):
    print(paises[x], "-", habitantes[x])