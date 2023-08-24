# Created by: Brayan Adrian Galvan Flores #

calif = list()

# Function #
def menu():
    print("\n\t1. Add calification\n\t2. Calculate")
    x = int(input("\tOption > "))
    return x

# Main #
print("\n\t1. Add calification\n\t2. Calculate")
opc = int(input("\tOption > "))
while opc != 2:
    calif.append(int(input("\t> ")))
    opc = menu()

sum = 0
size = len(calif)
while len(calif) != 0:
    tam = len(calif)-1
    sum += calif.pop(tam)

prom = sum/size
print(f"\n\tThe promedy is: {prom}")