import os
import libreria

# EJERCICIO 22
#DECLARCION DE VARIABLES

# input
perimetro=int(os.sys.argv[1])
base=int(os.sys.argv[1])
altura=int(os.sys.argv[1])
area_lateral=libreria.area_lateral(perimetro, base, altura)

# output
print("El area lateral del prisma es:")
