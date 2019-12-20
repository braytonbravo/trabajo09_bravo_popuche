import os
import libreria

# EJERCICIO 16
#DECLARCION DE VARIABLES

# input
cateto_opuesto=int(os.sys.argv[1])
cateto_adyacente=int(os.sys.argv[2])
tag=libreria.tangente(cateto_opuesto, cateto_adyacente)

# output
print("La tangente es:", tag)
