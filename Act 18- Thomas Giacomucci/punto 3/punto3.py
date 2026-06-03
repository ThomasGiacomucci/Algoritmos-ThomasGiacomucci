"""""
Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""
def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

# Bloque principal

print("=== Rectángulo 1 ===")
lado1_rect1 = float(input("Ingrese el lado 1 del rectángulo 1: "))
lado2_rect1 = float(input("Ingrese el lado 2 del rectángulo 1: "))
superficie_rect1 = retornar_superficie(lado1_rect1, lado2_rect1)

print("=== Rectángulo 2 ===")
lado1_rect2 = float(input("Ingrese el lado 1 del rectángulo 2: "))
lado2_rect2 = float(input("Ingrese el lado 2 del rectángulo 2: "))
superficie_rect2 = retornar_superficie(lado1_rect2, lado2_rect2)

# Mostrar cuál de los dos tiene una superficie mayor
if superficie_rect1 > superficie_rect2:
    print("El rectángulo 1 tiene una superficie mayor.")
elif superficie_rect2 > superficie_rect1:
    print("El rectángulo 2 tiene una superficie mayor.")
else:
    print("Ambos rectángulos tienen la misma superficie.")