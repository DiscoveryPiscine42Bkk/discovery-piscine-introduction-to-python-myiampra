#!/usr/bin/env python3

numk = int(input("Enter the first number: \n"))
numj = int(input("Enter the second number: \n"))
total = numk * numj
print (numk, 'x' ,numj, '=',total)
if total > 0:
    print("The result is positive.")
elif total < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
