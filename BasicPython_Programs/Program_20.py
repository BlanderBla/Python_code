# Created by: Brayan Adrian Galvan Flores #
word = input("Enter a word here > ")

def readChar():
    car = input("Put only a caracter")
    return car

def searchCar(c):

count = 6    

if len(word.split(" ")) > 1:
    print("Only one word")
else:
    x = readChar()
    if x in word:
        print 
    