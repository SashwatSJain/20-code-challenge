# Write a Python program to find the strings 
# in a given list, starting with a given prefix.

a = ["apple", "banana", "cherry", "orange",
     "kiwi", "melon", "mango", "strawberry"]

b = str(input("Enter a prefix: "))

for i in a:
    if i.startswith(b):
        print(i, end=" ")
