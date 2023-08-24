# Created by: Brayan Adrian Galvan Flores #
amount = int(input("Put the amount of character for the 'tree'> "))
i=1
for x in range(amount):
    for y in range(i):
        print("*",end=" "),
    i=i+1
    print("")

i = i - 1
for x in range(amount):
    for y in range(i):
        print("*",end=" "),
    i=i-1
    print("") 