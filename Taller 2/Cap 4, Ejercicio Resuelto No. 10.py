#Se ingresan los datos exigidos
numero_inscripcion=input("Ingrese el numero de inscripcion:")
nombre=input("Ingrese el nombre del estudiante:")
patrimonio=float(input("Ingrese el patrimonio del estudiante:"))
estrato=int(input("Ingrese el estrato social del estudiante:"))
#Se define el valor constante
constante=50_000
#Se evaluan las condiciones y se implementa o no el incremento
if patrimonio>2_000_000 and estrato>3:
    constante=constante+0.03*patrimonio
#Se imprimen los valores en pantalla
print(f"El estudiante {nombre}")
print(f"con numero de inscripción {numero_inscripcion}")
print(f"debera pagar {constante} pesos de matricula")
