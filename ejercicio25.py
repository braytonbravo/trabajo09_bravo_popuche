import os
import libreria

# EJERCICIO 25
#DECLARCION DE VARIABLES

# input
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
area_triangulo=libreria.triangulo(base, altura)

# output
print("EL area del triangulo es:", area_triangulo)
