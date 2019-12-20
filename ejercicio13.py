import os
import libreria

# EJERCICIO 13
# DECLARACION DE LAS VARIABLES
ganancia,p_venta,p_compra=0.0,0.0,0.0

# input
p_venta=float(os.sys.argv[1])
p_compra=float(os.sys.argv[2])
ganancia=libreria.ganancia(p_compra, p_venta)

# output
print("La ganancia es:", ganancia)
