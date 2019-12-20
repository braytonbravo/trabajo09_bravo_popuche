import os
import libreria

# EJERCICIO 15
# DECLARACION DE LAS VARIABLES
h,vo,vf,t=0,0,0,0

# input
vo=int(os.sys.argv[1])
vf=int(os.sys.argv[2])
t=int(os.sys.argv[3])
h=libreria.altura(vo, vf, t)

# output
print("La altura es:", h)
