# Created by: Brayan Adrian Galvan Flores #
import os

# Function to search the word to find in the Word.txt file
def searchWord(word):
    file = open("Word.txt", "r", encoding="utf8")
    container = file.read()
    file.close()

    if container.find(word) == -1:
        print("La palabra no existe")
    else:
        print("La palabra existe")

# 1. Open Diccionario.txt
name_file = "Diccionario.txt"
if os.path.isfile(name_file):
    print(f"¡El fichero {name_file} existe!")
    file = open("Diccionario.txt", "r", encoding="utf8")
    container = file.read()
    file.close()
  
    # 2. Copy Diccionario.txt to Words.txt
    file = open("Word.txt", "w", encoding="utf8")
    file.write(container)
    file.close()

    word = input("Enter the word to search: ")
    searchWord(word)

else:
    print(f"¡El fichero {name_file} no existe!")

name_file = "Words.txt"