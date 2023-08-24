# Created by: Brayan Adrian Galvan Flores #
# 30. Dada una matriz NumPy de 1D, reemplazar todos los valores mayores que un número dado por 0.

import numpy as np
import random as rnd

def cList(s):
    i=s
    valL = []
    while i!=0:
        valL.append(rnd.randint(1,100))
        i=i-1
    return valL

def normArr(arr,mid):
    i=0
    while i < len(arr):
        if arr[i] >= mid:
            arr[i] = 0
        i=i+1 
    return arr

number_elements = int(input("Enter the number of values of the array: "))
number_mid = int(input("Enter the value of the number in the middle: "))

arr = np.array(cList(number_elements))
print(arr)
arr_norm = normArr(arr,number_mid)
print(arr_norm)