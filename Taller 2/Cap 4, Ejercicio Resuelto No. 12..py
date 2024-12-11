#Ingresamos los datos basicos del trabajador:nombre, numero horas trabajadas y valor por hora normal
nombre=input("Ingrese el nombre del trabajador:")
numero_horas=float(input("Ingrese el numero de horas trabajadas:"))
valor_hora=float(input("Ingrese el valor por hora normal de trabajo:"))
#Calculamos las horas extra que se pagan al doble y al triple de precio
if numero_horas>40:
    if numero_horas>48:
        horas_doble=8
        horas_triple=numero_horas-40-8
        horas_normales=numero_horas-horas_doble-horas_triple
    else:
        horas_doble=numero_horas-40
        horas_triple=0
        horas_normales=numero_horas-horas_doble-horas_triple
else:
    horas_doble=0
    horas_triple=0
    horas_normales=numero_horas
#Calculamos la cantidad de dinero a pagar e imprimimos en pantalla
cantidad_dinero=(horas_normales*valor_hora)+(horas_doble*2*valor_hora)+(horas_triple*3*valor_hora)
print(f"El trabajador {nombre} recibira {cantidad_dinero} pesos por un total de {numero_horas} horas trabajadas, distribuidas en {horas_normales} horas normales, {horas_doble} horas extra al doble de precio y {horas_triple} horas extra al triple de precio")
