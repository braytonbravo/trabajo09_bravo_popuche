import os
import libreria

# EJERCICIO 10
# DECLARACION DE VARIABLES
fuerza,masa,aceleracion=0.0,0,0.0

# input
masa=int(os.sys.argv[1])
fuerza=int(os.sys.argv[2])
aceleracion=libreria.aceleracion(masa, aceleracion)

# uoutput
print("La aceleracion es:", aceleracion)
