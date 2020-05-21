
import os

file = open("1.txt","r")
print(file.tell())
words = file.readlines()
print(file.tell())
print(words)

