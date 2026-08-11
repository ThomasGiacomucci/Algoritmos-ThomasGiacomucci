"""""
5. Realizar un programa que lea los lados de n triángulos, e informar:
a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b. Cantidad de triángulos de cada tipo.
"""

n = int(input("¿Cuantos triangulos desea analizar? "))

equilateros = 0
isosceles = 0
escalenos = 0

for i in range(n):
    print(f"\nTriangulo {i+1}")
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))
    
    if a == b and b == c:
        print("Tipo: Equilátero")
        equilateros += 1
    elif a == b or a == c or b == c:
        print("Tipo: Isosceles")
        isosceles += 1
    else:
        print("Tipo: Escaleno")
        escalenos += 1

print("\nCantidad de triángulos:")
print("Equilateros:", equilateros)
print("Isosceles:", isosceles)
print("Escalenos:", escalenos)