import random as rnd

def sumar_numeros(*args):
    sum = 0
    arr = args[0]
    for i in arr:
        sum += + i
    return sum

listNum = []
n = int(input("Enter the amount of numbers to sum: "))
for i in range(n):
    x = rnd.randint(1,100)
    listNum.append(x)

x = sumar_numeros(listNum)
print(f"Value List: {listNum}\nSum: {x}")