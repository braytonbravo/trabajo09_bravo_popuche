import os
import libreria

# ejercicio 05
# HALLAR EL AREA DEL RECTANGULO
# DECLARACION DE VARIABLES

# input
base,altura,area=0,0,0
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
area=libreria.area_rectangulo(base,altura)

# output
print("EL area del rectangulo es:", area)
