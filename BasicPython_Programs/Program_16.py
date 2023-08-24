# Created by: Brayan Adrian Galvan Flores #

text = input("Enter a message > ")

def vowelList(text):
    vowel_list = list()
    count_a = count_e = count_i = count_o = count_u = i = 0
    x = len(text)
    while i != x:
        if text[i] == 'a':
            count_a = count_a + 1
        elif text[i] == 'e':
            count_e = count_e + 1
        elif text[i] == 'i':
            count_i = count_i + 1
        elif text[i] == 'o':
            count_o = count_o + 1
        elif text[i] == 'u':
            count_u = count_u + 1
        i=i+1

    vowel_list.append(count_a)
    vowel_list.append(count_e)
    vowel_list.append(count_i)
    vowel_list.append(count_o)
    vowel_list.append(count_u)
    print(vowel_list)
    return vowel_list

def checkList(vowels):
    if vowels[0]!=0 and vowels[1]!=0 and vowels[2]!=0 and vowels[3]!=0 and vowels[4]!=0:
        print("We have the 5 vowels in the text")
    else:
        print("We don't have the vowels in the text")

vowels = list()
vowels = vowelList(text)
checkList(vowels)