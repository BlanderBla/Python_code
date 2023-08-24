# Created by: Brayan Adrian Galvan Flores #

text = input("Enter a text: ")
print(f"Texto completo: {text}")
# Delete spaces
def spacedelete(text):
    return text.replace(" ","")

def reversetext(textclear):
    i=1
    x = len(textclear)
    textRev = ""
    while i <= x:
        textRev = textRev+textclear[-i]
        i=i+1
    return textRev

def verify(textclear,revText):
    if textclear == revText:
        print("Is a palindrom")
    else:
        print("Isn't a palindrom")
    
    return 0
        

textclear = spacedelete(text)
print(f"Texto limpio: {textclear}")

revTex = reversetext(textclear)
print(f"Texto en reversa: {revTex}")

verify(textclear,revTex)
