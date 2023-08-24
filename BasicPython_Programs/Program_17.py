# Created by: Brayan Adrian Galvan Flores #

acronym = input("Enter the acronym > ")
text = input("Enter the meaning > ")

list_word = text.split(" ")

i=0
firstLetter = ""
for x in list_word:
    firstLetter = firstLetter + x[0]
    i=i+1

if firstLetter == acronym:
    print("It's an acronym")
else:
    print("It is not an acronym")