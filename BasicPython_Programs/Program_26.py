# Created by: Brayan Adrian Galvan Flores #
# 27. Crear un array NumPy de números aleatorios y ordenarlo de menor a mayor.

import numpy as np
import random as rnd

def cList(x,max):
    i = 0
    lVal = []
    while i != x:
        y = rnd.randint(1,max)
        lVal.append(y)
        i = i + 1
    return lVal

num = int(input("Enter the max value to generate random values: "))
max_value = int(input("Enter the max value to generate: "))

arr_f = np.array(cList(num, max_value))
print(np.sort(arr_f))