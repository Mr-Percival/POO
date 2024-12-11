#Se ingresaron los valores de venta y salario de cada departamento
ventas_uno=float(input("Ingrese el valor de ventas del departamento 1:"))
ventas_dos=float(input("Ingrese el valor de ventas del departamento 2:"))
ventas_tres=float(input("Ingrese el valor de ventas del departamento 3:"))
salario_uno=float(input("Ingrese el valor de salario de los vendedores del departamento 1:"))
salario_dos=float(input("Ingrese el valor de salario de los vendedores del departamento 2:"))
salario_tres=float(input("Ingrese el valor de salario de los vendedores del departamento 3:"))
#Se calcula las ventas totales y se genera una lista de las ventas
ventas_totales=ventas_uno+ventas_dos+ventas_tres
lista=[ventas_uno,ventas_dos,ventas_tres]
#Se verifica que departamentos cumplen la condicion y se aplica el bono:
for i in lista:
    if i>(ventas_totales*0.33):
        if i==ventas_uno:
            salario_uno=salario_uno*1.2
        if i==ventas_dos:
            salario_dos=salario_dos*1.2
        if i==ventas_tres:
            salario_tres=salario_tres*1.2
#Se imprimen los salarios por departamento
print(f"El salario del departamento uno es de ${salario_uno} pesos")
print(f"El salario del departamento dos es de ${salario_dos} pesos")
print(f"El salario del departamento tres es de ${salario_tres} pesos")
