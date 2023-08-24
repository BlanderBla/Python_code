# Created by: Brayan Adrian Galvan Flores #
# 32. Dada una matriz NumPy, agregar una fila y una columna de unos al inicio de la matriz.

import numpy as np
import random as rnd

def cList(n,m):
    i=0
    valL = []
    while i != (n*m):
        valL.append(rnd.randint(1,10))
        i=i+1
    return valL

def listOne(n):
    i=0
    list_one = []
    while i!=n:
        list_one.append(1)
        i=i+1
    return list_one

n = rnd.randint(1,5)
m = rnd.randint(1,5)
matrix = np.reshape(np.array(cList(n,m)),(n,m))
print(f"Original matrix: \n{matrix}")

# ROWS
rows = len(matrix)
list_rows = listOne(rows)
list_rows.append(1)
arr_rows = np.array(list_rows)
tra_rows = np.transpose(arr_rows)
# COLS
columns = len(matrix[0])
arr_cols = np.array(listOne(columns))


# INSERT COLS
matriz_fila = np.insert(matrix, 0, arr_cols, axis=0)
# INSERT ROWS
matriz_fila = np.insert(matriz_fila, 0, tra_rows, axis=1)
print(f"\nFirst row and column with 1's: \n{matriz_fila}")