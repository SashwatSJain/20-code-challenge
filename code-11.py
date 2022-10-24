# Write a Python program to check whether the given strings are palindromes or not. Return True, False.

a = str(input("Enter a string: "))
b = a[::-1]
if a == b:
    print("True")

else:
    print("False")
    