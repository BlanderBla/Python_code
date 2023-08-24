# Created by: Brayan Adrian Galvan Flores #

import numpy as np

# Supongamos que tienes una matriz NumPy con algunos valores nulos (NaN)
matriz = np.array([[1.0, 2.0, np.nan],
                   [4.0, np.nan, 6.0],
                   [np.nan, 8.0, 9.0]])

# Encontrar valores nulos (NaN) en la matriz
valores_nulos = np.isnan(matriz)

print(valores_nulos)





