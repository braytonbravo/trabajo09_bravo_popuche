import os
import libreria

# EJERCICIO 23
#DECLARCION DE VARIABLES

# input
mas=int(os.sys.argv[1])
temperatura=int(os.sys.argv[2])
c_especifico=int(os.sys.argv[3])
calor=libreria.calor(mas, temperatura, c_especifico)

# output
print("El calor es:", calor)
