import os
import libreria

# EJERCICIO 19
#DECLARCION DE VARIABLES

# input
c=int(os.sys.argv[1])
d=int(os.sys.argv[2])
e=int(os.sys.argv[3])
volumen=libreria.volumen_paralepipedo(c, d, e)

# output
print("EL volumen del paralepipedo es:", volumen)
