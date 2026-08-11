# ---------------------------------------------------
# Punto 2
# Realizar un programa que pida la carga de dos
# listas numéricas enteras de 4 elementos cada una.
# Generar una tercera lista que surja de la suma
# de los elementos de la misma posición.
# Mostrar esta tercera lista.
# ---------------------------------------------------

# Crear listas
lista1 = []
lista2 = []
lista3 = []

# Cargar primera lista
print("Carga de la primera lista")

for x in range(4):
    valor = int(input("Ingrese un número: "))
    lista1.append(valor)

# Cargar segunda lista
print("\nCarga de la segunda lista")

for x in range(4):
    valor = int(input("Ingrese un número: "))
    lista2.append(valor)

# Sumar elementos de las listas
for x in range(4):
    suma = lista1[x] + lista2[x]
    lista3.append(suma)

# Mostrar tercera lista
print("\nTercera lista:")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
print(lista3)