import os
import libreria

# EJERCICIO 24
#DECLARCION DE VARIABLES

# input
fijo=int(os.sys.argv[1])
produccion=int(os.sys.argv[2])
medio=libreria.medio(fijo, produccion)

# output
print("EL medio es:", medio)
