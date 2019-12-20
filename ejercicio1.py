import os
import libreria

# ejercicio 01
# HALLAR LA POTENCIA
# DECLARACION DE VARIABLES
trabajo,tiempo,potencia=0.0,0,0.0

# input
trabajo=float(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
potencia=libreria.area_rectangulo(trabajo, tiempo)

# output
print("La potencia es :", potencia)
