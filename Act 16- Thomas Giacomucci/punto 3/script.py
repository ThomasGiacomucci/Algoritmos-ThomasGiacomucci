# ---------------------------------------------------
# Punto Extra 3
# Registrar nombres de 5 atletas y sus tiempos.
# Mostrar:
# - Promedio de tiempos
# - Mejor tiempo
# - Peor tiempo
# - Atletas que superaron el promedio
# ---------------------------------------------------

# Crear listas
atletas = []
tiempos = []

# Cargar datos
for x in range(5):

    nombre = input("Ingrese el nombre del atleta: ")
    tiempo = float(input("Ingrese el tiempo en segundos: "))

    atletas.append(nombre)
    tiempos.append(tiempo)

# Calcular promedio
suma = 0

for x in range(5):
    suma += tiempos[x]

promedio = suma / 5

# Buscar mejor y peor tiempo
mejor_tiempo = min(tiempos)
peor_tiempo = max(tiempos)

# Mostrar promedio
print("\nPromedio de tiempos:", promedio)

# Mostrar mejor tiempo
print("\nAtleta con mejor tiempo:")

for x in range(5):

    if tiempos[x] == mejor_tiempo:
        print(atletas[x], "-", tiempos[x])

# Mostrar peor tiempo
print("\nAtleta con peor tiempo:")

for x in range(5):

    if tiempos[x] == peor_tiempo:
        print(atletas[x], "-", tiempos[x])

# Mostrar quienes superaron el promedio
print("\nAtletas que superaron el promedio:")

for x in range(5):

    if tiempos[x] < promedio:
        print(atletas[x], "-", tiempos[x])