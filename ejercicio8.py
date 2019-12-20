import os
import libreria

# EJERCICIO 08
# DECLARACION DE VARIABLES
circulo,pi,radio=0.0,0.0,0.0

# input
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
circulo=libreria.area_circulo(pi, radio)

# output
print("El area del circulo es:", circulo)
