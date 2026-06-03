""""
Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.

"""

def mostrar_ordenados(a, b, c):
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    print(f"Ordenados de menor a mayor: {a} — {b} — {c}")

def cargar_y_ordenar():
    x = int(input("Primer entero: "))
    y = int(input("Segundo entero: "))
    z = int(input("Tercer entero: "))
    mostrar_ordenados(x, y, z)

# Bloque principal
cargar_y_ordenar()


