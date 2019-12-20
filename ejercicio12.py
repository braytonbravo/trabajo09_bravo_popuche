import os
import libreria

# EJERCICIO 12
# DECLARACION DE LAS VARIABLES
velocidad,distacia,tiempo=0.0,0.0,0.0

# input
distacia=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])
velocidad=libreria.velocidad(distacia, tiempo)

# output
print("La velocidad es:", velocidad)
