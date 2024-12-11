#Se importa la libreria Math
import math
# Ingresar los valores de A, B y C
a = float(input("Ingrese el valor del parámetro A: "))
b = float(input("Ingrese el valor del parámetro B: "))
c = float(input("Ingrese el valor del parámetro C: "))
# Calcular el discriminante y determinar las soluciones en función del discriminante
discriminante = b**2 - 4*a*c
if discriminante > 0:
    # Dos soluciones reales y diferentes
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
elif discriminante == 0:
    # Una solución real
    x = -b / (2*a)
    print(f"La solución es x = {x}")
else:
    # No hay soluciones reales
    print("No hay soluciones reales")
