"""""
1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
mayores_igual_7 = 0
menores_7 = 0

i = 1
while i <= 10:
    nota = float(input(f"Ingrese la nota {i}: "))
    
    if nota >= 7:
        mayores_igual_7 += 1
    else:
        menores_7 += 1
    
    i += 1

print("Cantidad de notas >= 7:", mayores_igual_7)
print("Cantidad de notas < 7:", menores_7)