import os
import libreria

# ejercicio 04
# HALLAR EL PRECIO DE VENTA
# DECLARACION DE VARIABLES
pc,ganancia,pv=0.0,0.0,0.0
# input
pc=float(os.sys.argv[1])
ganancia=float(os.sys.argv[2])
pv=libreria.precio_venta(pc,ganancia)

# output
print("EL precio de venta es:", pv)
