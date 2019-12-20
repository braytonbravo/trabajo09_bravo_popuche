import os
import libreria

# EJERCICIO 14
# DECLARACION DE LAS VARIABLES
vf,vo,a,t=0.0,0.0,0.0,0.0

# input
vo=float(os.sys.argv[1])
t=float(os.sys.argv[2])
a=float(os.sys.argv[3])
vf=libreria.velocidad_final(vo, a, t)

# output
print("La velocidad inicial es:", vf)
