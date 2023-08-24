# Created by: Brayan Adrian Galvan Flores #
# 26. Crear dos matrices 3x3 y realizar una suma y una resta de matrices.
import numpy as np
import random as rnd

def create_numbers():
    i = 0
    list_values = []
    while i != 9:
        x = rnd.randint(1, 100)
        list_values.append(x)
        i = i + 1
    return list_values

f_matriz = np.array(create_numbers())
f_matriz_rs = np.reshape(f_matriz,(3,3))
print(f"Matrix A: \n{f_matriz_rs}\n")

s_matriz = np.array(create_numbers())
s_matriz_rs = np.reshape(s_matriz,(3,3))
print(f"Matrix B: \n{s_matriz_rs}\n")

print(f"Sum A + B: \n{f_matriz_rs + s_matriz_rs}\n")
print(f"Minus A - B: \n{f_matriz_rs - s_matriz_rs}")