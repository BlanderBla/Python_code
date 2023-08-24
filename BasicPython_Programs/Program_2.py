# Created by: Brayan Adrian Galvan Flores #
"""
What we learn with this module?
    Excersice with input
    Input obtain a string, but, we can convert this type of data to any which we watn.
    int(input("Message")) --> For int values
    float(input("Message")) --> For float values
"""
x = float(input("\tPut the first numeric value > "))
y = float(input("\tPut the second numeric value > "))

if y == 0:
    print("\n\tWe can't divide by zero")
else:
    print(f"\n\tOperations\n\tSum: {x+y}\n\tRest: {x-y}\n\tProduct: {x*y}\n\tDivision: {x/y}")