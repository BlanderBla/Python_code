# Created by: Brayan Adrian Galvan Flores #
# 28. Calcular el producto punto de dos arrays NumPy de 1D.
# Note: The escalar product has to be the same lenght of values in each vector 
import numpy as np
import random as rnd

def cList(x):
    i = 0
    lVal = []
    while i != x:
        lVal.append(rnd.randint(1,100))
        i = i + 1
    return lVal

num = int(input("Enter the number of values for the vectors > "))
f_vector = np.array(cList(num))
s_vector = np.array(cList(num))
print(f"First vector: {f_vector}\nSecond vector: {s_vector}\nEscalar product > {f_vector@s_vector}")