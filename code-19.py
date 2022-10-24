# Write a Python program to compute the sum of 
# the ASCII values of the upper-case characters
# in a given string.

a = str(input("Enter a string: "))
s = 0
for i in a:
    if i.isupper():
        s+=ord(i)

print(s)