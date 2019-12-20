import os
import libreria

# ejercicio 02
# HALLAR EL PROMEDIO DE TRES NOTAS
# DECLARACION DE VARIABLES
nota1,nota2,nota3,calificacion=0,0,0,0

# input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.agrv[3])
calificacion=libreria.promedio(nota1, nota2, nota3)

# output
print("EL promedio es:", calificacion)
