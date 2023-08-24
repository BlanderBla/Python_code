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

def insertion_sort(list):
    n = len(list)
    for i in range(n):
        aux = list[i]
        j = i - 1
        while j>=0 and list[j] > aux:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = aux
    return list


number = int(input("Enter a value for the number of elements in the list: "))
lNum = create_List(number)
print(lNum)
nlNum = insertion_sort(lNum)
print(nlNum)
