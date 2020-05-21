
import os

fname = input("enter file name to read it`s content :")
fh = open(fname,"r")
r = fh.readlines()
n= str(r)
print(str.upper(n))





