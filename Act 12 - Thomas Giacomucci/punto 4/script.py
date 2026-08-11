"""""
4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a. La cantidad de valores ingresados negativos.
b. La cantidad de valores ingresados positivos.
c. La cantidad de múltiplos de 15.
d. El valor acumulado de los números ingresados que son pares.
"""

negativos = 0
positivos = 0
multiplos_15 = 0
suma_pares = 0

for i in range(10):
    numero = int(input("Ingrese un número entero: "))

    if numero < 0:
        negativos += 1

    if numero > 0:
        positivos += 1

    if numero % 15 == 0:
        multiplos_15 += 1

    if numero % 2 == 0:
        suma_pares += numero

print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos)
print("Cantidad de múltiplos de 15:", multiplos_15)
print("Valor acumulado de los pares:", suma_pares)