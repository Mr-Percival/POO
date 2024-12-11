#Ingresamos el valor de compra y el color de la bolita
valor=float(input("Ingrese el valor de la compra:"))
color=input("Ingrese el color de la bolita:")
#Identificamos el color y aplicamos el descuento
if color=="BLANCA" or color=="blanca":
       valor=valor
elif color=="VERDE" or color=="verde":
       valor=valor*0.9
elif color=="AMARILLA" or color=="amarilla":
       valor=valor*0.75
elif color=="AZUL" or color=="azul":
       valor=valor*0.5
elif color=="ROJA" or color=="roja":
      valor=valor*0
#Se imprime el valor a pagar
print(f"El valor a pagar es de ${valor} pesos")
