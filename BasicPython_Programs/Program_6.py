# Created by: Brayan Adrian Galvan Flores #

def celToFahr(x):
    return x+32

def celToKel(x):
    return x+273.15

x = float(input("Put the current temperatura (°C) > "))
y = celToFahr(x)
z = celToKel(x)
print(f"\nTemperature\n\t° C > {x}\n\t° F > {y}\n\t° K > {z}")