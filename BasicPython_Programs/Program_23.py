# Created by: Brayan Adrian Galvan Flores #
import random as rd

def generatePosition():
    position = rd.randint(1,26)
    return position

def generateNewList(x,abc):
    abc_new = list()
    while x < len(abc):
        abc_new.append(abc.pop(x))

    for i in abc:
        abc_new.append(i)
    return abc_new

def encrypt(text, abc, abc_end):
    encrypt_text = ""
    for i in text:
        value = abc.index(i)
        encrypt_text += abc_end[value]
    return encrypt_text

text = input("Enter the text to encrypt > ")
abc_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

abc_end = list()

posit = generatePosition()
print(f"\nPosition {posit}")
abc_end = generateNewList(posit,abc_lower)
print(abc_end)
abc_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
textEncr = encrypt(text, abc_lower, abc_end)
print(abc_lower)
print(textEncr)