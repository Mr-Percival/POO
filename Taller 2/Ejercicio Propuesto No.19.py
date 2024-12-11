#Se ingresa el valor del lado del triangulo equilatero
lado=float(input("Por favor, ingrese el valor del lado:"))
#Se calculan el perimetro, la altura y el area del triangulo
perimetro=lado*3
altura=(lado**2-(lado/2)**2)**(1/2)
area=(lado*altura)/2
#Se imprimen en pantalla los valores
print(f"El triangulo tiene un lado de {lado} unidades")
print(f"Un perimetro de {perimetro} unidades")
print(f"Una altura de {altura} unidades")
print(f"Un área de {area} unidades cuadradas")
