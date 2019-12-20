import os
import libreria

# EJERCICIO 06
# DECLARACION DE VARIABLES
trapecio,base_mayor,base_menor,h=0,0,0

# input
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
h=int(os.sys.argv[3])
trapecio=libreria.area_trapecio(base_mayor, base_menor, h)

# output
print("Area del trapecio:", trapecio)
