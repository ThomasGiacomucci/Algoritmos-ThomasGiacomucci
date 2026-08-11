"""""
1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""
n = int(input("Ingrese la cantidad de empleados: "))

entre_100_300 = 0
mas_300 = 0
total_sueldos = 0

for i in range(n):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))

    if 100 <= sueldo <= 300:
        entre_100_300 += 1
    elif sueldo > 300:
        mas_300 += 1

    total_sueldos += sueldo

print("Empleados que cobran entre $100 y $300:", entre_100_300)
print("Empleados que cobran mas de $300:", mas_300)
print("Gasto total en sueldos:", total_sueldos)