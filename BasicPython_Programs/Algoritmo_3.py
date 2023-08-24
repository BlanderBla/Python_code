# Created by: Brayan Adrian Galvan Flores #
# BUBBLE SORT ALGORITHM

import random as rnd

def create_List(n):
    listValue = []
    i = 0
    while i < n:
        listValue.append(rnd.randint(1,1000))
        i+=1
    return listValue

def bubble_Sort(list):
    aux = 0
    n = len(list)
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
    return list


number = int(input("Enter a value for the number of elements in the list: "))
lNum = create_List(number)
print(lNum)
nlNum = bubble_Sort(lNum)
print(nlNum)