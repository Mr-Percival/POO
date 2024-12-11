# Se ingresan los pesos de las 4 esferas
esfera_a = float(input("Ingresa el valor de la esfera A: "))
esfera_b = float(input("Ingresa el valor de la esfera B: "))
esfera_c = float(input("Ingresa el valor de la esfera C: "))
esfera_d = float(input("Ingresa el valor de la esfera D: "))
# Se identifica cuál de las esferas es la de diferente peso y se calcula la diferencia de peso
if esfera_a == esfera_b == esfera_c:
    diferente = "D"
    valor_diferencia = esfera_d - esfera_a
elif esfera_a == esfera_b == esfera_d:
    diferente = "C"
    valor_diferencia = esfera_c - esfera_a
elif esfera_a == esfera_c == esfera_d:
    diferente = "B"
    valor_diferencia = esfera_b - esfera_a
else:
    diferente = "A"
    valor_diferencia = esfera_a - esfera_b
# Se identifica si la esfera diferente pesa mas o menos
if valor_diferencia > 0:
    print(f"La esfera diferente es la {diferente} y es de mayor peso que las otras tres.")
else:
    print(f"La esfera diferente es la {diferente} y es de menor peso que las otras tres.")
