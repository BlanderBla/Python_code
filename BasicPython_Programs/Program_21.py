# Created by: Brayan Adrian Galvan Flores #
import random as rd

valueList = list()
x = int(input("Put the value of the list > "))
while x > 0:
    value = rd.randint(1,50)
    valueList.append(value)
    x = x - 1


counter = {}

for element in valueList:
    if element not in counter:
        counter[element] = 0
    counter[element] += 1

print(counter)
# COUNTER - COLLECTIONS #