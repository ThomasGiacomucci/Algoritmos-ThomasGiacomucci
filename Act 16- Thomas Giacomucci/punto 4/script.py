# ---------------------------------------------------
# Punto Extra 4
# Registrar nombres y calificaciones de 6 docentes.
# Mostrar:
# - Docente con mejor y peor calificación
# - Ordenar de mayor a menor
# - Cantidad de aprobados y desaprobados
# ---------------------------------------------------

# Crear listas
docentes = []
calificaciones = []

# Cargar datos
for x in range(6):

    nombre = input("Ingrese el nombre del docente: ")
    nota = float(input("Ingrese la calificación: "))

    docentes.append(nombre)
    calificaciones.append(nota)

# Buscar nota máxima y mínima
nota_maxima = max(calificaciones)
nota_minima = min(calificaciones)

# Mostrar docente con mayor nota
print("\nDocente con mejor calificación:")

for x in range(6):

    if calificaciones[x] == nota_maxima:
        print(docentes[x], "-", calificaciones[x])

# Mostrar docente con menor nota
print("\nDocente con peor calificación:")

for x in range(6):

    if calificaciones[x] == nota_minima:
        print(docentes[x], "-", calificaciones[x])

# Ordenar de mayor a menor
for x in range(5):

    for y in range(x + 1, 6):

        if calificaciones[x] < calificaciones[y]:

            # Intercambiar notas
            aux_nota = calificaciones[x]
            calificaciones[x] = calificaciones[y]
            calificaciones[y] = aux_nota

            # Intercambiar nombres
            aux_nombre = docentes[x]
            docentes[x] = docentes[y]
            docentes[y] = aux_nombre

# Mostrar ordenados
print("\nDocentes ordenados por calificación:")

for x in range(6):
    print(docentes[x], "-", calificaciones[x])

# Contar aprobados y desaprobados
aprobados = 0
desaprobados = 0

for x in range(6):

    if calificaciones[x] >= 6:
        aprobados += 1
    else:
        desaprobados += 1

# Mostrar resultados
print("\nCantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)