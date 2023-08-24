# Created by: Brayan Adrian Galvan Flores #
# BINARY SEARCH ALGORITHM
import random as rnd

def binary_search(list, element):
    start = 0
    end = len(list)-1
    while start <= end:
        half = (start+end)//2
        if list[half] == element:
            return half
        elif list[half] < element:
            start = half+1
        else:
            end = half-1
    return -1

# MAIN
listValue = []
n = int(input("Enter a value for the number of elements in the list: "))
i = 0
while i < n:
    listValue.append(rnd.randint(1,1000))
    i+=1

listValue.sort()
print(f"Value's list: {listValue}")

x = int(input("Enter the number to search: "))
result = binary_search(listValue, x)
print(result)
