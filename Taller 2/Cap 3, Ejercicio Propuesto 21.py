#Se importa la libreria math
import math
#Se ingresa el valor de los lados del triangulo
lado_uno=float(input("Por favor, ingrese el valor del 1er lado:"))
lado_dos=float(input("Por favor, ingrese el valor del 2do lado:"))
lado_tres=float(input("Por favor, ingrese el valor del 3er lado:"))
#Se calcula el perimetro y el semiperimetro
perimetro=lado_uno+lado_dos+lado_tres
semi_perimetro=perimetro/2
#Se usa la fórmula de Herón para calcular el área
area=math.sqrt(semi_perimetro*(semi_perimetro-lado_uno)*(semi_perimetro-lado_dos)*(semi_perimetro-lado_tres))
#Se imprimen en pantalla los valores
print(f"El triangulo con lados {lado_uno},{lado_dos} y {lado_tres} unidades, posee:")
print(f"Un perimetro de {perimetro} unidades, un semiperimetro de {semi_perimetro} unidades")
print(f"Y un área de {area} unidades cuadradas")
