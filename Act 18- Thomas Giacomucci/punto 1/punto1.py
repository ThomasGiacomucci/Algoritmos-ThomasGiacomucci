#Desarrollar un programa que solicite la carga de tres valores y muestre el
#menor. Desde el bloque principal del programa llamar 2 veces a dicha
#función (sin utilizar una estructura repetitiva)"


def carga_tres_valores():
    n1= int(input("Ingresar valor 1:   "))
    n2= int(input("Ingresar valor 2:   "))
    n3= int(input("Ingresar valor 3:   "))

    menor= n1

    if n2< menor:
        menor = n2

    else:
        if n3< menor:
            
            menor= n3
    return menor


#2 llamadas sin bucle
print("=== Primera llamada ===")
resultado1 = carga_tres_valores()
print(f"El menor es: {resultado1}")

print("=== Segunda llamada ===")
resultado2 = carga_tres_valores()
print(f"El menor es: {resultado2}")


#Programa principal

carga_tres_valores() 
