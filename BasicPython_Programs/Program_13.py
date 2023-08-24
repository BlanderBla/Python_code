# Created by: Brayan Adrian Galvan Flores #
message = input("Enter the message > ")
list_words = message.split(" ")
print(list_words)

for i in list_words:
    print(f"{i}: {list_words.count(i)}")
