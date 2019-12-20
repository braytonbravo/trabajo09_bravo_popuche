import os
import libreria

# EJERCICIO 17
#DECLARCION DE VARIABLES

# input
resistencia=int(os.sys.argv[1])
intensidad=int(os.sys.argv[2])
voltaje=libreria.voltaje(resistencia, intensidad)

# output
print("El voltaje es:", voltaje)
