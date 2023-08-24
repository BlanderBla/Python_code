# Created by: Brayan Adrian Galvan Flores #
import random as rd

valueList = list()
x = int(input("Put the value of the list > "))

while x > 0:
    value = rd.randint(1,100)
    valueList.append(value)
    x -= 1
print(f"No ordered list {valueList}")

valueList.sort()
print(f"Ordered list {valueList}")

size = len(valueList)
i=0

if size%2 == 0:
    i = size//2
    print(f"{valueList[i]}")
else:
    i = (size//2+size//2)//2
    print(f"{valueList[i]}")