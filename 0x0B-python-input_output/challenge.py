#!/usr/bin/python3

filename = "texto.txt"
var = "holberton"
#for i in var
with open(filename, 'r', encoding='utf-8') as f:    
    for line in f:
       # print(line)
        for word in line:
            #print(line, end="")
            print("---")
    for letter in word:
        print(word)
                # print(letter, end="")
            #for letter in word:
                #if word[letter] in var[i]:
                #print(word)
