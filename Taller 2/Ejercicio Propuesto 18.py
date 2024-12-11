#Se reciben los valores e inicializan las variables
codigo=int(input("Ingrese el codigo del trabajador:"))
nombre=input("Ingrese los nombres del trabajador:")
numero_horas=float(input("Ingrese el numero de horas trabajadas:"))
valor_hora=float(input("Ingrese el valor por hora:"))
porcentaje_retefuente=float(input("Ingrese el porcentaje de retención en la fuente como numero decimal (Ejemplo: ingrese 12.5 si el porcentaje es del 12.5%):"))
porcentaje_retefuente=porcentaje_retefuente/100
#Se calcula el salario bruto y neto
salario_bruto=numero_horas*valor_hora
salario_neto=salario_bruto-(salario_bruto*porcentaje_retefuente)
#se imprimen las salidas
print(f"El codigo del empleado es {codigo}")
print(f"El empleado se llama {nombre}")
print(f"El salario bruto es de {salario_bruto} pesos")
print(f"El salario neto es de {salario_neto} pesos")
