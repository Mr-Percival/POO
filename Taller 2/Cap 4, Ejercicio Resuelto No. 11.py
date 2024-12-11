#Se ingresan los valores diferentes a comparar
numero_uno=float(input("Ingrese el 1er numero a comparar:"))
numero_dos=float(input("Ingrese el 2do numero a comparar:"))
numero_tres=float(input("Ingrese el 3er numero a comparar:"))
#Se comparan los valores
if numero_uno>numero_dos:
    if numero_uno>numero_tres:
        print(f"El mayor valor es {numero_uno}")
    else:
        print(f"El mayor valor es {numero_tres}")
else:
    if numero_dos>numero_tres:
        print(f"El mayor valor es {numero_dos}")
    else:
        print(f"El mayor valor es {numero_tres}")
