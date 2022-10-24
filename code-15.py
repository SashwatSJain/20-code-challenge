# Write a Python program find the strings 
# in a given list containing a given substring.

a = str(input("Enter a substring: "))
l = ["this", "is", "a", "list", "of", "strings"]
for i in l:
    if a in i:
        print(i, end=" ")
