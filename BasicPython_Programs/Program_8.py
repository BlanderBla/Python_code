# Created by: Brayan Adrian Galvan Flores #

word= input("Put the text to invert > ")
drow = ""

i = 0
while len(word) != i:
    drow += word[-i-1]
    i=i+1

wordUpp = drow.upper()
wordLow = drow.lower()
print(f"Size: {len(drow)}\nReverse: {drow}\nUpper: {wordUpp}\nLower: {wordLow}")
