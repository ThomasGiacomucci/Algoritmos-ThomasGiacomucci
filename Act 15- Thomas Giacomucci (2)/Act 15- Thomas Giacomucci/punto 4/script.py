# ---------------------------------------------------
# Punto 4
# Cargar una lista con 5 elementos enteros.
# Ordenar de menor a mayor y mostrarla.
# Luego ordenar de mayor a menor e imprimirla.
# ---------------------------------------------------

# Crear lista
lista = []

# Cargar números
for x in range(5):
    numero = int(input("Ingrese un número entero: "))
    lista.append(numero) #Agrega numero a la lista

# Ordenar de menor a mayor
for i in range(4):
    for j in range(4):
        if lista[j] > lista[j + 1]:
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print("Lista ordenada de menor a mayor:")
print(lista)

