import os
import libreria

# EJERCICIO 20
#DECLARCION DE VARIABLES

# input
d_ma=int(os.sys.argv[1])
d_men=int(os.sys.argv[2])
area_rombo=libreria.rombo(d_ma, d_men)

# output
print("El area del rombo es:", area_rombo)
