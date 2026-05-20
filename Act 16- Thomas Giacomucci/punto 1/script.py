# ---------------------------------------------------
# Punto Extra 1
# Registrar nombres y calificaciones de 6 estudiantes.
# Mostrar:
# - Estudiante con nota más alta
# - Estudiante con nota más baja
# - Informar si hay notas máximas o mínimas repetidas
# ---------------------------------------------------

# Crear listas
nombres = []
notas = []

# Cargar datos
for x in range(6):

    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota: "))

    nombres.append(nombre)
    notas.append(nota)

# Buscar nota máxima y mínima
nota_maxima = max(notas)
nota_minima = min(notas)

# Mostrar estudiantes con nota máxima
print("\nEstudiantes con nota más alta:")

contador_max = 0

for x in range(6):

    if notas[x] == nota_maxima:
        print(nombres[x], "-", notas[x])
        contador_max += 1

# Mostrar estudiantes con nota mínima
print("\nEstudiantes con nota más baja:")

contador_min = 0

for x in range(6):

    if notas[x] == nota_minima:
        print(nombres[x], "-", notas[x])
        contador_min += 1

# Informar repetidos
if contador_max > 1:
    print("\nHay estudiantes con la misma nota máxima.")

if contador_min > 1:
    print("Hay estudiantes con la misma nota mínima.")