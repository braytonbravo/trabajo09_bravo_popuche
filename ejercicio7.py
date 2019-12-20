import os
import libreria

# EJERCICIO 07
# DECLARACION DE VARIABLES
pro_a,x,y=0,0,0

# input
x=int(os.sys.argv[1])
y=int(os.sys.argv[1])
pro_a=libreria.pro_armonico(x, y)

# output
print("El promedio armonico es:", pro_a)
