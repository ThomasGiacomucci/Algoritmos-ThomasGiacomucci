"""""
2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
altura promedio de las personas.
"""

n = int(input("¿Cuántas personas? "))
suma = 0
i = 1

while i <= n:
    altura = float(input(f"Ingrese la altura de la persona {i}: "))
    suma += altura
    i += 1

promedio = suma / n
print("Altura promedio:", promedio)