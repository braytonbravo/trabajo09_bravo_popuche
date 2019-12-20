import os
import libreria

# EJERCICIO 09
# DECLARACION DE VARIABLES
hipotenusa,co,ca=0,0,0

# input
co=int(os.sys.argv[1])
ca=int(os.sys.argv[2])
hipotenusa=libreria.hipotenusa(co, ca)

# output
print("La hipotenusa es:", hipotenusa)
