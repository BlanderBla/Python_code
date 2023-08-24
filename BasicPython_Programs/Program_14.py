# Created by: Brayan Adrian Galvan Flores #
j = 0
flag = True
fletter_fword = list()
sletter_sword = list()
while flag:
    f_word = input("Enter the first word > ")
    if len(f_word.split(" ")) > 1:
        print("Was a mistake, only one word")
        break
    s_word = input("Enter the second word > ")
    if len(s_word.split(" ")) > 1:
        print("Was a mistake, only one word")
        break

for letter in f_word:
    fletter_fword.append(letter)

for letter in s_word:
    sletter_sword.append(letter)

ofword = sorted(fletter_fword)
osword = sorted(sletter_sword)

print(ofword)
print(osword)

flag = False
if(len(ofword) == len(osword)):
    print("Same size")
    for ofword, osword in zip(ofword, osword):
        if ofword != osword:
            print("Dont can be an anagrama")
        else:
            flag = True;  
else:
    print("Don't have the same size, can't be an anagram")


if flag == True:
    print("Is an anagram")
        