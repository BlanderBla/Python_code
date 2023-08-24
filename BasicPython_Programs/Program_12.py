# Created by: Brayan Adrian Galvan Flores #
x = y = 1
result = count = 0
n = int(input("Generate the next amount of Fibonacci number > "))

print("1\n1")
while count < n-2:
    result = x + y;
    x = y
    y = result
    print(f"{result}")
    count = count + 1
