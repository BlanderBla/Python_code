# Created by: Brayan Adrian Galvan Flores #
"""
25. Crear un array NumPy con 10 elementos y realizar las siguientes operaciones:
    a) Calcular la media de los elementos.
    b) Obtener el máximo y mínimo de la lista.
"""

import numpy as np
import random as rnd

def cList():
    i=10
    valL = []
    while i!=0:
        valL.append(rnd.randint(1,100))
        i=i-1
    return valL

def showValues(arr,med,max,min):
    print(f"Array's Values\n\tArray: {arr}\n\tThe media is: {med}\n\tThe max value is: {max}\n\tThe min value is: {min}")

list_Numbers = cList()
arr_Numbers = np.array(list_Numbers)

med_arr = np.mean(arr_Numbers)
max_arr = np.max(arr_Numbers)
min_arr = np.min(arr_Numbers)
showValues(arr_Numbers, med_arr, max_arr, min_arr)

