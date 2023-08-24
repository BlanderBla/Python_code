# Created by: Brayan Adrian Galvan Flores #
# 29. Crear una matriz diagonal con valores de 1 a 5 y luego calcular la traza de la matriz.
import numpy as np
import random as rnd

def cList(s):
    i=0
    lVal = []
    while i!=(s*s):
        lVal.append(rnd.randint(1,10))
        i=i+1
    return lVal

def rMatrix(m,s):
    return np.reshape(m,(s,s))

def traMatrix(rMat):
    sum=0
    i=0
    while i!=len(rMat):
        sum=sum+rMat[i][i]
        i=i+1
    return sum

size = int(input("Enter the size of the matrix: "))
matrix = cList(size)
r_matrix = rMatrix(matrix,size)
print(f"Matrix: \n{r_matrix}\nTraza: {traMatrix(r_matrix)}")