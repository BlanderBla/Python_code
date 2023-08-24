# Created by: Brayan Adrian Galvan Flores #
# INSERTION SORT ALGORITHM

import random as rnd

def create_List(n):
    listValue = []
    i = 0
    while i < n:
        listValue.append(rnd.randint(1,1000))
        i+=1
    return listValue

def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if list[j] < list[min]:
                min = j
        if min != i:
            aux = list[i]
            list[i] = list[min]
            list[min] = aux
    return list

number = int(input("Enter a value for the number of elements in the list: "))
lNum = create_List(number)
print(lNum)
nlNum = selection_sort(lNum)
print(nlNum)