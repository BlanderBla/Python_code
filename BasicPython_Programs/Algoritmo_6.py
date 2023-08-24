# Created by: Brayan Adrian Galvan Flores #
# QUICK SORT ALGORITHM

import random as rnd

def create_List(n):
    listValue = []
    i = 0
    while i < n:
        listValue.append(rnd.randint(1,1000))
        i+=1
    return listValue

def quick_sort(list, start, end):
    if start < end:
        pivote = particionar(list, start, end)
        quick_sort(list, start, pivote - 1)
        quick_sort(list, pivote + 1, end)
    return list

def particionar(list, inicio, fin):
    pivote = list[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if list[j] <= pivote:
            i = i + 1
            list[i], list[j] = list[j], list[i]
    
    list[i + 1], list[fin] = list[fin], list[i + 1]
    return i + 1




number = int(input("Enter a value for the number of elements in the list: "))
lNum = create_List(number)
print(lNum)
inicio = 0
fin = len(lNum)-1
nlNum = quick_sort(lNum,inicio,fin)
print(nlNum)