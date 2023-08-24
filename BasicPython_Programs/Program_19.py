import random as rd

valueList_1 = list()
valueList_2 = list()
n = int(input("Put the amount of random values that It will generate > "))
while n != 0:
    value = rd.randint(1,1000)
    valueList_1.append(value)
    value = rd.randint(1,1000)
    valueList_2.append(value)
    n = n-1

conjA = set(valueList_1)
conjB = set(valueList_2)
print(f"The first conjunction A: \n{conjA}\n\nThe second conjunction B\n{conjB}")
conjU = conjA & conjB
print(f"\n\nThe intersection is: {conjU}")