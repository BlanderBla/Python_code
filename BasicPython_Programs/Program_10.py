# Created by: Brayan Adrian Galvan Flores #

text = input("Ingress the message: ")
sizeText = len(text)

i=0
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
while i != sizeText:
    if text[i] == 'a': count_a = count_a + 1
    elif text[i] == 'e': count_e = count_e + 1
    elif text[i] == 'i': count_i = count_i + 1
    elif text[i] == 'o': count_o = count_o + 1
    elif text[i] == 'u': count_u = count_u + 1 
    i=i+1

print(f"\nSize: {sizeText}\na: {count_a}\ne: {count_e}\ni: {count_i}\no: {count_o}\nu: {count_u}")