# Created by: Brayan Adrian Galvan Flores #
import random as rd

valueList = list()
n = int(input("Put the amount of random values that It will generate > "))
while n != 0:
    value = rd.randint(1,1000)    
    valueList.append(value)
    n = n-1

def max_value(maxvaluelist):
    max_value = maxvaluelist[0]
    i = 0
    while i < len(maxvaluelist):
        if maxvaluelist[i] > max_value:
            max_value = maxvaluelist[i]
        i=i+1
    return max_value

def min_value(minvaluelist):
    min_value = minvaluelist[0]
    i = 0
    while i < len(minvaluelist):
        if minvaluelist[i] < min_value:
            min_value = minvaluelist[i]
        i=i+1
    return min_value

print(f"\nList of values: {valueList}")
max = max_value(valueList)
min = min_value(valueList)
print(f"\tThe biggest value is: {max}\n\tThe minust value is:{min}")
orderList = valueList.sort()
print(f"List in order: {valueList}\n")