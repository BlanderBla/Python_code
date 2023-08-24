# Created by: Brayan Adrian Galvan Flores #
# LINEAL SEARCH ALGORITHM
import random as rnd

def create_List(n):
    listValue = []
    i = 0
    while i < n:
        listValue.append(rnd.randint(1,1000))
        i+=1
    return listValue

def lineal_Serch(list, element):
    for i in list:
        if i == element:
            return i
    return -1

number = int(input("Enter a value for the number of elements in the list: "))
lNum = create_List(number)
print(lNum)
x = int(input("Enter the number to search: "))
result = lineal_Serch(lNum,x)
print(result)
