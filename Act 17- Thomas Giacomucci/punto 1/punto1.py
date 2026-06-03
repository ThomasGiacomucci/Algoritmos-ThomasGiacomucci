""""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del
primer elemento de &quot;lista&quot;. El resto de enteros menores a 50 deben encontrarse
en una nueva posición dentro de la lista.
Volver a imprimir la lista.
"""

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print("Lista original:")
print(lista)

# Crear una nueva lista para los enteros menores a 50

nueva_lista = []

# Recorrer el primer elemento de la lista

for num in lista[0]:
    if num > 50:
        lista[0][lista[0].index(num)] = 0
    else:
        nueva_lista.append(num)

# Imprimir la lista modificada

print("Lista modificada:")
print(lista)

# Agregar la nueva lista a la lista original

lista.append(nueva_lista)

# Imprimir la lista final

print("Lista final con enteros menores a 50:")
print(lista)
