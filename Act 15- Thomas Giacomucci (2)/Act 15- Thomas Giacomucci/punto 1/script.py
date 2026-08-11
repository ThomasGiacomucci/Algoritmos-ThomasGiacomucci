# ---------------------------------------------------
# Punto 1
# En un curso de 4 alumnos se registraron las notas
# de sus exámenes y se deben procesar de acuerdo a:
# a) Ingresar nombre y nota
# b) Mostrar nombre, nota y condición
# c) Mostrar cantidad de alumnos "Muy Bueno"
# ---------------------------------------------------

# Crear listas
nombres = []
notas = []

# Cargar datos
for x in range(4):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = int(input("Ingrese la nota: "))

    nombres.append(nombre)
    notas.append(nota)

# Variable contador
muy_bueno = 0

# Mostrar resultados
print("\nListado de alumnos")

for x in range(4):

    if notas[x] >= 8:
        condicion = "Muy Bueno"
        muy_bueno += 1

    elif notas[x] >= 4:
        condicion = "Bueno"

    else:
        condicion = "Insuficiente"

    print(nombres[x], "-", notas[x], "-", condicion)

# Mostrar cantidad de alumnos Muy Bueno
print("\nCantidad de alumnos Muy Bueno:", muy_bueno)
