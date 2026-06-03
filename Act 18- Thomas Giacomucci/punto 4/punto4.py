""""
Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".
"""
def contar_letras_a(texto):
    contador = 0
    for letra in texto:
        if letra.lower() == 'a':
            contador += 1
    return contador
# Bloque principal
texto_usuario = input("Ingrese un texto: ")
cantidad_a = contar_letras_a(texto_usuario)
print(f"La cantidad de letras 'a' o 'A' en el texto es: {cantidad_a}")
