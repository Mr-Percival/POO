#Se ingresa el nombre del empleado, su salario por hora y el numero de horas trabajadas por mes
nombre=input("Ingrese el nombre del empleado:")
salario=float(input("Ingrese el salario por hora:"))
numero_horas=float(input("Ingrese el número de horas trabajadas:"))
#Se verifica la condicion y se imprime el mensaje
if (salario*numero_horas) > 450_000:
    print(f"El nombre del empleado es {nombre} y su salario mensual es de {salario*numero_horas}")
else:
    print(f"El nombre del empleado es {nombre}")
