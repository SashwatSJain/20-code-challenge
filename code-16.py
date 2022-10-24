# Write a Python program to create string consisting of the non-negative integers up to n inclusive.
s = ""
for i in range(0, int(input("Enter a number: "))+1):
    s+=str(i)

print(s)