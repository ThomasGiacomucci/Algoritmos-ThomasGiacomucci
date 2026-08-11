"""""
3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
(mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que
puede haber dos o más estructuras repetitivas en un algoritmo.
"""

lista1 = []
lista2 = []

print("Carga de lista 1")
for i in range(15):
    valor = int(input(f"Ingrese valor {i+1}: "))
    lista1.append(valor)

print("Carga de lista 2")
for i in range(15):
    valor = int(input(f"Ingrese valor {i+1}: "))
    lista2.append(valor)

suma1 = sum(lista1)
suma2 = sum(lista2)

if suma1 > suma2:
    print("Lista 1 mayor")
elif suma2 > suma1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")