#Se ingresan los dos valores a comparar
valor_uno=float(input("Ingrese el 1er valor:"))
valor_dos=float(input("Ingrese el 2do valor:"))
#Se comparan y se imprime en pantalla el mayor
if valor_uno>valor_dos:
    print(f"El mayor valor es {valor_uno}")
else:
    if valor_uno==valor_dos:
        print(f"Los valores {valor_uno} y {valor_dos} son iguales")
    else:
        print(f"El mayor valor es {valor_dos}")
