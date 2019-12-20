import os
import libreria

# EJERCICIO 11
# DECLARACION DE LAS VARIABLES
prom_geometrico,a,b=0,0,0

# input
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
geometrico=libreria.prom_geometrico(a, b)

# output
print("El promedio geometrico es:", geometrico)
