#!/usr/bin/python3

num = input("Give me a number: ")
f = float(num)
if f == int(f):
    print(num)
else: 
    print(int(f)+1)