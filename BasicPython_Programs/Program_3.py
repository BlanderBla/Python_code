# Created by: Brayan Adrian Galvan Flores #

import os

def menu():
    print("What area do you want to calculate?\n\t1. Circle\n\t2. Triangle\n\t3. Square\n\t4. Rectangle\n\t5. Exit")
    opc = int(input("\n\t> "))
    return opc

def switch(opc):
    if opc == 1:
        result = circle(float(input("\tPut the radius")))
        print(f"Area: {result}")
    elif opc == 2:
        b = float(input("\tPut the base >"))
        h = float(input("Put the height > "))
        result = triangle(b,h)
        print(f"Area: {result}")
    elif opc == 3:
        result = square(float(input("\tPut the side")))
        print(f"Area: {result}")
    elif opc == 4:
        b = float(input("\tPut the base >"))
        h = float(input("Put the height > "))
        result = rectangle(b,h)
    elif opc == 5:
        print("\n\tPress any key to close")

def circle(r):
    return 3.1416*r

def triangle(b,h):
    return b*h/2

def square(l):
    return l*l

def rectangle(b,h):
    return b*h

value = menu()
while(value != 5):
    switch(value)
    os.system('cls')
    value = menu()