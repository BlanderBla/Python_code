# Created by: Brayan Adrian Galvan Flores #
# 31. Dada una matriz NumPy, calcular la transposición de la matriz.

import numpy as np
import random as rnd

def cList(n,m):
    i=0
    valL = []
    while i != (n*m):
        valL.append(rnd.randint(1,100))
        i=i+1
    return valL


n = rnd.randint(1,10)
m = rnd.randint(1,10)
matrix = np.reshape(np.array(cList(n,m)),(n,m))
tra_matrix = np.transpose(matrix)
print(f"Original matrix: \n{matrix}\nTrans Matrix: \n{tra_matrix}")