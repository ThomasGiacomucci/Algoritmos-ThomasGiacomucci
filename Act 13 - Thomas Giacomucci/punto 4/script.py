"""""
4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de
puntos a procesar.
"""

cantidad = int(input("Ingrese la cantidad de puntos: "))

cuad1 = cuad2 = cuad3 = cuad4 = 0

for i in range(cantidad):
    x = float(input("Ingrese coordenada x: "))
    y = float(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        cuad1 += 1
    elif x < 0 and y > 0:
        cuad2 += 1
    elif x < 0 and y < 0:
        cuad3 += 1
    elif x > 0 and y < 0:
        cuad4 += 1

print("Primer cuadrante:", cuad1)
print("Segundo cuadrante:", cuad2)
print("Tercer cuadrante:", cuad3)
print("Cuarto cuadrante:", cuad4)