import os
import libreria

# EJERCICIO 21
#DECLARCION DE VARIABLES

# input
espacio=int(os.sys.argv[1])
rapidez=int(os.sys.argv[2])
tempo=libreria.tiempo(espacio, rapidez)

# output
print("EL tiempo es :", tempo)
