"""""
2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada
cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe
finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un
programa que lea los datos de las cuentas corrientes e informe:
● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo,
sabiendo que:
○ Estado de la cuenta:
○ “Acreedor” si el saldo es &gt; 0.
○ “Deudor” si el saldo es &lt; 0.
○ “Nulo” si el saldo es = 0.
● b) La suma total de los saldos acreedores.
"""

total_acreedores = 0

while True:
    numero_cuenta = int(input("Ingrese número de cuenta (negativo para salir): "))

    if numero_cuenta < 0:
        break

    saldo = float(input("Ingrese saldo actual: "))

    if saldo > 0:
        estado = "Acreedor"
        total_acreedores += saldo
    elif saldo < 0:
        estado = "Deudor"
    else:
        estado = "Nulo"

    print(f"Cuenta {numero_cuenta}: {estado}")

print("Total de saldos acreedores:", total_acreedores)